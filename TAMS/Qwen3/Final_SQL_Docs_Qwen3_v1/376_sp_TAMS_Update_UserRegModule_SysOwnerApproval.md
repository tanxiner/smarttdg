# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval

### Purpose
This stored procedure updates the registration module status to "Approved" and creates a new user account if necessary, based on the system owner's approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module status. |

### Logic Flow
1. Check if the registration module is external or not.
2. If it's external, set the workflow type to 'ExtUser'.
3. If it's not external, determine the workflow type based on the module type (TAR, DCC, OCC).
4. Retrieve the next stage ID and status from TAMS_WFStatus table.
5. Find the workflow ID associated with the current line and workflow type.
6. Get the endorser ID and role ID for the current line and workflow ID.
7. Check if there are any existing registration modules with the same ID, and update their status to 'Approved' if so.
8. Create a new user account if necessary (i.e., if the registration module is not external).
9. Insert an audit log entry for the system owner's approval.
10. Send an email notification to the registered users.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_User, TAMS_Action_Log
* Writes: TAMS_Reg_Module (updated status), TAMS_User (new account creation)