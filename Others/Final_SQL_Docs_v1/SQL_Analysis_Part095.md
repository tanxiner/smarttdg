# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters_bak20230727
**Type:** Stored Procedure

The procedure retrieves OCC authorisation data for a given set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID to retrieve data for. |

### Logic Flow
1. Checks if the user exists.
2. Retrieves the workflow ID from the TAMS_Workflow table based on the provided Line, TrackType, and WorkflowType parameters.
3. Inserts data into the #TMP_Endorser temporary table based on the retrieved workflow ID and user ID.
4. Retrieves traction power IDs and station names from the TAMS_Traction_Power and TAMS_Station tables.
5. Inserts data into the #TMP_OCCAuthPFR temporary table based on the retrieved traction power IDs and OCC authorisation data.
6. Iterates through the #TMP_OCCAuthPFR table, updating fields based on the endorser ID.
7. Closes all cursors and deallocates memory.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Traction_Power, TAMS_Station, TAMS_OCC_Auth, TAMS_OCC_Duty_Roster
* **Writes:** #TMP_Endorser, #TMP_OCCAuthPFR