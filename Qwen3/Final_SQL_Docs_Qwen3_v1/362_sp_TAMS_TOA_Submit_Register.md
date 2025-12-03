# Procedure: sp_TAMS_TOA_Submit_Register

### Purpose
This stored procedure submits a new registration for a TAMS TOA (Tactical Air Mission Support Team Operations) and updates related records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(20) | The user ID associated with the registration. |
| @PartiesWitness | BIGINT = 0 | The ID of the party witness, which is set to 0 by default. |
| @TOAID | BIGINT = 0 | The ID of the TAMS TOA being registered. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores any error message generated during the procedure execution. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0, indicating that no transactions are currently active.
2. If there is no current transaction, it sets the internal transaction flag to 1 and begins a new transaction.
3. It then updates the TAMS TOA record with the specified ID to reflect its new status as registered, along with the current date and time of registration and update.
4. An audit record is inserted into the TAMS TOA Audit table for the same ID, capturing the current date and time of the update.
5. The procedure then updates the parties witness record in the TAMS TOA Parties table to reflect that it has been designated as a witness for the specified TAMS TOA ID and party witness ID.
6. It also updates the book-in time field in the same parties witness record, setting it to the current date and time.
7. If any errors occur during these updates, an error message is stored in the @Message output parameter and the procedure proceeds to roll back the transaction if one was active.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA], [dbo].[TAMS_TOA_Audit], [dbo].[TAMS_TOA_Parties]
* **Writes:** [dbo].[TAMS_TOA], [dbo].[TAMS_TOA_Audit], [dbo].[TAMS_TOA_Parties]