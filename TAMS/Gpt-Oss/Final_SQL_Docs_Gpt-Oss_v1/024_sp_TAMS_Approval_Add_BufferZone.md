# Procedure: sp_TAMS_Approval_Add_BufferZone

### Purpose
Adds a buffer zone sector to a TAR record when the sector is not already linked.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @TARID    | BIGINT        | Identifier of the TAR to which the buffer zone will be added. |
| @SectorID | BIGINT        | Identifier of the sector to be added as a buffer zone. |
| @Message  | NVARCHAR(500) | Output message indicating success or error. |

### Logic Flow
1. Initialise a flag `@IntrnlTrans` to 0.  
2. If no active transaction exists (`@@TRANCOUNT = 0`), set the flag to 1 and begin a new transaction.  
3. Check whether a record already exists in `TAMS_TAR_Sector` for the supplied `@TARID` and `@SectorID`.  
4. If no such record exists:  
   a. Retrieve the `Line` value from `TAMS_TAR` for the given `@TARID`.  
   b. Look up the `ColourCode` in `TAMS_Type_Of_Work` where `Line` matches the retrieved line, `TypeOfWork` is `'Buffer Zone'`, and the record is active.  
   c. Insert a new row into `TAMS_TAR_Sector` with `TARId = @TARID`, `SectorId = @SectorID`, `IsBuffer = 1`, the retrieved colour code, and `IsAddedBuffer = 1`.  
5. If any error occurs during the insert, set `@Message` to `'ERROR INSERTING INTO TAMS_TAR'` and jump to the error handling section.  
6. On successful completion, commit the transaction if it was started internally and return the message.  
7. In the error handling section, rollback the transaction if it was started internally and return the message.

### Data Interactions
* **Reads:** `TAMS_TAR_Sector`, `TAMS_TAR`, `TAMS_Type_Of_Work`, `TAMS_Sector`  
* **Writes:** `TAMS_TAR_Sector`