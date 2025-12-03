# Procedure: sp_TAMS_Approval_Proceed_To_App

### Purpose
Approve a TAR, advance it to the next workflow level, handle sector‑conflict exceptions, update status, log the action, and trigger any required email notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR being processed |
| @TARWFID | INTEGER | Current workflow record ID for the TAR |
| @EID | INTEGER | Current endorser ID (unused in logic) |
| @ELevel | INTEGER | Current endorser level |
| @Remarks | NVARCHAR(1000) | Optional remarks; mandatory for reject, optional for approve/endorse |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag indicating whether to update TVF run mode |
| @UserLI | NVARCHAR(100) | Login ID of the user performing the action |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction, start a new one and flag that the procedure owns the transaction.

2. **Initial Variable Setup**  
   - Clear @Message and declare variables for user, TAR, workflow, endorser, and email data.

3. **User Lookup**  
   - Retrieve @UserID and @UserName from TAMS_User using @UserLI.

4. **Duplicate Approval Check**  
   - Count approved actions by @UserID on the TAR.  
   - If count > 0, set @Message to error code `1001` and exit.

5. **TVF Run Mode Update**  
   - If @TVFRunModeUpdInd = 1, update TAMS_TAR.TVfMode with @TVFRunMode.

6. **TAR Data Retrieval**  
   - Load TAR details (Line, AccessDate, AccessTimeSlot, TARType, AccessType, IsExclusive, Email, etc.) into local variables.

7. **Current Workflow Retrieval**  
   - Get @WFID from TAMS_TAR_Workflow using @TARWFID.

8. **Current Endorser Retrieval**  
   - Load current endorser details (ID, Title, WorkflowId, WFStatusId, RoleId, RequireValidation, RequireTVF) for @ELevel.

9. **Sector‑Conflict Exception Building**  
   - Create temporary tables #TmpExc and #TmpExcSector.  
   - Iterate over each sector of the TAR (cursor @Cur01).  
   - For each sector, insert matching TARs that share the same AccessDate/TimeSlot, are not the current TAR, and satisfy sector activity and date range.  
   - Use a nested cursor @Cur02 to process #TmpExcSector rows, applying rules based on AccessType and IsExclusive to populate #TmpExc with unique exception TARs.

10. **Exception TAR Cancellation**  
    - For each TAR in #TmpExc, update its status to `Cancelled` (NEL → 10, others → 9).  
    - Log the cancellation in TAMS_Action_Log.  
    - If the original TAR is of type `Urgent`, invoke `sp_TAMS_Email_Cancel_TAR` to notify relevant parties.

11. **Mark Current Workflow as Approved**  
    - Update TAMS_TAR_Workflow record @TARWFID to status `Approved`, set ActionBy and ActionOn.

12. **Determine Next Endorser**  
    - Query TAMS_Endorser for the next level (@ELevel + 1).  
    - If no next endorser exists:  
      - Update TAMS_TAR status to `Approved` (NEL → 9, others → 8).  
      - If TAR is `Urgent`, send urgent approval email via `sp_TAMS_Email_Urgent_TAR`.  
    - If a next endorser exists:  
      - Insert a new TAMS_TAR_Workflow record for the next endorser if not already present.  
      - Update TAMS_TAR status to the next workflow’s status ID.  
      - If TAR is `Urgent`, gather email addresses for the next role, add any special SDS contact if applicable, and call `sp_TAMS_Email_Apply_Urgent_TAR`.

13. **Log Approval**  
    - Insert a log entry into TAMS_Action_Log indicating the TAR was approved by the user.

14. **Urgent After Special Handling**  
    - If the workflow type is `UrgentAfter`, involve power is enabled, and current level is 2:  
      - Collect email addresses for the SDS role (Line + `_PFR`).  
      - Append any SDS contact from parameters.  
      - Call `sp_TAMS_Email_Urgent_TAR_OCC` to notify SDS.

15. **Error Handling**  
    - If any error occurs, set @Message to a generic error string and roll back the transaction if owned.

16. **Commit / Return**  
    - Commit the transaction if owned and return @Message.

### Data Interactions
* **Reads**  
  - TAMS_User  
  - TAMS_TAR  
  - TAMS_TAR_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR_Sector  
  - TAMS_Sector  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_Parameters  
  - TAMS_Workflow  

* **Writes**  
  - TAMS_TAR (status, TVFMode, UpdatedOn, UpdatedBy)  
  - TAMS_TAR_Workflow (WFStatus, ActionBy, ActionOn, new inserts)  
  - TAMS_Action_Log (approval and cancellation logs)  
  - Temporary tables #TmpExc, #TmpExcSector (used for exception processing)  

* **External Calls**  
  - sp_TAMS_Email_Cancel_TAR  
  - sp_TAMS_Email_Urgent_TAR  
  - sp_TAMS_Email_Apply_Urgent_TAR  
  - sp_TAMS_Email_Urgent_TAR_OCC  

---