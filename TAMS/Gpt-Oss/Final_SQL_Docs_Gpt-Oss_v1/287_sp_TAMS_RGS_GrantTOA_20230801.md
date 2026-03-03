# Procedure: sp_TAMS_RGS_GrantTOA_20230801

### Purpose
Grants a TOA for a specified TAR, updates its status, records an audit entry, and sends an acknowledgement SMS.

### Parameters
| Name      | Type            | Purpose |
| :-------- | :-------------- | :------ |
| @TARID    | BIGINT          | Identifier of the TAR to grant TOA for. |
| @EncTARID | NVARCHAR(250)   | Encrypted TAR identifier used in the SMS link. |
| @UserID   | NVARCHAR(500)   | User performing the grant. |
| @Message  | NVARCHAR(500)   | Output message indicating success or error. |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark it as internal.  
2. **Initialisation** – Clear the output message and declare variables for dates, numbers, and SMS content.  
3. **Retrieve TAR Details** – Select TARNo, Line, OperationDate, AccessType, and MobileNo from `TAMS_TAR` joined with `TAMS_TOA` where `TARId` matches `@TARID`.  
4. **Generate Reference Number** – Call `sp_Generate_Ref_Num_TOA` to obtain a new TOA reference number (`@RefNum`).  
5. **Update TOA Record** – Set `TOAStatus` to 3, store the new reference number, record grant time, and update audit fields in `TAMS_TOA`.  
6. **Audit Logging** – Insert a row into `TAMS_TOA_Audit` capturing the user, timestamp, operation type ('U'), and all columns from the updated `TAMS_TOA` row.  
7. **Build SMS Message** – Depending on `@AccessType` (Possession or other), compose a message that includes the reference number, TAR ID, and a link containing `@EncTARID` and a SMSType flag.  
8. **Send SMS** – If a mobile number exists, invoke `sp_api_send_sms` with the number, sender name, and message.  
9. **Trigger SMTP Alert** – Call `SP_Call_SMTP_Send_SMSAlert`; if it returns a non‑empty output, set the error message and jump to error handling.  
10. **Error Check** – If any error flag is set, set the error message and jump to error handling.  
11. **Commit or Rollback** – On normal exit, commit the internal transaction if it was started; on error, rollback.  
12. **Return** – Return the message string.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA`, `TAMS_TOA_Audit`