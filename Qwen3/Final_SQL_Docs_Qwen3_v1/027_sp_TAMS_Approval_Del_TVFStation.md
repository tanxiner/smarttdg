# Procedure: sp_TAMS_Approval_Del_TVFStation

The purpose of this stored procedure is to delete a TVF station from the TAMS_TAR table based on the provided TARID and TVFID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to be deleted. |
| @TVFID | BIGINT | The ID of the TVF station to be deleted. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message generated during the procedure execution. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag (@IntrnlTrans) to 0.
2. It then checks if there is an active transaction. If not, it sets @IntrnlTrans to 1 and begins a new transaction.
3. The procedure then deletes the specified TVF station from the TAMS_TAR table based on the provided TARID and TVFID.
4. After deletion, it checks for any errors that may have occurred during the process. If an error is found, it sets @Message to an error message and jumps to the TRAP_ERROR label.
5. If no errors are found, the procedure commits the transaction if one was started (@IntrnlTrans = 1) and returns the value of @Message.
6. If an error occurred, the procedure rolls back the transaction if one was started (@IntrnlTrans = 1) and also returns the value of @Message.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** TAMS_TAR table