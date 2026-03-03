# Procedure: sp_TAMS_TAR_View_Detail_OnLoad
**Type:** Stored Procedure

The procedure retrieves detailed information about a specific TAR (Test and Measurement) record, including its status, access history, and related data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to retrieve. |
| @LogInUser | NVARCHAR(20) | The username of the user who accessed the TAR record. |

### Logic Flow
1. Checks if a user exists for the given TAR ID.
2. Inserts into an audit table (not shown in this procedure).
3. Returns the detailed information about the TAR record.

### Data Interactions
* Reads: TAMS_TAR, TAMS_Sector, TAMS_Station, TAMS_Access_Requirement, TAMS_Possession, TAMS_Type_Of_Work, TAMS_TAR_Workflow
* Writes: None

# Procedure: sp_TAMS_TB_Gen_Report
**Type:** Stored Procedure

The procedure generates a report based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. (Optional) |
| @TrackType | NVARCHAR(50) | The track type to filter by. (Optional) |
| @AccessDateFrom | NVARCHAR(20) | The start date of the access period. (Optional) |
| @AccessDateTo | NVARCHAR(20) | The end date of the access period. (Optional) |
| @AccessType | NVARCHAR(20) | The access type to filter by. (Optional) |

### Logic Flow
1. Checks if a line number is provided and filters the report accordingly.
2. If no line number is provided, checks if a track type is provided and filters the report accordingly.
3. If neither a line number nor a track type is provided, generates a full report.

### Data Interactions
* Reads: TAMS_TAR
* Writes: None

# Procedure: sp_TAMS_TB_Gen_Report_20230904
**Type:** Stored Procedure

The procedure generates a report based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. (Optional) |
| @TrackType | NVARCHAR(50) | The track type to filter by. (Optional) |
| @AccessDateFrom | NVARCHAR(20) | The start date of the access period. (Optional) |
| @AccessDateTo | NVARCHAR(20) | The end date of the access period. (Optional) |
| @AccessType | NVARCHAR(20) | The access type to filter by. (Optional) |

### Logic Flow
1. Generates a report based on the provided parameters.
2. Filters the report by TAR status ID 8.

### Data Interactions
* Reads: TAMS_TAR
* Writes: None

# Procedure: sp_TAMS_TB_Gen_Report_20230904_M
**Type:** Stored Procedure

The procedure generates a report based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. (Optional) |
| @TrackType | NVARCHAR(50) | The track type to filter by. (Optional) |
| @AccessDateFrom | NVARCHAR(20) | The start date of the access period. (Optional) |
| @AccessDateTo | NVARCHAR(20) | The end date of the access period. (Optional) |
| @AccessType | NVARCHAR(20) | The access type to filter by. (Optional) |

### Logic Flow
1. Generates a report based on the provided parameters.
2. Filters the report by TAR status ID 8.

### Data Interactions
* Reads: TAMS_TAR
* Writes: None