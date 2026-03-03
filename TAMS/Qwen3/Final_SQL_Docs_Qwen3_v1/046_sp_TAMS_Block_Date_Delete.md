# Procedure: sp_TAMS_Block_Date_Delete

### Purpose
This stored procedure deletes a record from the TAMS_Block_TARDate table based on the provided BlockID and logs the deletion in the TAMS_Block_TARDate_Audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @BlockID | INTEGER | The ID of the block to be deleted. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and beginning a new transaction if no existing one is found.
2. It then inserts a record into the TAMS_Block_TARDate_Audit table with the current date, 'D' (deletion), and all columns from the TAMS_Block_TARDate table where ID matches @BlockID.
3. Next, it deletes the record from the TAMS_Block_TARDate table where ID equals @BlockID.
4. If any error occurs during deletion, an error message is set in @Message and the procedure jumps to the TRAP_ERROR label.
5. After successful deletion or if an error occurred, the procedure checks the internal transaction flag. If it's 1 (meaning a new transaction was started), it commits the transaction and returns the value of @Message. If it's 0 (no new transaction), it rolls back the transaction and also returns the value of @Message.

### Data Interactions
* **Reads:** TAMS_Block_TARDate, TAMS_Block_TARDate_Audit
* **Writes:** TAMS_Block_TARDate