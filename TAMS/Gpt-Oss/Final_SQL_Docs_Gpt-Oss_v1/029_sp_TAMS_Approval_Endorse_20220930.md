# Procedure: sp_TAMS_Approval_Endorse_20220930

### Purpose
Approve a TAR record, advance it through the workflow, send notifications, and log the action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR being processed |
| @TARWFID | INTEGER | Current workflow instance ID |
| @EID | INTEGER | Current endorser’s user ID |
| @ELevel | INTEGER | Current endorser’s level in the workflow |
| @Remarks | NVARCHAR(1000) | Comment supplied by the endorser (required for rejection, optional otherwise) |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag indicating whether to update TVF run mode |
| @UserLI | NVARCHAR(50) | Login ID of the user executing the procedure |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start an internal transaction and mark it for later commit or rollback.  
2. **Initialize Variables** – Clear the output message and declare variables for user, email, TAR details, workflow, and next‑level endorser information.  
3. **User Lookup** – Retrieve the internal user ID and name from `TAMS_User` using the supplied login ID.  
4. **Mark Current Workflow as Approved** – Update the current `TAMS_TAR_Workflow` record to status *Approved*, record the acting user and timestamp, and store the remarks.  
5. **Optional TVF Mode Update** – If the update flag is set, write the new TVF run mode into `TAMS_TAR`.  
6. **Load TAR Metadata** – Pull TAR type, line, email, company, TAR number, remarks, and access date from `TAMS_TAR`.  
7. **Determine Current Workflow ID** – Read the workflow ID from the current workflow record.  
8. **Identify Current Endorser** – Get the title of the endorser at the current level from `TAMS_Endorser`.  
9. **Find Next‑Level Endorser** – Query `TAMS_Endorser` for the record at level + 1, retrieving its ID, title, workflow ID, status ID, and role ID.  
10. **Last‑Level Approval Path** – If no next‑level endorser exists:  
    * Update `TAMS_TAR` status to *9* for NEL lines or *8* for DTL/LRT lines.  
    * If the TAR type is *Late*, trigger the *Late TAR* approval email via `sp_TAMS_Email_Late_TAR`.  
11. **Intermediate‑Level Path** – If a next‑level endorser exists:  
    * Ensure a pending workflow record exists for the next endorser; insert one if missing.  
    * Update `TAMS_TAR` status to the next workflow’s status ID.  
    * If the TAR type is *Late*, gather all active users with the next role, compose a comma‑separated email list, and call `sp_TAMS_Email_Apply_Late_TAR` to notify them.  
12. **Log the Action** – Insert a descriptive entry into `TAMS_Action_Log` indicating the user, line, and timestamp of the approval.  
13. **LateAfter Workflow Special Case** – If the workflow type is *LateAfter*, involves power is enabled, and the current level is 2:  
    * Build an email list of users whose role matches the line plus `_PFR`.  
    * Send a *Late TAR OCC* notification via `sp_TAMS_Email_Late_TAR_OCC`.  
14. **Error Check** – If any error flag is set, set the message to “ERROR INSERTING INTO TAMS_TAR” and jump to the error handler.  
15. **Commit or Rollback** – On normal exit, commit the internal transaction if it was started; on error, rollback.  
16. **Return** – Output the message string.

### Data Interactions
* **Reads:**  
  - TAMS_User  
  - TAMS_TAR_Workflow  
  - TAMS_TAR  
  - TAMS_Endorser  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_Workflow  
  - TAMS_Action_Log  

* **Writes:**  
  - TAMS_TAR_Workflow (update, insert)  
  - TAMS_TAR (update)  
  - TAMS_Action_Log (insert)  

---