# Procedure: sp_TAMS_Approval_Del_TVFStation

### Purpose
Deletes a specific TVF station record identified by TARId and ID from the TAMS_TAR_TVF table.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the TAR record to delete. |
| @TVFID    | BIGINT        | Identifier of the TVF station record to delete. |
| @Message  | NVARCHAR(500) | Output message indicating success or error. |

### Logic Flow
1. Initialise an internal transaction flag `@IntrnlTrans` to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Execute a DELETE on `TAMS_TAR_TVF` where `TARId = @TARID` and `ID = @TVFID`.  
4. If the DELETE causes an error (`@@ERROR <> 0`), set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
5. If no error, and an internal transaction was started, commit the transaction.  
6. Return the value of `@Message`.  
7. In the error handling section, if an internal transaction was started, roll it back, then return `@Message`.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_TAR_TVF` (DELETE operation)