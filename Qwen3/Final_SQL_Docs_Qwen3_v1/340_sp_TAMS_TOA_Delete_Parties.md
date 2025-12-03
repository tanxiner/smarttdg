# Procedure: sp_TAMS_TOA_Delete_Parties

### Purpose
This stored procedure deletes parties from the TAMS_TOA_Parties table and updates the corresponding TOA record in the TAMS_TOA table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | The ID of the party to be deleted. |
| @TOAID | BIGINT | The ID of the TOA associated with the parties. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag to indicate that a transaction is about to be started.
2. It then checks the number of parties associated with the specified TOA ID. If there are less than 2 parties, an error message is raised.
3. If there are 2 or more parties, the procedure deletes the specified party from the TAMS_TOA_Parties table and updates the corresponding TOA record in the TAMS_TOA table by setting the NoOfParties field to the count of remaining parties.
4. The procedure then checks for any errors that occurred during the execution of the stored procedure. If an error occurs, it sets the @Message parameter with an error message and exits the procedure.
5. If no errors occur, the procedure commits the transaction and returns the value of the @Message parameter.

### Data Interactions
* **Reads:** TAMS_TOA_Parties table
* **Writes:** TAMS_TOA_Parties table, TAMS_TOA table