# Procedure: sp_TAMS_RGS_Cancel_20221107

### Purpose
Cancels a RGS transaction by updating its status, logging the action, adjusting related OCC authorisations, and notifying the customer via SMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to cancel |
| @CancelRemarks | NVARCHAR(1000) | Text explaining why the cancellation is requested |
| @UserID | NVARCHAR(500) | Login ID of the user performing the cancellation |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction exists, start a new one and mark it as internal.
2. **Reset Message** – Initialise the output message to an empty string.
3. **Update TOA Status** – Set the TOA record identified by @TARID to status 6 (cancelled), store the remarks, and record the update timestamp and user.
4. **Resolve User ID** – Look up the numeric Userid for the supplied @UserID from TAMS_User.
5. **Prepare Variables** – Initialise date, time, and other working variables; fetch TARNo, TOANo, Line, AccessDate, OperationDate, and the customer’s mobile number (HPNo) from TAMS_TAR and TAMS_TOA.
6. **Log Action** – Insert a record into TAMS_Action_Log describing the cancellation.
7. **Determine Endorsers** – Depending on the Line value (DTL or NEL), query TAMS_Endorser and TAMS_Workflow to obtain the IDs of the first and second endorsers for OCC authorisation.
8. **Check All Acknowledgements** – Scan all TOA records for the same AccessDate and Line; if any have a status other than 5, flag that not all acknowledgements are present.
9. **If All Acknowledged** –  
   * **DTL Line**  
     - For each OCCAuth record with status 10 and PowerOn = 0, set status to 11, log the change, and insert a workflow entry with Endorser1.  
     - For each OCCAuth record with status 7, set status to 13, log the change, and insert a workflow entry with Endorser2.  
   * **NEL Line**  
     - For each OCCAuth record with status 7 and PowerOn = 0, set status to 8, log the change, and insert a workflow entry with Endorser1.
10. **Compose SMS** – Build a message that includes the TOANo, the line’s OCC acknowledgement time, and the current date.
11. **Send SMS** – If a mobile number exists, call sp_api_send_sms with the composed message.
12. **Error Check** – If an error occurred during the SMS call, set an error message and jump to the error handling section.
13. **Commit or Rollback** – If the procedure started its own transaction, commit it; otherwise leave it to the caller. Return the message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_Workflow, TAMS_OCC_Auth
* **Writes:** TAMS_TOA, TAMS_Action_Log, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow

---