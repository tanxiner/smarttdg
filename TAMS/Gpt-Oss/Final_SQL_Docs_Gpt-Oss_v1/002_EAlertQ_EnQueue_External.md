# Procedure: EAlertQ_EnQueue_External

### Purpose
Enqueues an email alert into the system, storing its core data, attachment, and recipient lists (To, CC, BCC) for later processing.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From | nvarchar(250) | Sender email address |
| @Sender | nvarchar(100) | Display name of the sender |
| @Subject | nvarchar(500) | Email subject line |
| @Sys | nvarchar(100) | Identifier of the originating system |
| @Greetings | ntext | Greeting text to prepend to the message |
| @AlertMsg | ntext | Main body of the alert message |
| @UserId | nvarchar(50) | User creating the alert |
| @SendTo | ntext | List of primary recipients, separated by @Separator |
| @CC | ntext | List of CC recipients, separated by @Separator |
| @BCC | ntext | List of BCC recipients, separated by @Separator |
| @Attachment | nvarchar(500) | File path of the attachment |
| @Separator | nvarchar(1) | Character used to split recipient lists |
| @AlertID | decimal(18,0) | Output identity of the inserted alert record |

### Logic Flow
1. Begin a transaction and capture the current timestamp.  
2. Insert a new record into **EAlertQ** with the supplied email metadata and the current timestamp for creation and last update.  
3. Retrieve the generated identity value into **@AlertID**.  
4. If an attachment path is supplied, insert a record into **EAlertQAtt** linking the attachment to the alert.  
5. For each recipient list (**SendTo**, **CC**, **BCC**):  
   - Create a temporary table holding the ntext value.  
   - Use a text pointer to locate the separator character.  
   - Loop: extract the substring before the separator, trim spaces, and insert it into the corresponding table (**EAlertQTo**, **EAlertQCC**, or **EAlertQBCC**) with audit fields.  
   - Remove the processed segment from the temporary text.  
   - Continue until no separator remains.  
   - After the loop, if any text remains, insert it as the final recipient.  
   - Drop the temporary table.  
6. Commit the transaction.

### Data Interactions
* **Reads:** None (only internal temp table operations).  
* **Writes:**  
  - EAlertQ  
  - EAlertQAtt  
  - EAlertQTo  
  - EAlertQCC  
  - EAlertQBCC