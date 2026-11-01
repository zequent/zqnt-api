import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from zqnt_api.generated.zqnt.capability.v3 import capability_pb2 as _capability_pb2
from zqnt_api.generated.zqnt.capability.v3 import command_pb2 as _command_pb2
from zqnt_api.generated.zqnt.common.v3 import common_pb2 as _common_pb2
from zqnt_api.generated.zqnt.telemetry.v3 import telemetry_pb2 as _telemetry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Lane(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANE_UNSPECIFIED: _ClassVar[Lane]
    LANE_ALARM: _ClassVar[Lane]
    LANE_COMMAND_REPLY: _ClassVar[Lane]
    LANE_STATUS: _ClassVar[Lane]
    LANE_TELEMETRY: _ClassVar[Lane]
    LANE_BULK: _ClassVar[Lane]

class LinkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINK_STATE_UNSPECIFIED: _ClassVar[LinkState]
    LINK_STATE_UP: _ClassVar[LinkState]
    LINK_STATE_DEGRADED: _ClassVar[LinkState]
    LINK_STATE_DOWN: _ClassVar[LinkState]

class MeshKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESH_KIND_UNSPECIFIED: _ClassVar[MeshKind]
    MESH_KIND_NONE: _ClassVar[MeshKind]
    MESH_KIND_IP_MESH: _ClassVar[MeshKind]
    MESH_KIND_FLOOD: _ClassVar[MeshKind]
    MESH_KIND_ROUTED: _ClassVar[MeshKind]
    MESH_KIND_SINGLE_HOP: _ClassVar[MeshKind]
LANE_UNSPECIFIED: Lane
LANE_ALARM: Lane
LANE_COMMAND_REPLY: Lane
LANE_STATUS: Lane
LANE_TELEMETRY: Lane
LANE_BULK: Lane
LINK_STATE_UNSPECIFIED: LinkState
LINK_STATE_UP: LinkState
LINK_STATE_DEGRADED: LinkState
LINK_STATE_DOWN: LinkState
MESH_KIND_UNSPECIFIED: MeshKind
MESH_KIND_NONE: MeshKind
MESH_KIND_IP_MESH: MeshKind
MESH_KIND_FLOOD: MeshKind
MESH_KIND_ROUTED: MeshKind
MESH_KIND_SINGLE_HOP: MeshKind

class MessageId(_message.Message):
    __slots__ = ("epoch", "seq")
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    seq: int
    def __init__(self, epoch: _Optional[int] = ..., seq: _Optional[int] = ...) -> None: ...

class Ack(_message.Message):
    __slots__ = ("epoch", "cumulative_seq", "selective_bitmap")
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_SEQ_FIELD_NUMBER: _ClassVar[int]
    SELECTIVE_BITMAP_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    cumulative_seq: int
    selective_bitmap: bytes
    def __init__(self, epoch: _Optional[int] = ..., cumulative_seq: _Optional[int] = ..., selective_bitmap: _Optional[bytes] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ("node_id", "id", "device_time", "lane", "clock_unsynced", "via_path", "sample", "detections", "alert", "command_event", "capabilities", "link_report", "topology")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TIME_FIELD_NUMBER: _ClassVar[int]
    LANE_FIELD_NUMBER: _ClassVar[int]
    CLOCK_UNSYNCED_FIELD_NUMBER: _ClassVar[int]
    VIA_PATH_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    DETECTIONS_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_EVENT_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    LINK_REPORT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    id: MessageId
    device_time: _timestamp_pb2.Timestamp
    lane: Lane
    clock_unsynced: bool
    via_path: _containers.RepeatedScalarFieldContainer[str]
    sample: _telemetry_pb2.TelemetrySample
    detections: _telemetry_pb2.DetectionBatch
    alert: _telemetry_pb2.Alert
    command_event: _command_pb2.CommandEvent
    capabilities: _capability_pb2.CapabilitySet
    link_report: LinkReport
    topology: TopologyReport
    def __init__(self, node_id: _Optional[str] = ..., id: _Optional[_Union[MessageId, _Mapping]] = ..., device_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., lane: _Optional[_Union[Lane, str]] = ..., clock_unsynced: _Optional[bool] = ..., via_path: _Optional[_Iterable[str]] = ..., sample: _Optional[_Union[_telemetry_pb2.TelemetrySample, _Mapping]] = ..., detections: _Optional[_Union[_telemetry_pb2.DetectionBatch, _Mapping]] = ..., alert: _Optional[_Union[_telemetry_pb2.Alert, _Mapping]] = ..., command_event: _Optional[_Union[_command_pb2.CommandEvent, _Mapping]] = ..., capabilities: _Optional[_Union[_capability_pb2.CapabilitySet, _Mapping]] = ..., link_report: _Optional[_Union[LinkReport, _Mapping]] = ..., topology: _Optional[_Union[TopologyReport, _Mapping]] = ...) -> None: ...

class UplinkFrame(_message.Message):
    __slots__ = ("hello", "envelope", "ack", "ping", "relay")
    HELLO_FIELD_NUMBER: _ClassVar[int]
    ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    hello: Hello
    envelope: Envelope
    ack: Ack
    ping: Ping
    relay: RelayBatch
    def __init__(self, hello: _Optional[_Union[Hello, _Mapping]] = ..., envelope: _Optional[_Union[Envelope, _Mapping]] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ..., relay: _Optional[_Union[RelayBatch, _Mapping]] = ...) -> None: ...

class DownlinkFrame(_message.Message):
    __slots__ = ("welcome", "ack", "command", "pong", "policy", "revocation", "relay_delivery")
    WELCOME_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_FIELD_NUMBER: _ClassVar[int]
    RELAY_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    welcome: Welcome
    ack: Ack
    command: CommandDelivery
    pong: Pong
    policy: PolicyUpdate
    revocation: Revocation
    relay_delivery: RelayDelivery
    def __init__(self, welcome: _Optional[_Union[Welcome, _Mapping]] = ..., ack: _Optional[_Union[Ack, _Mapping]] = ..., command: _Optional[_Union[CommandDelivery, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ..., policy: _Optional[_Union[PolicyUpdate, _Mapping]] = ..., revocation: _Optional[_Union[Revocation, _Mapping]] = ..., relay_delivery: _Optional[_Union[RelayDelivery, _Mapping]] = ...) -> None: ...

class UplinkBatch(_message.Message):
    __slots__ = ("node_id", "frames")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    frames: _containers.RepeatedCompositeFieldContainer[UplinkFrame]
    def __init__(self, node_id: _Optional[str] = ..., frames: _Optional[_Iterable[_Union[UplinkFrame, _Mapping]]] = ...) -> None: ...

class DownlinkBatch(_message.Message):
    __slots__ = ("frames",)
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[DownlinkFrame]
    def __init__(self, frames: _Optional[_Iterable[_Union[DownlinkFrame, _Mapping]]] = ...) -> None: ...

class Hello(_message.Message):
    __slots__ = ("node_id", "crypto_suite", "ephemeral_pub", "signature", "monotonic_ms", "wallclock", "encodings", "asset_sns", "link_kind", "runtime_version", "downlink_acked")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_SUITE_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_PUB_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    MONOTONIC_MS_FIELD_NUMBER: _ClassVar[int]
    WALLCLOCK_FIELD_NUMBER: _ClassVar[int]
    ENCODINGS_FIELD_NUMBER: _ClassVar[int]
    ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    LINK_KIND_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ACKED_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    crypto_suite: int
    ephemeral_pub: bytes
    signature: bytes
    monotonic_ms: int
    wallclock: _timestamp_pb2.Timestamp
    encodings: _containers.RepeatedScalarFieldContainer[str]
    asset_sns: _containers.RepeatedScalarFieldContainer[str]
    link_kind: str
    runtime_version: str
    downlink_acked: Ack
    def __init__(self, node_id: _Optional[str] = ..., crypto_suite: _Optional[int] = ..., ephemeral_pub: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., monotonic_ms: _Optional[int] = ..., wallclock: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., encodings: _Optional[_Iterable[str]] = ..., asset_sns: _Optional[_Iterable[str]] = ..., link_kind: _Optional[str] = ..., runtime_version: _Optional[str] = ..., downlink_acked: _Optional[_Union[Ack, _Mapping]] = ...) -> None: ...

class Welcome(_message.Message):
    __slots__ = ("ephemeral_pub", "signature", "clock_offset_ms", "resume_from", "session_id", "policy")
    EPHEMERAL_PUB_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CLOCK_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    RESUME_FROM_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    ephemeral_pub: bytes
    signature: bytes
    clock_offset_ms: int
    resume_from: Ack
    session_id: str
    policy: LinkPolicy
    def __init__(self, ephemeral_pub: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., clock_offset_ms: _Optional[int] = ..., resume_from: _Optional[_Union[Ack, _Mapping]] = ..., session_id: _Optional[str] = ..., policy: _Optional[_Union[LinkPolicy, _Mapping]] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ("nonce", "monotonic_ms")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MONOTONIC_MS_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    monotonic_ms: int
    def __init__(self, nonce: _Optional[int] = ..., monotonic_ms: _Optional[int] = ...) -> None: ...

class Pong(_message.Message):
    __slots__ = ("nonce", "monotonic_ms", "platform_time")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MONOTONIC_MS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TIME_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    monotonic_ms: int
    platform_time: _timestamp_pb2.Timestamp
    def __init__(self, nonce: _Optional[int] = ..., monotonic_ms: _Optional[int] = ..., platform_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LinkPolicy(_message.Message):
    __slots__ = ("revision", "ping_interval")
    REVISION_FIELD_NUMBER: _ClassVar[int]
    PING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    revision: str
    ping_interval: _duration_pb2.Duration
    def __init__(self, revision: _Optional[str] = ..., ping_interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PolicyUpdate(_message.Message):
    __slots__ = ("id", "policy")
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    id: MessageId
    policy: LinkPolicy
    def __init__(self, id: _Optional[_Union[MessageId, _Mapping]] = ..., policy: _Optional[_Union[LinkPolicy, _Mapping]] = ...) -> None: ...

class CommandDelivery(_message.Message):
    __slots__ = ("id", "context", "command_execution_id", "execute", "cancel")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    id: MessageId
    context: _common_pb2.RequestContext
    command_execution_id: str
    execute: _command_pb2.Command
    cancel: CommandCancel
    def __init__(self, id: _Optional[_Union[MessageId, _Mapping]] = ..., context: _Optional[_Union[_common_pb2.RequestContext, _Mapping]] = ..., command_execution_id: _Optional[str] = ..., execute: _Optional[_Union[_command_pb2.Command, _Mapping]] = ..., cancel: _Optional[_Union[CommandCancel, _Mapping]] = ...) -> None: ...

class CommandCancel(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class Revocation(_message.Message):
    __slots__ = ("id", "node_ids", "revoked_at", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: MessageId
    node_ids: _containers.RepeatedScalarFieldContainer[str]
    revoked_at: _timestamp_pb2.Timestamp
    reason: str
    def __init__(self, id: _Optional[_Union[MessageId, _Mapping]] = ..., node_ids: _Optional[_Iterable[str]] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...

class RelayItem(_message.Message):
    __slots__ = ("frame", "rx_link", "rssi", "snr", "mesh_hops", "relay_hop", "rx_time")
    FRAME_FIELD_NUMBER: _ClassVar[int]
    RX_LINK_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    MESH_HOPS_FIELD_NUMBER: _ClassVar[int]
    RELAY_HOP_FIELD_NUMBER: _ClassVar[int]
    RX_TIME_FIELD_NUMBER: _ClassVar[int]
    frame: bytes
    rx_link: str
    rssi: int
    snr: int
    mesh_hops: int
    relay_hop: int
    rx_time: _timestamp_pb2.Timestamp
    def __init__(self, frame: _Optional[bytes] = ..., rx_link: _Optional[str] = ..., rssi: _Optional[int] = ..., snr: _Optional[int] = ..., mesh_hops: _Optional[int] = ..., relay_hop: _Optional[int] = ..., rx_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RelayBatch(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[RelayItem]
    def __init__(self, items: _Optional[_Iterable[_Union[RelayItem, _Mapping]]] = ...) -> None: ...

class RelayDelivery(_message.Message):
    __slots__ = ("node_tag", "node_id", "frame", "expires_at", "id")
    NODE_TAG_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    node_tag: int
    node_id: str
    frame: bytes
    expires_at: _timestamp_pb2.Timestamp
    id: MessageId
    def __init__(self, node_tag: _Optional[int] = ..., node_id: _Optional[str] = ..., frame: _Optional[bytes] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[_Union[MessageId, _Mapping]] = ...) -> None: ...

class LinkStatus(_message.Message):
    __slots__ = ("link_id", "driver", "state", "state_reason", "rtt_ms", "loss", "bandwidth_estimate_bps", "bytes_used", "last_rx", "probe_failures")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    RTT_MS_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_ESTIMATE_BPS_FIELD_NUMBER: _ClassVar[int]
    BYTES_USED_FIELD_NUMBER: _ClassVar[int]
    LAST_RX_FIELD_NUMBER: _ClassVar[int]
    PROBE_FAILURES_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    driver: str
    state: LinkState
    state_reason: str
    rtt_ms: int
    loss: float
    bandwidth_estimate_bps: int
    bytes_used: int
    last_rx: _timestamp_pb2.Timestamp
    probe_failures: int
    def __init__(self, link_id: _Optional[str] = ..., driver: _Optional[str] = ..., state: _Optional[_Union[LinkState, str]] = ..., state_reason: _Optional[str] = ..., rtt_ms: _Optional[int] = ..., loss: _Optional[float] = ..., bandwidth_estimate_bps: _Optional[int] = ..., bytes_used: _Optional[int] = ..., last_rx: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., probe_failures: _Optional[int] = ...) -> None: ...

class LaneBacklog(_message.Message):
    __slots__ = ("lane", "items", "bytes", "oldest")
    LANE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    OLDEST_FIELD_NUMBER: _ClassVar[int]
    lane: Lane
    items: int
    bytes: int
    oldest: _timestamp_pb2.Timestamp
    def __init__(self, lane: _Optional[_Union[Lane, str]] = ..., items: _Optional[int] = ..., bytes: _Optional[int] = ..., oldest: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LinkReport(_message.Message):
    __slots__ = ("links", "backlog", "policy_revision")
    LINKS_FIELD_NUMBER: _ClassVar[int]
    BACKLOG_FIELD_NUMBER: _ClassVar[int]
    POLICY_REVISION_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[LinkStatus]
    backlog: _containers.RepeatedCompositeFieldContainer[LaneBacklog]
    policy_revision: str
    def __init__(self, links: _Optional[_Iterable[_Union[LinkStatus, _Mapping]]] = ..., backlog: _Optional[_Iterable[_Union[LaneBacklog, _Mapping]]] = ..., policy_revision: _Optional[str] = ...) -> None: ...

class MeshInfo(_message.Message):
    __slots__ = ("kind", "max_hops", "mesh_name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MAX_HOPS_FIELD_NUMBER: _ClassVar[int]
    MESH_NAME_FIELD_NUMBER: _ClassVar[int]
    kind: MeshKind
    max_hops: int
    mesh_name: str
    def __init__(self, kind: _Optional[_Union[MeshKind, str]] = ..., max_hops: _Optional[int] = ..., mesh_name: _Optional[str] = ...) -> None: ...

class Neighbor(_message.Message):
    __slots__ = ("peer_id", "node_tag", "rssi", "snr", "link_quality", "last_heard", "hops")
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_TAG_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    LINK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARD_FIELD_NUMBER: _ClassVar[int]
    HOPS_FIELD_NUMBER: _ClassVar[int]
    peer_id: str
    node_tag: int
    rssi: int
    snr: int
    link_quality: float
    last_heard: _timestamp_pb2.Timestamp
    hops: int
    def __init__(self, peer_id: _Optional[str] = ..., node_tag: _Optional[int] = ..., rssi: _Optional[int] = ..., snr: _Optional[int] = ..., link_quality: _Optional[float] = ..., last_heard: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., hops: _Optional[int] = ...) -> None: ...

class LinkTopology(_message.Message):
    __slots__ = ("link_id", "mesh", "neighbors")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    MESH_FIELD_NUMBER: _ClassVar[int]
    NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    mesh: MeshInfo
    neighbors: _containers.RepeatedCompositeFieldContainer[Neighbor]
    def __init__(self, link_id: _Optional[str] = ..., mesh: _Optional[_Union[MeshInfo, _Mapping]] = ..., neighbors: _Optional[_Iterable[_Union[Neighbor, _Mapping]]] = ...) -> None: ...

class TopologyReport(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[LinkTopology]
    def __init__(self, links: _Optional[_Iterable[_Union[LinkTopology, _Mapping]]] = ...) -> None: ...
