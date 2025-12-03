# Procedure: sp_TAMS_Form_Save_Possession_OtherProtection

### Purpose
Adds a new OtherProtection entry for a specified possession when that entry does not already exist.

### Parameters
| Name          | Type          | Purpose |
| :---          | :---          | :--- |
| @OtherProtection | NVARCHAR(50) | The protection value to associate with the possession. |
| @PossID          | BIGINT       | Identifier of the possession to which the protection is added. |
| @Message         | NVARCHAR(500) OUTPUT | Receives a status message indicating success or error. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0, indicating no internal transaction has been started yet.  
2. If the procedure is called outside an existing transaction (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Query the `TAMS_Possession_OtherProtection` table to count rows where `PossessionId` equals `@PossID` and `OtherProtection` equals the trimmed value of `@OtherProtection`.  
4. If the count is zero, insert a new row into `TAMS_Possession_OtherProtection` with the provided `@PossID` and trimmed `@OtherProtection`.  
5. After the insert attempt, check `@@ERROR`. If an error occurred, set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. If no error, and an internal transaction was started, commit the transaction.  
7. Return the value of `@Message`.  
8. In the error handling section, if an internal transaction was started, roll it back, then return `@Message`.

### Data Interactions
* **Reads:** `TAMS_Possession_OtherProtection` (count query)  
* **Writes:** `TAMS_Possession_OtherProtection` (insert)