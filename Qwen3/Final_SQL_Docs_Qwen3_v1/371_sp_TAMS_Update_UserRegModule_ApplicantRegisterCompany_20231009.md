# Procedure: sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany_20231009

### Purpose
This stored procedure updates company details for a registered user in the TAMS system, including sending an email to external users for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. The procedure starts by creating a temporary table #TMP_RegModule to store the modules that need to be updated.
2. It checks if there are any existing TAMS_Reg_Module records for the given RegID and updates the Company details in TAMS_Registration.
3. For each module, it retrieves the next stage ID from TAMS_Workflow and gets the corresponding endorser ID and workflow status ID.
4. It then inserts a new record into TAMS_Reg_Module with the updated values and sends an email to external users for approval using EAlertQ_EnQueue.
5. Finally, it commits or rolls back the transaction based on whether any errors occur during execution.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_Registration
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_WFStatus
	+ TAMS_User
	+ TAMS_User_Role
	+ TAMS_Parameters
* **Writes:** 
	+ #TMP_RegModule (temporary table)
	+ TAMS_Reg_Module
	+ TAMS_Action_Log