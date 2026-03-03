# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID_20231009

### Purpose
Reject a user registration request identified by a registration module ID, updating the workflow status to rejected, notifying the applicant, and recording the action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module to be rejected. |
| @UpdatedBy | INT | User ID performing the rejection. |

### Logic Flow
1. **Retrieve current registration context**  
   - Load the registration ID, line, module, and current status ID for the supplied module ID.  
   - Determine the textual workflow status (`WFStatus`) associated with that status ID.

2. **Handle company‑level pending statuses**  
   - If the status is *Pending Company Registration* or *Pending Company Approval*:  
     a. Open a cursor over all modules belonging to the same registration.  
     b. For each module:  
        - Find the workflow status ID that represents *Company Rejected*.  
        - Update the module’s `RegStatus` to that ID, set `WFStatus` to *Rejected*, and stamp the update.  
        - Queue an email to the registration’s primary address informing the applicant that the company registration (and thus the user application) has been rejected.  
     c. Close the cursor.  
     d. Insert a single audit log entry indicating that the entire user registration was rejected.

3. **Handle system‑level pending approvals**  
   - If the status is *Pending System Admin Approval* or *Pending System Approver Approval*:  
     a. Find the workflow status ID that represents *Rejected*.  
     b. Update only the specified module’s `RegStatus` and `WFStatus` to *Rejected*, stamping the update.  
     c. Insert an audit log entry noting that the module was rejected.  
     d. Queue an email to the registration’s primary address informing the applicant that the user registration for the specific line/module has been rejected.

4. **No further action** – the procedure ends after the above conditional blocks.

### Data Interactions
* **Reads:**  
  - `TAMS_Reg_Module` (to fetch registration details and iterate modules)  
  - `TAMS_WFStatus` (to translate status IDs to text and to find the “Rejected” status ID)  
  - `TAMS_Registration` (to obtain the applicant’s email address)

* **Writes:**  
  - `TAMS_Reg_Module` (updates to `RegStatus`, `WFStatus`, `UpdatedOn`, `UpdatedBy`)  
  - `TAMS_Action_Log` (audit entries)  
  - `EAlertQ_EnQueue` (procedure call that enqueues the rejection email)