# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20230112

### Purpose
This stored procedure updates the registration module status to "Approved" and creates a new user account if necessary, based on the system owner's approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who approved the registration module. |

### Logic Flow
1. Check if the registration module is external. If it is, set the workflow type to "ExtUser". Otherwise, determine the workflow type based on the module type.
2. Retrieve the current status and line number of the registration module from TAMS_Reg_Module and TAMS_Registration tables.
3. Find the next stage ID and status for the system owner's approval in TAMS_WFStatus table.
4. Get the workflow ID, role ID, and endorser ID associated with the registration module in TAMS_Workflow, TAMS_Endorser, and TAMS_Endorser tables respectively.
5. Check if the registration module already exists in TAMS_Reg_Module table. If it does, update its status to "Approved" and set the updated on and updated by fields.
6. Create a new user account for the registration module if necessary, based on the system owner's approval.
7. Insert an audit log entry for the system owner's approval.

### Data Interactions
* Reads: TAMS_Reg_Module, TAMS_Registration, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_Action_Log, TAMS_User
* Writes: TAMS_Reg_Module