# Procedure: sp_TAMS_Form_Save_Possession_WorkingLimit

### Purpose
Persist a working‑limit record for a possession, inserting it only if a record with the same PossessionId and RedFlashingLampsLoc does not already exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location identifier for the flashing lamps; trimmed of surrounding spaces before use. |
| @PossID | BIGINT | The identifier of the possession to which the working limit applies. |
| @Message | NVARCHAR(500) OUTPUT | Returns a status message; set to an error string if the insert fails. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If no outer transaction is active (`@@TRANCOUNT = 0`), set the flag to 1 and begin a new transaction.  
3. Query `TAMS_Possession_WorkingLimit` to count rows where `PossessionId` equals `@PossID` and `RedFlashingLampsLoc` equals the trimmed value of `@RedFlashingLampsLoc`.  
4. If the count is zero, perform an `INSERT` into `TAMS_Possession_WorkingLimit` with the supplied `@PossID` and trimmed `@RedFlashingLampsLoc`.  
5. After the insert, check `@@ERROR`. If an error occurred, set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. If no error, commit the transaction if it was started internally (`@IntrnlTrans = 1`).  
7. Return the (possibly empty) `@Message`.  
8. In the error handling section, roll back the transaction if it was started internally and return the error message.

### Data Interactions
* **Reads:** `TAMS_Possession_WorkingLimit` (count query)  
* **Writes:** `TAMS_Possession_WorkingLimit` (insert)  

---