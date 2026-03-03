# Procedure: sp_TAMS_Approval_Endorse20250120

### Purpose
Approve a TAR at the current workflow level, update status, propagate to the next level if applicable, send relevant email notifications, and log the action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR being processed |
| @TARWFID | INTEGER | Identifier of the current workflow record |
| @EID | INTEGER | Identifier of the current endorser (unused in logic) |
| @ELevel | INTEGER | Current endorser level in the workflow |
| @Remarks | NVARCHAR(1000) | Comment supplied by the endorser (mandatory for reject, optional otherwise) |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag indicating whether to update TVF run mode (1 = update) |
| @UserLI | NVARCHAR(100) | Login ID of the user executing the procedure |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message returned to caller |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction, start a new one and mark that the procedure owns the transaction.

2. **User Identification**  
   - Retrieve the internal user ID and name from `TAMS_User` using the supplied login ID.

3. **Duplicate Approval Check**  
   - Count how many times the current user has already approved this TAR in the current workflow.  
   - If the count is greater than zero, set `@Message` to `1001` and exit.

4. **Approve Current Workflow Record**  
   - Update the `TAMS_TAR_Workflow` record identified by `@TARWFID` to status `Approved`, record the acting user, timestamp, and remarks.

5. **Optional TVF Mode Update**  
   - If `@TVFRunModeUpdInd` equals 1, update the `TVFMode` column of the TAR record with `@TVFRunMode`.

6. **Load TAR Context**  
   - Pull TAR type, line, email addresses, TAR number, remarks, company, access date, and track type into local variables.

7. **Determine Current and Next Endorsers**  
   - Identify the current workflow ID from the approved workflow record.  
   - Retrieve the title of the current endorser based on the workflow ID and level.  
   - Retrieve the next level endorser’s ID, title, workflow ID, status ID, and role ID.  

8. **Last Level Handling**  
   - If no next endorser exists (i.e., the current level is the final one):  
     - Update the TAR status to `9` if the line is `NEL`, otherwise to `8`.  
     - If the TAR type is `Urgent`, invoke `sp_TAMS_Email_Urgent_TAR` to send an approval email.

9. **Intermediate Level Handling**  
   - If a next endorser exists:  
     - Insert a new `TAMS_TAR_Workflow` record for the next level with status `Pending` if one does not already exist.  
     - Update the TAR status to the next workflow’s status ID.  
     - If the TAR type is `Urgent`, prepare an email list for the next role:  
       - Concatenate emails of all active users whose role matches the next role ID.  
       - If the workflow type is `UrgentAfter` and the next title is `OCC Approval` or `SDS Approval`, append the corresponding contact email from `TAMS_Parameters`.  
       - Call `sp_TAMS_Email_Apply_Urgent_TAR` to notify the next level.

10. **Action Logging**  
    - Insert a record into `TAMS_Action_Log` noting the line, module, function, transaction ID, message, creation timestamp, and user ID.

11. **Urgent After Special Handling**  
    - If the workflow type is `UrgentAfter`, involves power is enabled, and the current level is 2:  
      - Build an email list for the role `<Line>_PFR` (e.g., `NEL_PFR`).  
      - Append the appropriate contact email from `TAMS_Parameters` based on the track type (`Mainline` or `Depot`).  
      - Call `sp_TAMS_Email_Urgent_TAR_OCC` to send an OCC‑specific notification.

12. **Error Handling**  
    - If any error occurs during the process, set `@Message` to an error string and roll back the transaction if it was started by the procedure.

13. **Commit or Rollback**  
    - Commit the transaction if it was started internally; otherwise leave it open.  
    - Return the `@Message` value to the caller.

### Data Interactions
* **Reads**  
  - `TAMS_User`  
  - `TAMS_TAR_Workflow`  
  - `TAMS_TAR`  
  - `TAMS_Endorser`  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_Parameters`  
  - `TAMS_Workflow`

* **Writes**  
  - `TAMS_TAR_Workflow` (UPDATE, INSERT)  
  - `TAMS_TAR` (UPDATE)  
  - `TAMS_Action_Log` (INSERT)

---