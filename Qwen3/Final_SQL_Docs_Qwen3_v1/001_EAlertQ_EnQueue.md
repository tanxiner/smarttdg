# Procedure: EAlertQ_EnQueue

### Purpose
This stored procedure enqueues an email alert by inserting a new record into the EAlertQ table and creating corresponding records in the EAlertQTo, EAlertQCC, and EAlertQBCC tables for recipients, CC, and BCC respectively.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | The sender's email address. |
| @Subject | nvarchar(500) | The subject of the email alert. |
| @Sys | nvarchar(100) | System information. |
| @Greetings | ntext | Greetings message. |
| @AlertMsg | nvarchar(max) | The main content of the email alert. |
| @UserId | nvarchar(50) | The user ID of the sender. |
| @SendTo | ntext | The recipient's email address separated by a separator. |
| @CC | ntext | The CC recipients' email addresses separated by a separator. |
| @BCC | ntext | The BCC recipients' email addresses separated by a separator. |
| @Separator | nvarchar(1) | The separator used to separate recipient, CC, and BCC email addresses. |
| @AlertID | decimal(18, 0) output | The ID of the newly created alert record. |
| @From | nvarchar(250) = null | The sender's full name (optional). |

### Logic Flow
1. Check if the `@SendTo` parameter is null; if so, exit the procedure.
2. Insert a new record into the EAlertQ table with the provided data.
3. Extract the recipient email addresses from the `@SendTo` parameter using the separator and insert corresponding records into the EAlertQTo table.
4. Repeat step 3 for CC recipients in the `@CC` parameter.
5. Repeat step 3 for BCC recipients in the `@BCC` parameter.
6. Drop temporary tables created during the procedure.

### Data Interactions
* **Reads:** EAlertQ, EAlertQTo, EAlertQCC, EAlertQBCC
* **Writes:** EAlertQ