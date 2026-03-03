# Procedure: sp_TAMS_Depot_RGS_GrantTOA

### Purpose
Grants a TOA for a specified TAR when its current TOA status is 2, updates the status, records an audit entry, and sends an SMS notification to the associated mobile number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to process |
| @EncTARID | NVARCHAR(250) | Encrypted TAR identifier used in callback URLs |
| @UserID | NVARCHAR(500) | User performing the operation |
| @toacallbacktiming | datetime | Scheduled callback time for the TOA |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message returned to caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns the transaction.  
2. **Initialize Variables** – Clear message, set defaults for TAR details, and prepare an empty SMS message.  
3. **Retrieve TAR Information** – Select TARNo, Line, OperationDate, AccessType, MobileNo, and current TOAStatus from TAMS_TAR joined with TAMS_TOA where the TAR id matches @TARID.  
4. **Check TOA Status**  
   - If TOAStatus equals 2 (ready to grant):  
     a. Generate a reference number for the TOA via sp_Generate_Ref_Num_TOA.  
     b. Update TAMS_TOA: set status to 3, store the reference number, callback time, grant time, and audit fields.  
     c. Insert the updated row into TAMS_TOA_Audit for audit trail.  
     d. Build an SMS message that includes the reference number, TAR number, callback timing, and a link containing @EncTARID and a SMSType parameter (2 for Possession, 1 otherwise).  
     e. If a mobile number exists, call sp_api_send_sms to deliver the message.  
   - If TOAStatus equals 3: set @Message to '1' (already granted) and jump to error handling.  
   - For any other status: set @Message to 'Invalid TAR status. Please refresh RGS.' and jump to error handling.  
5. **Error Check** – If any error flag is set during processing, set @Message to 'Error RGS Grant TOA' and jump to error handling.  
6. **Commit or Rollback** – If the procedure started the transaction, commit on success; otherwise rollback on error.  
7. **Return** – Return the @Message value to the caller.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA  
* **Writes:** TAMS_TOA, TAMS_TOA_Audit  

---