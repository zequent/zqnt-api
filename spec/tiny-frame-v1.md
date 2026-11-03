# Tiny frames, version 1

| | |
|---|---|
| Status | Draft for CTO review |
| Issue | zequent/zqnt-core#374 (part of #322, phase M2) |
| Schema registry | [`proto/v3/tiny_schemas.json`](../proto/v3/tiny_schemas.json) (version 1) |
| Contract | `Capability.tiny_schema_id` (`zqnt/capability/v3/capability.proto`), `Hello.encodings`, `RelayItem`, `RelayDelivery.node_tag` (`zqnt/edgelink/v3/edge_link.proto`) |
| Source plan | Transport plan "Edge nodes in the field": D4, D8, D9, §5.2, §5.4, §7, §10.2 |
| Related | [`edge-link-handshake-v1.md`](edge-link-handshake-v1.md) §1 rule 4 and §5 item 3 (labels `zqnt-edge-tiny-v1…` reserved there) |
| Test vectors | [`tiny-frame-v1.vectors.json`](tiny-frame-v1.vectors.json) |
| Deviations from the plan | Full 16-byte AEAD tag (§3.3), epoch in the header (§2), no `relayed` header bit (§2) |

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are used as in RFC 2119 and RFC 8174.

## 0. Scope

A tiny frame is a fixed binary encoding of at most **48 bytes**, sealed end to end with an AEAD
under a pre-provisioned 256-bit key, so positions, alarms, status, short command replies and short
commands fit LoRa at slow data rates, an ExpressLRS/MAVLink payload and an Iridium SBD message.
Relays and gateways carry tiny frames as opaque bytes (`RelayItem.frame`, `RelayDelivery.frame`);
only the node and the platform can read or forge them.

In scope: byte layout and limits, the crypto suites, the key schedule from `K_root`, nonces, the
replay window, the standard schemas and their registry, deliverability of commands.

Out of scope (later phases): how `K_root` reaches the node and the platform (enrollment, M4; until
then it is provisioned out of band, see §4.3), ACK, TIME_SYNC, BEACON and SCHEMA_SAMPLE frames
(ids reserved, M3/M4), link drivers (M3), relay mode (M4), per-organization schema assignment.

## 1. Encoding conventions

All integers are big-endian, fixed width. `u8/u16/u32` are unsigned, `i8/i16/i32` two's
complement. **Frame time** `t` is a `u32` of whole seconds since **2025-01-01T00:00:00Z** (Unix
1735689600); it covers until 2161. Coordinates are `i32` in units of 1e-7 degree (WGS 84);
decoders divide the integer by 1e7 in IEEE double precision.

## 2. Frame layout

```
 0        1        2        4             8             12                    n-16      n
 +--------+--------+--------+-------------+-------------+---------------------+---------+
 |  hdr   | suite  | epoch  |  node_tag   |   counter   | ciphertext          | tag     |
 |  u8    |  u8    |  u16   |    u32      |    u32      | (schema u16 + body) | 16 B    |
 +--------+--------+--------+-------------+-------------+---------------------+---------+
 \___________________ header, 12 bytes, AAD ___________/
```

| Field | Meaning |
|---|---|
| `hdr` bits 7–6 | version, `1` |
| `hdr` bit 5 | ACK_REQUESTED: the sender wants an acknowledgement (ACK frame, M3) |
| `hdr` bit 4 | reserved, MUST be 0 |
| `hdr` bit 3 | MORE: the sender has more frames queued for this receive window |
| `hdr` bits 2–0 | lane, the `Lane` enum value 1–5 (`LANE_ALARM` … `LANE_BULK`); 0, 6 and 7 are invalid |
| `suite` | tiny suite id (§3) |
| `epoch` | key epoch (§4.2) |
| `node_tag` | the node's pseudonym for this epoch (§4.1); the platform maps it back to the node |
| `counter` | per-node, per-direction frame counter of this epoch, starting at 1 (§5) |
| ciphertext | AEAD encryption of the plaintext `u16(schema) ‖ body` |
| `tag` | the AEAD tag, 16 bytes |

Limits:

| | Bytes |
|---|---|
| header | 12 |
| AEAD tag | 16 |
| schema id | 2 |
| fixed overhead | **30** (smallest valid frame, empty body) |
| largest frame | **48** |
| largest body | **18** |

A frame shorter than 30 or longer than 48 bytes is malformed. The lane is part of the
authenticated header, so a relay may read it to prioritise but cannot change it. Every schema has
a fixed lane (§7); a receiver MUST drop an authentic frame whose lane does not match its schema.

The plan had a `relayed` header bit. It is dropped: the header is authenticated, so a relay could
not set it without breaking the frame; relays report hops in `RelayItem.relay_hop` instead.

## 3. Suites

### 3.1 Registry

The tiny suite is a one-byte registry of its own (handshake spec §1 rule 4); it is not
`Hello.crypto_suite`.

| Value | Name | AEAD | Key | Nonce | Tag |
|---|---|---|---|---|---|
| `0x00` | invalid | | | | |
| `0x01` | T1-C, default | ChaCha20-Poly1305 (RFC 8439) | 32 B | 12 B | 16 B |
| `0x02` | T1-G | AES-256-GCM (NIST SP 800-38D) | 32 B | 12 B | 16 B |
| `0x10`–`0x1F` | reserved for S2 (FIPS / CNSA 1.0-style) | | | | |
| everything else | reserved | | | | |

A receiver MUST treat an unknown or reserved suite as malformed. The suite a node uses is
configuration (the node registry decides what the platform accepts, as for `allowed_suites`); there
is no negotiation on a tiny link. T1-C is the default for the same reason as S1-C (nodes without
AES instructions). Both suites only use AEADs available in the standard libraries the platform
builds on: Go `crypto/cipher` and `golang.org/x/crypto/chacha20poly1305`, the JDK's SunJCE
(`ChaCha20-Poly1305`, `AES/GCM/NoPadding`).

### 3.2 Post-quantum note

Tiny frames use only symmetric 256-bit keys; S3 (PQ hybrid, handshake spec §1) does not apply.

### 3.3 Why the tag is 16 bytes (deviation from the plan)

The plan (§7.1) truncated the tag to 8 bytes with AES-256-CCM or ChaCha20-Poly1305, for 18 bytes
of overhead. This spec keeps the **full 16-byte tag**:

1. Neither Go's standard library nor `x/crypto` implements CCM, and the JDK has no CCM either
   (only Bouncy Castle). A CCM or a truncated-Poly1305 verifier would be our own construction
   around a primitive, which we do not write.
2. RFC 8439 and SP 800-38D define 16-byte tags for these AEADs; truncating GCM below 12 bytes is
   discouraged by SP 800-38D Appendix C, and truncated Poly1305 has no standard profile.
3. An 8-byte tag lets an attacker on the air try to forge with probability 2^-64 per frame; on
   links where every frame costs airtime that is acceptable in theory, but it buys only 8 bytes.

Cost: overhead 30 instead of 18 bytes (with the explicit epoch), so a frame has at most 18 body
bytes instead of the plan's 30. All four standard uplink schemas and the standard commands fit
(§7); command params are limited to 12 bytes and command results to 13. **Decision for the CTO**
(§11, T-1).

## 4. Keys

### 4.1 Key schedule

Each node that may use tiny links has a **root key** `K_root` of 32 bytes from a CSPRNG. The
platform holds the same `K_root` for that node. Both sides derive, with HKDF-SHA-256 (RFC 5869):

```
prk      = HKDF-Extract(salt = "zqnt-edge-tiny-v1", IKM = K_root)
K_epoch  = HKDF-Expand(prk, info = "zqnt-edge-tiny-v1 key" ‖ u8(suite) ‖ u16(epoch), L = 32)
node_tag = u32( HKDF-Expand(prk, info = "zqnt-edge-tiny-v1 tag" ‖ u16(epoch), L = 4) )
```

Labels are ASCII without terminator. `K_epoch` depends on the suite, so one root key never keys
two different AEADs. `node_tag` does not depend on the suite; it changes every epoch, so frames of
two epochs cannot be linked by their tag (traffic analysis, plan §10.1). The plan derived the tag
from `K_epoch`; deriving it from `prk` gives the same unlinkability and lets the platform index tags
without the suite.

### 4.2 Epochs

`epoch` is a `u16`. A sender SHOULD use **whole days since 2025-01-01T00:00Z** of its own clock
(epoch 671 is 2026-11-03), and MUST:

- never use an epoch lower than one it already used with this `K_root`;
- move to a higher epoch before the counter of the current one would exceed `2^32 − 1`;
- delete `K_epoch` of epochs it no longer sends or receives in.

A sender without a trusted clock keeps its last epoch and moves on by counter exhaustion or on a
TIME_SYNC frame (M3). Because every `K_epoch` is derived from the long-lived `K_root`, deleting old
epoch keys does **not** give forward secrecy against a captured `K_root`; root keys are rotated by
re-provisioning (plan §10.2), which is what bounds the exposure.

### 4.3 Provisioning (until M4)

`K_root` is generated by the platform (or by the provisioning tool on a trusted machine), written
to the node during installation (USB provisioning or over an authenticated full-profile session)
and stored wrapped by the node's TPM or secure element, never in clear on flash. The platform
stores it encrypted (OpenBao Transit or the connector's credential encryption). Delivery inside
enrollment (`edge-link-handshake-v1.md` §3.3, "reserved for M4") replaces the manual step later.
A node MUST zeroize `K_root` on `node.zeroize` and on revocation.

## 5. Nonce and counter

```
nonce = u8(direction) ‖ 0x00 0x00 0x00 ‖ u32(node_tag) ‖ u32(counter)          12 bytes
direction: 0x01 = node → platform (uplink), 0x02 = platform → node (downlink)
AAD   = header bytes 0..11
```

The direction is not sent; each side knows which way it receives, so a frame reflected back to its
sender does not authenticate.

Nonce uniqueness is what keeps both AEADs secure. The `(K_epoch, direction, counter)` triple MUST
never repeat:

- The node keeps one uplink counter per epoch; the platform keeps one downlink counter per node and
  epoch. Counters start at 1; 0 is invalid.
- A sender MUST persist its counter **before** it sends with it. Recommended: reserve blocks
  (write `counter + 1024` to durable storage, then use the block), so a crash skips counters
  instead of reusing them.
- A frame that is resent (no acknowledgement) is **sealed again with a new counter**. Re-sending the
  same bytes is allowed (it is a replay the receiver drops), never re-sealing different content
  under an old counter.
- The platform side of a downlink counter is shared by every replica of edge-link (Redis `INCR`),
  never per replica.

## 6. Receiving

A receiver processes a frame in this order and stops at the first failure:

1. **Header** (§2): length 30–48, version 1, reserved bit 0, lane 1–5, known suite, counter ≠ 0.
   Otherwise: malformed.
2. **Candidates**: the platform looks up `(epoch, node_tag)` in its index of tiny-enabled nodes;
   a node accepts only its own tag (and, as a relay, forwards others unopened). Tags are 32 bits;
   two nodes may share one in an epoch, so the platform MUST try every candidate.
3. **Open** with `K_epoch` of the candidate for the header's suite and epoch, the nonce of §5 and
   the header as AAD. No candidate opens it: not authentic, dropped silently (counted).
4. **Replay window** (below), only after the frame authenticated.
5. **Schema**: the schema id is known for this direction, the lane matches, the body size is one
   the registry allows. Otherwise the frame is dropped as malformed (it was authentic, so its
   counter stays recorded).

### 6.1 Replay window

The receiver keeps, per node and direction, a window for the **current epoch** E (highest counter
seen and a 64-bit bitmap) and one for the **previous epoch** E−1, so frames delayed across the
epoch change by store-and-forward or relays are not lost.

| Frame epoch e | Rule |
|---|---|
| no window yet, or e > E | accept; the new current window starts at this counter; the old current becomes the previous window if e = E+1, otherwise the previous window is cleared |
| e = E | sliding window: a counter above the highest is accepted and slides the window; one within 64 below the highest is accepted once; anything older or seen is a replay |
| e = E−1 and a previous window exists | the same rule against the previous window |
| anything else | replay |

Window size 64 matches LoRa and SBD burst sizes; a receiver MAY use a larger window. On the
platform the window lives in Redis and is updated atomically (one replica may receive a frame
through one gateway and another replica the same frame through a second gateway; plan §7.2).
After a restart without state the platform accepts the next frame of the current epoch; a replay of
older frames within the window after that restart is the residual risk, bounded by the epoch: the
platform SHOULD refuse frames of an epoch more than one day older than its own clock's epoch.

For tiny frames the counter is also the message sequence of plan §5.2 (dedup across paths):
duplicates that several gateways deliver are dropped by the same window.

## 7. Schemas

The registry [`proto/v3/tiny_schemas.json`](../proto/v3/tiny_schemas.json) is normative for field
layouts, unknown markers, alarm codes and error codes; this section summarises it.

| Range | Use |
|---|---|
| `0x0000` | invalid |
| `0x0001`–`0x00FF` | standard frames (below) |
| `0x0100`–`0x0FFF` | standard commands: the schema id of a downlink COMMAND frame is the command's tiny schema |
| `0x1000`–`0x7FFF` | reserved |
| `0x8000`–`0xFFFF` | organization schemas, assigned by the platform per organization (later phase) |

Nodes learn schema ids during provisioning or over a full-profile link, never over a tiny link.

### 7.1 Uplink

| Id | Name | Lane | Body | Bytes | Frame | Decodes to |
|---|---|---|---|---|---|---|
| 1 | POSITION | TELEMETRY | `t u32 · lat i32 · lon i32 · alt i16 (m MSL) · speed u8 (0.5 m/s) · heading u8 (2°, 0–179) · battery u8 (%)` | 17 | 47 | `TelemetrySample` |
| 2 | ALARM | ALARM | `t u32 · code u16 · severity u8 (AlertSeverity) · [lat i32 · lon i32]` | 7 / 15 | 37 / 45 | `Alert` |
| 3 | STATUS | STATUS | `t u32 · battery u8 (%) · voltage u8 (0.1 V) · flags u8 · temperature i8 (°C) · rssi i8 (dBm)` | 9 | 39 | `TelemetrySample` |
| 4 | COMMAND_REPLY | COMMAND_REPLY | `downlink_seq u16 · state u8 (CommandState) · error u16 · result (≤ 13 B)` | 5–18 | 35–48 | `CommandEvent` |

Unknown values: altitude `-32768`, speed/heading/battery/voltage `255`, temperature/rssi `-128`.
A POSITION without coordinates is not sent; an ALARM without a position uses the 7-byte form.
STATUS flags: bit 0 charging, bit 1 external power, bit 2 GNSS fix, bit 3 clock unsynced, bit 4
tamper; bits 5–7 reserved (0). `ALARM.code` and `COMMAND_REPLY.error` are registry values that
map to the dotted `Alert.code` (e.g. `1` → `sensor.intrusion`) and `Error.code` (e.g. `1` →
`command.expired`).

### 7.2 Downlink

| Id | Name | Lane | Body | Bytes |
|---|---|---|---|---|
| 5 | COMMAND_CANCEL | COMMAND_REPLY | `downlink_seq u16 · expires u32 (frame time)` | 6 |
| `0x0100`–`0x0FFF`, `≥ 0x8000` | COMMAND | COMMAND_REPLY | `downlink_seq u16 · expires u32 · params (≤ 12 B, layout per command)` | 6–18 |

`downlink_seq` is the low 16 bits of the command's `CommandDelivery.id.seq`; the platform maps a
COMMAND_REPLY back to the `command_execution_id`. The node refuses a COMMAND after `expires`
(COMMAND_REPLY with state REJECTED, error `command.expired`) and runs each `downlink_seq` of an
epoch at most once.

Standard commands in registry version 1: `flight.return_to_home` (257), `flight.land` (258),
`flight.emergency_stop` (259), `mission.pause` (260), `mission.resume` (261), `mission.stop` (262)
without params, and `navigation.go_to` (263) with `lat i32 · lon i32 · alt i16` (metres relative to
the takeoff point, like every `go_to`).

### 7.3 `Capability.tiny_schema_id`

A capability's `tiny_schema_id` is the schema of its COMMAND frame; `0` means the command cannot be
sent over a tiny link. The Go runtime fills it for the standard commands of the registry when an
adapter leaves it at `0`; an adapter MAY set an organization schema instead.

## 8. Deliverability

A session is **tiny-only** when its `Hello.encodings` lists only `"tiny"`. The platform:

1. MUST NOT hand a command to a tiny-only path unless the command has a tiny schema (a standard
   command of the registry; organization schemas join once the platform assigns them). Cancels
   (COMMAND_CANCEL) may always use a tiny path.
2. Routes such a command over the node's newest path that is not tiny-only; while the node has none,
   the command stays `QUEUED` (it is not `SENT`) until a path that can carry it appears or
   `expires_at` passes, when it fails `TIMED_OUT` with `edge.undeliverable`.
3. In asset selection (plan §5.4), does not choose an asset reachable only over tiny for a command
   without a tiny schema.

## 9. Gateways and relays

A gateway or relay never holds `K_root` of the nodes it serves. It reads the header (lane, flags,
`node_tag`) to queue and route, forwards the frame unchanged as `RelayItem.frame`, and transmits
`RelayDelivery.frame` in the target's receive window (plan §7.2). It cannot read, change, forge or
replay frames undetected; it can drop or delay them, which the deadlines and acknowledgements cover.

## 10. Test vectors

File: [`tiny-frame-v1.vectors.json`](tiny-frame-v1.vectors.json). Generated with the Go reference
implementation (zqnt-sdk-go `edge/runtime/tiny`, Go standard library and `x/crypto`); the core
decoder (edge-link, JDK 25 SunJCE) reproduces every frame byte for byte.

| Section | Content |
|---|---|
| `inputs` | `root_key` = bytes `00..1f`, `other_root_key` = `20..3f`, time 2026-11-03T12:00:00Z, epoch 671 |
| `key_schedule` | `prk`, `node_tag`, `K_epoch` for both suites, both roots, epochs 671 and 672 |
| `frames` | POSITION, ALARM (with and without position), STATUS (with and without unknowns), COMMAND_REPLY (empty, and the largest 48-byte frame), a `navigation.go_to` COMMAND and a COMMAND_CANCEL: header fields, body, nonce, frame and decoded values |
| `negative` | flipped ciphertext, tag, lane and counter bits, wrong direction, changed suite (must not authenticate); version 2, reserved bit, lane 0, unknown suite, counter 0, 49 and 29 bytes (malformed) |
| `replay_window` | a sequence of `(epoch, counter)` with the expected accept/refuse, covering duplicates, the window edge, the epoch change and an epoch jump |

The root keys are fixed public test values, not secrets.

Spot values:

```
node_tag(root_key, 671)            d861453c
K_epoch(root_key, T1-C, 671)       3b11299f9a30921266325014e3e1fc56ac9ea84353220aaf9f54e2a0d943f812
POSITION frame (T1-C, counter 1)   4401029fd861453c000000012f5653aa887450fc704f41b5a2b3e2fa3e06513d
                                   26f61261331c3d029b3c16fbc3b6d7
```

Every implementation MUST pass all sections in its unit tests, reading a copy of the file (never
regenerated). The Go runtime and core edge-link pin the file's SHA-256.

## 11. Decisions

| # | Question | Recommendation |
|---|---|---|
| T-1 | 16-byte tag (30 B overhead) instead of the plan's truncated 8-byte tag (18 B) | Accept: standard AEADs only, no own constructions; every planned schema still fits 48 B |
| T-2 | Epoch carried in the header (2 B) | Accept: the platform finds the key without trying neighbouring epochs, and nodes without a clock still work |
| T-3 | Epoch = days since 2025-01-01 | Accept; rotation by counter exhaustion as a fallback |
| T-4 | `K_root` provisioning out of band until M4 | Accept; enrollment delivery in M4 |
| T-5 | Replay window 64 | Accept for LoRa/SBD; revisit for ELRS bursts |
