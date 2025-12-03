# Procedure: sp_TAMS_Approval_Add_TVFStation

The procedure is used to add a new TVF station for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The TAR ID associated with the TVF station. |
| @StationID	| BIGINT | The ID of the TVF station to be added. |
| @Direction	| NVARCHAR(20) | The direction of the TVF station. |
| @Message	| NVARCHAR(500) | An output parameter that stores an error message if any. |

### Logic Flow
1. The procedure starts by setting a flag `@IntrnlTrans` to 0, indicating that no internal transaction is currently in progress.
2. It then checks if there are any active transactions in the current session. If not, it sets `@IntrnalTrans` to 1 and begins a new transaction.
3. The procedure then checks if a TVF station with the given TAR ID, Station ID, and direction already exists in the TAMS_TAR_TVF table. If no such record is found, it inserts a new record into this table.
4. After inserting or updating the record, the procedure checks for any errors that may have occurred during this process. If an error occurs, it sets the `@Message` output parameter to an error message and exits the transaction.
5. If no errors occur, the procedure commits the transaction and returns the `@Message` output parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_TAR_TVF]
* **Writes:** [dbo].[TAMS_TAR_TVF]