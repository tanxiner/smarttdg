# Procedure: sp_TAMS_Form_Save_Possession_PowerSector

The procedure saves a new possession power sector record to the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PowerSector | NVARCHAR(4000) | The power sector value to be inserted. |
| @NoOFSCD | INT | The number of SCDs associated with this possession power sector. |
| @BreakerOut | NVARCHAR(5) | A flag indicating whether the breaker is out (Y) or not (N). |
| @PossID | BIGINT | The ID of the possession to which this power sector belongs. |
| @Message | NVARCHAR(500) | An output parameter containing an error message if any. |

### Logic Flow
1. The procedure checks if a transaction has already started by checking the @@TRANCOUNT variable.
2. If no transaction is in progress, it starts a new transaction and sets the internal transaction flag (@IntrnlTrans) to 1.
3. It then checks if a record with the same possession ID and power sector value already exists in the TAMS_Possession_PowerSector table.
4. If no such record exists, it inserts a new record into the table with the provided values.
5. After inserting or updating the record, it checks for any errors that may have occurred during the process.
6. If an error occurs, it sets the @Message parameter to an error message and exits the procedure.
7. If no errors occur, it commits the transaction (if one was started) and returns the @Message parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_PowerSector]
* **Writes:** [dbo].[TAMS_Possession_PowerSector]