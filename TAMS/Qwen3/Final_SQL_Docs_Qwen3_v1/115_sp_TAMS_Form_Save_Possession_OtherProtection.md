# Procedure: sp_TAMS_Form_Save_Possession_OtherProtection

### Purpose
This stored procedure saves a new possession with other protection details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OtherProtection | NVARCHAR(50) | The value of the other protection detail. |
| @PossID | BIGINT | The ID of the possession to be saved. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started.
2. If not, it sets a flag indicating that a transaction is in progress and begins a new transaction.
3. It then checks if the possession with the specified ID and other protection detail already exists in the database.
4. If no record is found, it inserts a new record into the TAMS_Possession_OtherProtection table with the provided possession ID and other protection detail.
5. After inserting or updating the record, it checks for any errors that may have occurred during this process.
6. If an error occurs, it sets the @Message parameter to indicate that there was an error inserting into TAMS_TAR.
7. Finally, if no errors occurred, it commits the transaction and returns the message in the @Message parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_OtherProtection]
* **Writes:** [dbo].[TAMS_Possession_OtherProtection]