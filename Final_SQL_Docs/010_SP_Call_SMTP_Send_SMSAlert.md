# Procedure: SP_Call_SMTP_Send_SMSAlert

### Purpose
Send queued SMS alerts via SMTP and mark them as sent.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Message | NVARCHAR(500) OUTPUT | Returns a status message; empty on success, “Error Sending SMS” on failure. |

### Logic Flow
1. Initialise an internal transaction flag (`@IntrnlTrans`) to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set the flag to 1 and begin a new transaction.  
3. Clear the output message (`@Message = ''`).  
4. Declare variables for alert details (`@p_Alertid`, `@p_from`, `@p_To`, `@p_Alertmsg`, `@p_sysname`).  
5. Open a cursor (`@CurMain`) that selects all alerts from `SMSEAlertQ` where `status = 'Q'`.  
6. For each alert record:  
   a. Open a nested cursor (`@CurDetl`) that selects all recipients from `SMSEAlertQTo` linked by `AlertID`.  
   b. For each recipient: call `SP_SMTP_SMS_NetPage` with the alert’s sender, recipient, message, alert ID, and system name.  
   c. Close and deallocate the recipient cursor.  
   d. Update the alert record in `SMSEAlertQ` setting `status = 'S'`, updating `LastUpdatedOn` to the current date/time and `LastUpdatedBy` to the system name.  
7. Close and deallocate the main cursor.  
8. If any error occurred (`@@ERROR <> 0`), set `@Message` to “Error Sending SMS” and jump to the error handling section.  
9. On normal completion, commit the transaction if it was started internally and return the (empty) message.  
10. On error, roll back the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** `SMSEAlertQ`, `SMSEAlertQTo`  
* **Writes:** `SMSEAlertQ` (updates `status`, `LastUpdatedOn`, `LastUpdatedBy`)