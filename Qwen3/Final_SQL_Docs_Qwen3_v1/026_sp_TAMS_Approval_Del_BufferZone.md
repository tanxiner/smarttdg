# Procedure: sp_TAMS_Approval_Del_BufferZone

### Purpose
This stored procedure deletes a buffer zone from the TAMS_TAR_Sector table based on the provided TARID and SectorID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR to delete the sector from. |
| @SectorID | BIGINT | The ID of the sector to delete. |
| @Message | NVARCHAR(500) | An output parameter that stores an error message if any. |

### Logic Flow
1. The procedure starts by setting a flag to indicate whether a transaction has been started.
2. It then checks if a transaction is already in progress and sets the flag accordingly.
3. If no transaction is in progress, it begins a new transaction.
4. The procedure then deletes the specified sector from the TAMS_TAR_Sector table based on the provided TARID and SectorID.
5. After deletion, it checks for any errors that may have occurred during this process.
6. If an error occurs, it sets the @Message parameter with an error message and skips to the TRAP_ERROR label.
7. If no errors occur, it commits the transaction if one was started and returns the @Message parameter.
8. If an error occurred, it rolls back the transaction and also returns the @Message parameter.

### Data Interactions
* **Reads:** TAMS_TAR_Sector table
* **Writes:** TAMS_TAR_Sector table