# Procedure: sp_TAMS_Form_Delete_Temp_Attachment

### Purpose
Deletes a temporary attachment record identified by TARId and TARAccessReqId from TAMS_TAR_Attachment_Temp.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | Identifier of the TAR record to delete |
| @TARAccessReqId | INTEGER | Identifier of the access request linked to the TAR record |

### Logic Flow
1. Initialise a return variable `@ret` as an empty string.  
2. Begin a TRY block and start a database transaction.  
3. Execute a DELETE statement that removes rows from `TAMS_TAR_Attachment_Temp` where `TARId` equals `@TARId` and `TARAccessReqId` equals `@TARAccessReqId`.  
4. Commit the transaction if the DELETE succeeds.  
5. If any error occurs, the CATCH block prints a message, returns the error number and message, rolls back the transaction, and sets `@ret` to the string `'Errror'`.  
6. Finally, return the value of `@ret` as `ReturnValue`.

### Data Interactions
* **Reads:** *none*  
* **Writes:** `TAMS_TAR_Attachment_Temp` (DELETE)