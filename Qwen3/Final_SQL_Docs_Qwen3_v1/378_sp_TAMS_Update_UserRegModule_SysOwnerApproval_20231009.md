# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20231009

### Purpose
This stored procedure updates a user registration module's status to "Approved" and creates or updates a corresponding user account if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module. |

### Logic Flow
1. The procedure checks if the registration module is external or not.
2. If it's external, it sets a specific workflow type; otherwise, it determines the workflow type based on the module name.
3. It retrieves the next stage title and ID from the TAMS_WFStatus table where the line matches the registration module's line.
4. It finds the workflow ID and work flow type that match the determined workflow type and the current date range.
5. If a corresponding user account exists, it updates the registration module's status to "Approved" and sets the updated on and updated by fields.
6. If no user account exists, it creates one based on the registration module's data.
7. It inserts an audit log entry for the system owner approving the registration module.
8. It sends an email notification to the registered users with a link to access TAMS.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_Action_Log, TAMS_User
* Writes: TAMS_Reg_Module (updated), TAMS_User (created or updated)