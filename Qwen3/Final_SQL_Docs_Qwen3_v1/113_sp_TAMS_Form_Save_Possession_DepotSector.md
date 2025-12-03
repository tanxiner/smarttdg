# Procedure: sp_TAMS_Form_Save_Possession_DepotSector

### Purpose
This stored procedure saves a possession depot sector record to the database, updating or inserting it based on whether a matching record already exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sector	| NVARCHAR(4000) | The sector value to be saved. |
| @PowerOff	| INT | The power off status of the possession depot sector. |
| @NoOFSCD	| INT | The number of SCDs in the possession depot sector. |
| @BreakerOut	| NVARCHAR(5) | The breaker out status of the possession depot sector. |
| @PossID			| BIGINT | The ID of the possession to be associated with the depot sector. |
| @Message		| NVARCHAR(500) | An output parameter containing a message indicating whether the operation was successful or not. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. If no transactions are currently active, it sets the flag to 1 and begins a new transaction.
3. It then checks if a matching record for the given possession ID and sector already exists in the TAMS_Possession_DepotSector table.
4. If no matching record is found, it inserts a new record into the table with the provided values.
5. If an error occurs during insertion, it sets the @Message parameter to an error message and rolls back the transaction if one was active.
6. Otherwise, it commits the transaction and returns the @Message parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_DepotSector]
* **Writes:** [dbo].[TAMS_Possession_DepotSector]