# Procedure: sp_TAMS_TOA_Add_Parties1

### Purpose
Adds a party to a TOA record, preventing duplicate FIN entries and maintaining the correct party count.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN | NVARCHAR(50) | FIN of the party to add |
| @PartiesName | NVARCHAR(200) | Name of the party |
| @IsTMC | NVARCHAR(5) | Indicator if the party is a TMC ('Y' or other) |
| @NoOfParties | BIGINT | Current number of parties for the TOA |
| @TOAID | BIGINT | Identifier of the TOA record |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start an internal transaction and mark it for later commit or rollback.  
2. **Initialize Variables** – Set internal transaction flag, party counter, and message to defaults.  
3. **Determine TMC Flag** – Convert @IsTMC to a numeric flag: 1 if 'Y', otherwise 0.  
4. **Duplicate Check** – Count rows in `TAMS_TOA_Parties` where `TOAId` matches @TOAID and the decrypted `NRIC` equals @PartiesFIN.  
5. **If Duplicate Exists** – Set @Message to `'1'` and skip insertion.  
6. **If No Duplicate** –  
   a. Update `TAMS_TOA.NoOfParties` to @NoOfParties.  
   b. Insert a new row into `TAMS_TOA_Parties` with the provided name, encrypted FIN, TMC flag, current time as `BookInTime`, and status `'In'`.  
   c. Re‑calculate and update `TAMS_TOA.NoOfParties` to the actual count of parties for that TOA.  
   d. Clear @Message.  
7. **Error Check** – If any error occurred during the above steps, set @Message to `'ERROR INSERTING TAMS_TOA_Parties'` and jump to error handling.  
8. **Commit or Rollback** – If the procedure started its own transaction, commit on success or rollback on error.  
9. **Return** – Return @Message as the procedure’s result.

### Data Interactions
* **Reads:** `TAMS_TOA_Parties` (count for duplicate check)  
* **Writes:** `TAMS_TOA` (update `NoOfParties` twice), `TAMS_TOA_Parties` (insert new party)