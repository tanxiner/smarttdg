# Procedure: sp_TAMS_TB_Gen_Summary
**Type:** Stored Procedure

The procedure generates a summary of TAMS TB data based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) for which to generate the summary. |

### Logic Flow
1. Checks if user exists and selects data from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables based on the provided parameters.
2. If @Line is 'DTL', generates a summary of DTL line data with multiple conditions (e.g., AccessType, Company, TrackType).
3. If @Line is 'NEL', generates a summary of NEL line data with specific conditions (e.g., AccessType, Company, TrackType).

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters
* **Writes:** None