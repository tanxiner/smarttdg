Here are the documented procedures:

### Procedure: sp_TAMS_TB_Gen_Report_20230911
**Type:** Stored Procedure

Purpose: This procedure generates a report for TAMS TB data from September 11, 2023.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the report by. |
| @TrackType | NVARCHAR(50) | The track type to filter the report by. |
| @AccessDateFrom | NVARCHAR(20) | The start date for access dates. |
| @AccessDateTo | NVARCHAR(20) | The end date for access dates. |
| @AccessType | NVARCHAR(20) | The access type to filter the report by. |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone
* Writes: None

### Procedure: sp_TAMS_TB_Gen_Report_20230911_M
**Type:** Stored Procedure

Purpose: This procedure generates a report for TAMS TB data from September 11, 2023, with modifications.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the report by. |
| @TrackType | NVARCHAR(50) | The track type to filter the report by. |
| @AccessDateFrom | NVARCHAR(20) | The start date for access dates. |
| @AccessDateTo | NVARCHAR(20) | The end date for access dates. |
| @AccessType | NVARCHAR(20) | The access type to filter the report by. |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone
* Writes: None

### Procedure: sp_TAMS_TB_Gen_Report_20230915
**Type:** Stored Procedure

Purpose: This procedure generates a report for TAMS TB data from September 15, 2023.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the report by. |
| @TrackType | NVARCHAR(50) | The track type to filter the report by. |
| @AccessDateFrom | NVARCHAR(20) | The start date for access dates. |
| @AccessDateTo | NVARCHAR(20) | The end date for access dates. |
| @AccessType | NVARCHAR(20) | The access type to filter the report by. |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone
* Writes: None

### Procedure: sp_TAMS_TB_Gen_Report_20230915_M
**Type:** Stored Procedure

Purpose: This procedure generates a report for TAMS TB data from September 15, 2023, with modifications.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the report by. |
| @TrackType | NVARCHAR(50) | The track type to filter the report by. |
| @AccessDateFrom | NVARCHAR(20) | The start date for access dates. |
| @AccessDateTo | NVARCHAR(20) | The end date for access dates. |
| @AccessType | NVARCHAR(20) | The access type to filter the report by. |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone
* Writes: None

### Procedure: sp_TAMS_TB_Gen_Report_20231009
**Type:** Stored Procedure

Purpose: This procedure generates a report for TAMS TB data from October 9, 2023.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the report by. |
| @TrackType | NVARCHAR(50) | The track type to filter the report by. |
| @AccessDateFrom | NVARCHAR(20) | The start date for access dates. |
| @AccessDateTo | NVARCHAR(20) | The end date for access dates. |
| @AccessType | NVARCHAR(20) | The access type to filter the report by. |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone
* Writes: None

### Tables used:

* TAMS_TAR
* TAMS_Get_Station
* TAMS_Get_ES_NoBufferZone