# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20230112

### Purpose
Approve a user registration module, update its status to Approved, create a user account if missing, log the action, and notify the applicant via email.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module record to approve |
| @UpdatedBy | INT | User ID performing the approval |

### Logic Flow
1. Start a transaction.  
2. Retrieve the `IsExternal` flag for the registration linked to the supplied `@RegModID`.  
3. Determine the workflow type:  
   * If external, set to `ExtUser`.  
   * If internal, set to `TARIntUser` when the module is `TAR`; otherwise set to `OCCIntUser`.  
4. Pull the registration ID, line, module, external flag, and current registration status from the registration module and registration tables.  
5. Identify the workflow status ID and status text for the `Approved` state that matches the module’s line.  
6. Locate the active workflow record for the line and workflow type whose effective date range includes today.  
7. Find the next endorser record: select the workflow status ID, role ID, and endorser ID where the level is one greater than the level of the current status, within the same workflow, line, and effective date range.  
8. If a registration module record exists for `@RegModID`:  
   a. Insert a new record into `TAMS_Reg_Module` with the same registration, line, and module, the next stage ID, workflow ID, endorser ID, status `Approved`, the status text, current timestamps, and the updater.  
   b. Update the existing module record to set its status to `Approved` and refresh its update timestamps.  
   c. Check whether a user with the registration’s login ID already exists.  
      * If not and the registration is internal, insert a new user record copying fields from the registration, marking it as non‑external, active, and setting timestamps.  
      * If not and the registration is external, insert a new user record copying all registration fields, preserving the external flag, password, company ID, contact person details, marking it active, and setting timestamps.  
   d. Insert an audit entry into `TAMS_Action_Log` recording the line, module, action type, registration ID, description, current time, and updater.  
   e. Prepare an email: set sender, system ID, subject, system name, greeting, recipient list from the registration email, and construct the body with a link to the appropriate login page (internal or external).  
   f. Enqueue the email via `EAlertQ_EnQueue`.  
9. Commit the transaction.  
10. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_User  
* **Writes:** TAMS_Reg_Module, TAMS_User, TAMS_Action_Log, EAlertQ_EnQueue (email queue)