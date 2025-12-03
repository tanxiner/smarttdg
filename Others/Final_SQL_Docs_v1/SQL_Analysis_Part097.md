# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216
**Type:** Stored Procedure

### Purpose
This stored procedure retrieves OCC authorisation data for a given set of parameters, including user ID, line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the OCC authorisation data. |

### Logic Flow
1. Checks if a workflow exists for the given line.
2. Inserts endorser data into a temporary table based on the workflow and line.
3. Retrieves traction power data from the system and inserts it into another temporary table.
4. Retrieves OCC authorisation data from the system, filtering by operation date, access date, and user ID.
5. Iterates through the retrieved OCC authorisation data, updating fields in the temporary tables based on specific endorser IDs.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power_Detail], [TAMS_Station], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** #TMP, #TMP_Endorser, #TMP_OCCAuthTC