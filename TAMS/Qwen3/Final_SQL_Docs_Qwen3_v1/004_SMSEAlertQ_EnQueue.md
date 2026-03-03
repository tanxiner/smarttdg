# Procedure: SMSEAlertQ_EnQueue

### Purpose
This stored procedure enqueues a new SMS alert by inserting data into several tables, including SMSEAlertQ, EAletQTo, EAletQCC, and EAletQBCC.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | The sender's name. |
| @Subject | nvarchar(500) | The subject of the SMS alert. |
| @Sys | nvarchar(100) | System information. |
| @Greetings | ntext | Greetings message. |
| @AlertMsg | ntext | Alert message. |
| @UserId | nvarchar(50) | User ID. |
| @SendTo | ntext | Recipient's email address. |
| @CC | ntext | CC recipient's email address. |
| @BCC | ntext | BCC recipient's email address. |
| @Separator | nvarchar(1) | Separator character used in the email addresses. |
| @AlertID | decimal(18, 0) output | The ID of the newly created alert. |
| @From | nvarchar(250) = null | Optional sender's name (default is null). |

### Logic Flow
The procedure follows these steps:

1. It checks if the `@SendTo` parameter is null and returns immediately if it is.
2. It inserts a new record into the `SMSEAlertQ` table with the provided data.
3. It creates temporary tables `#tsendto`, `#tcc`, and `#tbcc` to store the recipient's email addresses, CC recipients' email addresses, and BCC recipients' email addresses, respectively.
4. For each type of recipient (SendTo, CC, and BCC), it reads the email address from the temporary table using a pointer to the ntext data type.
5. It inserts new records into the corresponding tables (`EAletQTo`, `EAletQCC`, and `EAletQBCC`) with the alert ID and recipient's email address.
6. After processing all recipients, it drops the temporary tables.
7. Finally, it commits the transaction and returns.

### Data Interactions
* Reads: SMSEAlertQ, EAletQTo, EAletQCC, EAletQBCC
* Writes: SMSEAlertQ, EAletQTo, EAletQCC, EAletQBCC