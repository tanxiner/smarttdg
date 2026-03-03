# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters_bak20230711
**Type:** Stored Procedure

The purpose of this stored procedure is to update the OCC Authorisation status for a given user ID and OCC Auth ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user making the update. |
| @OCCAuthID | int | The ID of the OCC Auth being updated. |
| @Line | nvarchar(10) | The line number for which the update is being made. |
| @RemarksPFR | nvarchar(100) | The remarks for the PFR (Power and Fuel Record). |
| @SelectionValue | nvarchar(50) | The selected value for the OCC Auth status. |
| @StationName | nvarchar(50) | The name of the station where the update is being made. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table for Update action.
3. Updates the OCC Auth status based on the selected value and line number.
4. If the selected value is 'Select', it sets the value to 'Pending'.
5. If the selected value is not 'Select', it sets the first test result to the selected value.
6. Inserts into Audit table for Insert action.
7. Updates the OCC Auth status in the main table based on the updated values.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_OCC_Auth_Workflow], [dbo].[TAMS_OCC_Auth_Workflow_Audit], [dbo].[TAMS_OCC_Auth_Audit]
* **Writes:** [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit], [TAMS_OCC_Auth_Audit]