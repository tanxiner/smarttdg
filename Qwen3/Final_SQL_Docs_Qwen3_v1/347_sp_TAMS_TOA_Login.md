# Procedure: sp_TAMS_TOA_Login

### Purpose
This stored procedure performs a login operation for TAMS TOA, handling internal transactions and error messages.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARNo	| NVARCHAR(50) | TAR number |
| @TPOPCNRIC	| NVARCHAR(50) | POPCNRIC number |
| @Message	| NVARCHAR(500) | Error message |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. It checks if the current transaction count is 0, and if so, sets the internal transaction flag to 1 and begins a new transaction.
3. It then selects data from the TAMS_Parameters table.
4. If any errors occur during this process, it sets an error message and jumps to the TRAP_ERROR label.
5. Otherwise, it commits the transaction and returns the error message if the internal transaction flag is 1.
6. If an error occurs, it rolls back the transaction and returns the error message.

### Data Interactions
* **Reads:** TAMS_Parameters table