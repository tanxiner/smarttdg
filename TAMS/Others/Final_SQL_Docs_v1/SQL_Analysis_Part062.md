Here are the documented procedures:

### Procedure: sp_TAMS_GetTarEnquiryResult_User20250120
**Type:** Stored Procedure

Purpose: Retrieves TAR data for a specific user, filtered by various parameters.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |

Logic Flow:
1. Checks if the user exists in the system.
2. If the user exists, checks which roles they have access to based on their TrackType.
3. Based on the role, sets flags (@IsAll, @IsPower, @IsDep) indicating whether all, power, or department-specific data should be retrieved.
4. Constructs a WHERE clause based on the input parameters (Line, TarType, AccessType, TarStatusId, AccessDateFrom, AccessDateTo).
5. Executes a SELECT statement with ROW_NUMBER() to retrieve TAR data ordered by user name.

Data Interactions:
* Reads: TAMS_User, TAMS_TAR, TAMS_WFStatus
* Writes: None

### Procedure: sp_TAMS_GetTarForPossessionPlanReport
**Type:** Stored Procedure

Purpose: Retrieves TAR data for a specific line and track type.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Line number |
| @TrackType | nvarchar(50) | Track type |

Logic Flow:
1. Constructs a WHERE clause based on the input parameters (Line, TrackType).
2. Executes a SELECT statement to retrieve TAR data.

Data Interactions:
* Reads: TAMS_TAR
* Writes: None

### Procedure: sp_TAMS_GetTarOtherProtectionByPossessionId
**Type:** Stored Procedure

Purpose: Retrieves other protection data for a specific possession ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Possession ID |

Logic Flow:
1. Executes a SELECT statement to retrieve other protection data for the specified possession ID.
2. Orders the results by ID.

Data Interactions:
* Reads: TAMS_Possession_OtherProtection
* Writes: None

### Procedure: sp_TAMS_GetTarPossessionLimitByPossessionId
**Type:** Stored Procedure

Purpose: Retrieves possession limit data for a specific possession ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Possession ID |

Logic Flow:
1. Executes a SELECT statement to retrieve possession limit data for the specified possession ID.
2. Orders the results by ID.

Data Interactions:
* Reads: TAMS_Possession_Limit
* Writes: None

### Procedure: sp_TAMS_GetTarPossessionPlanByTarId
**Type:** Stored Procedure

Purpose: Retrieves possession plan data for a specific TAR ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | TAR ID |

Logic Flow:
1. Executes a SELECT statement to retrieve possession plan data for the specified TAR ID.
2. Joins with TAMS_Type_Of_Work to retrieve additional information.

Data Interactions:
* Reads: TAMS_Possession, TAMS_Type_Of_Work
* Writes: None

### Procedure: sp_TAMS_GetTarPossessionPowerSectorByPossessionId
**Type:** Stored Procedure

Purpose: Retrieves power sector data for a specific possession ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Possession ID |

Logic Flow:
1. Executes a SELECT statement to retrieve power sector data for the specified possession ID.
2. Orders the results by ID.

Data Interactions:
* Reads: TAMS_Possession_PowerSector
* Writes: None

### Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLine
**Type:** Stored Procedure

Purpose: Retrieves sectors data for a specific line and access date.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | Access date |
| @Line | nvarchar(10) | Line number |

Logic Flow:
1. Constructs two WHERE clauses based on the input parameters (Line, TrackType).
2. Executes a SELECT statement to retrieve sector data.
3. Updates ColourCode column with top 1 value.

Data Interactions:
* Reads: TAMS_Sector
* Writes: None

### Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection
**Type:** Stored Procedure

Purpose: Retrieves sectors data for a specific line, access date, and direction.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | Access date |
| @Line | nvarchar(10) | Line number |
| @TrackType | nvarchar(50) | Track type |
| @Direction | nvarchar(10) | Direction |

Logic Flow:
1. Constructs two WHERE clauses based on the input parameters (Line, TrackType).
2. Executes a SELECT statement to retrieve sector data.
3. Updates ColourCode column with top 1 value.

Data Interactions:
* Reads: TAMS_Sector
* Writes: None