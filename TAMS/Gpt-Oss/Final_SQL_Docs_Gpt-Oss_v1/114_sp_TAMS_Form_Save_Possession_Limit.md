# Procedure: sp_TAMS_Form_Save_Possession_Limit

### Purpose
Insert a new possession limit record when one with the same identifiers does not already exist.

### Parameters
| Name                     | Type          | Purpose |
| :---                     | :---          | :--- |
| @TypeOfProtectionLimit   | NVARCHAR(50)  | Protection type to be stored; trimmed of surrounding spaces. |
| @RedFlashingLampsLoc     | NVARCHAR(50)  | Location of red flashing lamps; trimmed of surrounding spaces. |
| @PossID                  | BIGINT        | Identifier of the possession to which the limit applies. |
| @Message                 | NVARCHAR(500) | Output message indicating success or error; defaults to NULL. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If no outer transaction is active (`@@TRANCOUNT = 0`), set the flag to 1 and begin a new transaction.  
3. Count rows in `TAMS_Possession_Limit` where `PossessionId` equals `@PossID`, `TypeOfProtectionLimit` equals the trimmed `@TypeOfProtectionLimit`, and `RedFlashingLampsLoc` equals the trimmed `@RedFlashingLampsLoc`.  
4. If the count is zero, insert a new row into `TAMS_Possession_Limit` with the supplied values (trimmed).  
5. If an error occurs during the insert, set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. If the flag indicates an internally started transaction, commit it.  
7. Return the value of `@Message`.  
8. In the error handling section, if the flag indicates an internally started transaction, roll it back, then return `@Message`.

### Data Interactions
* **Reads:** `TAMS_Possession_Limit` (via SELECT COUNT).  
* **Writes:** `TAMS_Possession_Limit` (INSERT).