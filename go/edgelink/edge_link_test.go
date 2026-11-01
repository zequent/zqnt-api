package edgelink_test

import (
	"testing"

	capabilityv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/capability/v3"
	commonv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/common/v3"
	edgelinkv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/edgelink/v3"
	telemetryv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/telemetry/v3"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protoreflect"
	"google.golang.org/protobuf/types/known/durationpb"
	"google.golang.org/protobuf/types/known/timestamppb"
)

var (
	at      = &timestamppb.Timestamp{Seconds: 1_793_000_000, Nanos: 125_000_000}
	expires = &timestamppb.Timestamp{Seconds: 1_793_000_060}
	asset   = &commonv3.AssetRef{Sn: "SIM-RADAR-1", Id: "asset-1"}
)

func p[T any](v T) *T { return &v }

func id(seq uint32) *edgelinkv3.MessageId { return &edgelinkv3.MessageId{Epoch: 3, Seq: seq} }

func ack() *edgelinkv3.Ack {
	return &edgelinkv3.Ack{Epoch: 3, CumulativeSeq: 41, SelectiveBitmap: []byte{0b0000_0101}, SelectiveBase: 57}
}

func policy() *edgelinkv3.LinkPolicy {
	return &edgelinkv3.LinkPolicy{Revision: "rev-7", PingInterval: durationpb.New(15e9)}
}

func linkReport() *edgelinkv3.LinkReport {
	return &edgelinkv3.LinkReport{
		Links: []*edgelinkv3.LinkStatus{{
			LinkId: "lte", Driver: "ip-session", State: edgelinkv3.LinkState_LINK_STATE_DEGRADED,
			StateReason: "loss above 20 %", RttMs: 180, Loss: 0.25, BandwidthEstimateBps: 2_000_000,
			BytesUsed: 1 << 20, LastRx: at, ProbeFailures: 1,
		}},
		Backlog: []*edgelinkv3.LaneBacklog{{
			Lane: edgelinkv3.Lane_LANE_TELEMETRY, Items: 1200, Bytes: 96_000, Oldest: at,
		}},
		PolicyRevision: "rev-7",
	}
}

func topology() *edgelinkv3.TopologyReport {
	return &edgelinkv3.TopologyReport{Links: []*edgelinkv3.LinkTopology{{
		LinkId: "lora",
		Mesh: &edgelinkv3.MeshInfo{
			Kind: edgelinkv3.MeshKind_MESH_KIND_FLOOD, MaxHops: 3, MeshName: "meshcore",
		},
		Neighbors: []*edgelinkv3.Neighbor{{
			PeerId: "a1b2c3", NodeTag: p[uint32](0xBEEF), Rssi: p[int32](-97), Snr: p[int32](-4),
			LinkQuality: p[float32](0.8), LastHeard: at, Hops: p[uint32](1),
		}},
	}}}
}

func envelope(seq uint32, lane edgelinkv3.Lane) *edgelinkv3.Envelope {
	return &edgelinkv3.Envelope{
		NodeId: "node-1", Id: id(seq), DeviceTime: at, Lane: lane, ClockUnsynced: true,
		ViaPath: []string{"relay-7", "gateway-1"}, HeldFrom: 38,
	}
}

func command() *capabilityv3.Command {
	return &capabilityv3.Command{
		Asset: asset, CommandId: "radar.scan.start", Timeout: durationpb.New(30e9), ExpiresAt: expires,
	}
}

// One populated instance per message of edge_link.proto, every oneof variant included.
func samples() []proto.Message {
	envelopes := []*edgelinkv3.Envelope{}
	bodies := []func(*edgelinkv3.Envelope){
		func(e *edgelinkv3.Envelope) {
			e.Body = &edgelinkv3.Envelope_Sample{Sample: &telemetryv3.TelemetrySample{Asset: asset, ObservedAt: at}}
		},
		func(e *edgelinkv3.Envelope) {
			e.Body = &edgelinkv3.Envelope_Detections{Detections: &telemetryv3.DetectionBatch{Asset: asset, ObservedAt: at}}
		},
		func(e *edgelinkv3.Envelope) {
			e.Body = &edgelinkv3.Envelope_Alert{Alert: &telemetryv3.Alert{
				Asset: asset, OccurredAt: at, Severity: telemetryv3.AlertSeverity_ALERT_SEVERITY_CRITICAL, Code: "radar.track",
			}}
		},
		func(e *edgelinkv3.Envelope) {
			e.Body = &edgelinkv3.Envelope_CommandEvent{CommandEvent: &capabilityv3.CommandEvent{
				CommandExecutionId: "exec-1", Asset: asset, State: capabilityv3.CommandState_COMMAND_STATE_QUEUED, OccurredAt: at,
			}}
		},
		func(e *edgelinkv3.Envelope) {
			e.Body = &edgelinkv3.Envelope_Capabilities{Capabilities: &capabilityv3.CapabilitySet{
				AssetSn: asset.Sn, Capabilities: []*capabilityv3.Capability{{CommandId: "radar.scan.start", TinySchemaId: 12}},
			}}
		},
		func(e *edgelinkv3.Envelope) { e.Body = &edgelinkv3.Envelope_LinkReport{LinkReport: linkReport()} },
		func(e *edgelinkv3.Envelope) { e.Body = &edgelinkv3.Envelope_Topology{Topology: topology()} },
	}
	for i, set := range bodies {
		e := envelope(uint32(42+i), edgelinkv3.Lane(1+i%5))
		set(e)
		envelopes = append(envelopes, e)
	}

	relay := &edgelinkv3.RelayBatch{Items: []*edgelinkv3.RelayItem{{
		Frame: []byte{0x41, 0x01, 0xBE, 0xEF}, RxLink: "lora", Rssi: -101, Snr: -7, MeshHops: 2, RelayHop: 1, RxTime: at,
	}}}
	uplinks := []*edgelinkv3.UplinkFrame{
		{Frame: &edgelinkv3.UplinkFrame_Hello{Hello: &edgelinkv3.Hello{
			NodeId: "node-1", CryptoSuite: 1, EphemeralPub: []byte{1, 2, 3}, Signature: []byte{4, 5, 6},
			MonotonicMs: 123_456, Wallclock: at, Encodings: []string{"full", "lean"}, AssetSns: []string{asset.Sn},
			LinkKind: "ip-session", RuntimeVersion: "0.1.0", DownlinkAcked: ack(),
		}}},
		{Frame: &edgelinkv3.UplinkFrame_Ack{Ack: ack()}},
		{Frame: &edgelinkv3.UplinkFrame_Ping{Ping: &edgelinkv3.Ping{Nonce: 9, MonotonicMs: 123_999}}},
		{Frame: &edgelinkv3.UplinkFrame_Relay{Relay: relay}},
	}
	for _, e := range envelopes {
		uplinks = append(uplinks, &edgelinkv3.UplinkFrame{Frame: &edgelinkv3.UplinkFrame_Envelope{Envelope: e}})
	}

	downlinks := []*edgelinkv3.DownlinkFrame{
		{Frame: &edgelinkv3.DownlinkFrame_Welcome{Welcome: &edgelinkv3.Welcome{
			EphemeralPub: []byte{7, 8}, Signature: []byte{9}, ClockOffsetMs: -1500, ResumeFrom: ack(),
			SessionId: "session-1", Policy: policy(),
		}}},
		{Frame: &edgelinkv3.DownlinkFrame_Ack{Ack: ack()}},
		{Frame: &edgelinkv3.DownlinkFrame_Command{Command: &edgelinkv3.CommandDelivery{
			Id: id(1), Context: &commonv3.RequestContext{RequestId: "req-1", IdempotencyKey: "key-1"},
			CommandExecutionId: "exec-1", Action: &edgelinkv3.CommandDelivery_Execute{Execute: command()},
		}}},
		{Frame: &edgelinkv3.DownlinkFrame_Command{Command: &edgelinkv3.CommandDelivery{
			Id: id(2), Context: &commonv3.RequestContext{RequestId: "req-2"}, CommandExecutionId: "exec-1",
			Action: &edgelinkv3.CommandDelivery_Cancel{Cancel: &edgelinkv3.CommandCancel{Reason: "operator"}},
		}}},
		{Frame: &edgelinkv3.DownlinkFrame_Pong{Pong: &edgelinkv3.Pong{Nonce: 9, MonotonicMs: 123_999, PlatformTime: at}}},
		{Frame: &edgelinkv3.DownlinkFrame_Policy{Policy: &edgelinkv3.PolicyUpdate{Id: id(3), Policy: policy()}}},
		{Frame: &edgelinkv3.DownlinkFrame_Revocation{Revocation: &edgelinkv3.Revocation{
			Id: id(4), NodeIds: []string{"node-9"}, RevokedAt: at, Reason: "captured",
		}}},
		{Frame: &edgelinkv3.DownlinkFrame_RelayDelivery{RelayDelivery: &edgelinkv3.RelayDelivery{
			NodeTag: 0xBEEF, NodeId: "node-2", Frame: []byte{0x42, 0x02}, ExpiresAt: expires, Id: id(5),
		}}},
	}

	msgs := []proto.Message{
		&edgelinkv3.UplinkBatch{NodeId: "node-1", Frames: uplinks},
		&edgelinkv3.DownlinkBatch{Frames: downlinks},
	}
	for _, f := range uplinks {
		msgs = append(msgs, f)
	}
	for _, f := range downlinks {
		msgs = append(msgs, f)
	}
	return msgs
}

func TestRoundTrip(t *testing.T) {
	for _, m := range samples() {
		name := m.ProtoReflect().Descriptor().FullName()
		wire, err := proto.Marshal(m)
		if err != nil {
			t.Fatalf("%s: marshal: %v", name, err)
		}
		back := m.ProtoReflect().New().Interface()
		if err := proto.Unmarshal(wire, back); err != nil {
			t.Fatalf("%s: unmarshal: %v", name, err)
		}
		if !proto.Equal(m, back) {
			t.Errorf("%s: differs after the round trip\nsent: %v\ngot:  %v", name, m, back)
		}
	}
}

// Every message of the file appears with every field set, and every oneof variant is used, so a
// new message or field without a test fails here.
func TestSamplesCoverEveryMessageAndField(t *testing.T) {
	seen := map[protoreflect.FullName]map[protoreflect.Name]bool{}
	var walk func(protoreflect.Message)
	walk = func(m protoreflect.Message) {
		d := m.Descriptor()
		if d.ParentFile().Path() != edgelinkv3.File_zqnt_edgelink_v3_edge_link_proto.Path() {
			return
		}
		if seen[d.FullName()] == nil {
			seen[d.FullName()] = map[protoreflect.Name]bool{}
		}
		m.Range(func(f protoreflect.FieldDescriptor, v protoreflect.Value) bool {
			seen[d.FullName()][f.Name()] = true
			switch {
			case f.IsList() && f.Message() != nil:
				for i := 0; i < v.List().Len(); i++ {
					walk(v.List().Get(i).Message())
				}
			case f.Message() != nil && !f.IsMap():
				walk(v.Message())
			}
			return true
		})
	}
	for _, m := range samples() {
		walk(m.ProtoReflect())
	}

	messages := edgelinkv3.File_zqnt_edgelink_v3_edge_link_proto.Messages()
	for i := 0; i < messages.Len(); i++ {
		d := messages.Get(i)
		fields, ok := seen[d.FullName()]
		if !ok {
			t.Errorf("%s: no sample", d.FullName())
			continue
		}
		for j := 0; j < d.Fields().Len(); j++ {
			if f := d.Fields().Get(j); !fields[f.Name()] {
				t.Errorf("%s.%s: never set in a sample", d.FullName(), f.Name())
			}
		}
	}
}

func TestFrameNumbering(t *testing.T) {
	want := map[string]map[protoreflect.FieldNumber]protoreflect.Name{
		"UplinkFrame": {1: "hello", 2: "envelope", 3: "ack", 4: "ping", 5: "relay"},
		"DownlinkFrame": {
			1: "welcome", 2: "ack", 3: "command", 4: "pong", 5: "policy", 6: "revocation", 7: "relay_delivery",
		},
	}
	for msg, fields := range want {
		d := edgelinkv3.File_zqnt_edgelink_v3_edge_link_proto.Messages().ByName(protoreflect.Name(msg))
		if d.Fields().Len() != len(fields) {
			t.Errorf("%s has %d fields, want %d", msg, d.Fields().Len(), len(fields))
		}
		for num, name := range fields {
			f := d.Fields().ByNumber(num)
			if f == nil || f.Name() != name {
				t.Errorf("%s field %d: got %v, want %s", msg, num, f, name)
			}
		}
		if r := d.ReservedRanges(); r.Len() != 1 || r.Get(0)[0] != protoreflect.FieldNumber(len(fields)+1) || r.Get(0)[1] != 16 {
			t.Errorf("%s: future frames must stay reserved up to 15, got %v", msg, r)
		}
	}
}
