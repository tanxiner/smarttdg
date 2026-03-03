# Procedure: EAlertQ_EnQueue
**Type:** Stored Procedure

Purpose: This stored procedure enqueues an email alert by inserting it into the EAlertQ table and its corresponding recipients into the EAlertQTo, EAlertQCC, and EAlertQBCC tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | The sender's email address. |
| @Subject | nvarchar(500) | The subject of the email alert. |
| @Sys | nvarchar(100) | The system information for the email alert. |
| @Greetings | ntext | The greeting message for the email alert. |
| @AlertMsg | nvarchar(max) | The main body of the email alert. |
| @UserId | nvarchar(50) | The ID of the user who created the email alert. |
| @SendTo | ntext | The recipient's email address separated by a separator. |
| @CC | ntext | The CC recipient's email address separated by a separator. |
| @BCC | ntext | The BCC recipient's email address separated by a separator. |
| @Separator | nvarchar(1) | The separator used to separate the recipients' email addresses. |
| @AlertID | decimal(18, 0) output | The ID of the newly created email alert. |
| @From | nvarchar(250) = null | The sender's name (optional). |

### Logic Flow
1. Checks if the send-to recipient is null.
2. Inserts a new record into the EAlertQ table with the provided information.
3. Retrieves the ID of the newly created email alert.
4. Loops through each recipient in the send-to list:
   1. Extracts the recipient's email address from the ntext pointer.
   2. Inserts a new record into the EAlertQTo table for the recipient.
5. Loops through each CC recipient:
   1. Extracts the CC recipient's email address from the ntext pointer.
   2. Inserts a new record into the EAlertQCC table for the recipient.
6. Loops through each BCC recipient:
   1. Extracts the BCC recipient's email address from the ntext pointer.
   2. Inserts a new record into the EAlertQBCC table for the recipient.

### Data Interactions
* Reads: EAlertQ, EAlertQTo, EAlertQCC, EAlertQBCC
* Writes: EAlertQ