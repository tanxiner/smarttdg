# Procedure: sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany_20231009

### Purpose
Updates the company details for a user registration and advances the registration workflow to the next approval stage, notifying the appropriate approvers by email.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Identifier of the user registration record to update |
| @Company | NVARCHAR(200) | New company name |
| @UENNo | NVARCHAR(200) | New UEN number |
| @BizOwner | NVARCHAR(200) | New business owner name |
| @OfficeTel | NVARCHAR(20) | New office telephone number |
| @Mobile | NVARCHAR(20) | New mobile number |
| @Email | NVARCHAR(200) | New company email address |

### Logic Flow
1. Begin a transaction to ensure atomicity.  
2. Create a temporary table to hold pending workflow modules for the specified registration.  
3. Verify that a registration module with the given `@RegID` exists and is active (`RegStatus = 1`).  
4. If the module exists, update the `TAMS_Registration` record with the new company details supplied in the parameters.  
5. Populate the temporary table with all rows from `TAMS_Reg_Module` that are pending approval for this registration.  
6. Open a cursor over the temporary table and iterate through each pending module:  
   a. Determine the next workflow stage by querying `TAMS_Workflow` for the current line and workflow type.  
   b. Retrieve the next endorser’s status, role, and ID from `TAMS_Endorser` based on the current status level.  
   c. Translate the new status ID into a status description via `TAMS_WFStatus`.  
   d. Insert a new record into `TAMS_Reg_Module` representing the next approval step, marking it as pending.  
   e. Update the current module record to `WFStatus = 'Approved'` and set its `UpdatedOn` timestamp.  
   f. Build an email notification: gather all users who hold the role identified in step b, concatenate their email addresses, and compose a message that includes the company name, UEN, and a link to the login page.  
   g. Queue the email through the `EAlertQ_EnQueue` procedure.  
7. After processing all pending modules, close and deallocate the cursor.  
8. Insert an audit entry into `TAMS_Action_Log` to record that the external user updated company details.  
9. Commit the transaction.  
10. If any error occurs, roll back the transaction to preserve data integrity.

### Data Interactions
* **Reads:**  
  - TAMS_Reg_Module  
  - TAMS_Registration  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_WFStatus  
  - TAMS_User  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_Parameters  

* **Writes:**  
  - TAMS_Registration (UPDATE)  
  - TAMS_Reg_Module (INSERT and UPDATE)  
  - TAMS_Action_Log (INSERT)  
  - Temporary table `#TMP_RegModule` (CREATE, INSERT, DELETE)  
  - Email queue via `EAlertQ_EnQueue` (procedure call)