# Procedure: SP_SMTP_Send_SMSAlert

### Purpose
This stored procedure sends SMS alerts using SMTP for all pending alerts in the SMSEAlertQ table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_Alertid | int | Alert ID of the alert to be sent |
| @p_from | varchar(100) | Sender's email address |
| @p_To | varchar(100) | Recipient's email address |
| @p_Alertmsg | varchar(max) | SMS message content |
| @p_sysname | varchar(50) | System name |

### Logic Flow
1. The procedure starts by declaring variables for the alert ID, sender's email, recipient's email, SMS message, and system name.
2. It then opens a cursor to iterate over all pending alerts in the SMSEAlertQ table where the status is 'Q'.
3. For each alert, it opens another cursor to retrieve the recipient's email address from the SMSEAlertTo table matching the current alert ID.
4. The procedure then executes the SP_SMTP_SMS_NetPage stored procedure for each recipient, passing in the sender's email, recipient's email, SMS message, alert ID, and system name as parameters.
5. After sending the SMS alert, the procedure updates the status of the alert in the SMSEAlertQ table to 'S' and sets the LastUpdatedOn and LastUpdatedBy fields accordingly.
6. The process repeats for all pending alerts until there are no more records to fetch.

### Data Interactions
* **Reads:** SMSEAlertQ, SMSEAlertTo
* **Writes:** SMSEAlertQ