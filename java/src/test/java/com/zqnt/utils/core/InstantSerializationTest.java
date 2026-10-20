package com.zqnt.utils.core;

import com.google.protobuf.Timestamp;
import com.zqnt.utils.JsonUtils;
import com.zqnt.utils.asset.domains.AssetDTO;
import org.junit.jupiter.api.Test;

import java.time.Instant;

import static org.junit.jupiter.api.Assertions.*;

class InstantSerializationTest {

    private static final Instant AT = Instant.parse("2026-10-20T08:15:30.250Z");

    @Test
    void timestampRoundTripKeepsTheInstant() {
        Timestamp timestamp = ProtobufHelpers.toTimestamp(AT);

        assertEquals(AT.getEpochSecond(), timestamp.getSeconds());
        assertEquals(AT.getNano(), timestamp.getNanos());
        assertEquals(AT, ProtobufHelpers.toInstant(timestamp));
    }

    @Test
    void absentValuesStayAbsent() {
        assertNull(ProtobufHelpers.toTimestamp((Instant) null));
        assertNull(ProtobufHelpers.toInstant(null));
    }

    @Test
    void jsonCarriesInstantsAsIsoUtc() {
        String json = JsonUtils.toJson(AssetDTO.builder().createdAt(AT).build());

        assertTrue(json.contains("\"createdAt\":\"2026-10-20T08:15:30.250Z\""), json);
        assertEquals(AT, JsonUtils.fromJson(json, AssetDTO.class).getCreatedAt());
    }

    @Test
    void jsonWithAnOffsetReadsAsTheSameInstant() {
        AssetDTO dto = JsonUtils.fromJson("{\"createdAt\":\"2026-10-20T10:15:30.250+02:00\"}", AssetDTO.class);

        assertEquals(AT, dto.getCreatedAt());
    }
}
