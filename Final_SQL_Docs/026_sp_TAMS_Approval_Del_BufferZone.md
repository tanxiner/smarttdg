# Procedure: sp_TAMS_Approval_Del_BufferZone

### Purpose
Removes a sector assignment from a TAR record and ensures transactional integrity.

### Parameters
| Name      | Type      | Purpose |
| :-------- | :-------- | :------ |
| @TARID    | BIGINT    | Identifier of the TAR to modify. |
| @SectorID | BIGINT    | Identifier of the sector to remove. |
| @Message  | NVARCHAR(500) OUTPUT | Returns status or error message. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to indicate whether the procedure started a new transaction.  
2. If no transaction is active (`@@TRANCOUNT = 0`), set the flag to 1 and begin a new transaction.  
3. Execute a `DELETE` on `TAMS_TAR_Sector` where the TAR and sector IDs match the supplied parameters.  
4. If the delete operation fails (`@@ERROR <> 0`), set `@Message` to an error string and jump to the error handling section.  
5. If the delete succeeds, commit the transaction if it was started internally and return the (possibly null) message.  
6. In the error handling section, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_TAR_Sector` (DELETE)