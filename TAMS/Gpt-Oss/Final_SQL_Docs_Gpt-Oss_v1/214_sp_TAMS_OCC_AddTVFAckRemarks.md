# Procedure: sp_TAMS_OCC_AddTVFAckRemarks

### Purpose
Adds a remark to a TVF acknowledgement and records the action in an audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | int | Identifier of the user performing the operation |
| @TVFAckId | int | Identifier of the TVF acknowledgement to which the remark is added |
| @TVFRemarks | nvarchar(1000) | Text of the remark to be stored |

### Logic Flow
1. Begin a transaction.  
2. Insert a new row into **TAMS_TVF_Ack_Remark** with the supplied acknowledgement ID, remark text, current timestamp, and user ID for both created and updated fields.  
3. Capture the identity value of the newly inserted remark row into a local variable.  
4. Insert a corresponding audit record into **TAMS_TVF_Ack_Remark_Audit**.  
   - The audit record includes the user ID, current timestamp, action type ‘I’ (insert), the new remark ID, and copies of all fields from the newly inserted remark row.  
5. Commit the transaction.  
6. If any error occurs during the transaction, roll back all changes.

### Data Interactions
* **Reads:** TAMS_TVF_Ack_Remark  
* **Writes:** TAMS_TVF_Ack_Remark, TAMS_TVF_Ack_Remark_Audit