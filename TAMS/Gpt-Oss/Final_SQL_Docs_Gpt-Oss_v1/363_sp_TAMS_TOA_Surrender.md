# Procedure: sp_TAMS_TOA_Surrender

### Purpose
Surrenders a TOA record by updating its status and logging the change.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TOAID    | BIGINT        | Identifier of the TOA to surrender |
| @Message  | NVARCHAR(500) | Output message indicating success or error |

### Logic Flow
1. Initialize a flag `@IntrnlTrans` to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Update the `TAMS_TOA` row with `ID = @TOAID` that is not already in status 6: set `TOAStatus` to 4, `SurrenderTime` to the current date/time, and `UpdatedOn` to the current date/time.  
4. Insert a new audit record into `TAMS_TOA_Audit` by selecting all columns from the updated `TAMS_TOA` row (prefixing with an empty string for the audit ID).  
5. If any error occurs during the update or insert, set `@Message` to `'ERROR UPDATING TAMS_TOA'` and jump to the error handling section.  
6. On successful completion, commit the transaction if it was started internally and return `@Message`.  
7. In the error handling section, rollback the transaction if it was started internally and return `@Message`.

### Data Interactions
* **Reads:** `TAMS_TOA`  
* **Writes:** `TAMS_TOA`, `TAMS_TOA_Audit`