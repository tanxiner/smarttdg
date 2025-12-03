# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_001
**Type:** Stored Procedure

The procedure retrieves OCC authorisation details based on user ID, operation date, access date, and roster code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve authorisation for. |

### Logic Flow
1. Checks if a workflow exists for the given line.
2. Retrieves endorser details from the #TMP_Endorser table based on the workflow ID and line.
3. Iterates through each endorser, updating the corresponding fields in the #TMP_OCCAuthNEL table based on the endorser's level and role.
4. Fetches all OCC authorisation records from the #TMP_OCCAuthNEL table.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TAMS_OCC_Auth_Workflow]