# Procedure: SP_SMTP_SMS_NetPage

### Purpose
Sends an SMS alert via NetPage, logs the request, and cleans up old log entries.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @From     | varchar(100)  | Sender identifier used in the log. |
| @To       | varchar(max)  | Recipient mobile number. |
| @ActualMsg| varchar(max)  | Text of the SMS to send. |
| @AlertiD  | int           | Identifier for the alert message. |
| @SysName  | varchar(100)  | Name of the system initiating the send. |

### Logic Flow
1. Assign the recipient number to a local variable `@stateid`.  
2. Ensure `@ActualMsg` is a string and wrap it in double quotes, storing the result in `@pcno`.  
3. Delete any rows from `SMTP_SMSAlertQ` whose `Createdon` date is older than 60 days.  
4. Insert a new row into `SMTP_SMSAlertQ` with the supplied parameters and the current timestamp.  
5. If the insert fails, raise an error and exit.  
6. Execute the external batch file `SMS_NetPage.bat` via `xp_cmdshell`, passing the mobile number and quoted message as arguments.  

### Data Interactions
* **Reads:** None.  
* **Writes:** `SMTP_SMSAlertQ` (insert and delete operations).  

---