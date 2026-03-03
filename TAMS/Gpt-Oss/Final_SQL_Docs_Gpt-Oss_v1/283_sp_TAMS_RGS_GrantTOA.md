# Procedure: sp_TAMS_RGS_GrantTOA

### Purpose
Grants a TOA for a specified TAR when its current status is 2, updates the record, logs the change, and notifies the user via SMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to process |
| @EncTARID | NVARCHAR(250) | Encrypted TAR identifier used in the acknowledgement link |
| @UserID | NVARCHAR(500) | User performing the grant |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction, start a new one and flag that the procedure owns it.  
2. **Variable Initialization** – Clear all working variables, including the output message.  
3. **Retrieve TAR Details** – Join `TAMS_TAR` and `TAMS_TOA` on the TAR ID to fetch the TAR number, line, operation date, access type, mobile number, and current TOA status.  
4. **Check TOA Status**  
   - **Status = 2 (Pending Grant)**  
     a. Generate a reference number for the TOA via `sp_Generate_Ref_Num_TOA`.  
     b. Update `TAMS_TOA` setting status to 3, storing the reference number, grant time, and audit fields.  
     c. Insert the updated row into `TAMS_TOA_Audit` for audit trail.  
     d. Build an SMS message that includes the reference number, TAR number, and a link to acknowledge the TOA; the link type (SMSType) depends on whether the access type is “Possession”.  
     e. If a mobile number exists, call `sp_api_send_sms` to send the message.  
   - **Status = 3 (Already Granted)** – Set message to “1” and jump to error handling.  
   - **Any Other Status** – Set message to “Invalid TAR status. Please refresh RGS.” and jump to error handling.  
5. **Error Check** – If any error flag is set, set message to “Error RGS Grant TOA” and jump to error handling.  
6. **Commit or Rollback** – If the procedure started the transaction, commit on success or rollback on error.  
7. **Return** – Return the message string to the caller.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA`, `TAMS_TOA_Audit`  

---