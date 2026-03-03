# Procedure: sp_TAMS_TB_Gen_Summary_20230904_M
**Type:** Stored Procedure

This procedure generates a summary report for TAMS TB data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to generate the report for. |

### Logic Flow
1. Checks if user exists and specifies the line type (@Line = 'DTL' or @Line = 'NEL').
2. If @Line is 'DTL', generates a detailed report with access dates, TAR IDs, electrical sections, nature of work, remarks, and more.
3. If @Line is 'NEL', generates a summary report for NEL data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone (for NEL reports)
* **Writes:** None