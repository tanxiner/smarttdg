# Procedure: sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany
**Type:** Stored Procedure

### Purpose
This stored procedure updates company details for a registered user and triggers the approval process for the applicant registration.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. Checks if the user exists with the given RegID.
2. Updates the company details in TAMS_Registration table.
3. Retrieves the next stage ID for each TAMS_Reg_Module record associated with the updated RegID.
4. Inserts new records into TAMS_Reg_Module to reflect the updated status and workflow IDs.
5. Sends an email notification to the endorser(s) and other relevant users.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User, TAMS_User_Role
* **Writes:** TAMS_Action_Log