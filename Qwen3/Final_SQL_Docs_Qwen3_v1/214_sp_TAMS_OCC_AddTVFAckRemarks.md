# Procedure: sp_TAMS_OCC_AddTVFAckRemarks

### Purpose
This stored procedure adds a new record to the TAMS_TVF_Ack_Remark table, which stores remarks for TVF acknowledgments, and also inserts an audit record into the TAMS_TVF_Ack_Remark_Audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | int | The ID of the user who is adding the remark. |
| @TVFAckId | int | The ID of the TVF acknowledgment being added a remark for. |
| @TVFRemarks | nvarchar(1000) | The text of the remark to be added. |

### Logic Flow
1. The procedure starts by declaring a variable @NewID, which will hold the ID of the newly inserted record.
2. It then attempts to start a transaction and insert a new record into the TAMS_TVF_Ack_Remark table with the provided @TVFRemarks and @UserId.
3. After inserting the record, it selects the ID of the newly inserted record from the SCOPE_IDENTITY() function and stores it in @NewID.
4. Next, it inserts an audit record into the TAMS_TVF_Ack_Remark_Audit table with the provided information, including the user who added the remark and the date and time of the addition.
5. If any part of this process fails, the transaction is rolled back to maintain data consistency.

### Data Interactions
* **Reads:** None explicitly listed from tables; however, it uses GETDATE() and @UserID which are likely derived from other tables or variables.
* **Writes:** 
	+ TAMS_TVF_Ack_Remark table (new record)
	+ TAMS_TVF_Ack_Remark_Audit table (audit record)