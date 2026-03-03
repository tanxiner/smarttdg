# Procedure: EAlertQ_EnQueue

### Purpose
Enqueues an alert message and distributes its recipients to the appropriate queue tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | Email address of the sender |
| @Subject | nvarchar(500) | Subject line of the alert |
| @Sys | nvarchar(100) | System identifier that generated the alert |
| @Greetings | ntext | Greeting text to prepend to the alert |
| @AlertMsg | nvarchar(max) | Body of the alert message |
| @UserId | nvarchar(50) | Identifier of the user creating the alert |
| @SendTo | ntext | Comma‑separated list of primary recipients |
| @CC | ntext | Comma‑separated list of CC recipients |
| @BCC | ntext | Comma‑separated list of BCC recipients |
| @Separator | nvarchar(1) | Delimiter used in the recipient lists |
| @AlertID | decimal(18,0) output | Identity of the inserted alert record |
| @From | nvarchar(250) = null | Optional “From” address for the alert |

### Logic Flow
1. If `@SendTo` is null, exit immediately.  
2. Insert a new row into `EAlertQ` with the supplied alert details; capture the new identity into `@AlertID`.  
3. **Process SendTo**  
   - Create a temporary table `#tsendto` and insert `@SendTo`.  
   - Use a text pointer to locate each occurrence of `@Separator`.  
   - In a loop, extract the substring before the separator, trim it, and insert it into `EAlertQTo` with the current `@AlertID`.  
   - Remove the processed portion from the text and repeat until no separator remains.  
   - After the loop, if any text remains, insert it as the final recipient into `EAlertQTo`.  
   - Drop `#tsendto`.  
4. **Process CC**  
   - Repeat the same pointer‑based extraction logic with a temporary table `#tcc` and insert each address into `EAlertQCC`.  
   - Drop `#tcc`.  
5. **Process BCC**  
   - Repeat the same logic with a temporary table `#tbcc` and insert each address into `EAlertQBCC`.  
   - Drop `#tbcc`.  
6. End of procedure.

### Data Interactions
* **Reads:** None  
* **Writes:** `EAlertQ`, `EAlertQTo`, `EAlertQCC`, `EAlertQBCC`