# Procedure: sp_TAMS_TOA_Save_ProtectionType

### Purpose
This stored procedure saves a new or updated protection type for a given TOAID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @toaid | int | The ID of the TOA to save the protection type for. |
| @protectiontype | nvarchar(50) | The new or updated protection type. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that returns a message indicating success or failure. |

### Logic Flow
1. The procedure starts by checking if there is an active transaction. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It then checks if the protection type is 'B'. If so, it deletes all records from TAMS_TOA_PointNo where TOAID matches the provided @toaid.
3. Next, it updates the ProtectionType field in TAMS_TOA for the specified Id (@toaid) to the value of @protectiontype.
4. After updating the data, it sets the @Message output parameter to an empty string.
5. If any errors occur during this process (i.e., @@ERROR is not 0), it sets @Message to 'ERROR SELECTING PROTECTION TYPE' and jumps to the TRAP_ERROR label.
6. If no errors occurred, it commits the transaction if there was one and returns the value of @Message.
7. If an error did occur, it rolls back the transaction and also returns the value of @Message.

### Data Interactions
* **Reads:** TAMS_TOA_PointNo, TAMS_TOA
* **Writes:** TAMS_TOA_PointNo, TAMS_TOA