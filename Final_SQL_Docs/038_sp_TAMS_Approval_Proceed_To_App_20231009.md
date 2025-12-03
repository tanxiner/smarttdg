# Procedure: sp_TAMS_Approval_Proceed_To_App_20231009

### Purpose
Advances a TAR through the approval workflow, handling validation, exception handling, status updates, and email notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR to process |
| @TARWFID | INTEGER | Current workflow record ID |
| @EID | INTEGER | Current endorser ID |
| @ELevel | INTEGER | Current endorser level |
| @Remarks | NVARCHAR(1000) | Comment for reject or approval actions |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag to update TVF run mode |
| @UserLI | NVARCHAR(100) | Login ID of the user executing the procedure |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message |

### Logic Flow
1. **Transaction Setup** – Starts a transaction if none exists and initializes a message variable.  
2. **User Context** – Retrieves the internal user ID and name from the login ID.  
3. **Duplicate Approval Check** – Counts existing approved actions by the same user on the TAR; if found, returns error code `1001`.  
4. **TVF Mode Update** – If the update flag is set, writes the new TVF mode to the TAR record.  
5. **TAR Metadata Load** – Pulls line, access date, type, exclusivity, and email details into local variables.  
6. **Current Workflow Load** – Retrieves the workflow ID associated with the current workflow record.  
7. **Current Endorser Load** – Loads details of the endorser at the current level (role, validation requirement, etc.).  
8. **Exception TAR Collection** –  
   - Creates temporary tables for sector‑conflict exceptions.  
   - Iterates over each sector of the current TAR.  
   - For buffer sectors, selects non‑buffer TARs with matching access date and active sector; for non‑buffer sectors, selects all matching TARs.  
   - For each selected TAR, applies rules based on access type and exclusivity to decide whether to add it to the exception list.  
9. **Exception Handling** – For each TAR in the exception list:  
   - Sets its status to `Cancelled` (10) if the line is `NEL`, otherwise to `Rejected` (9).  
   - Logs the cancellation.  
   - If the TAR is urgent, triggers a cancellation email.  
10. **Workflow Status Update** – Marks the current workflow record as `Approved` and records the action timestamp and user.  
11. **Next Endorser Determination** – Loads the next level endorser.  
12. **Final Status Decision** –  
    - If no next endorser exists, updates the TAR status to `Approved` (9) for `NEL` or `Completed` (8) otherwise, logs the approval, and sends urgent TAR email if applicable.  
    - If a next endorser exists, inserts a pending workflow record for that endorser if not already present, updates the TAR status to the next workflow status, logs the approval, and sends urgent TAR email to the next role if the TAR is urgent.  
13. **Urgent After Workflow Special Case** – If the workflow type is `UrgentAfter`, involves power is enabled, and the current level is 2, sends an urgent TAR OCC email to the role matching the line plus `_PFR`.  
14. **Error Handling** – If any error occurs, rolls back the transaction and returns an error message; otherwise commits and returns the message code.

### Data Interactions
* **Reads:**  
  - TAMS_User  
  - TAMS_TAR  
  - TAMS_TAR_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR_Sector  
  - TAMS_Sector  
  - TAMS_Workflow  
  - TAMS_User_Role  
  - TAMS_Role  

* **Writes:**  
  - TAMS_TAR (status, TVFMode, UpdatedOn, UpdatedBy)  
  - TAMS_TAR_Workflow (WFStatus, ActionBy, ActionOn, new pending records)  
  - TAMS_Action_Log (log entries for approval, cancellation, and status changes)  
  - Temporary tables #TmpExc and #TmpExcSector (in‑memory only)  

---