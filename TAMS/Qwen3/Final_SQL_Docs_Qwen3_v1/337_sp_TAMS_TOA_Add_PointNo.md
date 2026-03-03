# Procedure: sp_TAMS_TOA_Add_PointNo

### Purpose
This stored procedure adds a new point number to the TAMS_TOA table, including the TOAID and creation date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | nvarchar(200) | The point number to be added. |
| @toaid | int | The ID of the TOA associated with the point number. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores any error message generated during the procedure execution. |
| @CreatedBy | nvarchar(50) | The user who created the new point number. |

### Logic Flow
1. The procedure starts by declaring a variable to track internal transactions.
2. It checks if there are any active transactions and sets the internal transaction flag accordingly.
3. If no transactions are active, it begins a new transaction.
4. It initializes an error message variable to empty.
5. Inside the transaction block:
   * It inserts a new record into the TAMS_TOA_PointNo table with the provided TOAID, point number, creation date, and creator's name.
   * If any errors occur during this insertion, it sets the error message and jumps to the TRAP_ERROR label.
6. After successful insertion or if an error occurs:
   * It checks the internal transaction flag. If it is 1 (indicating a new transaction), it commits the transaction and returns the error message.
   * If the internal transaction flag is not 1, it rolls back the transaction and returns the error message.

### Data Interactions
* **Reads:** None explicitly listed; however, the procedure uses system tables like @@TRANCOUNT to track transactions.
* **Writes:** 
    + TAMS_TOA_PointNo table: inserted records.