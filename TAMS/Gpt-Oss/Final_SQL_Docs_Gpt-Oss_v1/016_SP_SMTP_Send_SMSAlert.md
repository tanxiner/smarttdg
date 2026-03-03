# Procedure: SP_SMTP_Send_SMSAlert

### Purpose
Send queued SMS alerts via SMTP and mark them as sent.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | | The procedure has no input parameters; all values are derived from database tables. |

### Logic Flow
1. Declare local variables to hold alert details and system name.  
2. Create a cursor (`@CurMain`) that selects all alerts from `SMSEAlertQ` where `status` equals `'Q'`.  
3. Open `@CurMain` and fetch the first alert into the local variables.  
4. While a row is fetched:  
   a. Create a second cursor (`@CurDetl`) that selects all recipients from `SMSEAlertQTo` for the current `AlertID`.  
   b. Open `@CurDetl` and fetch each recipient into `@p_To`.  
   c. For every recipient, execute the helper procedure `SP_SMTP_SMS_NetPage`, passing the sender, recipient, message, alert ID, and system name.  
   d. Continue fetching recipients until none remain, then close and deallocate `@CurDetl`.  
   e. Update the processed alert in `SMSEAlertQ`: set `status` to `'S'`, update `LastUpdatedOn` to the current date/time, and set `LastUpdatedBy` to the system name.  
   f. Fetch the next alert from `@CurMain`.  
5. After all alerts are processed, close and deallocate `@CurMain`.

### Data Interactions
* **Reads:** `SMSEAlertQ`, `SMSEAlertQTo`  
* **Writes:** `SMSEAlertQ` (status update, timestamps, user)