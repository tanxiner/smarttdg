# Procedure: sp_TAMS_TOA_BookOut_Parties

### Purpose
This stored procedure performs a book out operation for a specified party, updating its status and recording the current date and time.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | The ID of the party to be booked out. |
| @TOAID | BIGINT | The ID of the TOA (Treatment Order Assignment) associated with the party. |
| @Message | NVARCHAR(500) | An output parameter that stores any error messages generated during the procedure execution. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. If no transactions are currently active, it sets the flag to 1 and begins a new transaction.
3. It initializes an error message variable to empty.
4. The procedure updates the BookOutTime and BookInStatus columns in the TAMS_TOA_Parties table for the specified party (identified by @PartiesID) and TOA ID (@TOAID).
5. If any errors occur during this update, it sets the error message variable and jumps to the TRAP_ERROR label.
6. After successful updates, if an internal transaction was started, it commits the transaction and returns the error message.
7. If an error occurred, it rolls back the internal transaction and returns the error message.

### Data Interactions
* **Reads:** TAMS_TOA_Parties table
* **Writes:** TAMS_TOA_Parties table