# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval
**Type:** Stored Procedure

The purpose of this stored procedure is to update a user's registration module status from "External" or "Internal" (depending on the module type) to "Approved" by the system owner.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module status. |

### Logic Flow
1. Checks if the user exists in the TAMS_Registration table.
2. Retrieves the current stage and workflow ID for the specified registration module.
3. Determines the next stage title based on the current stage and workflow type.
4. Updates the registration module status to "Approved" and inserts a new record into the TAMS_Reg_Module table with the updated status.
5. If the user does not exist in the TAMS_User table, creates a new user account for the registered user.
6. Inserts an audit log entry to track the update of the registration module status.
7. Sends an email notification to the registered user with instructions on how to access the system.

### Data Interactions
* **Reads:** 
	+ TAMS_Registration table
	+ TAMS_Reg_Module table
	+ TAMS_WFStatus table
	+ TAMS_Workflow table
	+ TAMS_Endorser table
	+ TAMS_User table
* **Writes:**
	+ TAMS_Reg_Module table
	+ TAMS_Action_Log table