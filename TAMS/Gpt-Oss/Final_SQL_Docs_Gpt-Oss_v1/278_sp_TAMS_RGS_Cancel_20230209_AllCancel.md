# Procedure: sp_TAMS_RGS_Cancel_20230209_AllCancel

### Purpose
Cancels a TAMS TOA record, logs the action, updates related OCC authorisations, and sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR whose TOA is being cancelled |
| @CancelRemarks | NVARCHAR(1000) | Text to record why the TOA was cancelled |
| @UserID | NVARCHAR(500) | Login ID of the user performing the cancel |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller |

### Logic Flow
1. **Transaction handling** – If no active transaction, start one and mark that the procedure owns it.  
2. **Initialisation** – Clear the output message and set a newline character for later use.  
3. **Cancel TOA** – Update the TAMS_TOA row for the supplied @TARID: set status to 6 (cancelled), store @CancelRemarks, and record the update timestamp and user.  
4. **Audit** – Insert a copy of the updated TOA row into TAMS_TOA_Audit with the user and timestamp.  
5. **User lookup** – Retrieve the numeric Userid from TAMS_User that matches @UserID.  
6. **Gather context** – From TAMS_TAR and TAMS_TOA obtain TARNo, TOANo, Line, AccessDate, OperationDate, and the mobile number (HPNo).  
7. **Action log** – Insert a record into TAMS_Action_Log noting the cancellation action for the TAR.  
8. **Determine endorser IDs** –  
   * If Line = 'DTL', fetch Endorser1 (Level 10) and Endorser2 (Level 12) for the DTL OCC workflow.  
   * Otherwise (Line = 'NEL'), fetch Endorser1 (Level 7) for the NEL OCC workflow.  
9. **Check TOA status** – Scan all TOA rows for the TAR that share the same AccessDate and Line.  
   * If any row has a status other than 5, set a flag indicating not all TOAs are acknowledged/surrendered.  
10. **If all TOAs are acknowledged/surrendered** –  
    * **DTL line**  
      * Update every OCC_Auth record for the TAR, Line, AccessDate, and OperationDate where PowerOn = 0: set status to 11.  
      * Insert a workflow entry for each updated record with Endorser1, status “Pending”.  
      * Update every OCC_Auth record that is a buffer zone (IsBuffer = 1): set status to 13 and insert a