# Procedure: sp_TAMS_Form_Cancel

### Purpose
This stored procedure cancels a TAMS form by deleting its associated records from the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS form to be cancelled. |

### Logic Flow
1. The procedure starts by setting default values for the TARID and error message variables.
2. It then checks if a transaction is already in progress, and if not, it begins a new transaction.
3. The procedure deletes the records from the TAMS_TAR table where the Id matches the provided TARID.
4. Next, it deletes the temporary attachment records for the same TARID.
5. If any errors occur during this process, an error message is set and the procedure jumps to the TRAP_ERROR label.
6. If no errors occurred, the procedure commits the transaction (if one was started) and returns the error message.
7. If an error did occur, the procedure rolls back the transaction and also returns the error message.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** TAMS_TAR table, TAMS_TAR_Attachment_Temp table