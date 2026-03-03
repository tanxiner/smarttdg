# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval

### Purpose
Updates a user registration module to the approved state, creates a user record if necessary, logs the action, and sends an approval notification email.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module to approve |
| @UpdatedBy | INT | User ID performing the approval |

### Logic Flow
1. Begin a transaction and declare local variables for workflow and user data.  
2. Retrieve the `IsExternal` flag for the registration associated with the supplied module ID.  
3. Load the module’s registration ID, line, track type, module code, and current status into variables.  
4. Determine the workflow type:  
   * If external, set to `ExtUser`.  
   * If internal, set based on module code (`TARIntUser`, `DCCIntUser`, or `OCCIntUser`).  
5. Identify the final approval status: query `TAMS_WFStatus` for the status named `Approved` on the module’s line.  
6. Find the active workflow definition matching the line and workflow type.  
7. Locate the next endorser record whose level is one greater than the current status level, ensuring it is active and within its effective date range.  
8. If the module exists:  
   * Insert a new record into `TAMS_Reg_Module` with the approved status and related workflow data.  
   * Update the existing module record’s status, updated timestamp, and updater.  
   * If no user exists for the registration’s login ID, insert a new user record:  
     * For internal users, populate standard fields and set `IsExternal` to 0.  
     * For external users, include external‑specific fields such as password and company ID.  
   * Insert an audit entry into `TAMS_Action_Log` describing the approval.  
   * Compose an email notification: set sender, subject, body, and recipient based on the registration’s email, adjusting the login link for external users.  
   * Queue the email via `EAlertQ_EnQueue`.  
9. Commit the transaction.  
10. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_Registration`, `TAMS_Reg_Module`, `TAMS_WFStatus`, `TAMS_Workflow`, `TAMS_Endorser`, `TAMS_User`  
* **Writes:** `TAMS_Reg_Module` (insert & update), `TAMS_User` (insert), `TAMS_Action_Log` (insert)