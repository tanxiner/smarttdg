# Procedure: sp_TAMS_RGS_AckReg_20221107

### Purpose
Acknowledges a TAR registration, updates its status, and sends an SMS notification to the associated mobile number.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the TAR record to acknowledge. |
| @UserID   | NVARCHAR(500) | User performing the acknowledgment, used for audit fields. |
| @Message  | NVARCHAR(500) OUTPUT | Returns a status message indicating success or the type of error encountered. |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction exists, start a new one and flag that the procedure owns the transaction.

2. **Reset Output**  
   - Initialise `@Message` to an empty string.

3. **Update Registration Status**  
   - Set `TOAStatus` to 2, record the current time in `AckRegisterTime`, and update audit columns (`UpdatedOn`, `UpdatedBy`) for the row in `TAMS_TOA` that matches `@TARID`.

4. **Gather Data for SMS**  
   - Retrieve the TAR number, line identifier, acknowledgment time, and mobile number by joining `TAMS_TAR` and `TAMS_TOA` on the TAR ID.
   - Format the current date and acknowledgment time for inclusion in the message.

5. **Compose SMS Text**  
   - If the line is `DTL`, craft a message indicating acknowledgment by DTL OCC; otherwise, indicate acknowledgment by NEL OCC.
   - The message includes the TAR number, acknowledgment time, current date, and a note not to track yet.

6. **Send SMS via API**  
   - If both the mobile number and message are non‑empty, call `sp_api_send_sms` to transmit the SMS. Capture the return value in `@RetVal`.

7. **Trigger SMTP Alert**  
   - Execute `SP_Call_SMTP_Send_SMSAlert` to send an additional alert.  
   - If this call returns a non‑empty output, set `@Message` to “Error SMS Sending” and jump to error handling.

8. **Error Check**  
   - If the last SQL operation produced an error, set `@Message` to “ERROR INSERTING TAMS_TOA_Parties” (note: no actual insert occurs) and jump to error handling.

9. **Commit or Rollback**  
   - On normal completion, commit the transaction if it was started by the procedure and return the (empty) `@Message`.  
   - On error, rollback the transaction if it was started by the procedure and return the error message.

### Data Interactions
* **Reads:** `TAMS_TOA`, `TAMS_TAR`  
* **Writes:** `TAMS_TOA` (status and audit fields updated)