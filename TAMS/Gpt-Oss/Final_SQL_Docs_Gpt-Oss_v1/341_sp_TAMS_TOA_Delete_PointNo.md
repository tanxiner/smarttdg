# Procedure: sp_TAMS_TOA_Delete_PointNo

### Purpose
Deletes a specific point record from the TAMS_TOA_PointNo table for a given TOAID.

### Parameters
| Name      | Type   | Purpose |
| :-------- | :----- | :------ |
| @pointid  | BIGINT | Identifier of the point to delete. |
| @TOAID    | BIGINT | Identifier of the TOA record to which the point belongs. |
| @Message  | NVARCHAR(500) OUTPUT | Status message indicating success or error. |

### Logic Flow
1. Initialize a flag `@IntrnlTrans` to 0, indicating no internal transaction has been started yet.  
2. If the procedure is called outside an existing transaction (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Clear the output message (`@Message = ''`).  
4. Attempt to delete the row from `TAMS_TOA_PointNo` where `TOAId` matches `@TOAID` and `Id` matches `@pointid`.  
5. If the delete operation fails (`@@ERROR <> 0`), set an error message, print a diagnostic string, and jump to the error handling section (`TRAP_ERROR`).  
6. If the delete succeeds, exit the TRY block normally.  
7. In the CATCH block, capture the error details, re‑raise the error with `RAISERROR`, and allow the flow to continue to the exit label.  
8. At the `FORCE_EXIT_PROC` label, if an internal transaction was started, commit it. Return the message.  
9. At the `TRAP_ERROR` label, if an internal transaction was started, roll it back. Return the message.

### Data Interactions
* **Reads:** *None*  
* **Writes:** Deletes from `TAMS_TOA_PointNo`  

---