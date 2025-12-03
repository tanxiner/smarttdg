# Procedure: sp_TAMS_TB_Gen_Summary_20230904

### Purpose
This stored procedure generates a summary of TAMS TB data for a specific date range, including access dates, TAR IDs, electrical sections, nature of work, and remarks.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to generate summary for. |

### Logic Flow

1. The procedure checks if the specified line type is 'DTL'. If true, it generates a summary of DTL data.
2. For DTL data, it selects records from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables based on specific conditions (e.g., access date range, TAR status ID, access type).
3. The procedure then orders the results by access date and TAR number.
4. If the specified line type is 'NEL', it generates a summary of NEL data.
5. For NEL data, it selects records from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables based on specific conditions (e.g., access date range, TAR status ID, access type).
6. The procedure then orders the results by access date.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES, TAMS_Get_Station_Dir, TAMS_Get_ES, TAMS_Get_TVF_Station, and TAMS_Get_Station tables.
* **Writes:** No writes are performed by this stored procedure.