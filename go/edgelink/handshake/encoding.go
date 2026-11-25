// Package handshake implements the Edge Link handshake of spec/edge-link-handshake-v1.md (suite
// S1): the canonical transcript encoding, the signed transcripts, key ids, ECDSA P-256 signatures
// in r || s form and the session key schedule.
package handshake

import (
	"encoding/binary"

	edgelinkv3 "github.com/zequent/zqnt-api/go/v3/gen/zqnt/edgelink/v3"
	"google.golang.org/protobuf/types/known/durationpb"
	"google.golang.org/protobuf/types/known/timestamppb"
)

// Encoder appends values in the canonical encoding of spec §4.1.
type Encoder struct {
	buf []byte
}

func (e *Encoder) Bytes() []byte { return e.buf }

func (e *Encoder) U8(v uint8) *Encoder {
	e.buf = append(e.buf, v)
	return e
}

func (e *Encoder) U32(v uint32) *Encoder {
	e.buf = binary.BigEndian.AppendUint32(e.buf, v)
	return e
}

func (e *Encoder) U64(v uint64) *Encoder {
	e.buf = binary.BigEndian.AppendUint64(e.buf, v)
	return e
}

func (e *Encoder) I32(v int32) *Encoder { return e.U32(uint32(v)) }

func (e *Encoder) I64(v int64) *Encoder { return e.U64(uint64(v)) }

func (e *Encoder) EncBytes(b []byte) *Encoder {
	e.U32(uint32(len(b)))
	e.buf = append(e.buf, b...)
	return e
}

func (e *Encoder) EncStr(s string) *Encoder {
	e.U32(uint32(len(s)))
	e.buf = append(e.buf, s...)
	return e
}

func (e *Encoder) ListStr(l []string) *Encoder {
	e.U32(uint32(len(l)))
	for _, s := range l {
		e.EncStr(s)
	}
	return e
}

func (e *Encoder) ListU32(l []uint32) *Encoder {
	e.U32(uint32(len(l)))
	for _, v := range l {
		e.U32(v)
	}
	return e
}

func (e *Encoder) Timestamp(t *timestamppb.Timestamp) *Encoder {
	return e.I64(t.GetSeconds()).I32(t.GetNanos())
}

func (e *Encoder) Duration(d *durationpb.Duration) *Encoder {
	return e.I64(d.GetSeconds()).I32(d.GetNanos())
}

func (e *Encoder) Ack(a *edgelinkv3.Ack) *Encoder {
	return e.U32(a.GetEpoch()).U32(a.GetCumulativeSeq()).U32(a.GetSelectiveBase()).EncBytes(a.GetSelectiveBitmap())
}

// Present writes opt(): u8(0) when absent, u8(1) otherwise. The caller appends the value after
// it when it returns true.
func (e *Encoder) Present(present bool) bool {
	if present {
		e.U8(1)
	} else {
		e.U8(0)
	}
	return present
}
