# Procedure: sp_TAMS_TOA_Update_TOA_URL

### Purpose
This stored procedure updates a record in the TAMS_TOA_URL table with new values for the specified parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PLine	| NVARCHAR(50) | The line number to be updated. |
| @PLoc	| NVARCHAR(50) | The location to be updated. |
| @PType	| NVARCHAR(50) | The type to be updated. |
| @EncPLine	| NVARCHAR(100) | The encrypted line number. |
| @EncPLoc	| NVARCHAR(100) | The encrypted location. |
| @EncPType	| NVARCHAR(100) | The encrypted type. |
| @GenURL	| NVARCHAR(500) | The generated URL. |
| @Message	| NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. If the current transaction count is 0, it sets the internal transaction flag to 1 and begins a new transaction.
3. It then inserts a new record into the TAMS_TOA_URL table with the provided values for PLine, PLoc, PType, EncPLine, EncPLoc, EncPType, and GenURL.
4. If an error occurs during the insertion process, it sets the @Message output parameter to an error message and jumps to the TRAP_ERROR label.
5. If no errors occur, it commits the transaction if one was started and returns the value of the @Message output parameter.
6. If an error occurred, it rolls back the transaction and returns the value of the @Message output parameter.

### Data Interactions
* **Reads:** None explicitly selected from tables.
* **Writes:** TAMS_TOA_URL table (insertion)