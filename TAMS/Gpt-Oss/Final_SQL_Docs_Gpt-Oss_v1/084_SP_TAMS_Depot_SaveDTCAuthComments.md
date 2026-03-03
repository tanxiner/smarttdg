# Procedure: SP_TAMS_Depot_SaveDTCAuthComments

### Purpose
Persist comment text for depot authorization records, updating or inserting remark rows as needed.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @str | TAMS_DTC_AUTH_COMMENTS readonly | Table‑valued parameter containing pairs of authid and comment text to be processed. |
| @success | bit OUTPUT | Flag set to 1 on successful completion, 0 on error. |
| @Message | NVARCHAR(500) OUTPUT | Error message populated when an exception occurs. |

### Logic Flow
1. Disable row‑count messages with `SET NOCOUNT ON`.  
2. Initialize a flag `@IntrnlTrans` to 0.  
3. If no active transaction exists (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
4. Declare local variables `@authid` (int) and `@comments` (nvarchar(max)).  
5. Open a cursor over the rows of `@str`.  
6. For each fetched row:  
   a. Retrieve the current `RemarkID` for the authorization record identified by `@authid` from `TAMS_Depot_Auth`.  
   b. If a `RemarkID` exists (`<> -1`):  
      - Update the corresponding row in `TAMS_Depot_Auth_Remark` with the new comment.  
   c. If no `RemarkID` exists:  
      - Insert a new row into `TAMS_Depot_Auth_Remark` with the comment.  
      - Capture the new identity value into `@remarkid`.  
      - Update the `TAMS_Depot_Auth` record to reference this new `RemarkID`.  
7. Close and deallocate the cursor.  
8. If any error occurred during the loop (`@@ERROR <> 0`):  
   - Set `@Message` to a generic error string.  
   - Jump to the error handling section.  
9. On normal completion:  
   - Commit the transaction if it was started internally (`@IntrnlTrans = 1`).  
   - Set `@success` to 1 and return.  
10. On error:  
    - Roll back the transaction if it was started internally.  
    - Set `@success` to 0 and return.

### Data Interactions
* **Reads:** `TAMS_Depot_Auth`, `TAMS_Depot_Auth_Remark`, table variable `@str`.  
* **Writes:** `TAMS_Depot_Auth_Remark`, `TAMS_Depot_Auth`.