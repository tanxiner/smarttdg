# Procedure: sp_TAMS_Block_Date_Delete

### Purpose
Deletes a TARDate record identified by @BlockID while archiving the original row in the audit table.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @BlockID  | INTEGER       | Identifier of the TARDate row to delete |
| @Message  | NVARCHAR(500) | Output message indicating success or error |

### Logic Flow
1. Initialize @IntrnlTrans to 0.  
2. If no active transaction exists, set @IntrnlTrans to 1 and begin a new transaction.  
3. Clear @Message.  
4. Insert a copy of the target row into TAMS_Block_TARDate_Audit, prefixing the record with an empty string, the current date, and the action code 'D'.  
5. Delete the row from TAMS_Block_TARDate where ID equals @BlockID.  
6. If an error occurs during the insert or delete, set @Message to 'ERROR DELETING TAMS_BLOCK_TARDATE' and jump to the error handling section.  
7. If the procedure started its own transaction, commit it.  
8. Return @Message.  
9. Error handling: if a transaction was started internally, roll it back, then return @Message.

### Data Interactions
* **Reads:** TAMS_Block_TARDate  
* **Writes:** TAMS_Block_TARDate_Audit (INSERT), TAMS_Block_TARDate (DELETE)