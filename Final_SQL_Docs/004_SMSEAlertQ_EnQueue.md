# Procedure: SMSEAlertQ_EnQueue

### Purpose
Enqueues an SMS/email alert by inserting the alert details and its recipients into the queue tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | Email address or identifier of the message sender |
| @Subject | nvarchar(500) | Subject line of the alert |
| @Sys | nvarchar(100) | System or source generating the alert |
| @Greetings | ntext | Opening greeting text for the message body |
| @AlertMsg | ntext | Main alert message content |
| @UserId | nvarchar(50) | Identifier of the user creating the alert |
| @SendTo | ntext | Comma‑separated list of primary recipients |
| @CC | ntext | Comma‑separated list of CC recipients |
| @BCC | ntext | Comma‑separated list of BCC recipients |
| @Separator | nvarchar(1) | Delimiter used in the recipient lists |
| @AlertID | decimal(18,0) OUTPUT | Returns the identity of the newly inserted alert record |
| @From | nvarchar(250) = null | Optional “From” address for the alert |

### Logic Flow
1. Begin a transaction.  
2. If @SendTo is null, exit immediately.  
3. Insert a new record into SMSEAlertQ with the supplied alert details; capture its identity into @AlertID.  
4. Process the @SendTo list:  
   - Create a temporary table holding the ntext value.  
   - Use TEXTPTR and PATINDEX to locate each separator.  
   - In a loop, extract each email address, trim spaces, and insert it into SMSEAlertQTo with the alert ID.  
   - Remove the processed segment from the temporary text.  
   - After the loop, insert any remaining text as the final recipient.  
   - Drop the temporary table.  
5. Repeat step 4 for the @CC list, inserting into SMSEAlertQCC.  
6. Repeat step 4 for the @BCC list, inserting into SMSEAlertQBCC.  
7. Commit the transaction.  

### Data Interactions
* **Reads:** None from persistent tables.  
* **Writes:**  
  - SMSEAlertQ  
  - SMSEAlertQTo  
  - SMSEAlertQCC  
  - SMSEAlertQBCC