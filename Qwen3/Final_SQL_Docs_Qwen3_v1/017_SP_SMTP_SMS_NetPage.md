# Procedure: SP_SMTP_SMS_NetPage

### Purpose
This stored procedure sends an SMS alert using NetPage, a third-party service that allows for sending SMS messages programmatically.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From | varchar(100) | The sender's email address. |
| @To | varchar(max) | The recipient's mobile number. |
| @ActualMsg | varchar(max) | The actual message to be sent in the SMS. |
| @AlertiD | int | A unique identifier for the alert. |
| @SysName | varchar(100) | The system name (e.g., SMTP). |

### Logic Flow
1. The procedure starts by declaring variables for the state ID, PC number, and SQL command.
2. It sets the state ID to the recipient's mobile number and concatenates the actual message with a prefix to create the PC number.
3. It deletes any SMS alerts from the database that are older than 60 days.
4. It inserts a new record into the SMTP_SMSAlertQ table, which logs the sent SMS alert, including the sender's email address, recipient's mobile number, alert ID, message, system name, and timestamp.
5. If an error occurs during this process, it raises an error with a specific message.
6. Finally, it executes a command to send the SMS using the NetPage service, which involves executing a batch file that takes the state ID and PC number as arguments.

### Data Interactions
* Reads: None explicitly stated; however, it is assumed that the procedure interacts with the database tables SMTP_SMSAlertQ.
* Writes: 
  * SMTP_SMSAlertQ table (inserting new records)