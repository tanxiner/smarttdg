# Procedure: SMTP_GET_Email_Attachments

### Purpose
Retrieve file paths of active attachments for a specified alert.

### Parameters
| Name     | Type | Purpose |
| :---     | :--- | :--- |
| @AlertID | int  | Identifier of the alert whose attachments are requested |

### Logic Flow
1. Accept an alert identifier as input.  
2. Query the attachment table for records where the alert matches the input and the attachment is marked active.  
3. Return the file path column for each qualifying record.

### Data Interactions
* **Reads:** EAlertQAtt  
* **Writes:** None