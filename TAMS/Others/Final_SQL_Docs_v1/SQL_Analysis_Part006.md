# Procedure: sp_TAMS_Applicant_List_Master_OnLoad
**Type:** Stored Procedure

Purpose: This stored procedure retrieves a list of applicants from the TAMS system, filtered by line, track type, access date range, and TAR type.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by |
| @TrackType | NVARCHAR(50) | The track type to filter by |
| @ToAccessDate | NVARCHAR(20) | The end date of the access range |
| @FromAccessDate | NVARCHAR(20) | The start date of the access range |
| @TARType | NVARCHAR(20) | The TAR type to filter by |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_Sector, TAMS_TAR
* Writes: #TmpSector

# Procedure: sp_TAMS_Applicant_List_OnLoad
**Type:** Stored Procedure

Purpose: This stored procedure retrieves a list of applicants from the TAMS system, filtered by line, access date range, and TAR type.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by |
| @ToAccessDate | NVARCHAR(20) | The end date of the access range |
| @FromAccessDate | NVARCHAR(20) | The start date of the access range |
| @TARType | NVARCHAR(20) | The TAR type to filter by |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_Sector, TAMS_TAR
* Writes: #TmpSector

# Procedure: sp_TAMS_Approval_Add_BufferZone
**Type:** Stored Procedure

Purpose: This stored procedure adds a buffer zone to the TAMS system for a given TAR and sector ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to add the buffer zone to |
| @SectorID | BIGINT | The sector ID to add the buffer zone to |
| @Message | NVARCHAR(500) | An output parameter for error messages |

Logic Flow:
1. Checks if user exists.
2. Inserts into TAMS_TAR_Sector table.

Data Interactions:
* Reads: TAMS_Sector
* Writes: TAMS_TAR_Sector

# Procedure: sp_TAMS_Approval_Add_TVFStation
**Type:** Stored Procedure

Purpose: This stored procedure adds a TVF station to the TAMS system for a given TAR and sector ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to add the TVF station to |
| @StationID | BIGINT | The TVF station ID to add |
| @Direction | NVARCHAR(20) | The direction of the TVF station |
| @Message | NVARCHAR(500) | An output parameter for error messages |

Logic Flow:
1. Checks if user exists.
2. Inserts into TAMS_TAR_TVF table.

Data Interactions:
* Reads: TAMS_Sector
* Writes: TAMS_TAR_TVF

# Procedure: sp_TAMS_Approval_Del_BufferZone
**Type:** Stored Procedure

Purpose: This stored procedure deletes a buffer zone from the TAMS system for a given TAR and sector ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to delete the buffer zone from |
| @SectorID | BIGINT | The sector ID to delete the buffer zone from |
| @Message | NVARCHAR(500) | An output parameter for error messages |

Logic Flow:
1. Deletes from TAMS_TAR_Sector table.

Data Interactions:
* Reads: TAMS_TAR_Sector
* Writes: None

# Procedure: sp_TAMS_Approval_Del_TVFStation
**Type:** Stored Procedure

Purpose: This stored procedure deletes a TVF station from the TAMS system for a given TAR and TVF ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to delete the TVF station from |
| @TVFID | BIGINT | The TVF station ID to delete |
| @Message | NVARCHAR(500) | An output parameter for error messages |

Logic Flow:
1. Deletes from TAMS_TAR_TVF table.

Data Interactions:
* Reads: TAMS_TAR_TVF
* Writes: None