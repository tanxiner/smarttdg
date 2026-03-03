# Procedure: sp_TAMS_RGS_AckSMS_20221214

### Purpose
Acknowledges a RGS request, updates the corresponding TOA record, logs the change, and optionally sends an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process. |
| @EncTARID | NVARCHAR(250) | Encoded TAR identifier used in the SMS link. |
| @SMSType | NVARCHAR(5) | Type of SMS to send; used to determine message content. |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns the transaction.  
2. **Initialize Variables** – Clear all local variables and set the current date string.  
3. **Retrieve TAR Details** – Select the TAR number, line, access type, TOA number, and mobile number from `TAMS_TAR` and `TAMS_TOA` where the TAR ID matches `@TARID`.  
4. **Conditional Updates**  
   * If the access type is **Possession**:  
     * When `@SMSType` equals **2**: update `AckGrantTOATime` and `ReqProtectionLimitTime` in `TAMS_TOA`; build an SMS message that includes a link containing `@EncTARID` and `SMSType=3`.  
     * Otherwise: update only `AckProtectionLimitTime`.  
   * If the access type is not **Possession**: update `AckGrantTOATime` only.  
5. **Audit Logging** – Insert a new row into `TAMS_TOA_Audit` capturing the current timestamp, the action code **U**, and all columns from the updated `TAMS_TOA` row.  
6. **SMS Sending (if a message was built)**  
   * Call `sp_api_send_sms` with the mobile number, a fixed sender name, and the constructed message.  
   * Immediately trigger the SMTP send routine `SP_Call_SMTP_Send_SMSAlert`.  
   * If the SMTP routine returns a non‑empty output, set `@Message` to **Error SMS Sending**.  
7. **Error Check** – If any error occurred during the procedure, set `@Message` to **Error RGS Ack SMS** and jump to the error handling section.  
8. **Commit or Rollback** – If the procedure started the transaction, commit it on success; otherwise rollback on error.  
9. **Return** – Exit the procedure, returning the status message in `@Message`.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA`, `TAMS_TOA_Audit`  

---