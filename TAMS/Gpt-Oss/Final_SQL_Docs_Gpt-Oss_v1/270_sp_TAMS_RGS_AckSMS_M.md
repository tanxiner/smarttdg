# Procedure: sp_TAMS_RGS_AckSMS_M

### Purpose
Sends an acknowledgement SMS for a TAMS request and records the action in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process |
| @EncTARID | NVARCHAR(250) | Encrypted TAR identifier used in the SMS link |
| @SMSType | NVARCHAR(5) | Type of SMS to send (e.g., '2' or '3') |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark it as internal.
2. **Variable Initialization** – Clear all local variables and set `@Message` to an empty string.
3. **Data Retrieval** – Select `TARNo`, `Line`, `AccessType` from `TAMS_TAR` and `TOANo` from `TAMS_TOA` where `TAMS_TAR.Id = @TARID`. Store a hard‑coded mobile number in `@HPNo`.
4. **Current Date** – Store the current date in `@CurrDate` (unused thereafter).
5. **SMS Message Construction** –  
   - If `AccessType` is 'Possession':  
     - If `@SMSType` = '2', build a message that includes the TOA number and a link containing `@EncTARID` and `SMSType=3`.  
     - If `@SMSType` ≠ '2', build a different message (currently empty).  
   - If `AccessType` is not 'Possession', build a generic message (currently empty).  
   (Commented‑out code indicates intended updates to `TAMS_TOA` timestamps.)
6. **Audit Logging** – Insert a copy of the current `TAMS_TOA` row into `TAMS_TOA_Audit` with an action code 'U' and the current timestamp.
7. **SMS Sending** – If a message was built:  
   - Call `sp_api_send_sms` with the mobile number, a fixed sender name, and the message.  
   - Capture the return value in `@RetVal`.  
   - Call `SP_Call_SMTP_Send_SMSAlert` to trigger an immediate SMS alert.  
   - If the alert call returns a non‑empty string, set `@Message` to 'Error SMS Sending'.
8. **Error Handling** – If any error occurs, set `@Message` to 'Error RGS Ack SMS' and jump to the error trap.
9. **Commit/Rollback** – Commit the transaction if it was started internally; otherwise leave it unchanged. Return `@Message`.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`
* **Writes:** `TAMS_TOA_Audit` (insert), potential updates to `TAMS_TOA` (commented out)  
* **External Calls:** `sp_api_send_sms`, `SP_Call_SMTP_Send_SMSAlert`