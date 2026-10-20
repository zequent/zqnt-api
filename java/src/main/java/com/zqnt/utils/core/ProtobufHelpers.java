package com.zqnt.utils.core;

import com.google.protobuf.Timestamp;

import java.time.Instant;
import java.time.OffsetDateTime;
import java.time.ZoneId;
import java.time.ZoneOffset;


public class ProtobufHelpers {

	public static Timestamp toTimestamp(Instant instant) {
		if (instant == null) {
			return null;
		}
		return Timestamp.newBuilder()
				.setSeconds(instant.getEpochSecond())
				.setNanos(instant.getNano())
				.build();
	}

	public static Instant toInstant(Timestamp timestamp) {
		if (timestamp == null) {
			return null;
		}
		return Instant.ofEpochSecond(timestamp.getSeconds(), timestamp.getNanos());
	}

	// Protobuf Timestamp → OffsetDateTime (UTC)
	public static OffsetDateTime toOffsetDateTime(Timestamp timestamp) {
		if (timestamp == null || (timestamp.getSeconds() == 0 && timestamp.getNanos() == 0)) {
			// Empty/default Timestamp → use current time
			return OffsetDateTime.now(ZoneOffset.UTC);
		}
		Instant instant = Instant.ofEpochSecond(timestamp.getSeconds(), timestamp.getNanos());
		return OffsetDateTime.ofInstant(instant, ZoneOffset.UTC);
	}

	// Protobuf Timestamp → OffsetDateTime mit spezifischer Timezone
	public static OffsetDateTime toOffsetDateTime(Timestamp timestamp, ZoneId zoneId) {
		if (timestamp == null || (timestamp.getSeconds() == 0 && timestamp.getNanos() == 0)) {
			// Empty/default Timestamp → use current time
			return OffsetDateTime.now(zoneId);
		}
		Instant instant = Instant.ofEpochSecond(timestamp.getSeconds(), timestamp.getNanos());
		return OffsetDateTime.ofInstant(instant, zoneId);
	}

	// OffsetDateTime → Protobuf Timestamp
	public static Timestamp toTimestamp(OffsetDateTime offsetDateTime) {
		if (offsetDateTime == null) {
			return null;
		}
		Instant instant = offsetDateTime.toInstant();
		return Timestamp.newBuilder()
				.setSeconds(instant.getEpochSecond())
				.setNanos(instant.getNano())
				.build();
	}

	// Aktuelle Zeit als Timestamp
	public static Timestamp now() {
		Instant instant = Instant.now();
		return Timestamp.newBuilder()
				.setSeconds(instant.getEpochSecond())
				.setNanos(instant.getNano())
				.build();
	}
}
