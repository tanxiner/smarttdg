# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID

### Purpose
Reject a user registration request by module ID, updating status to the final rejection stage and notifying the applicant.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module to process |
| @UpdatedBy | INT | User ID performing the rejection |

### Logic Flow
1. **Retrieve current registration context**  
   - Load the registration ID, line, module, and current status ID for the supplied module ID from `TAMS_Reg_Module`.  
   - Resolve the workflow status text from `TAMS_WFStatus` using the status ID.

2. **Handle company‑level pending states**  
   - If the workflow status is *Pending Company Registration* or *Pending Company Approval*:  
     a. Open a cursor over all modules belonging to the same registration.  
     b. For each module:  
        - Determine the workflow ID that represents *Company Rejected*.  
        - Update the module’s status to that ID, set `WFStatus` to *Rejected*, and stamp `UpdatedOn`/`UpdatedBy`.  
        - Queue an email to the registration’s email address informing the applicant that the company registration (and thus the user application) has been rejected.  
     c. Close the cursor.  
     d. Insert a single audit log entry indicating that the entire user registration was rejected.

3. **Handle system‑level pending states**  
   - If the workflow status is *Pending System Admin Approval* or *Pending System Approver Approval*:  
     a. Find the workflow ID that represents *Rejected* for the module’s line.  
     b. Update the specific module to that status, set `WFStatus` to *Rejected*, and stamp `UpdatedOn`/`UpdatedBy`.  
     c. Insert an audit log entry noting that the module in the registration was rejected.  
     d. Queue an email to the registration’s email address informing the applicant that the user registration request for the specific line/module has been rejected.

4. **No action for other statuses**  
   - If the workflow status does not match any of the above conditions, the procedure completes without modifying data or sending notifications.

### Data Interactions
* **Reads:**  
  - `TAMS_Reg_Module` (to fetch registration details and module list)  
  - `TAMS_WFStatus` (to resolve status text and target rejection status IDs)  
  - `TAMS_Registration` (to obtain the applicant’s email address)

* **Writes:**  
  - `TAMS_Reg_Module` (updates to status, `WFStatus`, `UpdatedOn`, `UpdatedBy`)  
  - `TAMS_Action_Log` (audit entries for rejection events)  
  - `EAlertQ_EnQueue` (enqueues rejection notification emails)