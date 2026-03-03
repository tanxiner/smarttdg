# Procedure: sp_TAMS_RGS_AckReg_20230807_M

### Purpose
Acknowledges a TAR registration, updates its status, and sends an SMS notification to the associated mobile number.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the TAR record to acknowledge. |
| @UserID   | NVARCHAR(500) | User performing the acknowledgment. |
| @Message  | NVARCHAR(500) OUTPUT | Returns status or error message after execution. |

### Logic Flow
1. **Transaction Setup**  
   - If no active transaction, start a new one and flag that the procedure owns the transaction.

2. **Initialize Variables**  
   - Clear the output message and set a newline character for later use.

3. **Retrieve Current Status**  
   - Query `TAMS_TAR` and `TAMS_TOA` to obtain the current `TOAStatus` for the specified `@TARID`.

4. **Process Based on Status**  
   - **If `TOAStatus` = 1 (pending acknowledgment)**  
     a. Update `TAMS_TOA` to set `TOAStatus` to 2, record the acknowledgment time, and update audit fields (`UpdatedOn`, `UpdatedBy`).  
     b. Gather TAR details (`TARNo`, `Line`, `AckRegisterTime`, `MobileNo`) from the joined tables.  
     c. Build an SMS message that includes the TAR number, acknowledgment time, current date, and a note that the user should not go down to track yet. The message wording differs if the line is `DTL` versus other lines.  
     d. If a mobile number and message are present, call `sp_api_send_sms` to queue the SMS.  
     e. Immediately trigger SMS delivery by calling `SP_Call_SMTP_Send_SMSAlert`.  
     f. If the alert call returns a non‑empty output, set the message to “Error SMS Sending” and jump to error handling.  
   - **If `TOAStatus` = 2 (already acknowledged)**  
     - Set the message to “1” (indicating already granted) and jump to error handling.  
   - **Any other status**  
     - Set the message to “Invalid TAR status. Please refresh RGS.” and jump to error handling.

5. **Error Check**  
   - If any SQL error occurred (`@@ERROR` ≠ 0), set the message to “Error RGS Ack Reg” and jump to error handling.

6. **Commit or Rollback**  
   - On normal exit, commit the transaction if it was started by the procedure and return the message.  
   - On error, rollback the transaction if it was started by the procedure and return the message.

### Data Interactions
* **Reads:**  
  - `TAMS_TAR`  
  - `TAMS_TOA`

* **Writes:**  
  - `TAMS_TOA` (status update, timestamps, audit fields)