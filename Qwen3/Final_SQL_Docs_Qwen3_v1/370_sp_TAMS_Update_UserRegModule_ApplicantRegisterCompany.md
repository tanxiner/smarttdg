# Procedure: sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany

### Purpose
This stored procedure updates company details for a registered user and triggers the approval process for the applicant registration.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. The procedure starts by checking if there is an existing record in TAMS_Reg_Module with a pending status for the given RegID.
2. If such a record exists, it updates the company details in TAMS_Registration and creates a new record in #TMP_RegModule.
3. It then iterates through each record in #TMP_RegModule, retrieves the next stage ID for the current record, and updates the corresponding record in TAMS_Reg_Module with the new status.
4. After updating all records, it sends an email to the registered user's email address with a link to access TAMS for approval/rejection of the registration.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_Registration
	+ TAMS_User
	+ TAMS_User_Role
	+ TAMS_WFStatus
	+ TAMS_Endorser
	+ TAMS_Workflow
	+ TAMS_Action_Log
* **Writes:**
	+ #TMP_RegModule (temporary table)
	+ TAMS_Reg_Module
	+ TAMS_Registration