# Procedure: EAlertQ_EnQueue_External

### Purpose
This stored procedure enqueues an external alert, which includes sending emails to recipients specified in the CC and BCC fields.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From	| nvarchar(250) | The sender's email address. |
| @Sender	| nvarchar(100) | The sender's name. |
| @Subject	nvarchar(500) | The subject of the email. |
| @Sys	| nvarchar(100) | System information. |
| @Greetings	ntext | Greeting message for the email. |
| @AlertMsg	ntext | Alert message for the email. |
| @UserId	| nvarchar(50) | User ID who created the alert. |
| @SendTo	| ntext | Email addresses to send the alert to. |
| @CC		| ntext | Email addresses in the CC field. |
| @BCC		| ntext | Email addresses in the BCC field. |
| @Attachment	nvarchar(500) | Attachment file for the email. |
| @Separator	nvarchar(1) | Separator used to split email addresses. |
| @AlertID	decimal(18, 0)	output | Unique ID of the enqueued alert. |

### Logic Flow
The procedure follows these steps:

1. It inserts a new record into the `EAlertQ` table with the provided sender information.
2. If an Alert ID is generated, it inserts another record into the `EAlertQAtt` table to mark the alert as active.
3. It creates temporary tables for CC and BCC recipients and reads their email addresses from the ntext fields.
4. For each recipient in the CC and BCC lists, it inserts a new record into the `EAlertQTo`, `EAlertQCC`, or `EAlertQBCC` table, depending on whether they are in the CC or BCC field.
5. After processing all recipients, it drops the temporary tables.

### Data Interactions
* **Reads:** EAlertQ, EAlertQAtt, EAlertQTo, EAlertQCC, EAlertQBCC