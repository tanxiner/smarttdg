# Procedure: sp_TAMS_RGS_AckSMS_20221214_M

### Purpose
Send an acknowledgement SMS for a TAMS request and log the acknowledgement status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process |
| @EncTARID | NVARCHAR(250) | Encoded TAR ID used in the acknowledgement URL |
| @SMSType | NVARCHAR(5) | Type of SMS to send (e.g., '2' for possession acknowledgement) |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and mark it as internal.  
2. **Initialize Variables** – Clear all string variables and set the current date string.  
3. **Retrieve TAR Details** – Join `TAMS_TAR` and `TAMS_TOA` on `TARId` to fetch `TARNo`, `Line`, `AccessType`, `TOANo`, and set a hard‑coded mobile number `HPNo`.  
4. **Determine Access Type** –  
   * If `AccessType` is `'Possession'`:  
     * If `SMSType` equals `'2'`:  
       * Update `TAMS_TOA` to set `AckGrantTOATime` and `ReqProtectionLimitTime` to now.  
       * Build an SMS message that includes the TOA number, a link containing `@EncTARID` and `SMSType=3`, and the site URL.  
     * Else: update `TAMS_TOA` to set `AckProtectionLimitTime` to now.  
   * Else (non‑Possession): update `TAMS_TOA` to set `AckGrantTOATime` to now.  
5. **Audit Logging** – Insert a copy of the updated `TAMS_TOA` row into `TAMS_TOA_Audit` with a new audit ID, timestamp, and operation type `'U'`.  
6. **Send SMS** – If an SMS message was constructed:  
   * Call `sp_api_send_sms` with the mobile number, sender name `'TAMS RGS'`, and the message.  
   * Trigger a quick SMTP send via `SP_Call_SMTP_Send_SMSAlert`.  
   * If the SMTP call returns a non‑empty output, set `@Message` to `'Error SMS Sending'`.  
7. **Error Check** – If any error flag is set, set `@Message` to `'Error RGS Ack SMS'` and jump to error handling.  
8. **Commit or Rollback** – Commit the internal transaction if it was started; otherwise rollback on error.  
9. **Return** – Return the status message in `@Message`.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA` (updates), `TAMS_TOA_Audit` (insert)