package handshake

import (
	"bytes"
	"crypto/ecdh"
	"crypto/ecdsa"
	"crypto/elliptic"
	"encoding/hex"
	"encoding/json"
	"errors"
	"os"
	"testing"

	edgelinkv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/edgelink/v3"
	"google.golang.org/protobuf/types/known/durationpb"
	"google.golang.org/protobuf/types/known/timestamppb"
)

const vectorsFile = "testdata/edge-link-handshake-v1.vectors.json"

type hexBytes []byte

func (h *hexBytes) UnmarshalJSON(b []byte) error {
	var s string
	if err := json.Unmarshal(b, &s); err != nil {
		return err
	}
	v, err := hex.DecodeString(s)
	*h = v
	return err
}

type signed struct {
	Transcript hexBytes `json:"transcript"`
	Signature  hexBytes `json:"signature"`
}

type vectors struct {
	Inputs struct {
		AnchorPrivate            hexBytes `json:"anchor_private"`
		ClaimCode                string   `json:"claim_code"`
		EnrollmentChallenge      hexBytes `json:"enrollment_challenge"`
		InstallationID           string   `json:"installation_id"`
		NodeEphemeralPrivate     hexBytes `json:"node_ephemeral_private"`
		NodeID                   string   `json:"node_id"`
		NodeIdentityPrivate      hexBytes `json:"node_identity_private"`
		OrganizationID           string   `json:"organization_id"`
		PlatformEphemeralPrivate hexBytes `json:"platform_ephemeral_private"`
		PlatformHandshakePrivate hexBytes `json:"platform_handshake_private"`
		RotationNewPrivate       hexBytes `json:"rotation_new_identity_private"`
		ServerNonce              hexBytes `json:"server_nonce"`
		TLSChannelBinding        hexBytes `json:"tls_channel_binding"`
	} `json:"inputs"`
	Keys struct {
		AnchorKeyID             hexBytes `json:"anchor_key_id"`
		AnchorPublic            hexBytes `json:"anchor_public"`
		NodeEphemeralPublic     hexBytes `json:"node_ephemeral_public"`
		NodeIdentityKeyID       hexBytes `json:"node_identity_key_id"`
		NodeIdentityPublic      hexBytes `json:"node_identity_public"`
		PlatformEphemeralPublic hexBytes `json:"platform_ephemeral_public"`
		PlatformHandshakeKeyID  hexBytes `json:"platform_handshake_key_id"`
		PlatformHandshakePublic hexBytes `json:"platform_handshake_public"`
		RotationNewKeyID        hexBytes `json:"rotation_new_identity_key_id"`
		RotationNewPublic       hexBytes `json:"rotation_new_identity_public"`
	} `json:"keys"`
	PlatformKeyCertificate struct {
		signed
		NotBefore int64 `json:"not_before"`
		NotAfter  int64 `json:"not_after"`
	} `json:"platform_key_certificate"`
	Hello struct {
		signed
		TranscriptSHA256 hexBytes `json:"transcript_sha256"`
	} `json:"hello"`
	Welcome     signed `json:"welcome"`
	KeySchedule struct {
		Exporter       hexBytes `json:"exporter"`
		IVN2P          hexBytes `json:"iv_n2p"`
		IVP2N          hexBytes `json:"iv_p2n"`
		KeyN2P         hexBytes `json:"key_n2p"`
		KeyP2N         hexBytes `json:"key_p2n"`
		PRK            hexBytes `json:"prk"`
		SharedSecret   hexBytes `json:"shared_secret"`
		TranscriptHash hexBytes `json:"transcript_hash"`
	} `json:"key_schedule"`
	HelloRetry struct {
		FirstHelloTranscript  hexBytes `json:"first_hello_transcript"`
		RetryTranscript       hexBytes `json:"retry_transcript"`
		RetrySignature        hexBytes `json:"retry_signature"`
		SecondHelloTranscript hexBytes `json:"second_hello_transcript"`
		SecondHelloSignature  hexBytes `json:"second_hello_signature"`
	} `json:"hello_retry"`
	EnrollmentProof struct {
		signed
		ClaimCodeNormalized string   `json:"claim_code_normalized"`
		ClaimDigest         hexBytes `json:"claim_digest"`
	} `json:"enrollment_proof"`
	KeyRotation struct {
		Transcript      hexBytes `json:"transcript"`
		SignatureOldKey hexBytes `json:"signature_old_key"`
		SignatureNewKey hexBytes `json:"signature_new_key"`
	} `json:"key_rotation"`
	CredentialRenewal signed `json:"credential_renewal"`
	Negative          []struct {
		Case       string   `json:"case"`
		Transcript hexBytes `json:"transcript"`
		Signature  hexBytes `json:"signature"`
		PeerPublic hexBytes `json:"peer_public"`
	} `json:"negative"`
}

func load(t *testing.T) *vectors {
	t.Helper()
	raw, err := os.ReadFile(vectorsFile)
	if err != nil {
		t.Fatal(err)
	}
	var v vectors
	if err := json.Unmarshal(raw, &v); err != nil {
		t.Fatal(err)
	}
	return &v
}

func signingKey(t *testing.T, private []byte) *ecdsa.PrivateKey {
	t.Helper()
	k, err := ecdsa.ParseRawPrivateKey(elliptic.P256(), private)
	if err != nil {
		t.Fatal(err)
	}
	return k
}

func publicBytes(t *testing.T, k *ecdsa.PrivateKey) []byte {
	t.Helper()
	b, err := k.PublicKey.Bytes()
	if err != nil {
		t.Fatal(err)
	}
	return b
}

func x25519(t *testing.T, private []byte) *ecdh.PrivateKey {
	t.Helper()
	k, err := ecdh.X25519().NewPrivateKey(private)
	if err != nil {
		t.Fatal(err)
	}
	return k
}

func equal(t *testing.T, what string, got, want []byte) {
	t.Helper()
	if !bytes.Equal(got, want) {
		t.Errorf("%s\n got: %x\nwant: %x", what, got, want)
	}
}

func must(t *testing.T) func([]byte, error) []byte {
	return func(b []byte, err error) []byte {
		t.Helper()
		if err != nil {
			t.Fatal(err)
		}
		return b
	}
}

// verifies checks the vector signature and that our own signature over the same transcript
// verifies too (ECDSA signatures need not be deterministic, so they are not compared).
func verifies(t *testing.T, what string, key *ecdsa.PrivateKey, transcript, signature []byte) {
	t.Helper()
	pub := publicBytes(t, key)
	if err := Verify(AlgECDSAP256, pub, transcript, signature); err != nil {
		t.Errorf("%s: vector signature: %v", what, err)
	}
	own, err := Sign(key, transcript)
	if err != nil {
		t.Fatalf("%s: sign: %v", what, err)
	}
	if len(own) != SignatureSize {
		t.Errorf("%s: own signature has %d bytes", what, len(own))
	}
	if err := Verify(AlgECDSAP256, pub, transcript, own); err != nil {
		t.Errorf("%s: own signature: %v", what, err)
	}
}

type fixture struct {
	v                                *vectors
	node, anchor, platform, rotated  *ecdsa.PrivateKey
	nodeEphemeral, platformEphemeral *ecdh.PrivateKey
	platformKey                      *edgelinkv3.PlatformKey
}

func setup(t *testing.T) *fixture {
	v := load(t)
	f := &fixture{
		v:                 v,
		node:              signingKey(t, v.Inputs.NodeIdentityPrivate),
		anchor:            signingKey(t, v.Inputs.AnchorPrivate),
		platform:          signingKey(t, v.Inputs.PlatformHandshakePrivate),
		rotated:           signingKey(t, v.Inputs.RotationNewPrivate),
		nodeEphemeral:     x25519(t, v.Inputs.NodeEphemeralPrivate),
		platformEphemeral: x25519(t, v.Inputs.PlatformEphemeralPrivate),
	}
	f.platformKey = &edgelinkv3.PlatformKey{
		InstallationId: v.Inputs.InstallationID,
		AnchorKeyId:    v.Keys.AnchorKeyID,
		KeyId:          v.Keys.PlatformHandshakeKeyID,
		KeyAlg:         uint32(AlgECDSAP256),
		PublicKey:      v.Keys.PlatformHandshakePublic,
		NotBefore:      v.PlatformKeyCertificate.NotBefore,
		NotAfter:       v.PlatformKeyCertificate.NotAfter,
		Signature:      v.PlatformKeyCertificate.Signature,
	}
	return f
}

func (f *fixture) hello(wallclock bool, nonce []byte) *edgelinkv3.Hello {
	h := &edgelinkv3.Hello{
		NodeId:         f.v.Inputs.NodeID,
		CryptoSuite:    uint32(edgelinkv3.CryptoSuite_CRYPTO_SUITE_S1_CHACHA20_POLY1305),
		EphemeralPub:   f.nodeEphemeral.PublicKey().Bytes(),
		MonotonicMs:    123456789,
		Encodings:      []string{"full"},
		AssetSns:       []string{"SIM-DRONE-01", "SIM-RADAR-07"},
		LinkKind:       "ip-session",
		RuntimeVersion: "3.0.0",
		DownlinkAcked:  &edgelinkv3.Ack{Epoch: 1, CumulativeSeq: 41, SelectiveBitmap: []byte{0x05}},
		IdentityKeyId:  f.v.Keys.NodeIdentityKeyID,
		ServerNonce:    nonce,
	}
	if wallclock {
		h.Wallclock = &timestamppb.Timestamp{Seconds: 1793534400, Nanos: 250000000}
	}
	return h
}

func (f *fixture) welcome() *edgelinkv3.Welcome {
	return &edgelinkv3.Welcome{
		EphemeralPub:   f.platformEphemeral.PublicKey().Bytes(),
		ClockOffsetMs:  -1500,
		ResumeFrom:     &edgelinkv3.Ack{Epoch: 3, CumulativeSeq: 1200},
		SessionId:      "5d2f1e8a-9b47-4c30-a6d1-0e7f3b2c9a84",
		Policy:         &edgelinkv3.LinkPolicy{Revision: "PT15S", PingInterval: durationpb.New(15e9)},
		PlatformKey:    f.platformKey,
		ServedAssetSns: []string{"SIM-DRONE-01"},
	}
}

func TestKeys(t *testing.T) {
	f := setup(t)
	k := f.v.Keys
	for _, c := range []struct {
		name       string
		key        *ecdsa.PrivateKey
		pub, keyID []byte
	}{
		{"node identity", f.node, k.NodeIdentityPublic, k.NodeIdentityKeyID},
		{"anchor", f.anchor, k.AnchorPublic, k.AnchorKeyID},
		{"platform handshake", f.platform, k.PlatformHandshakePublic, k.PlatformHandshakeKeyID},
		{"rotation new identity", f.rotated, k.RotationNewPublic, k.RotationNewKeyID},
	} {
		pub := publicBytes(t, c.key)
		equal(t, c.name+" public key", pub, c.pub)
		equal(t, c.name+" key id", KeyID(AlgECDSAP256, pub), c.keyID)
		if _, err := ParsePublicKey(pub); err != nil {
			t.Errorf("%s: %v", c.name, err)
		}
	}
	equal(t, "node ephemeral", f.nodeEphemeral.PublicKey().Bytes(), k.NodeEphemeralPublic)
	equal(t, "platform ephemeral", f.platformEphemeral.PublicKey().Bytes(), k.PlatformEphemeralPublic)
}

func TestPlatformKeyCertificate(t *testing.T) {
	f := setup(t)
	tr := must(t)(PlatformKeyTranscript(f.platformKey))
	equal(t, "T_pkey", tr, f.v.PlatformKeyCertificate.Transcript)
	verifies(t, "T_pkey", f.anchor, tr, f.v.PlatformKeyCertificate.Signature)
}

func TestHelloWelcomeAndKeySchedule(t *testing.T) {
	f := setup(t)
	cb := f.v.Inputs.TLSChannelBinding

	hello := HelloTranscript(f.hello(true, nil), f.v.Inputs.OrganizationID, cb)
	equal(t, "T_hello", hello, f.v.Hello.Transcript)
	equal(t, "SHA-256(T_hello)", Hash(hello), f.v.Hello.TranscriptSHA256)
	verifies(t, "T_hello", f.node, hello, f.v.Hello.Signature)

	welcome := WelcomeTranscript(Hash(hello), f.welcome())
	equal(t, "T_welcome", welcome, f.v.Welcome.Transcript)
	verifies(t, "T_welcome", f.platform, welcome, f.v.Welcome.Signature)

	ks := f.v.KeySchedule
	nodeSS, err := SharedSecret(f.nodeEphemeral, f.platformEphemeral.PublicKey().Bytes())
	if err != nil {
		t.Fatal(err)
	}
	platformSS, err := SharedSecret(f.platformEphemeral, f.nodeEphemeral.PublicKey().Bytes())
	if err != nil {
		t.Fatal(err)
	}
	equal(t, "shared secret (node)", nodeSS, ks.SharedSecret)
	equal(t, "shared secret (platform)", platformSS, ks.SharedSecret)

	keys, err := DeriveSessionKeys(uint32(edgelinkv3.CryptoSuite_CRYPTO_SUITE_S1_CHACHA20_POLY1305), nodeSS, hello, welcome)
	if err != nil {
		t.Fatal(err)
	}
	equal(t, "th", keys.TranscriptHash, ks.TranscriptHash)
	equal(t, "prk", keys.prk, ks.PRK)
	equal(t, "key_n2p", keys.KeyN2P, ks.KeyN2P)
	equal(t, "key_p2n", keys.KeyP2N, ks.KeyP2N)
	equal(t, "iv_n2p", keys.IVN2P, ks.IVN2P)
	equal(t, "iv_p2n", keys.IVP2N, ks.IVP2N)
	equal(t, "exporter", keys.Exporter, ks.Exporter)

	keys.Zero()
	for _, b := range [][]byte{keys.prk, keys.KeyN2P, keys.KeyP2N, keys.IVN2P, keys.IVP2N, keys.Exporter} {
		if !bytes.Equal(b, make([]byte, len(b))) {
			t.Errorf("not zeroized: %x", b)
		}
	}
}

func TestHelloRetry(t *testing.T) {
	f := setup(t)
	r := f.v.HelloRetry
	cb := f.v.Inputs.TLSChannelBinding

	first := HelloTranscript(f.hello(false, nil), f.v.Inputs.OrganizationID, cb)
	equal(t, "first T_hello", first, r.FirstHelloTranscript)

	retry := must(t)(HelloRetryTranscript(Hash(first), &edgelinkv3.HelloRetry{
		ServerNonce:  f.v.Inputs.ServerNonce,
		PlatformTime: &timestamppb.Timestamp{Seconds: 1793534460},
		Reason:       edgelinkv3.HelloRetryReason_HELLO_RETRY_REASON_CLOCK_UNTRUSTED,
		PlatformKey:  f.platformKey,
	}))
	equal(t, "T_retry", retry, r.RetryTranscript)
	verifies(t, "T_retry", f.platform, retry, r.RetrySignature)

	second := HelloTranscript(f.hello(false, f.v.Inputs.ServerNonce), f.v.Inputs.OrganizationID, cb)
	equal(t, "second T_hello", second, r.SecondHelloTranscript)
	verifies(t, "second T_hello", f.node, second, r.SecondHelloSignature)
}

func TestEnrollmentProof(t *testing.T) {
	f := setup(t)
	p := f.v.EnrollmentProof
	if got := NormalizeClaimCode(f.v.Inputs.ClaimCode); got != p.ClaimCodeNormalized {
		t.Errorf("normalized claim code %q, want %q", got, p.ClaimCodeNormalized)
	}
	equal(t, "claim_digest", ClaimDigest(f.v.Inputs.ClaimCode), p.ClaimDigest)

	tr := must(t)(EnrollmentProofTranscript(&edgelinkv3.CompleteEnrollmentRequest{
		ClaimCode: f.v.Inputs.ClaimCode,
		Challenge: f.v.Inputs.EnrollmentChallenge,
		IdentityKey: &edgelinkv3.IdentityKey{
			Alg:        uint32(AlgECDSAP256),
			PublicKey:  f.v.Keys.NodeIdentityPublic,
			Protection: edgelinkv3.KeyProtection_KEY_PROTECTION_SOFTWARE_DEV,
		},
		CryptoSuites: []uint32{
			uint32(edgelinkv3.CryptoSuite_CRYPTO_SUITE_S1_CHACHA20_POLY1305),
			uint32(edgelinkv3.CryptoSuite_CRYPTO_SUITE_S1_AES_256_GCM),
		},
		Assets:         []*edgelinkv3.EnrollingAsset{{Sn: "SIM-DRONE-01", Name: "not signed"}},
		RuntimeVersion: "3.0.0",
		DisplayName:    "not signed",
	}, f.v.Inputs.TLSChannelBinding))
	equal(t, "T_proof", tr, p.Transcript)
	verifies(t, "T_proof", f.node, tr, p.Signature)
}

func TestKeyRotation(t *testing.T) {
	f := setup(t)
	r := f.v.KeyRotation
	tr := must(t)(RotateTranscript(f.v.Inputs.OrganizationID, f.v.Inputs.NodeID, &edgelinkv3.RotateIdentityKeyRequest{
		Challenge: f.v.Inputs.EnrollmentChallenge,
		OldKeyId:  f.v.Keys.NodeIdentityKeyID,
		NewKey: &edgelinkv3.IdentityKey{
			Alg:        uint32(AlgECDSAP256),
			PublicKey:  f.v.Keys.RotationNewPublic,
			Protection: edgelinkv3.KeyProtection_KEY_PROTECTION_SOFTWARE_DEV,
		},
	}, f.v.Inputs.TLSChannelBinding))
	equal(t, "T_rotate", tr, r.Transcript)
	verifies(t, "T_rotate (old key)", f.node, tr, r.SignatureOldKey)
	verifies(t, "T_rotate (new key)", f.rotated, tr, r.SignatureNewKey)
}

func TestCredentialRenewal(t *testing.T) {
	f := setup(t)
	tr := RenewTranscript(f.v.Inputs.OrganizationID, f.v.Inputs.NodeID, &edgelinkv3.RenewCredentialRequest{
		Challenge: f.v.Inputs.EnrollmentChallenge,
		KeyId:     f.v.Keys.NodeIdentityKeyID,
	}, f.v.Inputs.TLSChannelBinding)
	equal(t, "T_renew", tr, f.v.CredentialRenewal.Transcript)
	verifies(t, "T_renew", f.node, tr, f.v.CredentialRenewal.Signature)
}

func TestNegative(t *testing.T) {
	f := setup(t)
	pub := publicBytes(t, f.node)
	for _, n := range f.v.Negative {
		if len(n.PeerPublic) > 0 {
			if _, err := SharedSecret(f.nodeEphemeral, n.PeerPublic); err == nil {
				t.Errorf("%s: key agreement accepted", n.Case)
			}
			continue
		}
		if err := Verify(AlgECDSAP256, pub, n.Transcript, n.Signature); !errors.Is(err, ErrSignature) {
			t.Errorf("%s: got %v, want ErrSignature", n.Case, err)
		}
	}
}

func TestVerifyRefusesMalformedInput(t *testing.T) {
	f := setup(t)
	pub := publicBytes(t, f.node)
	tr := f.v.Hello.Transcript
	sig := f.v.Hello.Signature
	if err := Verify(AlgEd25519, pub, tr, sig); err == nil {
		t.Error("accepted an unsupported algorithm")
	}
	if err := Verify(AlgECDSAP256, pub[:33], tr, sig); err == nil {
		t.Error("accepted a compressed-length key")
	}
	offCurve := bytes.Clone(pub)
	offCurve[64] ^= 1
	if err := Verify(AlgECDSAP256, offCurve, tr, sig); err == nil {
		t.Error("accepted a point off the curve")
	}
	if err := Verify(AlgECDSAP256, pub, tr, sig[:63]); !errors.Is(err, ErrSignature) {
		t.Errorf("short signature: %v", err)
	}
	if _, err := HelloRetryTranscript(nil, &edgelinkv3.HelloRetry{Reason: 256}); err == nil {
		t.Error("accepted a reason that does not fit in one byte")
	}
	if _, err := PlatformKeyTranscript(&edgelinkv3.PlatformKey{KeyAlg: 258}); err == nil {
		t.Error("accepted a key_alg that does not fit in one byte")
	}
}

func TestVectorsMatchSpec(t *testing.T) {
	spec, err := os.ReadFile("../../../spec/edge-link-handshake-v1.vectors.json")
	if errors.Is(err, os.ErrNotExist) {
		t.Skip("spec not present outside the repository")
	}
	if err != nil {
		t.Fatal(err)
	}
	copied, err := os.ReadFile(vectorsFile)
	if err != nil {
		t.Fatal(err)
	}
	if !bytes.Equal(spec, copied) {
		t.Error("testdata vectors differ from spec/edge-link-handshake-v1.vectors.json; copy them, never regenerate")
	}
}
