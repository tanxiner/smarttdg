# Procedure: sp_TAMS_RGS_GrantTOA_20221107

### Purpose
Grants a TOA for a specified TAR, updates its status, generates a reference number, and sends an acknowledgement SMS to the associated mobile number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to grant TOA for |
| @EncTARID | NVARCHAR(250) | Encoded TAR identifier used in the acknowledgement link |
| @UserID | NVARCHAR(500) | User performing the grant operation |
| @Message | NVARCHAR(500) OUTPUT | Status or error message returned to the caller |

### Logic Flow
1. **Transaction Setup** – If no active transaction exists, start a new one and flag that the procedure owns the transaction.  
2. **Initialize Variables** – Clear all local variables, set a newline marker, and prepare an empty SMS message.  
3. **Retrieve TAR Details** – Select the TAR number, line, operation date, access type, and mobile number from `TAMS_TAR` joined with `TAMS_TOA` where the TAR ID matches the input.  
4. **Generate Reference Number** – Call `sp_Generate_Ref_Num_TOA` with the line and operation date to obtain a new TOA reference number and a message.  
5. **Update TOA Record** – Set `TOAStatus` to 3, store the generated reference number in `TOANo`, record the grant time, and update audit fields (`UpdatedOn`, `UpdatedBy`) for the matching `TAMS_TOA` row.  
6. **Build SMS Content** – Depending on the `AccessType` value, compose an SMS message that includes the reference number, TAR number, and a link to acknowledge the TOA. The link differs for 'Possession' versus other access types.  
7. **Send SMS** – If a mobile number exists, invoke `sp_api_send_sms` to deliver the message.  
8. **Error Check** – If an error occurred during the SMS send, set an error message and jump to the error handling section.  
9. **Commit or Rollback** – If the procedure started the transaction, commit it on success; otherwise, rollback on error. Return the message (empty on success or containing an error description).

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA` (update of status, reference number, timestamps, and audit fields)  

---