# Procedure: sp_TAMS_RGS_AckSMS

### Purpose
Send an acknowledgement SMS for a TAMS request and update the corresponding timestamps in the TAMS_TOA table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process. |
| @EncTARID | NVARCHAR(250) | Encrypted TAR identifier used in the SMS link. |
| @SMSType | NVARCHAR(5) | Type of SMS to send (e.g., '2' for protection limit acknowledgement). |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Variable Initialization** – Clear all local variables and set `@Message` to an empty string.  
3. **Retrieve TAR Details** – Select `TARNo`, `Line`, `AccessType` from `TAMS_TAR` and `TOANo`, `MobileNo` from `TAMS_TOA` where `TAMS_TAR.Id = @TARID`.  
4. **Current Date** – Store the current date in `@CurrDate` (unused in subsequent logic).  
5. **Update TAMS_TOA Based on AccessType**  
   * If `AccessType` is `'Possession'`:  
     * If `@SMSType` equals `'2'`: update `AckGrantTOATime` and `ReqProtectionLimitTime` to now, and build an SMS message that includes a link containing `@EncTARID` and `SMSType=3`.  
     * Otherwise, update only `AckProtectionLimitTime` to now.  
   * If `AccessType` is not `'Possession'`: update `AckGrantTOATime` to now.  
6. **Send SMS** – If a mobile number and a message exist, call `sp_api_send_sms` with the number, a fixed sender name, and the message. Capture the return value in `@RetVal`.  
7. **Error Check** – If any error occurred during the procedure, set `@Message` to `'Error RGS Ack SMS'` and jump to the error handling section.  
8. **Commit or Rollback** – If the procedure started its own transaction, commit it on success; otherwise leave it untouched. On error, rollback the transaction if it was started by the procedure.  
9. **Return** – Return the value of `@Message` (empty on success, error text on failure).

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA` (updates to `AckGrantTOATime`, `AckProtectionLimitTime`, `ReqProtectionLimitTime`)  

---