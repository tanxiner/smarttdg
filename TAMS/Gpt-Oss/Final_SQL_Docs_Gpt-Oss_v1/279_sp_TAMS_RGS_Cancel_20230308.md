# Procedure: sp_TAMS_RGS_Cancel_20230308

### Purpose
Cancels a RGS transaction by marking the associated TOA record as cancelled, updating related OCC authorisation states, logging the action, and notifying the customer via SMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to cancel |
| @CancelRemarks | NVARCHAR(1000) | Text explaining why the cancellation is requested |
| @UserID | NVARCHAR(500) | Login ID of the user performing the cancellation |
| @Message | NVARCHAR(500) OUTPUT | Result message returned to the caller (success or error description) |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction exists, start a new one and flag that the procedure owns the transaction.

2. **Initialisation**  
   - Clear the output message and set a newline character for later use.

3. **Cancel TOA Record**  
   - Update the TAMS_TOA row that matches @TARID: set TOAStatus to 6 (cancelled), store @CancelRemarks, and record the update timestamp and user.

4. **Audit the Change**  
   - Insert a copy of the updated TAMS_TOA row into TAMS_TOA_Audit, prefixed with the user ID, current time, and an action code ‘U’.

5. **Resolve User ID**  
   - Look up the numeric Userid from TAMS_User where LoginId equals @UserID.

6. **Gather Contextual Data**  
   - Retrieve TARNo, TOANo, Line, AccessDate, OperationDate, and the customer’s mobile number (HPNo) by joining TAMS_TAR and TAMS_TOA on the TARId.

7. **Log the Action**  
   - Insert a record into TAMS_Action_Log with the line, action type ‘RGS-Cancel’, the TARId, a descriptive message, the current timestamp, and a status code 88.

8. **Determine Endorsers**  
   - Based on the Line value (DTL or NEL), query TAMS_Endorser and TAMS_Workflow to find the IDs of the first and second endorsers required for OCC authorisation.

9. **Check TOA Statuses**  
   - Scan all TOA records for the same AccessDate and Line that are not in status 0 or 6.  
   - If any record has a status other than 5 (acknowledged/surrendered), flag that not all are acknowledged.

10. **If All TOAs Acknowledged**  
    - **For DTL Line**  
      - Find OCC_Auth records with status 10 (pending) and PowerOn = 0; update them to status 11, record the update, and insert a workflow entry with Endorser1.  
      - Find OCC_Auth records with status 7; update them to status 13, record the update, and insert a workflow entry with Endorser2.  
    - **For NEL Line**  
      - Find OCC_Auth records with status 8 and PowerOn = 0; update them to status 9, record the update, and insert a workflow entry with Endorser1.

11. **Compose SMS Message**  
    - If the Line is DTL:  
      - If TOANo is empty, message references the TARNo; otherwise it references the TOANo.  
      - The message instructs the customer to contact OCC 67187110 immediately or if required.  
    - If the Line is NEL:  
      - Similar logic but the contact number is 64132001.

12. **Send SMS**  
    - If a mobile number (HPNo) exists, call sp_api_send_sms with the number, a fixed title ‘TAMS RGS’, and the composed message.

13. **Trigger SMTP Alert**  
    - Call SP_Call_SMTP_Send_SMSAlert to send any queued SMS alerts.  
    - If the alert call returns a non‑empty message, set @Message to ‘Error SMS Sending’ and jump to error handling.

14. **Error Check**  
    - If any SQL error occurred, set @Message to ‘Error RGS Cancel’ and jump to error handling.

15. **Commit or Rollback**  
    - If the procedure started its own transaction, commit it on success; otherwise leave it to the caller.  
    - On error, rollback the transaction if it was started here.

16. **Return**  
    - Return the @Message value to the caller.

### Data Interactions
* **Reads:**  
  - TAMS_TOA  
  - TAMS_TOA_Audit (select for audit copy)  
  - TAMS_User  
  - TAMS_TAR  
  - TAMS_Action_Log (for logging)  
  - TAMS_Endorser  
  - TAMS_Workflow  
  - TAMS_OCC_Auth  

* **Writes:**  
  - TAMS_TOA (status update)  
  - TAMS_TOA_Audit (audit insert)  
  - TAMS_Action_Log (log insert)  
  - TAMS_OCC_Auth (status updates)  
  - TAMS_OCC_Auth_Workflow (workflow inserts)  

---