# Procedure: sp_TAMS_TOA_Add_Parties

### Purpose
Adds a party to a TOA record, ensuring no duplicate FIN exists, updates the party count, and records the party details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN | NVARCHAR(50) | FIN of the party to add |
| @PartiesName | NVARCHAR(200) | Name of the party |
| @IsTMC | NVARCHAR(5) | Flag indicating if the party is a TMC ('Y' or other) |
| @NoOfParties | BIGINT | Updated total number of parties for the TOA |
| @TOAID | BIGINT | Identifier of the TOA record |
| @Message | NVARCHAR(500) OUTPUT | Result code: '1' for duplicate, '' for success, error message on failure |

### Logic Flow
1. Initialise an internal transaction flag to 0.  
2. If no outer transaction is active, set the flag to 1 and begin a new transaction.  
3. Convert @IsTMC to a numeric flag @DerIsTMC (1 if 'Y', else 0).  
4. Count existing parties in TAMS_TOA_Parties where TOAId matches @TOAID and the decrypted NRIC equals @PartiesFIN.  
5. If a match is found, set @Message to '1' (duplicate) and skip insertion.  
6. If no match, update TAMS_TOA.NoOfParties to @NoOfParties for the given @TOAID.  
7. Insert a new record into TAMS_TOA_Parties with the provided name, encrypted FIN, default flags for InCharge and Witness, the numeric TMC flag, current timestamp for BookInTime, NULL for BookOutTime, and status 'In'.  
8. Clear @Message to indicate success.  
9. If any error occurs during the update or insert, set @Message to 'ERROR INSERTING TAMS_TOA_Parties' and jump to error handling.  
10. On normal exit, commit the transaction if it was started internally and return @Message.  
11. On error, rollback the transaction if it was started internally and return @Message.

### Data Interactions
* **Reads:** TAMS_TOA_Parties, TAMS_TOA  
* **Writes:** TAMS_TOA, TAMS_TOA_Parties