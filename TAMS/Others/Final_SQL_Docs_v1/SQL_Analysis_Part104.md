# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELByParameters_bak20230711
**Type:** Stored Procedure

The purpose of this stored procedure is to update the OCC authorization level for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to be updated. |
| @OCCAuthID | int | The ID of the OCC authorization to be updated. |
| @OCCLevel | int | The new level of the OCC authorization. |
| @Line | nvarchar(10) | The line number for which the OCC authorization is being updated. |
| @Remarks | nvarchar(100) | Any remarks associated with the update. |
| @SelectionValue | nvarchar(50) | The value to be used in the OCC authorization workflow. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table for Update action.
3. Updates the OCC authorization level based on the provided OCCLevel.
4. For each OCCLevel, it updates the corresponding WFStatus and inserts a new record into TAMS_OCC_Auth_Workflow with the selected value.
5. Updates the OCCAuthStatusId in TAMS_OCC_Auth based on the updated WFStatus.
6. If @OCCLevel is 15, it sets the OCCAuthStatusId to 15.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit], [TAMS_OCC_Auth_Audit]
* **Writes:** [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow_Audit], [TAMS_OCC_Auth_Audit]