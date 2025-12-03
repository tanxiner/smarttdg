# Procedure: sp_TAMS_Approval_Add_TVFStation

### Purpose
Adds a TVF station to a TAR record when the combination does not already exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to which the station will be linked. |
| @StationID | BIGINT | Identifier of the TVF station to associate. |
| @Direction | NVARCHAR(20) | Direction of the TVF station; may be NULL. |
| @Message | NVARCHAR(500) OUTPUT | Returns a status message indicating success or error. |

### Logic Flow
1. Declare a flag `@IntrnlTrans` and set it to 0.  
2. If no outer transaction is active (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Query `TAMS_TAR_TVF` to determine whether a row with the supplied `@TARID`, `@StationID`, and `@Direction` already exists.  
4. If no such row exists, insert a new record into `TAMS_TAR_TVF` with the provided values.  
5. If the insert fails (`@@ERROR <> 0`), set `@Message` to an error string and jump to the error handling section.  
6. If no error occurred, commit the transaction if it was started internally (`@IntrnlTrans = 1`).  
7. Return the current value of `@Message`.  
8. In the error handling section, rollback the transaction if it was started internally and return `@Message`.

### Data Interactions
* **Reads:** `TAMS_TAR_TVF`  
* **Writes:** `TAMS_TAR_TVF`  

---