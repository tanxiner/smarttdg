# Procedure: sp_TAMS_TB_Gen_Summary20250120
**Type:** Stored Procedure

This procedure generates a summary of TAMS data for a specific date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Specifies the track type |
| @AccessDateFrom | NVARCHAR(20) | Start date of access range |
| @AccessDateTo | NVARCHAR(20) | End date of access range |
| @AccessType | NVARCHAR(20) | Access type |

### Logic Flow
1. Checks if user exists and specifies the line type (DTL or NEL).
2. For DTL line type, it generates a summary for each track type by selecting data from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables.
3. For NEL line type, it generates a summary for each track type by selecting data from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters
* **Writes:** None