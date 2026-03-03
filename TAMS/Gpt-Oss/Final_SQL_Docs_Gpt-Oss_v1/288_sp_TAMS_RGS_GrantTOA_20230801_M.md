# Procedure: sp_TAMS_RGS_GrantTOA_20230801_M

### Purpose
Grants a TOA for a specified TAR when its current TOA status is 2, updates the status, logs the change, and notifies the user via SMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to process |
| @EncTARID | NVARCHAR(250) | Encrypted TAR ID used in the acknowledgement link |
| @UserID | NVARCHAR(500) | User performing the grant operation |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and mark that the procedure owns it.  
2. **Variable Initialization** – Clear all working variables, including the SMS message buffer.  
3. **Retrieve TAR Details** – Select TARNo, Line, OperationDate, AccessType, MobileNo, and current TOAStatus from TAMS_TAR and TAMS_TOA where the TARId matches @TARID.  
4. **Check TOA Status**  
   - If TOAStatus equals 2 (pending grant):  
     a. Generate a reference number for the TOA using `sp_Generate_Ref_Num_TOA`.  
     b. Update TAMS_TOA: set TOAStatus to 3, store the reference number, record grant time, and update audit fields.  
     c. Insert a copy of the updated row into TAMS_TOA_Audit for audit trail.  
     d. Build an SMS message that includes the reference number, TAR ID, and a link to acknowledge the TOA. The link’s SMSType parameter is 2 if AccessType is ‘Possession’, otherwise 1.  
     e. If a mobile number exists, call `sp_api_send_sms` to send the SMS.  
     f. Trigger a quick SMTP send via `SP_Call_SMTP_Send_SMSAlert`; if it returns a message, treat it as an error and jump to error handling.  
   - If TOAStatus equals 3 (already granted): set @Message to '1' and jump to error handling.  
   - For any other status: set @Message to 'Invalid TAR status. Please refresg RGS.' and jump to error handling.  
5. **Error Check** – If any SQL error occurred, set @Message to 'Error RGS Grant TOA' and jump to error handling.  
6. **Commit or Rollback** – If the procedure started the transaction, commit on success; otherwise rollback on error.  
7. **Return** – Return the @Message value to the caller.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA  
* **Writes:** TAMS_TOA (UPDATE), TAMS_TOA_Audit (INSERT)  

---