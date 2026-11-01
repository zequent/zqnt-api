# Edge Link handshake and node identity, version 1 (suite S1)

| | |
|---|---|
| Status | Draft for CTO review |
| Issue | zequent/zqnt-core#370 (part of #322); blocks core#326 and zequent/zqnt-sdk-go#19 |
| Contract | `proto/v3/zqnt/edgelink/v3/edge_link.proto` (zqnt-api `6a5ef80`, `feature/r7-sprint1`) |
| Source plan | Transport plan "Edge nodes in the field": D9, §5.1–5.2, §10.1–10.3, §14 Q3 |
| Test vectors | [`edge-link-handshake-v1.vectors.json`](edge-link-handshake-v1.vectors.json) |
| Deviation from the plan | The node identity key is **ECDSA P-256**, not Ed25519 (§1, R-1) |

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are used as in RFC 2119 and RFC 8174.
Statements marked **assumption** have not been verified and need checking before they are relied on.
Section 9 lists the recommendations that await CTO confirmation (R-1 to R-5) and the open decisions.

## 0. Scope and current state

This spec covers how an Edge Node gets a long-term identity (enrollment), how it proves that
identity when it opens an Edge Link session (Hello), how the platform proves its identity back
(Welcome), which session keys both sides derive, how sessions are bound to TLS, how this relates to
edge credentials and revocation, and the extra rules for nodes carried by a person (§6.3). It defines
suite S1 normatively. S2 and S3 only have reserved ids.

Out of scope: the end-to-end AEAD frame format for lean, relayed and tiny paths (M2/M4), the tiny
profile's symmetric keys, `PostBatch` authentication, and any national approval.

What exists today (read from `feature/r7-sprint1`, 2026-11-01):

- **core `services/edge-link`** (`EdgeLinkGrpcService`, `NodeSession`). `Connect` requires a service
  token with scope `edge` (the edge credential, a bearer token). The first frame must be `Hello`.
  `Hello` is **not verified**: `node_id` is taken from the frame (regex `[A-Za-z0-9._:-]{1,128}`) and
  the organization from the token. Any holder of an organization's edge credential can therefore open
  a session as any `node_id` of that organization and declare any `asset_sns`. Because a newer session
  of a node takes over the link (`takenOver`), a forged Hello also disconnects the real node. `Welcome`
  is unsigned. Revocation is per credential `jti` (deny-list). `PostBatch` returns UNIMPLEMENTED.
- **zqnt-sdk-go `edge/runtime/session`**. The Hello is sent unsigned unless a `Signer` is set; the
  `Signer` hook signs the deterministic protobuf encoding of the Hello (replaced by §4.1). The Welcome
  is applied without any check. `ipsession` dials TLS 1.3 and sends `token_file` as
  `authorization: Bearer`.
- **Edge credentials** (`ServiceCredentialService`, admin-console). Compact JWS (EdDSA) signed with the
  OpenBao Transit key `credential` (or `SERVICE_AUTH_PRIVATE_KEY`); `sub = edge:<name>:<uuid>`,
  `scope = [edge]`, `org_id`, `jti`; default 365 days, max 730; revocation puts the `jti` on the
  deny-list, re-asserted every 10 minutes. Credentials are not bound to a node.
- **Asset claims** (`AssetClaimService`, connector; `zqnt.asset.v3.AssetClaimService` in
  zqnt-contracts). Code `ZQ-XXXXX-XXXXX` (10 symbols of a 32-symbol alphabet, about 50 bits), stored
  as a peppered hash, TTL 15 min (max 1 day), up to 10 redemptions. `RedeemClaim` creates one asset in
  the claim's organization; every refusal answers alike. No key is bound.

## 1. Suite registry

`Hello.crypto_suite` is a `uint32`: `(family << 8) | variant`.

| Value | Name | Status | Ephemeral key exchange | Identity and platform signatures | KDF / hash | AEAD (end-to-end frames) |
|---|---|---|---|---|---|---|
| `0x0000` | invalid | — | — | — | — | — |
| `0x0101` | S1-C | **normative**, default | X25519 | ECDSA P-256 / SHA-256 (alg 2) | HKDF-SHA-256 | ChaCha20-Poly1305 |
| `0x0102` | S1-G | **normative** | X25519 | ECDSA P-256 / SHA-256 (alg 2) | HKDF-SHA-256 | AES-256-GCM |
| `0x0201`–`0x02FF` | S2 "FIPS / CNSA 1.0-style" | reserved | ECDH P-384 | ECDSA P-384 | SHA-384 | AES-256-GCM |
| `0x0301`–`0x03FF` | S3 "PQ hybrid" | reserved | X25519 or P-384 + ML-KEM-768/1024 | P-256/P-384 or ML-DSA | SHA-384 | AES-256-GCM |
| everything else | — | reserved | | | | |

Signature algorithm registry (`alg`): `1` = Ed25519 (reserved, not used by S1); `2` = ECDSA over
NIST P-256 with SHA-256 (S1); `3` = ECDSA P-384 with SHA-384 (reserved for S2).

Rules:

1. A sender MUST NOT send `0x0000`. A receiver MUST treat an unknown value as unsupported (§4.7).
2. **Deviation from plan D9 / §10.3** (which named Ed25519): S1 uses ECDSA P-256 for long-term
   signing keys, because the hardware that is meant to hold them does not do Ed25519: TPM 2.0 parts
   implement RSA and NIST curves, Microchip ATECC608B supports only P-256, and phones (Android
   Keystore/StrongBox, Apple Secure Enclave) only hold P-256 keys (assumption for individual chips:
   verify per part on the hardware list). With Ed25519 the identity key could not be non-exportable on
   any of them. The platform's own keys (§4.3) use P-256 too, so a node needs one signature algorithm
   only, which ATECC608B can also verify in hardware. X25519 stays for the ephemeral exchange: it is
   done in software on every node and is fast and hard to misuse. This is recommendation R-1.
3. The two S1 variants differ only in the AEAD used for end-to-end frames, which v1 does not use on
   IP sessions (§5). The variant is fixed and signed at handshake time so M2 cannot be downgraded.
   S1-C is the default because many nodes lack AES instructions (assumption: Raspberry Pi 4).
4. The suite is independent of the transport crypto (TLS 1.3 on IP links). The tiny profile's
   one-byte header suite field (plan §7.1) is a **separate registry**, defined in M4.
5. A Hello offers exactly one suite. There is no in-band negotiation: the node's registry entry
   (`allowed_suites`, §3.3) decides what the platform accepts.

## 2. Node identity

### 2.1 Identity key

1. Every Edge Node MUST have exactly one active long-term identity key pair of an algorithm its suite
   allows (S1: ECDSA P-256).
2. The key pair MUST be generated on the node. The private key MUST NOT leave the node, MUST NOT be
   generated by the platform and MUST NOT be backed up (no cloud keychain sync).
3. Where the hardware can hold a non-exportable P-256 key, the key MUST be generated inside it: TPM 2.0,
   secure element (ATECC608B, SE050), Android Keystore (StrongBox when present) or Apple Secure Enclave.
4. Key protection classes (`key_protection`, recorded in the registry and shown in the console):

   | Value | Name | Meaning |
   |---|---|---|
   | 0 | `UNSPECIFIED` | invalid |
   | 1 | `SOFTWARE_DEV` | plain key file. Development, simulator (`SIM-*`) and CI only. |
   | 2 | `SOFTWARE_SEALED` | software key encrypted at rest by a key held in a TPM/SE of the device |
   | 3 | `TPM` | generated in and non-exportable from a TPM 2.0 |
   | 4 | `SECURE_ELEMENT` | generated in and non-exportable from a discrete secure element |
   | 5 | `MOBILE_TEE` | Android Keystore backed by the TEE |
   | 6 | `MOBILE_SECURE_HW` | Android StrongBox or Apple Secure Enclave |

   Without attestation (§3.5) the class is **self-declared**: the registry stores it as
   `key_protection_claimed`, and only a verified attestation sets `key_protection_attested`.
5. An organization policy `edge_nodes.minimum_key_protection` is enforced at enrollment and at every
   Hello. Default: `SOFTWARE_DEV` on dev installations, `SOFTWARE_SEALED` otherwise (OD-5). The console
   MUST mark nodes with `SOFTWARE_DEV` keys as development nodes.

### 2.2 Key encoding and key id

- Public keys: SEC 1 uncompressed point, 65 bytes (`0x04 || X || Y`). Receivers MUST reject anything
  else and points not on the curve.
- Signatures: ECDSA P-256 over `SHA-256(transcript)`, encoded `r || s`, 32 bytes each, big-endian
  (IEEE P1363, 64 bytes). Android Keystore, Apple Security framework and the JDK default emit DER;
  implementations convert. Signers MUST use a CSPRNG nonce or RFC 6979. Verifiers MUST NOT require
  low-S and MUST NOT use a signature as an identifier (ECDSA signatures are malleable; nothing in this
  spec keys on them).
- Hardware that signs a digest (TPM2_Sign, ATECC608B) is given `SHA-256(transcript)`; the result is
  the same signature.
- `key_id(alg, pub) = SHA-256( enc_bytes("zqnt-key-id-v1") || u8(alg) || enc_bytes(pub) )[0..16]`
  (16 bytes, encoding in §4.1). The same function names node, anchor and platform handshake keys.

### 2.3 node_id

1. `node_id` is **assigned by the platform** at enrollment: a random UUID (version 4), canonical
   lowercase. It is unique within the installation and stable across key rotation and re-enrollment.
2. It is not derived from the key, so rotation does not rename the node.
3. The node MUST persist `node_id`, `organization_id` and `installation_id` from the enrollment
   response and use exactly those values in every transcript.
4. The display name is separate, operator-chosen, and never part of a transcript.
5. Nodes with self-chosen ids today (simulator, tests) re-enroll; there is no compatibility path.

## 3. Enrollment

Enrollment extends the claim-code flow. The node calls a new public service
`zqnt.edgelink.v3.EdgeEnrollmentService` (§10.1), served by core `edge-link` without a bearer token:
the claim code is the credential, as with `RedeemClaim` today. `edge-link` forwards to connector
(`zqnt.edgenode.v3.EdgeNodeRegistryService`, §10.2), the system of record.

### 3.1 Flow

```
node                                   edge-link                         connector
 | TLS 1.3 to edge-link; cb = channel binding (§4.2)                     |
 | BeginEnrollment(purpose=ENROLL)        |                                   |
 |--------------------------------------->| challenge = 32 random bytes       |
 |<---------------------------------------| store SHA-256(challenge), 5 min  |
 | generate identity key in hardware      |                                   |
 | sig = Sign(sk, T_proof)                |                                   |
 | CompleteEnrollment(code, challenge,    |                                   |
 |   key, protection, suites,             |                                   |
 |   attestation?, assets, sig)           |                                   |
 |--------------------------------------->| consume challenge, own cb         |
 |                                        | EnrollNode(..., cb) ------------->| verify PoP, consume claim,
 |                                        |                                   | create node, key, assets
 |                                        |<----------------------------------| node record
 |                                        | mint node-bound edge credential   |
 |<---------------------------------------| node_id, org, credential, anchors |
```

### 3.2 Proof of possession

The node signs

```
T_proof = enc_bytes("zqnt-edge-enroll-v1 proof")
       || enc_bytes(challenge)                       32 bytes from BeginEnrollment
       || enc_bytes(channel_binding)                 32 bytes, §4.2
       || enc_bytes(claim_digest)
       || u8(identity_key_alg)
       || enc_bytes(identity_public_key)
       || u8(key_protection)
       || enc_list_u32(suites)                       in the order sent
       || enc_bytes(attestation_digest)              SHA-256(attestation.evidence), or empty
       || enc_list_str(asset_sns)                    in the order sent
       || enc_str(runtime_version)

claim_digest = SHA-256( enc_bytes("zqnt-claim-code-v1") || enc_str(normalize(code)) )
```

`normalize` is `ClaimCodes.normalize`: upper-case, keep only `0-9A-Z`. The digest, not the code, is
signed so that a logged signature never contains the code.

Connector MUST, in one transaction:

1. Accept the challenge only as consumed by edge-link with purpose `ENROLL` (atomic get-and-delete in
   Redis), and verify the signature itself over `T_proof` built with the channel binding edge-link
   computed for its own TLS session. A request relayed by a TLS man-in-the-middle carries a different
   binding and fails.
2. Reject a public key that does not decode or is not on the curve.
3. Reject a `key_id` that was ever enrolled before (active or historical).
4. Check the organization's `minimum_key_protection`, the allowed suites and the claim's `node_class`
   rules (§6.3).
5. Consume one redemption of the claim (`consumeRedemption`; unknown, expired, revoked, exhausted and
   vendor/type mismatch all fail alike). **One enrollment consumes one redemption**, however many
   assets it brings.
6. Create the node record (§3.3) and key record, create each listed asset in the claim's organization
   as `RedeemClaim` does (refuse an existing serial before consuming), and bind them to the node (§3.4).
7. Write an audit record (`AuditService`): node enrolled, claim id, key id, protection class, class.

Every refusal returns the same `UNAUTHENTICATED` "enrollment refused" (no oracle). Enrollment calls
MUST be rate limited per source address and per claim.

Residual risk: a TLS man-in-the-middle during enrollment sees the claim code and can enroll **its own**
key with it (it cannot reuse the node's proof). The real node's enrollment then fails, and the console
shows a node whose key fingerprint does not match the device. Operators SHOULD compare the key
fingerprint the device shows with the console after enrollment; provisioning files (§4.3) avoid the
exposure.

### 3.3 Node registry (connector)

Table `schema_zequent.edge_nodes`:

| Column | Type | Notes |
|---|---|---|
| `id` | uuid | the `node_id` |
| `organization_id` | uuid | from the claim, never changeable |
| `node_class` | enum | `INFRASTRUCTURE` or `PERSONAL` (§6.3); from the claim, never changeable |
| `display_name` | text | operator-editable |
| `status` | enum | `ACTIVE`, `SUSPENDED`, `REVOKED` |
| `allowed_suites` | int[] | default `{0x0101, 0x0102}` |
| `roles` | text[] | `relay`, `gateway` (plan D1); empty for `PERSONAL` |
| `active_key_id` | bytea(16) | FK to `edge_node_keys` |
| `credential_id` | uuid | `jti` of the node-bound edge credential |
| `enrolled_at`, `enrolled_claim_id`, `enrolled_runtime_version` | | provenance |
| `suspended_at/by`, `revoked_at/by`, `revoke_reason` | | lifecycle |

Table `schema_zequent.edge_node_keys` (history, never deleted, so old signed audit logs stay verifiable):
`key_id` (PK), `node_id`, `generation`, `alg`, `public_key`, `key_protection_claimed`,
`key_protection_attested` (nullable), `attestation_format`, `attestation_digest`,
`attestation_summary` (jsonb; the evidence itself is not kept), `valid_from`, `valid_to`, `end_reason`
(`ROTATED`, `REVOKED`, `REENROLLED`).

Table `schema_zequent.edge_node_assets`: `asset_id` (PK), `node_id`, `bound_at`, `bound_by`.

Columns on `asset_claims`: `node_class` (default `INFRASTRUCTURE`), `reenroll_node_id` (nullable,
§3.6).

Reserved for M4 (no column yet): reference to the node's tiny root key `K_root`.

### 3.4 Asset binding

1. An asset is bound to at most one node (`edge_node_assets.asset_id` unique).
2. Bindings come from enrollment (the assets the node created) or from an organization admin in the
   console (`assets:update` plus `edge_nodes:manage`). Moving an asset to another node is an audited
   admin action.
3. At Hello the platform serves `served = Hello.asset_sns ∩ bound assets of the node`. Data for any
   other asset is dropped (today's `UNDECLARED_ASSET` path), and commands for any other asset are never
   routed to the node. `served` is returned, signed, in `Welcome.served_asset_sns`.
4. A node listing an unbound asset is not refused (a newly attached adapter must not take the node
   down); the platform logs it once per session and the console offers to bind it. Not for `PERSONAL`
   nodes (§6.3).

### 3.5 Attestation (optional in v1)

1. `CompleteEnrollment` MAY carry `Attestation { format, evidence }`. Reserved formats:
   `TPM2_CERTIFY` (TPM2_Certify/Quote with EK/AK chain; the challenge is the qualifying data),
   `NXP_SE050`, `ANDROID_KEY_ATTESTATION` (Keystore certificate chain; the challenge is the
   attestation challenge), `APPLE_APP_ATTEST` (needs Apple's servers, so not usable air-gapped).
2. In v1 the platform stores format and digest and verifies nothing; `key_protection_attested` stays
   null. Verification and an organization policy that requires it come later (R-5, OD-2).

### 3.6 Rotation, renewal and re-enrollment

All three start with `BeginEnrollment(purpose)` and use the challenge once; all three are bound to the
TLS session by `channel_binding`.

- **Key rotation** (`RotateIdentityKey`, purpose `ROTATE`, node credential):

  ```
  T_rotate = enc_bytes("zqnt-edge-enroll-v1 rotate") || enc_str(organization_id) || enc_str(node_id)
          || enc_bytes(challenge) || enc_bytes(channel_binding) || enc_bytes(old_key_id)
          || u8(new_alg) || enc_bytes(new_public_key) || u8(key_protection) || enc_bytes(attestation_digest)
  ```

  signed by the **old** and the **new** key. Connector verifies both and switches the active key
  atomically (`valid_to`, `end_reason = ROTATED`, `generation + 1`); the old key is refused afterwards.
  If the node misses the response, it tries a Hello with the new key, then with the old one. Rotation
  MUST NOT be used after a suspected compromise: revoke and re-enroll.
- **Credential renewal** (`RenewCredential`, purpose `RENEW`, node credential):
  `T_renew = enc_bytes("zqnt-edge-enroll-v1 renew") || enc_str(organization_id) || enc_str(node_id)
  || enc_bytes(challenge) || enc_bytes(channel_binding) || enc_bytes(key_id)`, signed by the active
  key. Returns a new credential; the old one is deny-listed after an overlap (24 h infrastructure,
  10 min personal). The runtime renews when a third of the lifetime remains.
- **Re-enrollment** (lost key, replaced hardware, found device after revocation): an admin cuts a claim
  with `reenroll_node_id`. Enrollment with it keeps `node_id`, class and bindings, ends the previous key
  (`REENROLLED`), revokes the previous credential and sets `ACTIVE`. A normal claim can never take over
  an existing `node_id`.

## 4. Handshake

### 4.1 Canonical encoding

Transcripts are **not** protobuf bytes. Protobuf serialization is not canonical across
implementations (unknown fields are kept and re-emitted, default and ordering behaviour differs between
Go, Java, Python, Kotlin and Swift, and "deterministic" mode is only deterministic within one library
version). Signing re-encoded protobuf would make verification depend on library versions. Each
transcript is a fixed sequence of fields in this encoding:

| Notation | Encoding |
|---|---|
| `u8(v)`, `u32(v)`, `u64(v)` | unsigned, big-endian, fixed width |
| `i32(v)`, `i64(v)` | two's complement, big-endian, fixed width |
| `enc_bytes(b)` | `u32(len(b)) || b` |
| `enc_str(s)` | `enc_bytes(UTF-8 bytes of s)`; no normalization |
| `enc_list_str(l)`, `enc_list_u32(l)` | `u32(count)` then each element, in wire order |
| `enc_ts(t)` | `i64(seconds) || i32(nanos)` of the `google.protobuf.Timestamp` |
| `enc_dur(d)` | `i64(seconds) || i32(nanos)` of the `google.protobuf.Duration` |
| `opt(x)` | `u8(0)` if the message field is absent, else `u8(1) || x` |
| `enc_ack(a)` | `u32(epoch) || u32(cumulative_seq) || u32(selective_base) || enc_bytes(selective_bitmap)` |

Every transcript starts with `enc_bytes(label)`; labels are ASCII and unique per transcript type
(domain separation). Repeated fields are encoded in wire order; receivers MUST verify over the order
received and MUST NOT sort. A field holding the protobuf default is encoded as that value. Transcripts
are built from the decoded fields, never from frame bytes.

**Extension rule.** A field added later to `Hello`, `Welcome`, `HelloRetry` or `PlatformKey` is not
covered by a v1 signature. A receiver MUST NOT base a security decision on an uncovered field. A field
that needs integrity requires a new transcript version (`zqnt-edge-link-v2 …`).

### 4.2 Transcripts and channel binding

`organization_id` and `node_id` are lowercase canonical UUIDs. `organization_id` and
`channel_binding` are **never sent**: both sides know or compute them, so a Hello signed for one
organization or one TLS connection is useless in another.

**Channel binding** (R-4). `channel_binding` is the TLS 1.3 exporter of RFC 9266 ("tls-exporter"):
`TLS-Exporter(label = "EXPORTER-Channel-Binding", context = empty, length = 32)` of the TLS connection
the frame travels on. The node computes it from its TLS client connection, `edge-link` from its TLS
server session (JDK 25 `ExtendedSSLSession.exportKeyingMaterialData`, verified present; reaching the
`SSLSession` from Quarkus gRPC via `Grpc.TRANSPORT_ATTR_SSL_SESSION` is an assumption to verify; Go:
`credentials.TLSInfo.State.ExportKeyingMaterial` from the stream's peer, assumption to verify). This
requires TLS to terminate **in edge-link**: the ingress passes Edge Link traffic through by SNI (TCP
passthrough) instead of terminating it. On link kinds without a TLS connection between node and
edge-link (lean via a broker, relayed; M2/M4), `channel_binding` is empty and the platform accepts that
only for link kinds its policy lists (v1: none). A Hello on `ip-session` with an empty binding is refused.

**Hello** (signed by the node's identity key; `Hello.signature`):

```
T_hello = enc_bytes("zqnt-edge-link-v1 hello")
       || u32(crypto_suite)
       || enc_str(organization_id)          not sent
       || enc_str(node_id)
       || enc_bytes(identity_key_id)        Hello.identity_key_id, 16 bytes (new field 12)
       || enc_bytes(channel_binding)        not sent; 32 bytes on ip-session
       || enc_bytes(ephemeral_pub)          32 bytes, X25519
       || u64(monotonic_ms)
       || opt(enc_ts(wallclock))
       || enc_bytes(server_nonce)           Hello.server_nonce (new field 13); empty unless retried
       || enc_list_str(encodings)
       || enc_list_str(asset_sns)
       || enc_str(link_kind)
       || enc_str(runtime_version)
       || opt(enc_ack(downlink_acked))
```

**Welcome** (signed by the platform handshake key; `Welcome.signature`):

```
T_welcome = enc_bytes("zqnt-edge-link-v1 welcome")
         || enc_bytes(SHA-256(T_hello))
         || enc_bytes(platform_key.key_id)     16 bytes
         || enc_bytes(ephemeral_pub)           32 bytes, X25519
         || enc_str(session_id)
         || i64(clock_offset_ms)
         || opt(enc_ack(resume_from))
         || opt( enc_str(policy.revision) || opt(enc_dur(policy.ping_interval)) )
         || enc_list_str(served_asset_sns)     new field 8
```

Suite, encodings, channel binding and everything else the node sent are covered through
`SHA-256(T_hello)`.

**HelloRetry** (new downlink frame 8, signed by the platform handshake key):

```
T_retry = enc_bytes("zqnt-edge-link-v1 hello-retry")
       || enc_bytes(SHA-256(T_hello of the Hello being answered))
       || enc_bytes(platform_key.key_id)
       || enc_bytes(server_nonce)            32 random bytes
       || enc_ts(platform_time)
       || u8(reason)                         1 = CLOCK_UNTRUSTED, 2 = NONCE_REQUIRED
```

**Platform key certificate** (`PlatformKey`, signed by an anchor key):

```
T_pkey = enc_bytes("zqnt-edge-link-v1 platform-key")
      || enc_str(installation_id)
      || enc_bytes(anchor_key_id)
      || enc_bytes(key_id)
      || u8(key_alg)                          2 = ECDSA P-256
      || enc_bytes(public_key)                65 bytes
      || i64(not_before)                      Unix seconds
      || i64(not_after)                       Unix seconds
```

### 4.3 Platform keys and how the node trusts them

**Per installation, no Zequent-wide key** (R-3). Every installation (each customer's on-prem or
air-gapped platform, and each Zequent-operated environment) has its own anchor. Zequent holds no key
that nodes of a customer installation trust, so Zequent cannot impersonate a customer's platform, and a
compromise of one installation does not reach another.

1. **Anchor key** (ECDSA P-256). One per installation, plus at most one overlapping successor during
   rollover. It lives in the installation's OpenBao as Transit key `edge-link-anchor` (type
   `ecdsa-p256`, non-exportable) and signs only `T_pkey`. Without OpenBao (dev, local stack):
   `EDGE_LINK_ANCHOR_PRIVATE_KEY`, refused in prod mode by `DevKeyStartupGuard`. It MUST NOT be the
   service-token or credential key: a leaked credential key must not let anyone impersonate the
   platform to nodes, and the reverse. An offline anchor for military installs is OD-4.
2. **Handshake key** (ECDSA P-256). Each `edge-link` replica generates one in memory at start, never
   persists it, and has the anchor sign a `PlatformKey` for it valid for at most 72 h (default
   `not_before = now − 5 min`, `not_after = now + 48 h`), renewed every 12 h. Signing a Welcome needs no
   OpenBao call, and a stolen handshake key is useful only until it expires.

Node trust store:

1. The node pins one or two **anchor public keys** and the `installation_id`. It receives them in
   `CompleteEnrollmentResponse` (trust on first use over the enrollment TLS connection) or from a
   provisioning file or QR code (air-gapped installs, phones). When both exist they MUST match, or the
   node aborts enrollment.
2. The console shows the anchor fingerprint (`key_id` as hex, grouped); the installer SHOULD compare it
   with the node. For military and police installs the provisioning file or QR code SHOULD be used.
3. Anchor rollover: the successor anchor arrives through re-enrollment or a provisioning file. A signed
   in-band rollover frame is reserved.

### 4.4 Message flow and checks

```
node                                              edge-link (terminates TLS)
 | TLS 1.3, authorization: Bearer <node credential>  |
 | Hello(suite, node_id, key_id, e_N, wallclock, …, sig_N)   cb on both sides
 |-------------------------------------------------->| checks 1–8
 |               [clock untrusted or absent]         |
 |<--------------------------------------------------| HelloRetry(nonce, platform_time, pkey, sig)
 | Hello(…, server_nonce = nonce, new e_N, sig_N')   |
 |-------------------------------------------------->| checks 1–8, nonce instead of clock
 |<--------------------------------------------------| Welcome(e_P, session_id, offset, resume, policy,
 | verify pkey + sig_P; derive keys                  |         served_asset_sns, pkey, sig_P)
```

Platform, on a Hello, in this order:

1. The interceptor verified the bearer credential (signature, audience, expiry, deny-list, scope
   `edge`). Edge Link additionally requires the claim `node_id` (§6.1).
2. Structure: suite is a registered S1 value; `node_id` is a UUID; `identity_key_id` 16 bytes;
   `ephemeral_pub` 32 bytes; `signature` 64 bytes; at most 256 `asset_sns`, 16 `encodings`, strings at
   most 256 bytes. Otherwise `INVALID_ARGUMENT` "malformed hello" (`FAILED_PRECONDITION`
   "unsupported crypto suite" for an unregistered suite value).
3. The credential's `node_id` and `org_id` equal `Hello.node_id` and the node's organization.
4. Registry (cached, invalidated by change events, at most 60 s stale; 10 s for `PERSONAL`): node
   exists, status `ACTIVE`, `identity_key_id` is the active key, suite ∈ `allowed_suites`, key
   protection meets the organization minimum.
5. Compute `channel_binding` from this TLS session (or empty where policy allows) and verify the
   signature over `T_hello` with the active key.
6. Freshness, one of:
   - `server_nonce` non-empty: a nonce issued to this node on this stream within the last 60 s and not
     used before (atomic get-and-delete); the wall clock is then not checked.
   - `server_nonce` empty: `wallclock` present and `|platform_now − wallclock| ≤ 120 s` (OD-8).
     Otherwise send `HelloRetry` (`CLOCK_UNTRUSTED`) and wait for a second Hello. At most one
     `HelloRetry` per stream; a second Hello without a valid nonce is refused.
7. Replay: `SET NX` of `SHA-256(ephemeral_pub)` under the node's key, TTL twice the freshness window;
   an existing entry is refused. Inserted only after step 5.
8. Open the session (taking over an older one), compute `served_asset_sns`, send the signed Welcome.

Node, on the first downlink frame:

1. Anything other than `Welcome` or (once) `HelloRetry`: close the stream.
2. Verify `platform_key`: `anchor_key_id` pinned, `installation_id` matches, `key_alg = 2`, anchor
   signature over `T_pkey`, and validity: with trusted time `not_before ≤ now ≤ not_after`; without,
   `not_after` later than the persisted time high-water mark.
3. Verify the frame signature with `platform_key.public_key` over `T_welcome` or `T_retry`, computed
   with `SHA-256(T_hello)` of the Hello this node sent on this stream (which includes its own view of
   the channel binding).
4. On `HelloRetry`: adopt `platform_time` as trusted time (authenticated and bound to this Hello), raise
   the high-water mark, send a new Hello with a **new** ephemeral key and `server_nonce`.
5. On `Welcome`: key agreement (§5); a low-order platform ephemeral is refused. Only then apply
   `clock_offset_ms`, `resume_from`, `policy` and `served_asset_sns`.
6. No valid Welcome within 15 s of the Hello: close the stream.

### 4.5 Downgrade protection

- Suite and encodings are in `T_hello` (node signature) and covered by `SHA-256(T_hello)` in
  `T_welcome` (platform signature). Changing either breaks a signature (vector `negative[1]`).
- No negotiation: the platform accepts or refuses the one suite offered, against the registry. A node
  MUST NOT retry with another suite after a refusal; its suite is configuration.
- No unsigned mode: after enrollment a node MUST NOT accept an unsigned Welcome, and the platform MUST
  NOT accept an unsigned Hello. The current unsigned path is deleted when the signed path ships.
- Channel binding cannot be stripped: it is in the signed transcript, and the platform decides from
  the link kind (signed) whether an empty value is allowed.

### 4.6 Replay and relay protection

| Attack | Defence |
|---|---|
| Replaying a captured Hello | wall-clock window or single-use nonce; ephemeral-key replay cache; channel binding of a different TLS connection; the replayer lacks `e_N`'s private key |
| Relaying a live Hello through a TLS man-in-the-middle (compromised CA, inspection proxy, compromised ingress) | channel binding: the platform's binding differs from the node's, the signature fails |
| Replaying a Welcome or HelloRetry | bound to `SHA-256(T_hello)` of the node's current Hello |
| Replaying an old `PlatformKey` | validity window and time high-water mark |
| Replaying enrollment, rotation, renewal | single-use 5-minute challenge, channel binding, counted redemptions |
| Injecting frames after the handshake | TLS 1.3 terminating in edge-link, bound to the handshake |

### 4.7 Failure behaviour

| Condition | gRPC status | Description |
|---|---|---|
| No / invalid / revoked bearer credential | existing interceptor (`UNAUTHENTICATED` / `PERMISSION_DENIED`) | unchanged |
| Malformed Hello (step 2) | `INVALID_ARGUMENT` | `malformed hello` |
| Unregistered suite value | `FAILED_PRECONDITION` | `unsupported crypto suite` |
| Steps 3–7 fail for any reason | `UNAUTHENTICATED` | `handshake refused` |
| Registry or Redis unavailable | `UNAVAILABLE` | `try again` |

- The description MUST NOT say which check failed. The reason is logged, counted in
  `edge_link_handshake_refused{reason}` and, for revoked or suspended nodes, audited.
- For an unknown node or key the platform SHOULD still verify against a fixed dummy key so timing does
  not reveal whether the node exists.
- Failed handshakes MUST be rate limited per credential and source address (`RESOURCE_EXHAUSTED`).
- The node, on any refusal or failed check, backs off exponentially with jitter (1 s to 5 min), writes a
  local audit record, and never changes suite or drops the signature.

## 5. Session keys

After a valid Welcome both sides compute:

```
ss   = X25519(e_N_private, E_P) = X25519(e_P_private, E_N)     refuse if all-zero (low-order input)
th   = SHA-256( enc_bytes(T_hello) || enc_bytes(T_welcome) )
prk  = HKDF-Extract(salt = th, IKM = ss)                         HKDF-SHA-256, RFC 5869
K(name, L) = HKDF-Expand(prk, info = enc_bytes("zqnt-edge-link-v1 " + name) || u32(crypto_suite), L)

key_n2p  = K("key n2p", 32)      node → platform AEAD key
key_p2n  = K("key p2n", 32)      platform → node AEAD key
iv_n2p   = K("iv n2p", 12)       node → platform nonce base
iv_p2n   = K("iv p2n", 12)       platform → node nonce base
exporter = K("exporter", 32)     for later features (key confirmation, sealing to a session)
```

Ephemeral keys are fresh for every Hello (including after `HelloRetry`), from a CSPRNG, never reused.

Encryption inside TLS, decided:

1. **IP links, full profile (v1):** TLS 1.3, terminating in `edge-link`, bound to the handshake by the
   channel binding. No additional per-frame AEAD. The derived keys are computed (so every
   implementation is tested against the vectors from the start) and zeroized at session end. With
   channel binding, a party that terminates or relays TLS cannot take over a session; what remains is
   a compromise of `edge-link` itself, which is the platform.
2. **Lean (MQTT/HTTP batch through a broker), relayed and gateway paths (M2/M4):** end-to-end AEAD with
   these keys is REQUIRED before those paths ship, because a broker or relay sees the frames. Reserved
   for M2: nonce = `iv XOR (0x00000000 || u64(seq))`, AAD = frame header, AEAD per suite variant.
3. **Tiny (M4):** no handshake; pre-provisioned 256-bit `K_root` and per-epoch keys (plan §7.1, §10.2).
   Delivery of `K_root` during enrollment is reserved; labels beginning `zqnt-edge-tiny-v1` are reserved.
4. `PostBatch` stays refused until M2 specifies batch authentication.

## 6. Credentials, revocation and person-carried nodes

### 6.1 Bearer credential

Decision for v1: **keep the bearer credential as transport admission, bind it to the node, and take
identity from the signed Hello.**

- Why keep it: the interceptor rejects unauthenticated traffic before any frame is parsed; it carries
  the organization, the licence check and the deny-list; rate limits key on it cheaply.
- Enrollment mints it with `ServiceTokenIssuer.mintCredential` (Transit key `credential`):
  `sub = edge:node:<node_id>`, `scope = [edge]`, `org_id`, plus a **new claim `node_id`** (constant in
  `ServiceTokens` and the SDK constants). Lifetime: 365 days for `INFRASTRUCTURE`, 24 h for `PERSONAL`,
  both renewed by `RenewCredential`. It is recorded like console-issued credentials so it can be listed
  and revoked (assumption: `ServiceCredentialStore` is writable from the enrolling service; otherwise
  enrollment calls admin-console over gRPC).
- Edge Link refuses a credential without `node_id`. Console-issued edge credentials keep working for the
  adapter RPCs they serve today, not for Edge Link.
- Neither the credential alone nor the key alone opens a session. Replacing the bearer token by mTLS
  node certificates or a token-less handshake is OD-6.

### 6.2 Revocation

1. **Registry is authoritative.** `RevokeNode` sets `REVOKED` (final for that key), ends the active key
   and deny-lists the credential `jti`. `SuspendNode` sets `SUSPENDED` (reversible, no deny-list, no
   Revocation frame).
2. Connector publishes a node-change event; `edge-link` drops the cache entry and ends every open
   session of the node with `UNAUTHENTICATED` "handshake refused" (target: within 5 s of the action).
   Any later Hello fails step 4.
3. `edge-link` sends a `Revocation` frame (numbered downlink, acknowledged, resent) to every connected
   node of the organization with role `relay` or `gateway`, and the organization's current revoked list
   to each such node right after its Welcome. Best effort, also to the revoked node's own session just
   before closing it.
4. A node receiving a `Revocation` for other nodes MUST stop relaying and accepting their frames and
   persist the list. A node that finds its own `node_id` MUST end all sessions, erase session keys,
   credential and queued downlink, MUST NOT use that identity again, MAY erase the identity key, and
   MUST keep its local audit log. Zeroize remains the separate `node.zeroize` command.
5. A captured node cannot be relied on to obey; platform-side refusal is the control.
6. `Revocation` frames are authenticated by the session they travel in. Relayed beyond one session
   (M4) they need a platform signature; reserved.
7. Revoke and suspend are audited. Dual control: OD-7.

### 6.3 Person-carried nodes (R-2)

Individual soldiers and officers are assets. Their positions come from personal devices: a phone app
over LTE, a handheld or soldier MANET radio, a LoRa tracker. Such devices are often lost or captured.

**Which devices are nodes.** A phone running the Zequent app is an Edge Node of class `PERSONAL`. A
MANET radio or LoRa tracker that cannot run a node is not one: its position reports (MANET PLI, tiny
frames) reach the platform through an `INFRASTRUCTURE` gateway node that is explicitly bound to the
corresponding person assets (§3.4), and tiny trackers get their own `K_root` in M4.

**Rules for `PERSONAL` nodes:**

1. The class comes from the claim (`node_class = PERSONAL`) and cannot change.
2. A personal node is bound to **exactly one** asset, the person it is carried by (assumption: an asset
   type for persons has to be added to the asset model). Enrollment creates or binds only that asset;
   `BindAsset` refuses a second one; unbound `asset_sns` in its Hello are ignored without an offer to
   bind. It therefore cannot report for, or receive commands for, any other asset.
3. It has no `relay` or `gateway` role and its `RelayBatch` frames are dropped.
4. Accepted envelope bodies: telemetry samples and alerts of its own asset, command events for commands
   addressed to it, link reports. Capability sets are accepted only within an organization allow-list
   (default: none), so a captured phone cannot announce itself as able to run effector or vehicle
   commands.
5. Short-lived trust: credential 24 h; session maximum age 8 h (the platform closes the stream, the node
   handshakes again); registry cache staleness at most 10 s.
6. **Lost device, one action.** "Report lost" is available to the person's own account, their unit
   leader and organization admins, needs no second approval, and **revokes** the node (§6.2: sessions
   end within seconds, credential deny-listed). A found device re-enrolls through a re-enrollment QR
   code, keeping node and asset. The console shows the last position and time before revocation.
7. Key storage on phones: Android Keystore P-256 key, StrongBox when available, non-exportable; Apple
   Secure Enclave P-256 key with a `…ThisDeviceOnly` accessibility class (no backup, no sync). Whether
   the key is usable only while the phone is unlocked (strong, but background position reports stop
   while it is locked) or after first unlock (reports continue; a captured unlocked-once phone can still
   sign until revoked) is OD-3; recommended default "after first unlock" plus fast revocation.
8. A rooted or jailbroken phone cannot extract a hardware key but can use it. Attestation
   (`ANDROID_KEY_ATTESTATION`) detects this at enrollment only; this is a residual risk covered by
   revocation and the short credential.
9. The phone app (Kotlin, Swift) implements this spec natively or through the Go runtime compiled for
   mobile; either way it MUST pass the test vectors.

Positions of named persons are personal data; retention and visibility rules are a compliance decision
(OD-10), not part of this spec.

## 7. Key storage and zeroization on the node

| Secret | Storage | Lifetime | Erase |
|---|---|---|---|
| Identity private key | TPM / SE / Keystore / Secure Enclave, non-exportable; else sealed software key | until rotation or revocation | delete in hardware; for sealed keys delete the blob and the sealing key |
| Ephemeral X25519 private key | RAM | until `ss` is computed | overwrite right after key agreement |
| `ss`, `prk`, session keys, exporter | RAM | one session | overwrite at session end and on link loss; never persisted, no resumption |
| Bearer credential | file `0600` (owner = runtime user, dir `0700`); app-private storage on phones | until renewal | delete on revocation, zeroize, re-enrollment |
| Trust store (anchors, `installation_id`, `node_id`, `organization_id`, time high-water mark) | root-owned file read-only to the runtime; app-private storage | until re-enrollment | integrity matters more than secrecy |

Software keys:

1. `SOFTWARE_SEALED`: the P-256 private scalar is encrypted (AES-256-GCM or ChaCha20-Poly1305) under a
   key held in the device's TPM/SE, bound to the measured boot state where secure boot exists, and
   decrypted into memory only while the runtime runs. For boards without any TPM/SE.
2. `SOFTWARE_DEV`: plain file `0600`. The runtime logs a warning at start and reports the class.
3. No silent fallback: if the configured key store is unavailable, the node does not connect.

Limits:

- Go: `crypto/ecdh` and `crypto/ecdsa` keys cannot be wiped reliably (GC copies). Implementations keep
  secrets in `[]byte` they control and overwrite them, and SHOULD use `runtime/secret` once it leaves
  `GOEXPERIMENT` (assumption: an experiment in Go 1.26). Best effort, documented as such.
- Java (core): JCA private keys do not support `destroy()` (assumption, JDK 25). Core keeps ephemeral
  and handshake keys in memory only and overwrites the `byte[]` copies it holds.
- Crypto-erase: erasing the identity key and sealing key makes the encrypted queue unreadable (plan
  §10.2). Verified erase of flash is not claimed.

## 8. Test vectors

File: [`edge-link-handshake-v1.vectors.json`](edge-link-handshake-v1.vectors.json). Generated by a Go
1.26 program that uses only the standard library (`crypto/ecdsa` with RFC 6979 deterministic signing,
`crypto/ecdh`, `crypto/hkdf`, `crypto/sha256`) and reproducible byte for byte. Cross-checked with the
JDK 25 providers (`SHA256withECDSAinP1363Format`, `X25519`, `HmacSHA256`): every signature verifies,
and shared secret, transcript hash, PRK and every derived key match.

| Section | Content |
|---|---|
| `inputs` | 32-byte private values: node identity `00..1f`, anchor `20..3f`, platform handshake `40..5f`, node ephemeral `60..7f`, platform ephemeral `80..9f`, challenge `a0..bf`, server nonce `c0..df`, rotation new key `e0..ff`; `tls_channel_binding` = SHA-256("zqnt test tls-exporter channel binding"); fixed `organization_id`, `node_id`, `installation_id`, claim code |
| `keys` | public keys (SEC 1 uncompressed) and key ids |
| `platform_key_certificate` | `T_pkey`, anchor signature (`not_before` 2026-11-01T00:00Z, `not_after` 2026-11-04T00:00Z) |
| `hello` | `T_hello`, signature, `SHA-256(T_hello)` |
| `welcome` | `T_welcome`, signature |
| `key_schedule` | `ss`, `th`, `prk`, `key_n2p`, `key_p2n`, `iv_n2p`, `iv_p2n`, `exporter` (suite `0x0101`) |
| `hello_retry` | Hello without wall clock, `T_retry` + signature, second Hello with nonce + signature |
| `enrollment_proof` | normalized code, `claim_digest`, `T_proof`, signature |
| `key_rotation` | `T_rotate`, signatures by old and new key |
| `credential_renewal` | `T_renew`, signature |
| `negative` | reordered `asset_sns` and changed suite with the original signature (must not verify); all-zero X25519 peer (must be refused) |

Hello values: suite `0x0101`, `monotonic_ms` 123456789, wall clock 1793534400 s + 250000000 ns,
encodings `["full"]`, assets `["SIM-DRONE-01","SIM-RADAR-07"]`, link kind `ip-session`, runtime
`3.0.0`, `downlink_acked` = {1, 41, 0, `05`}. Welcome values: session
`5d2f1e8a-9b47-4c30-a6d1-0e7f3b2c9a84`, offset −1500 ms, `resume_from` = {3, 1200, 0, empty}, policy
revision `PT15S`, ping 15 s, served `["SIM-DRONE-01"]`.

Spot values:

```
tls_channel_binding        cfad0fa7708add4526830867b0ecc283e00040101aad4b78b742d872412839fb
node_identity_key_id       a5fa57dcb4ae880712a7b69586f5cca4
anchor_key_id              a9c6451c6ffc4d2ccf7043e60e4d3cee
platform_handshake_key_id  a9b80dbc19cd6c50d7cf069cca348f7f
SHA-256(T_hello)           867f6a17ba59041acd6d6d1c56c277ddb382f12754300b8e113b1ce29a702385
shared secret              fbfb11adeb1d6f71c0571bc1b5dd87519f9a6620b10a5ebc314cbd420c43ba43
transcript hash th         3839a833f189e4125c854bf6a04bfa68e09a05af1a5718a5c7fe51832b8a7d7a
key_n2p                    f2e128f97eba2b6a13c980e73ea6e9a07105c20b757e3d3f656b50f16f745d27
```

Every implementation (zqnt-api Go helper, Go runtime, core Java, phone app) MUST pass all sections in
unit tests, reading the file (copied into test resources, never regenerated). Signers are tested by
verifying their own output, since ECDSA signatures need not be deterministic. Not covered yet: ECDSA
edge cases (invalid points, `r` or `s` out of range); add a set such as Wycheproof's P-256 cases when
the verifiers are built.

## 9. Recommendations awaiting CTO confirmation, and open decisions

These map to the last task box of zequent/zqnt-core#370. Each needs an answer or an explicit deferral
with a date.

### 9.1 Recommendations (written into this spec, awaiting confirmation)

| # | Recommendation | Where |
|---|---|---|
| R-1 | Node identity and platform keys are ECDSA P-256 in S1 (deviation from plan D9: TPM 2.0, ATECC608B and phones do not hold Ed25519 keys); X25519 stays for the ephemeral exchange | §1, §2.2 |
| R-2 | Person-carried devices are `PERSONAL` nodes: one bound asset, no relay/gateway role, capability allow-list, 24 h credentials, 8 h sessions, one-action "report lost" that revokes | §6.3 |
| R-3 | One platform anchor per installation, in that installation's OpenBao; no Zequent-wide key | §4.3 |
| R-4 | TLS exporter channel binding (RFC 9266) in every node-signed transcript; TLS terminates in edge-link (ingress passthrough) | §4.2 |
| R-5 | Attestation optional in v1 (stored, not verified); an organization policy can require it later | §3.5 |

### 9.2 Open decisions

| # | Decision | Recommendation | Needed before |
|---|---|---|---|
| OD-1 | Timing of S2 (FIPS/CNSA) and S3 (PQ hybrid) | Keep reserved; S2 when the first customer requiring FIPS 140-3 signs; S3 after M4 | nothing in v1 |
| OD-2 | When attestation becomes required, for which customers, which formats first | TPM2 and Android key attestation first; required by policy for military/police organizations once verification exists | node registry contract (field set) |
| OD-3 | Phone key usable only while unlocked, or after first unlock | After first unlock (positions keep flowing) plus fast revocation; "while unlocked" as an organization option | phone app |
| OD-4 | Anchor custody in military/air-gapped installs: OpenBao Transit, or an offline anchor/HSM (then one long-lived handshake key per installation instead of per-replica keys) | OpenBao by default; offline anchor as documented option | core key manager |
| OD-5 | Software keys in production: refused, or allowed per organization | `SOFTWARE_SEALED` minimum by default; `SOFTWARE_DEV` only on dev installations | enrollment |
| OD-6 | Bearer credential long term: keep, replace by mTLS node certificates, or token-less | Keep in 3.0 (node-bound); revisit with S2 | nothing in v1 |
| OD-7 | Dual control for revoke and zeroize (plan §14) | No dual control for revoke or "report lost" (speed after loss matters); dual control for zeroize | console |
| OD-8 | Freshness window | 120 s; nodes outside it use HelloRetry | core edge-link |
| OD-9 | First customer and classification level (plan §14 Q3: police VS-NfD, Bundeswehr, NATO partner) | Decide before promising anything for classified traffic: S1 is commercial crypto without approval; classified traffic needs approved crypto underneath | sales commitments |
| OD-10 | Retention and visibility of person positions (personal data) | Compliance decision (CEO), before personal nodes ship | phone app release |
| OD-11 | Identity key rotation cadence | No forced cadence; rotate on re-enrollment and hardware change | Go runtime |

## 10. Contract changes

### 10.1 zqnt-api (public, additive only)

`proto/v3/zqnt/edgelink/v3/edge_link.proto`:

```proto
message Hello {
  // ... fields 1-11 unchanged ...
  bytes identity_key_id = 12;          // key_id of the identity key that signed this Hello
  bytes server_nonce = 13;             // echo of HelloRetry.server_nonce; empty otherwise
}

message Welcome {
  // ... fields 1-6 unchanged ...
  PlatformKey platform_key = 7;        // certificate of the key that signed this Welcome
  repeated string served_asset_sns = 8;
}

message DownlinkFrame {
  reserved 9 to 15;                    // was 8 to 15
  oneof frame {
    // ... 1-7 unchanged ...
    HelloRetry hello_retry = 8;
  }
}

message PlatformKey {
  string installation_id = 1;
  bytes anchor_key_id = 2;
  bytes key_id = 3;
  uint32 key_alg = 4;                  // signature algorithm registry: 2 = ECDSA P-256
  bytes public_key = 5;                // SEC 1 uncompressed
  int64 not_before = 6;                // Unix seconds
  int64 not_after = 7;
  bytes signature = 8;                 // anchor signature over T_pkey, r||s
}

enum HelloRetryReason {
  HELLO_RETRY_REASON_UNSPECIFIED = 0;
  HELLO_RETRY_REASON_CLOCK_UNTRUSTED = 1;
  HELLO_RETRY_REASON_NONCE_REQUIRED = 2;
}

message HelloRetry {
  bytes server_nonce = 1;
  google.protobuf.Timestamp platform_time = 2;
  HelloRetryReason reason = 3;
  PlatformKey platform_key = 4;
  bytes signature = 5;
}

// Constants for Hello.crypto_suite (the field stays uint32).
enum CryptoSuite {
  CRYPTO_SUITE_UNSPECIFIED = 0;
  CRYPTO_SUITE_S1_CHACHA20_POLY1305 = 257;   // 0x0101
  CRYPTO_SUITE_S1_AES_256_GCM = 258;         // 0x0102
}
```

The channel binding is computed, never sent, so it needs no field. The `Hello`/`Welcome` comments and
the frame-numbering comment block change to point at this spec; moving the `DownlinkFrame` reserved
range is wire-additive.

New file `proto/v3/zqnt/edgelink/v3/edge_enrollment.proto`, same package (the Go runtime and the phone
app depend only on zqnt-api, so node-facing RPCs must be public):

```proto
service EdgeEnrollmentService {
  rpc BeginEnrollment(BeginEnrollmentRequest) returns (BeginEnrollmentResponse);           // anonymous
  rpc CompleteEnrollment(CompleteEnrollmentRequest) returns (CompleteEnrollmentResponse);  // anonymous
  rpc RotateIdentityKey(RotateIdentityKeyRequest) returns (RotateIdentityKeyResponse);     // node credential
  rpc RenewCredential(RenewCredentialRequest) returns (RenewCredentialResponse);            // node credential
}

enum EnrollmentPurpose { ENROLLMENT_PURPOSE_UNSPECIFIED = 0; ENROLLMENT_PURPOSE_ENROLL = 1;
                         ENROLLMENT_PURPOSE_ROTATE = 2; ENROLLMENT_PURPOSE_RENEW = 3; }
enum KeyProtection { KEY_PROTECTION_UNSPECIFIED = 0; KEY_PROTECTION_SOFTWARE_DEV = 1;
                     KEY_PROTECTION_SOFTWARE_SEALED = 2; KEY_PROTECTION_TPM = 3;
                     KEY_PROTECTION_SECURE_ELEMENT = 4; KEY_PROTECTION_MOBILE_TEE = 5;
                     KEY_PROTECTION_MOBILE_SECURE_HW = 6; }
enum AttestationFormat { ATTESTATION_FORMAT_UNSPECIFIED = 0; ATTESTATION_FORMAT_TPM2_CERTIFY = 1;
                         ATTESTATION_FORMAT_NXP_SE050 = 2; ATTESTATION_FORMAT_ANDROID_KEY_ATTESTATION = 3;
                         ATTESTATION_FORMAT_APPLE_APP_ATTEST = 4; }
enum NodeClass { NODE_CLASS_UNSPECIFIED = 0; NODE_CLASS_INFRASTRUCTURE = 1; NODE_CLASS_PERSONAL = 2; }

message BeginEnrollmentRequest  { EnrollmentPurpose purpose = 1; }
message BeginEnrollmentResponse { bytes challenge = 1; google.protobuf.Timestamp expires_at = 2; }

message IdentityKey { uint32 alg = 1; bytes public_key = 2; KeyProtection protection = 3; }
message Attestation { AttestationFormat format = 1; bytes evidence = 2; }
message EnrollingAsset { string sn = 1; string name = 2; string vendor = 3; string type = 4; }

message CompleteEnrollmentRequest {
  string claim_code = 1;
  bytes challenge = 2;
  IdentityKey identity_key = 3;
  repeated uint32 crypto_suites = 4;
  Attestation attestation = 5;
  repeated EnrollingAsset assets = 6;
  string runtime_version = 7;
  string display_name = 8;             // not signed; the operator can change it
  bytes signature = 9;                 // over T_proof
}

message TrustAnchor { bytes key_id = 1; uint32 alg = 2; bytes public_key = 3; }

message CompleteEnrollmentResponse {
  string node_id = 1;
  string organization_id = 2;
  string organization_name = 3;
  string installation_id = 4;
  repeated TrustAnchor anchors = 5;
  string credential = 6;               // node-bound edge credential, shown once
  google.protobuf.Timestamp credential_expires_at = 7;
  bytes identity_key_id = 8;
  repeated uint32 allowed_suites = 9;
  NodeClass node_class = 10;
}

message RotateIdentityKeyRequest {
  bytes challenge = 1; bytes old_key_id = 2; IdentityKey new_key = 3; Attestation attestation = 4;
  bytes signature_old = 5; bytes signature_new = 6;
}
message RotateIdentityKeyResponse { bytes identity_key_id = 1; }
message RenewCredentialRequest  { bytes challenge = 1; bytes key_id = 2; bytes signature = 3; }
message RenewCredentialResponse { string credential = 1; google.protobuf.Timestamp credential_expires_at = 2; }
```

Also in zqnt-api: a Go helper package (e.g. `go/v3/edgelink/handshake`) with the transcript encoders,
key id and key schedule, tested against the vectors, shared by the runtime and Go tools.

### 10.2 zqnt-contracts (internal), package `zqnt.edgenode.v3`

`proto/v3/zqnt/edgenode/v3/edge_node.proto` (imports `zqnt.edgelink.v3` for the shared enums after
`scripts/sync-api-protos.sh`):

```proto
package zqnt.edgenode.v3;

service EdgeNodeRegistryService {
  rpc EnrollNode(EnrollNodeRequest) returns (EnrollNodeResponse);          // edge-link only
  rpc GetNode(GetNodeRequest) returns (GetNodeResponse);                   // edge-link (cached)
  rpc ListNodes(ListNodesRequest) returns (ListNodesResponse);             // console
  rpc UpdateNode(UpdateNodeRequest) returns (UpdateNodeResponse);          // display name, roles, suites
  rpc RotateNodeKey(RotateNodeKeyRequest) returns (RotateNodeKeyResponse); // edge-link only
  rpc RecordCredential(RecordCredentialRequest) returns (RecordCredentialResponse);
  rpc SuspendNode(SuspendNodeRequest) returns (SuspendNodeResponse);
  rpc ReinstateNode(ReinstateNodeRequest) returns (ReinstateNodeResponse);
  rpc RevokeNode(RevokeNodeRequest) returns (RevokeNodeResponse);          // also "report lost"
  rpc BindAsset(BindAssetRequest) returns (BindAssetResponse);
  rpc UnbindAsset(UnbindAssetRequest) returns (UnbindAssetResponse);
  rpc ListRevokedNodes(ListRevokedNodesRequest) returns (ListRevokedNodesResponse); // for relays
}

enum NodeStatus { NODE_STATUS_UNSPECIFIED = 0; NODE_STATUS_ACTIVE = 1;
                  NODE_STATUS_SUSPENDED = 2; NODE_STATUS_REVOKED = 3; }

message NodeKey {
  bytes key_id = 1; uint32 alg = 2; bytes public_key = 3; uint32 generation = 4;
  zqnt.edgelink.v3.KeyProtection protection_claimed = 5;
  zqnt.edgelink.v3.KeyProtection protection_attested = 6;   // UNSPECIFIED = not attested
  zqnt.edgelink.v3.AttestationFormat attestation_format = 7;
  bytes attestation_digest = 8;
  google.protobuf.Timestamp valid_from = 9;
  google.protobuf.Timestamp valid_to = 10;
  string end_reason = 11;
}

message EdgeNode {
  string node_id = 1; string organization_id = 2; string display_name = 3; NodeStatus status = 4;
  zqnt.edgelink.v3.NodeClass node_class = 5;
  NodeKey active_key = 6; repeated uint32 allowed_suites = 7; repeated string roles = 8;
  repeated string asset_sns = 9; string credential_id = 10;
  google.protobuf.Timestamp enrolled_at = 11; string enrolled_claim_id = 12;
  string enrolled_runtime_version = 13;
  google.protobuf.Timestamp revoked_at = 14; string revoked_by = 15; string revoke_reason = 16;
}

message EnrollNodeRequest {
  zqnt.common.v3.RequestContext context = 1;
  string claim_code = 2; bytes challenge = 3;
  bytes channel_binding = 4;                    // computed by edge-link for its TLS session
  zqnt.edgelink.v3.IdentityKey identity_key = 5; repeated uint32 crypto_suites = 6;
  zqnt.edgelink.v3.Attestation attestation = 7; repeated zqnt.edgelink.v3.EnrollingAsset assets = 8;
  string runtime_version = 9; string display_name = 10; bytes signature = 11;
}
message EnrollNodeResponse { EdgeNode node = 1; }
// The remaining request/response messages carry context + node_id plus their obvious fields;
// RotateNodeKeyRequest also carries channel_binding.
```

`zqnt.asset.v3.CreateClaimRequest` and `zqnt.asset.v3.AssetClaim` gain `node_class` and
`reenroll_node_id` (additive).

## 11. Implementation steps per repository

Order per CLAUDE.md: zqnt-api → zqnt-contracts → zqnt-sdk-go → core; console, deployment and the phone
app independently.

1. **zqnt-api**: this spec and vectors (this PR). Then the proto changes of §10.1, regenerated Go and
   Python, and the Go `handshake` helper with vector tests.
2. **zqnt-contracts**: sync zqnt-api protos; add `zqnt.edgenode.v3` (§10.2) and the claim fields;
   regenerate.
3. **zqnt-sdk-go** (zqnt-sdk-go#19): replace `Signer` with an identity provider (`Suite`, `KeyID`,
   `Sign`) and key stores: software file (DEV), sealed software (TPM-sealed), TPM 2.0 P-256, ATECC608B
   later; channel binding from the TLS connection (the `ipsession` handshake function receives it);
   fresh X25519 per Hello; transcripts from the helper; Welcome/HelloRetry verification and time
   high-water mark; trust store; `enroll` / `rotate` / `renew` commands and the renewal loop; erase on
   revocation; delete the unsigned path.
4. **core**
   - `components/tenancy`: `node_id` claim constant; `GrpcAccessPolicy` anonymous entries for
     `BeginEnrollment`/`CompleteEnrollment`, edge entries for `RotateIdentityKey`/`RenewCredential`.
   - `connector`: Flyway migration (`edge_nodes`, `edge_node_keys`, `edge_node_assets`, claim
     columns); `EdgeNodeRegistryService` with proof verification, claim consumption, asset creation and
     binding, class rules, audit; change events on Redis pub/sub.
   - `edge-link`: TLS termination in the service and channel binding from the `SSLSession`;
     `EdgeEnrollmentService` (challenges, credential minting and recording); platform key manager
     (anchor via OpenBao Transit `edge-link-anchor`, dev env key behind `DevKeyStartupGuard`, in-memory
     handshake keys, certificate renewal); Hello checks 1–8, HelloRetry, replay cache, generic
     refusals, rate limits, metrics; signed Welcome with `served_asset_sns`; session keys derived and
     zeroized; `PERSONAL` rules (session age, envelope and capability filtering); registry cache;
     Revocation fan-out; delete the unsigned path; native reflection registrations and a local native
     build proving P-256 / X25519 / TLS exporter work in the native image.
   - `admin-console`: REST for nodes (list, rename, roles, suspend, reinstate, revoke, report lost,
     bind/unbind, enrollment and re-enrollment claims with QR codes) and the anchor fingerprint.
5. **console**: Edge Nodes screen (status, class, key protection with development badge, attestation
   state, bound and unbound assets, last position of a lost personal device, report lost / revoke /
   suspend, anchor fingerprint).
6. **phone app** (new; repository to be decided): Keystore / Secure Enclave key, enrollment by QR code,
   transcripts and vectors, position reporting as a `PERSONAL` node.
7. **simulator**: enroll simulated nodes with `SOFTWARE_DEV` keys through a claim.
8. **deployment**: ingress TCP passthrough (SNI) for Edge Link and a certificate for edge-link;
   OpenBao Transit key `edge-link-anchor` (`ecdsa-p256`) and policy; dev values.
9. **zqnt-docs**: operator guide for enrollment, fingerprint check, lost devices and revocation; a
   security note that S1 has no national approval.
