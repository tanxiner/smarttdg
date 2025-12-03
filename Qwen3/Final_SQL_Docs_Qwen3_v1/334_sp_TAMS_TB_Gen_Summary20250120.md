# Procedure: sp_TAMS_TB_Gen_Summary20250120

### Purpose
This stored procedure generates a summary of TAMS data for a specific date range, including access dates, TAR IDs, electrical sections, nature of work, and remarks.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to be processed. |

### Logic Flow

1. The procedure checks if the specified line type is 'DTL'. If true, it processes data for 'DTL' lines.
2. For 'DTL' lines, it selects data from multiple tables based on various conditions and filters, including access dates, TAR IDs, electrical sections, nature of work, and remarks.
3. The procedure also checks if the specified line type is 'NEL'. If true, it processes data for 'NEL' lines.
4. For 'NEL' lines, it selects data from multiple tables based on various conditions and filters, including access dates, TAR IDs, electrical sections, nature of work, and remarks.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station_Dir, TAMS_Get_ES_NoBufferZone, TAMS_Get_TVF_Station, and TAMS_Parameters.
* **Writes:** None