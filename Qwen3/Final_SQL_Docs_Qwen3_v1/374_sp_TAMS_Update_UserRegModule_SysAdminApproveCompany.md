# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany

### Purpose
This stored procedure is used to update a user's registration module status from "Pending Company Approval" to "Approved" by a system administrator, and also sends an email notification to the endorser and other relevant stakeholders.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @UserID | NVARCHAR(200) | The ID of the user whose registration module status is being updated. |

### Logic Flow
1. Check if the specified registration module exists and has a pending company approval status.
2. If it does, retrieve the relevant information from the TAMS_Reg_Module table.
3. Create a temporary table to store the data for further processing.
4. Open a cursor to iterate through the data in the temporary table.
5. For each iteration, check if there is an active workflow with the same line and track type as the current registration module.
6. If an active workflow exists, retrieve the next stage ID for this TAMS_Reg_Module.
7. Update the WFStatus column in the TAMS_Reg_Module table to reflect the new status.
8. Send an email notification to the endorser and other relevant stakeholders using the EAlertQ_EnQueue stored procedure.
9. If a company registration record exists for the user, update its CompanyID field with the ID of the newly created company.
10. Insert an audit log entry into the TAMS_Action_Log table.

### Data Interactions
* Reads: 
	+ TAMS_Reg_Module
	+ TAMS_WFStatus
	+ TAMS_Endorser
	+ TAMS_Workflow
	+ TAMS_Company
	+ TAMS_Registration
	+ TAMS_User_Role
	+ TAMS_Action_Log
* Writes:
	+ TAMS_Reg_Module (updated WFStatus column)
	+ TAMS_Company (newly created company record)