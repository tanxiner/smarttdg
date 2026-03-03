# Procedure: sp_TAMS_TB_Gen_Summary_20230904
**Type:** Stored Procedure

The procedure generates a summary report for TAMS TB data based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to generate the report for. |

### Logic Flow
1. Checks if the specified line type is 'DTL'. If true, it generates a detailed report with various fields such as Access Date, TAR ID, Electrical Section, Nature of Work, and Remarks.
2. If the specified line type is not 'DTL', it checks if the line type is 'NEL'. If true, it generates a summary report for NEL data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters, TAMS_Get_ES, TAMS_Get_Station_Dir, TAMS_Get_ES, TAMS_Get_TVF_Station
* **Writes:** None