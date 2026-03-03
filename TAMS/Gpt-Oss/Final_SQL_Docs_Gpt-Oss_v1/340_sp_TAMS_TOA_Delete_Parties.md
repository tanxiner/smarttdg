# Procedure: sp_TAMS_TOA_Delete_Parties

### Purpose
Delete a specific party from a TOA record while ensuring at least two parties remain and updating the party count.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | Identifier of the party to delete |
| @TOAID | BIGINT | Identifier of the TOA from which the party is removed |
| @Message | NVARCHAR(500) OUTPUT | Status or error message returned to the caller |

### Logic Flow
1. Initialise an internal transaction flag to 0.  
2. If no active transaction exists, set the flag to 1 and begin a new transaction.  
3. Clear the output message.  
4. Count how many parties are currently linked to the specified TOA.  
5. If the count is 2 or fewer, raise an error stating that at least two parties must remain; exit the procedure.  
6. Otherwise, delete the party record that matches both the TOAId and the provided party Id.  
7. Re‑calculate the number of parties for that TOA and update the `NoOfParties` column in the TOA table.  
8. If any error occurs during the delete or update, set a generic error message and jump to the error handling section.  
9. In the error handling section, capture the error details, re‑raise them, and roll back the transaction if it was started internally.  
10. If no errors occurred, commit the transaction if it was started internally and return the (empty) message.

### Data Interactions
* **Reads:** `TAMS_TOA_Parties`, `TAMS_TOA`  
* **Writes:** `TAMS_TOA_Parties` (DELETE), `TAMS_TOA` (UPDATE)