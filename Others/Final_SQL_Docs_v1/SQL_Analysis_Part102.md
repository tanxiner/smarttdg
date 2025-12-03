# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationCCByParameters
**Type:** Stored Procedure

The purpose of this stored procedure is to update the OCC authorization status for a given user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user whose OCC authorization status needs to be updated. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [dbo].[TAMS_Workflow], [dbo].[TAMS_Endorser], [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_OCC_Auth_Workflow]
* **Writes:** [dbo].[TAMS_OCC_Auth_Workflow_Audit], [dbo].[TAMS_OCC_Auth_Audit]