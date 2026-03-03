# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_001

### Purpose
This stored procedure retrieves OCC authorisation details based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve authorisation for. |

### Logic Flow
1. The procedure starts by selecting the workflow ID from the TAMS_Workflow table where the line matches the provided line parameter and the workflow type is 'OCCAuth' and the record is active.
2. It then inserts data into a temporary table #TMP_Endorser, which contains endorser IDs, levels, titles, and roles for the specified line.
3. The procedure creates another temporary table #TMP_OCCAuthNEL to store OCC authorisation details.
4. A cursor is created to iterate through the OCC authorisation ID in #TMP_OCCAuthNEL.
5. For each OCC authorisation ID, a sub-procedure is executed to update the corresponding endorser IDs and levels in #TMP_Endorser.
6. The procedure then updates the OCC authorisation details in #TMP_OCCAuthNEL based on the updated endorser data.
7. Finally, the procedure selects all data from #TMP_OCCAuthNEL.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_Traction_Power, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow