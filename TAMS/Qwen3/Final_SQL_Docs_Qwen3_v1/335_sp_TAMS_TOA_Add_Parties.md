# Procedure: sp_TAMS_TOA_Add_Parties

### Purpose
This stored procedure adds new parties to a TAMS TOA record, updating the number of parties if they already exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN	| NVARCHAR(50) | The NRIC of the party being added |
| @PartiesName	| NVARCHAR(200) | The name of the party being added |
| @IsTMC	| NVARCHAR(5) | Whether the party is in charge (Y/N) |
| @NoOfParties	| BIGINT | The new number of parties |
| @TOAID	| BIGINT | The ID of the TAMS TOA record being updated |
| @Message	| NVARCHAR(500) | An output parameter containing a message about the result |

### Logic Flow
1. Check if a transaction has already started; if not, start one.
2. Determine if the party is in charge based on the value of @IsTMC.
3. Count the number of existing parties with the same NRIC as the new party being added.
4. If a party with the same NRIC exists, set @Message to '1' (indicating an update).
5. Otherwise, update the TAMS TOA record with the new number of parties and insert a new party into the TAMS_TOA_Parties table.
6. Check for any errors during insertion; if found, roll back the transaction and set @Message to an error message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Parties