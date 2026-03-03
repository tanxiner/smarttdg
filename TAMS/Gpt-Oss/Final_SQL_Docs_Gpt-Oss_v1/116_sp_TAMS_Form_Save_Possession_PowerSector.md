# Procedure: sp_TAMS_Form_Save_Possession_PowerSector

### Purpose
Insert a new possession power sector record when one does not already exist for the given possession ID and power sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PowerSector | NVARCHAR(4000) | Power sector value to be stored, trimmed of surrounding spaces. |
| @NoOFSCD | INT | Numeric flag indicating the number of OFSCDs. |
| @BreakerOut | NVARCHAR(5) | Indicator ('Y' or other) that is converted to a bit value for storage. |
| @PossID | BIGINT | Identifier of the possession to which the power sector belongs. |
| @Message | NVARCHAR(500) OUTPUT | Receives an error message if the insert fails; otherwise remains NULL. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set `@IntrnlTrans` to 1 and begin a new transaction.  
3. Check whether a record already exists in `TAMS_Possession_PowerSector` with the supplied `@PossID` and trimmed `@PowerSector`.  
4. If no such record exists, insert a new row with the supplied values, converting `@BreakerOut` to 1 when it equals 'Y', otherwise 0.  
5. If the insert operation generates an error (`@@ERROR <> 0`), set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. On normal completion, if a transaction was started internally, commit it and return `@Message`.  
7. In the error handling section, if a transaction was started internally, roll it back and return `@Message`.

### Data Interactions
* **Reads:** `TAMS_Possession_PowerSector` (COUNT query)  
* **Writes:** `TAMS_Possession_PowerSector` (INSERT)  

---