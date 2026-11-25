package handshake

import (
	"crypto"
	"crypto/ecdh"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/hkdf"
	"crypto/rand"
	"crypto/sha256"
	"encoding/asn1"
	"encoding/binary"
	"errors"
	"fmt"
	"math/big"
)

// Signature algorithm registry (spec §1).
const (
	AlgEd25519   uint8 = 1
	AlgECDSAP256 uint8 = 2
	AlgECDSAP384 uint8 = 3
)

const (
	KeyIDSize          = 16
	PublicKeySize      = 65
	SignatureSize      = 64
	EphemeralKeySize   = 32
	ChannelBindingSize = 32
)

var ErrSignature = errors.New("handshake: signature invalid")

// KeyID names an identity, anchor or platform handshake key: the first 16 bytes of
// SHA-256(enc_bytes("zqnt-key-id-v1") || u8(alg) || enc_bytes(public key)).
func KeyID(alg uint8, publicKey []byte) []byte {
	return Hash(label(LabelKeyID).U8(alg).EncBytes(publicKey).Bytes())[:KeyIDSize]
}

// ParsePublicKey accepts only a 65-byte SEC 1 uncompressed P-256 point on the curve.
func ParsePublicKey(publicKey []byte) (*ecdsa.PublicKey, error) {
	if len(publicKey) != PublicKeySize {
		return nil, fmt.Errorf("handshake: public key has %d bytes, want %d", len(publicKey), PublicKeySize)
	}
	return ecdsa.ParseUncompressedPublicKey(elliptic.P256(), publicKey)
}

// Sign signs SHA-256(transcript) with an ECDSA P-256 signer (a private key, a TPM or another
// crypto.Signer that returns ASN.1) and returns r || s.
func Sign(signer crypto.Signer, transcript []byte) ([]byte, error) {
	der, err := signer.Sign(rand.Reader, Hash(transcript), crypto.SHA256)
	if err != nil {
		return nil, err
	}
	return P1363FromASN1(der)
}

// P1363FromASN1 converts a DER ECDSA P-256 signature to r || s (32 bytes each, big-endian).
func P1363FromASN1(der []byte) ([]byte, error) {
	var sig struct{ R, S *big.Int }
	rest, err := asn1.Unmarshal(der, &sig)
	if err != nil || len(rest) != 0 || sig.R.Sign() <= 0 || sig.S.Sign() <= 0 ||
		sig.R.BitLen() > 256 || sig.S.BitLen() > 256 {
		return nil, errors.New("handshake: malformed ASN.1 ECDSA signature")
	}
	out := make([]byte, SignatureSize)
	sig.R.FillBytes(out[:32])
	sig.S.FillBytes(out[32:])
	return out, nil
}

// Verify checks an r || s signature over SHA-256(transcript). Only AlgECDSAP256 is supported.
func Verify(alg uint8, publicKey, transcript, signature []byte) error {
	if alg != AlgECDSAP256 {
		return fmt.Errorf("handshake: unsupported signature algorithm %d", alg)
	}
	pub, err := ParsePublicKey(publicKey)
	if err != nil {
		return err
	}
	if len(signature) != SignatureSize {
		return ErrSignature
	}
	r := new(big.Int).SetBytes(signature[:32])
	s := new(big.Int).SetBytes(signature[32:])
	if !ecdsa.Verify(pub, Hash(transcript), r, s) {
		return ErrSignature
	}
	return nil
}

// SharedSecret is X25519(private, peer); a low-order peer key (all-zero result) is refused.
func SharedSecret(private *ecdh.PrivateKey, peer []byte) ([]byte, error) {
	pub, err := ecdh.X25519().NewPublicKey(peer)
	if err != nil {
		return nil, err
	}
	return private.ECDH(pub)
}

// SessionKeys is the key schedule of spec §5.
type SessionKeys struct {
	TranscriptHash []byte
	KeyN2P         []byte
	KeyP2N         []byte
	IVN2P          []byte
	IVP2N          []byte
	Exporter       []byte
	prk            []byte
}

// DeriveSessionKeys derives the session keys from the X25519 shared secret and the two signed
// transcripts of the handshake.
func DeriveSessionKeys(suite uint32, sharedSecret, helloTranscript, welcomeTranscript []byte) (*SessionKeys, error) {
	th := Hash(new(Encoder).EncBytes(helloTranscript).EncBytes(welcomeTranscript).Bytes())
	prk, err := hkdf.Extract(sha256.New, sharedSecret, th)
	if err != nil {
		return nil, err
	}
	k := &SessionKeys{TranscriptHash: th, prk: prk}
	for _, d := range []struct {
		name string
		size int
		dst  *[]byte
	}{
		{"key n2p", 32, &k.KeyN2P},
		{"key p2n", 32, &k.KeyP2N},
		{"iv n2p", 12, &k.IVN2P},
		{"iv p2n", 12, &k.IVP2N},
		{"exporter", 32, &k.Exporter},
	} {
		info := binary.BigEndian.AppendUint32(label("zqnt-edge-link-v1 "+d.name).Bytes(), suite)
		if *d.dst, err = hkdf.Expand(sha256.New, prk, string(info), d.size); err != nil {
			return nil, err
		}
	}
	return k, nil
}

// Zero overwrites every derived secret.
func (k *SessionKeys) Zero() {
	for _, b := range [][]byte{k.prk, k.KeyN2P, k.KeyP2N, k.IVN2P, k.IVP2N, k.Exporter} {
		clear(b)
	}
}
