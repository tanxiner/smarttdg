# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany_20231009
**Type:** Stored Procedure

The purpose of this stored procedure is to update a user's registration status from "Pending Company Approval" to "Approved" after being approved by the system administrator.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module that needs approval. |
| @UserID | NVARCHAR(200) | The ID of the user whose registration is being updated. |

### Logic Flow
1. Checks if the user exists and has a pending company approval status.
2. Retrieves the company information from TAMS_Registration table based on the user's ID.
3. Inserts or updates the company information into TAMS_Company table.
4. Updates the Company ID in TAMS_Registration table with the newly inserted ID.
5. Inserts an audit log entry to track the system administrator's approval of the company registration for the user.
6. Sends an email notification to the endorser and other relevant parties with a link to access TAMS.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module table
	+ TAMS_WFStatus table
	+ TAMS_Workflow table
	+ TAMS_Endorser table
	+ TAMS_Registration table
	+ TAMS_Company table
	+ TAMS_Action_Log table
* **Writes:**
	+ TAMS_Reg_Module table
	+ TAMS_Company table
	+ TAMS_Registration table
	+ TAMS_Action_Log table