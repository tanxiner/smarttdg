# Procedure: sp_TAMS_TOA_Submit_Register

### Purpose
Registers a TOA record by setting its status, recording timestamps, auditing the change, marking a witness party, and logging the book‑in time.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(20) | Identifier of the user performing the registration |
| @PartiesWitness | BIGINT | ID of the party to be flagged as a witness |
| @TOAID | BIGINT | ID of the TOA record to update |
| @Message | NVARCHAR(500) OUTPUT | Error message returned if the procedure fails |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to indicate whether the procedure started a new transaction.  
2. If no outer transaction exists, set the flag and begin a new transaction.  
3. Update the `TAMS_TOA` row identified by `@TOAID`: set `TOAStatus` to 1, record the current time in `RegisteredTime`, `UpdatedOn`, and store the user name in `UpdatedBy`.  
4. Insert a new audit record into `TAMS_TOA_Audit` capturing the current user, timestamp, action code 'I', and all columns from the updated `TAMS_TOA` row.  
5. Mark the specified party as a witness by setting `IsWitness` to 1 in `TAMS_TOA_Parties` where `TOAId` equals `@TOAID` and `Id` equals `@PartiesWitness`.  
6. Record the book‑in time for all parties of the TOA by setting `BookInTime` to the current time in `TAMS_TOA_Parties` where `TOAId` equals `@TOAID`.  
7. If any error occurs during the above steps, set `@Message` to 'ERROR UPDATING TAMS_TOA' and jump to the error handling section.  
8. On successful completion, commit the transaction if it was started internally and return the (empty) message.  
9. In the error handling section, rollback the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** `TAMS_TOA` (for audit capture)  
* **Writes:** `TAMS_TOA` (status and timestamps), `TAMS_TOA_Audit` (audit record), `TAMS_TOA_Parties` (witness flag and book‑in time)