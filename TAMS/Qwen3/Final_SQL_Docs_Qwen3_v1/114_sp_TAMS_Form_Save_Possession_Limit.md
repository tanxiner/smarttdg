# Procedure: sp_TAMS_Form_Save_Possession_Limit

### Purpose
This stored procedure saves a new possession limit record to the TAMS_Possession_Limit table if no existing record is found for the specified PossID, TypeOfProtectionLimit, and RedFlashingLampsLoc.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TypeOfProtectionLimit | NVARCHAR(50) | The type of protection limit to be saved. |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location of the red flashing lamps. |
| @PossID | BIGINT | The ID of the possession for which the limit is being saved. |
| @Message | NVARCHAR(500) | An output parameter that contains an error message if any. |

### Logic Flow
1. The procedure checks if a transaction has already been started by checking the @@TRANCOUNT system variable.
2. If no transaction exists, it starts a new one and sets a flag to indicate this.
3. It then checks if an existing record is found in the TAMS_Possession_Limit table for the specified PossID, TypeOfProtectionLimit, and RedFlashingLampsLoc.
4. If no record is found, it inserts a new record into the TAMS_Possession_Limit table with the provided values.
5. If an error occurs during the insertion process, it sets the @Message parameter to an error message and jumps to the TRAP_ERROR label.
6. After successfully inserting or not finding a record, the procedure checks if any errors occurred. If so, it rolls back the transaction and returns the error message. Otherwise, it commits the transaction and returns the saved @Message value.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_Limit]
* **Writes:** [dbo].[TAMS_Possession_Limit]