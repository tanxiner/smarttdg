# Procedure: sp_TAMS_TOA_Surrender

The purpose of this stored procedure is to update the status of a TAMS TOA record from an inactive state to a surrendered state, and also logs the audit trail for the change.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS TOA record to be updated. |
| @Message | NVARCHAR(500) | An output parameter that stores an error message if any error occurs during the procedure execution. |

### Logic Flow
1. The procedure first checks if a transaction is already in progress by checking the @@TRANCOUNT system variable.
2. If no transaction is in progress, it sets @IntrnlTrans to 1 and begins a new transaction.
3. It then updates the TOAStatus column of the TAMS_TOA table from an inactive state (not equal to 6) to a surrendered state (equal to 4), and also updates the SurrenderTime and UpdatedOn columns with the current date and time.
4. Next, it inserts a new record into the TAMS_TOA_Audit table that includes the updated record's data, along with the timestamp of the update and a flag indicating the type of operation (U for Update).
5. If any error occurs during this process, it sets @Message to an error message and jumps to the TRAP_ERROR label.
6. Otherwise, if a transaction was started earlier, it commits the transaction and returns the @Message output parameter.
7. If an error occurred, it rolls back the transaction and also returns the @Message output parameter.

### Data Interactions
* Reads: TAMS_TOA table
* Writes: TAMS_TOA table (update), TAMS_TOA_Audit table (insert)