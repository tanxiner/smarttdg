# Procedure: SP_Call_SMTP_Send_SMSAlert

### Purpose
This stored procedure sends SMS alerts using SMTP for a list of recipients.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Message | NVARCHAR(500) | Output parameter containing the result message |

### Logic Flow
1. The procedure starts by checking if there are any open transactions, and if not, it sets a flag to indicate that an internal transaction has started.
2. It then initializes variables for storing the alert ID, sender, recipient, alert message, and system name.
3. A cursor is opened to iterate over the SMSEAlertQ table where the status is 'Q', which indicates that the alert needs to be sent.
4. For each row in the cursor, another cursor is opened to retrieve the recipients for the current alert ID.
5. The procedure then executes a stored procedure (SP_SMTP_SMS_NetPage) to send SMS alerts to the recipients using SMTP.
6. After sending the SMS alerts, the status of the SMSEAlertQ table is updated to 'S' to indicate that the alert has been sent successfully.
7. If any errors occur during the process, an error message is stored in the @Message variable and the procedure returns it.

### Data Interactions
* **Reads:** dbo.SMSEAlertQ
* **Writes:** dbo.SMSEAlertQ