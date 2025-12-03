# Procedure: sp_TAMS_TOA_Add_Parties1

### Purpose
This stored procedure adds new parties to a TAMS TOA record, updating the number of parties associated with it if a party with the same NRIC already exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN	| NVARCHAR(50) | The FIN (Financial Identification Number) of the party to be added. |
| @PartiesName	| NVARCHAR(200) | The name of the party to be added. |
| @IsTMC	| NVARCHAR(5) | A flag indicating whether the party is in charge or not. |
| @NoOfParties	| BIGINT | The number of parties associated with the TAMS TOA record. |
| @TOAID	| BIGINT | The ID of the TAMS TOA record to be updated. |
| @Message	| NVARCHAR(500) | An output parameter containing a message indicating the result of the procedure. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It then checks if a party with the same NRIC (as encrypted) already exists in the TAMS_TOA_Parties table for the specified TOAID.
3. If a party is found, it updates the number of parties associated with the TAMS TOA record to 1 and sets an error message indicating that a duplicate party was found.
4. If no party is found, it inserts a new party into the TAMS_TOA_Parties table for the specified TOAID, updating the number of parties associated with the TAMS TOA record accordingly.
5. The procedure then checks if any errors occurred during the insertion process and sets an error message if necessary.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Parties