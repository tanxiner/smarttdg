# Procedure: sp_TAMS_RGS_GrantTOA_001

### Purpose
Grant a TOA for a specified TAR, update status, generate a reference number, log the change, and send an acknowledgement SMS.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to grant TOA for |
| @EncTARID | NVARCHAR(250) | Encrypted TAR identifier used in the acknowledgement link |
| @UserID | NVARCHAR(500) | User performing the grant operation |
| @Message | NVARCHAR(500) OUTPUT | Result message indicating success or error |

### Logic Flow
1. Initialise an internal transaction flag and begin a transaction if none is active.  
2. Reset the output message to an empty string.  
3. Declare and initialise variables for SMS content, dates, TAR details, and reference numbers.  
4. Retrieve TAR details (TARNo, Line, OperationDate, AccessType, MobileNo) by joining TAMS_TAR and TAMS_TOA on the TAR ID.  
5. Generate a TOA reference number by calling sp_Generate_Ref_Num_TOA with the line and operation date.  
6. Update the TAMS_TOA record for the TAR: set status to 3, store the generated reference number, record grant time, update timestamps, and the user who performed the update.  
7. Insert a snapshot of the updated TAMS_TOA row into TAMS_TOA_Audit, marking the operation as an update ('U').  
8. Build an SMS message:  
   - If AccessType is 'Possession', use SMSType=2 in the acknowledgement link.  
   - Otherwise, use SMSType=1.  
   The message includes the reference number, TAR number, and a link containing the encrypted TAR ID.  
9. If a mobile number exists, send the SMS via sp_api_send_sms.  
10. Trigger a quick SMS send routine by calling SP_Call_SMTP_Send_SMSAlert; if it returns an error message, set the output message to “Error SMS Sending” and jump to error handling.  
11. If any error occurred during the process, set the output message to “Error RGS Grant TOA” and jump to error handling.  
12. On successful completion, commit the transaction if it was started internally and return the (empty) output message.  
13. In the error handling block, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA  
* **Writes:** TAMS_TOA (UPDATE), TAMS_TOA_Audit (INSERT)