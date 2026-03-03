# Procedure: sp_TAMS_OCC_GetOCCTVFAckFromTableByParameters

### Purpose
Retrieves and prepares a list of TVF acknowledgements for a specified line, operation date and access date, applying direction and mode logic for the DTL line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Unused in current logic |
| @Line | nvarchar(10) | Determines if special DTL processing is applied |
| @OperationDate | date | Filters acknowledgements by operation date |
| @AccessDate | date | Filters acknowledgements by access date |

### Logic Flow
1. **Initialize** temporary tables for stations, TVF data, update candidates, and acknowledgement output.  
2. **If** @Line equals 'DTL':  
   1. Count rows in `TAMS_TVF_Acknowledge` where `AccessDate` matches @AccessDate.  
   2. **If** count is zero (no acknowledgements yet):  
      1. Truncate the update candidate table.  
      2. Populate the TVF temp table with records from `TAMS_TAR` joined to `TAMS_TAR_TVF` where `AccessDate` matches and `TVFMode` is defined.  
      3. Iterate over the TVF temp table with a cursor, building the update candidate table:  
         - For each unique station/mode, insert a row with direction bits set according to `TVFDirection` ('XB' sets bit1, 'BB' sets bit2).  
         - If the station/mode already exists, update its mode and adjust direction bits; emergency mode updates both bits, congestion mode updates only the relevant bit.  
      4. Load active DTL stations into the station temp table.  
      5. Insert acknowledgement rows into the output temp table by joining `TAMS_TVF_Acknowledge` with the station table, converting user IDs to names, and ordering by TVF ID.  
      6. Update the output temp table with direction and mode values from the update candidate table.  
      7. Return the populated output temp table.  
   3. **Else** (acknowledgements already exist):  
      1. Load active DTL stations into the station temp table.  
      2. Insert acknowledgement rows into the output temp table as in step 2.2.5.  
      3. Return the output temp table ordered by StationId.  
3. **Drop** all temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_TVF_Acknowledge`  
  - `TAMS_TAR`  
  - `TAMS_TAR_TVF`  
  - `TAMS_Station`  
  - `TAMS_User`  

* **Writes:**  
  - Temporary tables `#TMP_Station`, `#TMP_TVF`, `#TMP_TVF_ToUpdate`, `#TMP_OCCTVF_Ack` (insert, update, truncate)  

---