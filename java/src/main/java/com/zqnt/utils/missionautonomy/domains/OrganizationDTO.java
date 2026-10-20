package com.zqnt.utils.missionautonomy.domains;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.time.Instant;
import java.util.Set;
import java.util.UUID;

/**
 * DTO for {@link com.zequent.framework.services.connector.entities.Organization}
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class OrganizationDTO implements Serializable {
	private UUID id;
	private Instant createdAt;
	private Instant modifiedAt;
	private String modifiedFrom;
	private String name;
	private String description;
	private Set<UUID> assets;
}