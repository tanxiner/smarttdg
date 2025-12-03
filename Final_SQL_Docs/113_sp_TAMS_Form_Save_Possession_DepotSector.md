# Procedure: sp_TAMS_Form_Save_Possession_DepotSector

### Purpose
Persist a new depot sector record for a possession when it does not already exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sector | NVARCHAR(4000) | The sector identifier to be stored. |
| @PowerOff | INT | Flag indicating power status (0 or 1). |
| @NoOFSCD | INT | Numeric code for OFSCD status. |
| @BreakerOut | NVARCHAR(5) | Indicator ('Y' or other) that is converted to a binary flag. |
| @PossID | BIGINT | Identifier of the possession to which the sector belongs. |
| @Message | NVARCHAR(500) OUTPUT | Returns a status message; set to an error string if insertion fails. |

### Logic Flow
1. Initialise a local flag `@IntrnlTrans` to 0.  
2. If the procedure is not already running inside a transaction (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Count rows in `TAMS_Possession_DepotSector` where `PossessionId` equals `@PossID` and `Sector` equals the trimmed value of `@Sector`.  
4. If the count is zero, insert a new row into `TAMS_Possession_DepotSector` with the supplied values, converting `@BreakerOut` to 1 when it equals 'Y', otherwise 0.  
5. After the insert attempt, check `@@ERROR`. If an error occurred, set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. If no error, and if a transaction was started internally (`@IntrnlTrans = 1`), commit the transaction.  
7. Return the value of `@Message` (which will be NULL on success).  
8. In the error handling section, if a transaction was started internally, roll it back, then return `@Message`.

### Data Interactions
* **Reads:** `TAMS_Possession_DepotSector` (count query)  
* **Writes:** `TAMS_Possession_DepotSector` (insert)