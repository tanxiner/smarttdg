# Procedure: sp_TAMS_Approval_Proceed_To_App_20220930

### Purpose
Moves a TAR through the approval workflow, handling sector‑conflict exceptions, updating status, and sending notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR being processed |
| @TARWFID | INTEGER | Current workflow instance ID |
| @EID | INTEGER | Current endorser ID |
| @ELevel | INTEGER | Current endorser level |
| @Remarks | NVARCHAR(1000) | Comment supplied for reject or approval actions |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag indicating whether to update TVF run mode |
| @UserLI | NVARCHAR(50) | Login ID of the user executing the procedure |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to caller |

### Logic Flow
1. **Transaction Setup** – Starts a transaction if none exists and clears the output message.  
2. **User Context** – Retrieves the user’s internal ID and name from TAMS_User using the supplied login ID.  
3. **TVF Mode Update** – If the update flag is set, writes the new TVF run mode into TAMS_TAR for the target TAR.  
4. **TAR Snapshot** – Loads key TAR attributes (line, access date, type, exclusivity, email, etc.) into local variables.  
5. **Current Endorser Details** – Pulls the current endorser’s workflow, status, role, and validation requirements from TAMS_Endorser.  
6. **Sector‑Conflict Exception Collection**  
   * Creates temporary tables #TmpExc and #TmpExcSector.  
   * Iterates over each sector linked to the TAR.  
   * For each sector, selects other TARs that share the same access date, sector, and are in a pending state, distinguishing buffer versus non‑buffer sectors.  
   * Populates #TmpExcSector with these candidate TARs.  
   * Processes #TmpExcSector to build a final exception list in #TmpExc, applying rules that skip duplicate entries and respect exclusivity flags.  
7. **Exception Handling** – For every TAR in #TmpExc:  
   * Updates its status to cancelled (NEL → 10, others → 9).  
   * Logs the cancellation in TAMS_Action_Log.  
   * If the TAR is of type Late, triggers an email cancellation routine.  
8. **Workflow Advancement** – Marks the current workflow instance as Approved and records the action.  
9. **Next Endorser Determination** – Looks up the next level endorser.  
   * If none exists, finalises the TAR status (NEL → 9, others → 8) and, for Late TARs, sends an approval email.  
   * If a next endorser exists, inserts a new pending workflow record for that endorser, updates the TAR status to the next workflow status, and, for Late TARs, sends an email to the role’s users.  
10. **Action Log** – Records the approval event in TAMS_Action_Log.  
11. **Late‑After Workflow Special Case** – If the workflow type is LateAfter, involves power is enabled, and the current level is 2, sends a Late TAR OCC email to the appropriate role.  
12. **Error Handling** – On any error, rolls back the transaction and returns an error message; otherwise commits and returns success.

### Data Interactions
* **Reads**  
  * TAMS_User  
  * TAMS_TAR  
  * TAMS_TAR_Workflow  
  * TAMS_Endorser  
  * TAMS_TAR_Sector  
  * TAMS_Sector  
  * TAMS_Workflow  
  * TAMS_User_Role  
  * TAMS_Role  
* **Writes**  
  * TAMS_TAR (TVFMode, status updates)  
  * TAMS_TAR_Workflow (status update, new pending record)  
  * TAMS_Action_Log (approval and cancellation logs)  
  * Temporary tables #TmpExc, #TmpExcSector (in‑memory only)  

---