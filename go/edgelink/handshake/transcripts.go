package handshake

import (
	"crypto/sha256"
	"fmt"
	"strings"

	edgelinkv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/edgelink/v3"
)

const (
	LabelHello       = "zqnt-edge-link-v1 hello"
	LabelWelcome     = "zqnt-edge-link-v1 welcome"
	LabelHelloRetry  = "zqnt-edge-link-v1 hello-retry"
	LabelPlatformKey = "zqnt-edge-link-v1 platform-key"
	LabelEnrollProof = "zqnt-edge-enroll-v1 proof"
	LabelRotate      = "zqnt-edge-enroll-v1 rotate"
	LabelRenew       = "zqnt-edge-enroll-v1 renew"
	LabelKeyID       = "zqnt-key-id-v1"
	LabelClaimCode   = "zqnt-claim-code-v1"
)

func u8(name string, v uint32) (uint8, error) {
	if v > 0xFF {
		return 0, fmt.Errorf("handshake: %s %d does not fit in one byte", name, v)
	}
	return uint8(v), nil
}

func label(l string) *Encoder { return new(Encoder).EncBytes([]byte(l)) }

// HelloTranscript is T_hello. organizationID and channelBinding are never sent; both sides
// supply their own view of them.
func HelloTranscript(h *edgelinkv3.Hello, organizationID string, channelBinding []byte) []byte {
	e := label(LabelHello).
		U32(h.GetCryptoSuite()).
		EncStr(organizationID).
		EncStr(h.GetNodeId()).
		EncBytes(h.GetIdentityKeyId()).
		EncBytes(channelBinding).
		EncBytes(h.GetEphemeralPub()).
		U64(h.GetMonotonicMs())
	if e.Present(h.GetWallclock() != nil) {
		e.Timestamp(h.GetWallclock())
	}
	e.EncBytes(h.GetServerNonce()).
		ListStr(h.GetEncodings()).
		ListStr(h.GetAssetSns()).
		EncStr(h.GetLinkKind()).
		EncStr(h.GetRuntimeVersion())
	if e.Present(h.GetDownlinkAcked() != nil) {
		e.Ack(h.GetDownlinkAcked())
	}
	return e.Bytes()
}

// WelcomeTranscript is T_welcome; helloHash is SHA-256(T_hello) of the Hello it answers.
func WelcomeTranscript(helloHash []byte, w *edgelinkv3.Welcome) []byte {
	e := label(LabelWelcome).
		EncBytes(helloHash).
		EncBytes(w.GetPlatformKey().GetKeyId()).
		EncBytes(w.GetEphemeralPub()).
		EncStr(w.GetSessionId()).
		I64(w.GetClockOffsetMs())
	if e.Present(w.GetResumeFrom() != nil) {
		e.Ack(w.GetResumeFrom())
	}
	if p := w.GetPolicy(); e.Present(p != nil) {
		e.EncStr(p.GetRevision())
		if e.Present(p.GetPingInterval() != nil) {
			e.Duration(p.GetPingInterval())
		}
	}
	return e.ListStr(w.GetServedAssetSns()).Bytes()
}

// HelloRetryTranscript is T_retry; helloHash is SHA-256(T_hello) of the Hello it answers.
func HelloRetryTranscript(helloHash []byte, r *edgelinkv3.HelloRetry) ([]byte, error) {
	reason, err := u8("reason", uint32(r.GetReason()))
	if err != nil {
		return nil, err
	}
	return label(LabelHelloRetry).
		EncBytes(helloHash).
		EncBytes(r.GetPlatformKey().GetKeyId()).
		EncBytes(r.GetServerNonce()).
		Timestamp(r.GetPlatformTime()).
		U8(reason).
		Bytes(), nil
}

// PlatformKeyTranscript is T_pkey, signed by the installation's anchor key.
func PlatformKeyTranscript(k *edgelinkv3.PlatformKey) ([]byte, error) {
	alg, err := u8("key_alg", k.GetKeyAlg())
	if err != nil {
		return nil, err
	}
	return label(LabelPlatformKey).
		EncStr(k.GetInstallationId()).
		EncBytes(k.GetAnchorKeyId()).
		EncBytes(k.GetKeyId()).
		U8(alg).
		EncBytes(k.GetPublicKey()).
		I64(k.GetNotBefore()).
		I64(k.GetNotAfter()).
		Bytes(), nil
}

// NormalizeClaimCode upper-cases the code and keeps only 0-9 and A-Z, like core's ClaimCodes.
func NormalizeClaimCode(code string) string {
	var b strings.Builder
	for _, c := range strings.ToUpper(code) {
		if c >= '0' && c <= '9' || c >= 'A' && c <= 'Z' {
			b.WriteRune(c)
		}
	}
	return b.String()
}

// ClaimDigest is what T_proof signs instead of the claim code.
func ClaimDigest(code string) []byte {
	sum := sha256.Sum256(label(LabelClaimCode).EncStr(NormalizeClaimCode(code)).Bytes())
	return sum[:]
}

// AttestationDigest is SHA-256 of the evidence, or empty without attestation.
func AttestationDigest(a *edgelinkv3.Attestation) []byte {
	if len(a.GetEvidence()) == 0 {
		return nil
	}
	sum := sha256.Sum256(a.GetEvidence())
	return sum[:]
}

func identityKey(k *edgelinkv3.IdentityKey) (alg, protection uint8, err error) {
	if alg, err = u8("key alg", k.GetAlg()); err != nil {
		return 0, 0, err
	}
	protection, err = u8("key protection", uint32(k.GetProtection()))
	return alg, protection, err
}

// EnrollmentProofTranscript is T_proof of a CompleteEnrollment.
func EnrollmentProofTranscript(r *edgelinkv3.CompleteEnrollmentRequest, channelBinding []byte) ([]byte, error) {
	alg, protection, err := identityKey(r.GetIdentityKey())
	if err != nil {
		return nil, err
	}
	sns := make([]string, len(r.GetAssets()))
	for i, a := range r.GetAssets() {
		sns[i] = a.GetSn()
	}
	return label(LabelEnrollProof).
		EncBytes(r.GetChallenge()).
		EncBytes(channelBinding).
		EncBytes(ClaimDigest(r.GetClaimCode())).
		U8(alg).
		EncBytes(r.GetIdentityKey().GetPublicKey()).
		U8(protection).
		ListU32(r.GetCryptoSuites()).
		EncBytes(AttestationDigest(r.GetAttestation())).
		ListStr(sns).
		EncStr(r.GetRuntimeVersion()).
		Bytes(), nil
}

// RotateTranscript is T_rotate, signed by both the old and the new identity key.
func RotateTranscript(organizationID, nodeID string, r *edgelinkv3.RotateIdentityKeyRequest, channelBinding []byte) ([]byte, error) {
	alg, protection, err := identityKey(r.GetNewKey())
	if err != nil {
		return nil, err
	}
	return label(LabelRotate).
		EncStr(organizationID).
		EncStr(nodeID).
		EncBytes(r.GetChallenge()).
		EncBytes(channelBinding).
		EncBytes(r.GetOldKeyId()).
		U8(alg).
		EncBytes(r.GetNewKey().GetPublicKey()).
		U8(protection).
		EncBytes(AttestationDigest(r.GetAttestation())).
		Bytes(), nil
}

// RenewTranscript is T_renew, signed by the active identity key.
func RenewTranscript(organizationID, nodeID string, r *edgelinkv3.RenewCredentialRequest, channelBinding []byte) []byte {
	return label(LabelRenew).
		EncStr(organizationID).
		EncStr(nodeID).
		EncBytes(r.GetChallenge()).
		EncBytes(channelBinding).
		EncBytes(r.GetKeyId()).
		Bytes()
}

// Hash is SHA-256 of a transcript, as T_welcome and T_retry embed it.
func Hash(transcript []byte) []byte {
	sum := sha256.Sum256(transcript)
	return sum[:]
}
