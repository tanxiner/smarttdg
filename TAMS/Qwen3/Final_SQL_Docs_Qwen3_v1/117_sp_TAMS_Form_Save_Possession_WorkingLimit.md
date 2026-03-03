# Procedure: sp_TAMS_Form_Save_Possession_WorkingLimit

### Purpose
This stored procedure saves a new possession working limit record to the TAMS_Possession_WorkingLimit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location of the red flashing lamps. |
| @PossID | BIGINT | The ID of the possession being saved. |
| @Message | NVARCHAR(500) | An output parameter that stores an error message if one occurs. |

### Logic Flow
1. The procedure checks if a transaction has already been started by checking the @@TRANCOUNT variable.
2. If no transaction is in progress, it starts a new transaction and sets the internal transaction flag to 1.
3. It then checks if a record with the same possession ID and red flashing lamps location already exists in the TAMS_Possession_WorkingLimit table.
4. If no such record exists, it inserts a new record into the table with the provided possession ID and red flashing lamps location.
5. After inserting or updating the record, the procedure checks if an error occurred during this process.
6. If an error did occur, it sets the @Message output parameter to an error message and exits the transaction.
7. If no errors occurred, the procedure commits the transaction and returns the @Message output parameter.
8. If an error did occur but a transaction was already in progress, the procedure rolls back the transaction and returns the @Message output parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_WorkingLimit]
* **Writes:** [dbo].[TAMS_Possession_WorkingLimit]