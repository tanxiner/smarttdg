# Procedure: sp_TAMS_Block_Date_Save

### Purpose
This stored procedure saves a new block date record to the TAMS_Block_TARDate table, ensuring that the block date is within a certain timeframe and not already existing.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line			| NVARCHAR(20) | The line number associated with the block. |
| @TrackType		| NVARCHAR(50) | The type of track being blocked. |
| @BlockDate		| NVARCHAR(20) | The date for which the block is being applied. |
| @BlockReason	| NVARCHAR(100) | The reason for the block. |
| @UserLI			| NVARCHAR(50) | The login ID of the user performing the action. |
| @Message		| NVARCHAR(500) | An output parameter containing a message indicating the result of the operation. |

### Logic Flow
1. The procedure first checks if a transaction has already been started, and if not, it sets an internal flag to indicate that a new transaction is beginning.
2. It then retrieves the user ID from the TAMS_User table based on the provided login ID.
3. The procedure calculates the week number for both the current date and the block date, taking into account leap years and month boundaries.
4. If the block date is within 5 weeks of the current date in the same year, it proceeds to check if a record already exists for this combination of line, track type, and block date.
5. If a record does not exist, the procedure inserts a new record into the TAMS_Block_TARDate table with the provided data.
6. It also inserts an audit record into the TAMS_Block_TARDate_Audit table to track changes made to this record.
7. Finally, if any errors occur during the insertion process, the procedure rolls back the transaction and returns an error message; otherwise, it commits the transaction and returns a success message.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Block_TARDate, TAMS_Block_TARDate_Audit
* **Writes:** TAMS_Block_TARDate