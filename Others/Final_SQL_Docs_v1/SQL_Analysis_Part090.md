# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL
**Type:** Stored Procedure

This stored procedure retrieves OCC authorisation data for a specified user and parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve OCC authorisation data for. |

### Logic Flow
1. Checks if a workflow exists for the specified user and track type.
2. Retrieves endorser information from the TAMS_Endorser table based on the workflow ID.
3. Iterates through each endorser and updates the corresponding fields in the #TMP_OCCAuthNEL table.
4. Updates the OCC authorisation data with the retrieved endorser information.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** #TMP_OCCAuthNEL