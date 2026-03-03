# Procedure: sp_TAMS_RGS_GrantTOA_20221214

### Purpose
Grants a TOA for a specified TAR, updates status, logs the change, and sends an acknowledgement SMS to the associated mobile number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to grant a TOA. |
| @EncTARID | NVARCHAR(250) | Encrypted TAR ID used in acknowledgement URLs. |
| @UserID | NVARCHAR(500) | User performing the grant operation. |
| @Message | NVARCHAR(500) OUTPUT | Status message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Variable Initialization** – Clear all working variables, including message buffers and date placeholders.  
3. **Retrieve TAR and TOA Data** – Select the TAR number, line, operation date, access type, and mobile number from TAMS_TAR and TAMS_TOA where the TAR ID matches @TARID.  
4. **Generate Reference Number** – Call sp_Generate_Ref_Num_TOA with the line and operation date to obtain a new TOA reference number.  
5. **Update TOA Record** – Set TOAStatus to 3 (granted), store the new reference number, record the grant time, and update audit fields (UpdatedOn, UpdatedBy).  
6. **Audit Logging** – Insert a copy of the updated TOA row into TAMS_TOA_Audit with the user ID, current timestamp, and operation type 'U'.  
7. **Compose SMS Message** – Build a message that includes the reference number and TAR ID, and a link to acknowledge the TOA. The link’s SMSType parameter is 2 if AccessType is 'Possession', otherwise 1.  
8. **Send SMS** – If a mobile number exists, invoke sp_api_send_sms to deliver the message.  
9. **Trigger SMTP Alert** – Call SP_Call_SMTP_Send_SMSAlert to send any queued SMS alerts; if it returns an error message, set @Message to “Error SMS Sending” and jump to error handling.  
10. **Error Check** – If any previous step raised an error, set @Message to “Error RGS Grant TOA” and jump to error handling.  
11. **Commit or Rollback** – If the procedure started its own transaction, commit on success; otherwise leave the transaction state unchanged.  
12. **Return** – Return the @Message value (empty on success).

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA  
* **Writes:** TAMS_TOA, TAMS_TOA_Audit  

---