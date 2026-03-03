# Procedure: sp_TAMS_RGS_AckSMS_20221107

### Purpose
Acknowledges a TAMS request, updates the corresponding TOA record, and sends an SMS notification to the associated mobile number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process |
| @EncTARID | NVARCHAR(250) | Encoded TAR identifier used in the SMS link |
| @SMSType | NVARCHAR(5) | Type of SMS to send (e.g., '2' triggers a specific message) |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Variable Initialization** – Clear all local variables, set `@Message` to an empty string, and prepare a newline character.  
3. **Data Retrieval** – Select `TARNo`, `Line`, `AccessType` from `TAMS_TAR` and `TOANo`, `MobileNo` from `TAMS_TOA` where `TAMS_TAR.Id = @TARID`.  
4. **Current Date** – Store the current date in `@CurrDate` (unused in subsequent logic).  
5. **Conditional Updates** –  
   - If `AccessType` is `'Possession'`:  
     - If `@SMSType` equals `'2'`: update `AckGrantTOATime` and `ReqProtectionLimitTime` to the current time, then build an SMS message that includes a link with `@EncTARID` and `SMSType=3`.  
     - Otherwise, update only `AckProtectionLimitTime`.  
   - If `AccessType` is not `'Possession'`: update `AckGrantTOATime` only.  
6. **SMS Sending** – If a mobile number (`@HPNo`) and a message (`@SMSMsg`) are present, call `sp_api_send_sms` with the number, a fixed sender name, the message, and capture the return value in `@RetVal`.  
7. **Error Check** – If an error occurred during the SMS call, set `@Message` to `'ERROR INSERTING TAMS_TOA_Parties'` and jump to the error handling section.  
8. **Commit or Rollback** – If the procedure started its own transaction, commit it; otherwise leave it untouched.  
9. **Return** – Return the value of `@Message` to the caller.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA` (updates to `AckGrantTOATime`, `ReqProtectionLimitTime`, `AckProtectionLimitTime`)  

---