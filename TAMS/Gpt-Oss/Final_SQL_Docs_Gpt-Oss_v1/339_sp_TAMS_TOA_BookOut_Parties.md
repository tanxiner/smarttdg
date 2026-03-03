# Procedure: sp_TAMS_TOA_BookOut_Parties

### Purpose
Marks a specific party record as booked out by setting its BookOutTime to the current time and BookInStatus to 'Out'.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | Identifier of the party record to update |
| @TOAID | BIGINT | Identifier of the TOA to which the party belongs |
| @Message | NVARCHAR(500) OUTPUT | Returns an empty string on success or an error message if the update fails |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If no outer transaction is active (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Clear the output message (`@Message = ''`).  
4. Execute an UPDATE on `TAMS_TOA_Parties` setting `BookOutTime` to the current timestamp and `BookInStatus` to 'Out' where `TOAId` equals `@TOAID` and `Id` equals `@PartiesID`.  
5. If the UPDATE generates an error (`@@ERROR <> 0`), set `@Message` to `'ERROR INSERTING TAMS_TOA_Parties'` and jump to the error handling section.  
6. If no error occurred, commit the transaction if it was started internally (`@IntrnlTrans = 1`) and return the (empty) message.  
7. In the error handling section, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_TOA_Parties` (UPDATE)