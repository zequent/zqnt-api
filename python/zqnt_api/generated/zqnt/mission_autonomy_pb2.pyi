import datetime

from . import common_pb2 as _common_pb2
from . import base_pb2 as _base_pb2
from . import asset_pb2 as _asset_pb2
from . import device_control_contracts_pb2 as _device_control_contracts_pb2
from . import detection_pb2 as _detection_pb2
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2
from . import capability_execution_contracts_pb2 as _capability_execution_contracts_pb2
from . import mission_autonomy_contracts_pb2 as _mission_autonomy_contracts_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import mission_autonomy_dto_pb2 as _mission_autonomy_dto_pb2_1
from . import mission_autonomy_types_pb2 as _mission_autonomy_types_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlightPathVerdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLIGHT_PATH_VERDICT_UNSPECIFIED: _ClassVar[FlightPathVerdict]
    FLIGHT_PATH_VERDICT_CLEAR: _ClassVar[FlightPathVerdict]
    FLIGHT_PATH_VERDICT_ADVISORY: _ClassVar[FlightPathVerdict]
    FLIGHT_PATH_VERDICT_REQUIRES_APPROVAL: _ClassVar[FlightPathVerdict]
    FLIGHT_PATH_VERDICT_BLOCKED: _ClassVar[FlightPathVerdict]
FLIGHT_PATH_VERDICT_UNSPECIFIED: FlightPathVerdict
FLIGHT_PATH_VERDICT_CLEAR: FlightPathVerdict
FLIGHT_PATH_VERDICT_ADVISORY: FlightPathVerdict
FLIGHT_PATH_VERDICT_REQUIRES_APPROVAL: FlightPathVerdict
FLIGHT_PATH_VERDICT_BLOCKED: FlightPathVerdict

class EvaluateDetectionRequest(_message.Message):
    __slots__ = ("base", "detection_id", "asset_sn", "object_type", "confidence", "detection_latitude", "detection_longitude", "detection_altitude", "organization_id", "runtime_config", "theatre_id", "capability_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LATITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    detection_id: str
    asset_sn: str
    object_type: str
    confidence: float
    detection_latitude: float
    detection_longitude: float
    detection_altitude: float
    organization_id: str
    runtime_config: _mission_autonomy_types_pb2_1.DynamicConfigProto
    theatre_id: str
    capability_id: str
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., detection_id: _Optional[str] = ..., asset_sn: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., detection_latitude: _Optional[float] = ..., detection_longitude: _Optional[float] = ..., detection_altitude: _Optional[float] = ..., organization_id: _Optional[str] = ..., runtime_config: _Optional[_Union[_mission_autonomy_types_pb2_1.DynamicConfigProto, _Mapping]] = ..., theatre_id: _Optional[str] = ..., capability_id: _Optional[str] = ...) -> None: ...

class DecisionResultProto(_message.Message):
    __slots__ = ("decision_id", "detection_id", "selected_asset_sn", "strategy_used", "status", "considered_asset_sns", "rejection_reasons", "decided_at", "resolved_config", "selected_actions")
    class RejectionReasonsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DECISION_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_USED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONSIDERED_ASSET_SNS_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASONS_FIELD_NUMBER: _ClassVar[int]
    DECIDED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    decision_id: str
    detection_id: str
    selected_asset_sn: str
    strategy_used: str
    status: str
    considered_asset_sns: _containers.RepeatedScalarFieldContainer[str]
    rejection_reasons: _containers.ScalarMap[str, str]
    decided_at: _timestamp_pb2.Timestamp
    resolved_config: _mission_autonomy_types_pb2_1.DynamicConfigProto
    selected_actions: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_types_pb2_1.DecisionActionProto]
    def __init__(self, decision_id: _Optional[str] = ..., detection_id: _Optional[str] = ..., selected_asset_sn: _Optional[str] = ..., strategy_used: _Optional[str] = ..., status: _Optional[str] = ..., considered_asset_sns: _Optional[_Iterable[str]] = ..., rejection_reasons: _Optional[_Mapping[str, str]] = ..., decided_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_config: _Optional[_Union[_mission_autonomy_types_pb2_1.DynamicConfigProto, _Mapping]] = ..., selected_actions: _Optional[_Iterable[_Union[_mission_autonomy_types_pb2_1.DecisionActionProto, _Mapping]]] = ...) -> None: ...

class DecisionResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "timestamp", "error", "decision_result")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DECISION_RESULT_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    timestamp: _timestamp_pb2.Timestamp
    error: _base_pb2.GlobalErrorMessage
    decision_result: DecisionResultProto
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., decision_result: _Optional[_Union[DecisionResultProto, _Mapping]] = ...) -> None: ...

class SimulateAssetSelectionRequest(_message.Message):
    __slots__ = ("base", "organization_id", "object_type", "confidence", "latitude", "longitude", "theatre_id", "capability_id", "priority")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    object_type: str
    confidence: float
    latitude: float
    longitude: float
    theatre_id: str
    capability_id: str
    priority: int
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., object_type: _Optional[str] = ..., confidence: _Optional[float] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., theatre_id: _Optional[str] = ..., capability_id: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class AssetSelectionCandidateProto(_message.Message):
    __slots__ = ("sn", "asset_type", "battery_percent", "available", "held_by_priority", "distance_meters", "theatre_id", "reason")
    SN_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    HELD_BY_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    sn: str
    asset_type: str
    battery_percent: int
    available: bool
    held_by_priority: int
    distance_meters: float
    theatre_id: str
    reason: str
    def __init__(self, sn: _Optional[str] = ..., asset_type: _Optional[str] = ..., battery_percent: _Optional[int] = ..., available: bool = ..., held_by_priority: _Optional[int] = ..., distance_meters: _Optional[float] = ..., theatre_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class AssetSelectionPolicyStepProto(_message.Message):
    __slots__ = ("policy_id", "priority", "strategy", "outcome", "note", "rejections", "level")
    class RejectionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    REJECTIONS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    priority: int
    strategy: str
    outcome: str
    note: str
    rejections: _containers.ScalarMap[str, str]
    level: str
    def __init__(self, policy_id: _Optional[str] = ..., priority: _Optional[int] = ..., strategy: _Optional[str] = ..., outcome: _Optional[str] = ..., note: _Optional[str] = ..., rejections: _Optional[_Mapping[str, str]] = ..., level: _Optional[str] = ...) -> None: ...

class SimulateAssetSelectionResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "error", "selected_asset_sn", "answered_by_policy_id", "summary", "steps", "candidates", "theatre_id", "status")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ASSET_SN_FIELD_NUMBER: _ClassVar[int]
    ANSWERED_BY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    THEATRE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    error: _base_pb2.GlobalErrorMessage
    selected_asset_sn: str
    answered_by_policy_id: str
    summary: str
    steps: _containers.RepeatedCompositeFieldContainer[AssetSelectionPolicyStepProto]
    candidates: _containers.RepeatedCompositeFieldContainer[AssetSelectionCandidateProto]
    theatre_id: str
    status: str
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., selected_asset_sn: _Optional[str] = ..., answered_by_policy_id: _Optional[str] = ..., summary: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[AssetSelectionPolicyStepProto, _Mapping]]] = ..., candidates: _Optional[_Iterable[_Union[AssetSelectionCandidateProto, _Mapping]]] = ..., theatre_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class CheckFlightPathRequest(_message.Message):
    __slots__ = ("base", "organization_id", "command_id", "latitude", "longitude", "altitude")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    base: _base_pb2.RequestBase
    organization_id: str
    command_id: str
    latitude: float
    longitude: float
    altitude: float
    def __init__(self, base: _Optional[_Union[_base_pb2.RequestBase, _Mapping]] = ..., organization_id: _Optional[str] = ..., command_id: _Optional[str] = ..., latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[float] = ...) -> None: ...

class FlightPathZoneHitProto(_message.Message):
    __slots__ = ("zone_id", "zone_name", "enforcement", "destination_inside")
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_INSIDE_FIELD_NUMBER: _ClassVar[int]
    zone_id: str
    zone_name: str
    enforcement: _mission_autonomy_types_pb2_1.ZoneEnforcementType
    destination_inside: bool
    def __init__(self, zone_id: _Optional[str] = ..., zone_name: _Optional[str] = ..., enforcement: _Optional[_Union[_mission_autonomy_types_pb2_1.ZoneEnforcementType, str]] = ..., destination_inside: bool = ...) -> None: ...

class CheckFlightPathResponse(_message.Message):
    __slots__ = ("has_errors", "tid", "error", "verdict", "summary", "zones", "reroute", "position_known")
    HAS_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    REROUTE_FIELD_NUMBER: _ClassVar[int]
    POSITION_KNOWN_FIELD_NUMBER: _ClassVar[int]
    has_errors: bool
    tid: str
    error: _base_pb2.GlobalErrorMessage
    verdict: FlightPathVerdict
    summary: str
    zones: _containers.RepeatedCompositeFieldContainer[FlightPathZoneHitProto]
    reroute: _containers.RepeatedCompositeFieldContainer[_mission_autonomy_dto_pb2_1.GeoPointProtoDTO]
    position_known: bool
    def __init__(self, has_errors: bool = ..., tid: _Optional[str] = ..., error: _Optional[_Union[_base_pb2.GlobalErrorMessage, _Mapping]] = ..., verdict: _Optional[_Union[FlightPathVerdict, str]] = ..., summary: _Optional[str] = ..., zones: _Optional[_Iterable[_Union[FlightPathZoneHitProto, _Mapping]]] = ..., reroute: _Optional[_Iterable[_Union[_mission_autonomy_dto_pb2_1.GeoPointProtoDTO, _Mapping]]] = ..., position_known: bool = ...) -> None: ...
