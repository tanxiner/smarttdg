# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany_20231009

### Purpose
This stored procedure is used to update a user's registration module status from 'Pending Company Approval' to 'Approved' by a system administrator, and also registers the company information into TAMS_Company.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UserID | NVARCHAR(200) | The user ID associated with the registration module. |

### Logic Flow
1. Check if the specified registration module exists and has a status of 'Pending Company Approval'. If not, exit the procedure.
2. Retrieve the company information from TAMS_Registration based on the user's ID.
3. Create a temporary table to store the updated registration modules with the new workflow status.
4. Open a cursor to iterate through the rows in the temporary table and update the corresponding registration module with the new workflow status.
5. Insert an audit log entry for the system administrator approving the company registration.
6. Register the company information into TAMS_Company if it does not already exist.
7. Update the Company ID in TAMS_Registration based on the retrieved company information.
8. Commit the transaction.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_WFStatus
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_User
	+ TAMS_Registration
	+ TAMS_Company
	+ TAMS_Action_Log
* **Writes:** 
	+ TAMS_Reg_Module
	+ TAMS_Action_Log