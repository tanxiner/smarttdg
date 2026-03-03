# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters_Preview

### Purpose
Retrieves a preview of TVF acknowledgement records for the DTL line on a specified operation and access date, mapping station codes to names and translating user IDs to names.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user invoking the procedure (unused in current logic). |
| @Line | nvarchar(10) | Target line; only 'DTL' triggers processing. |
| @TrackType | nvarchar(50) | Track type filter (unused in current logic). |
| @OperationDate | date | Date of the operation to filter acknowledgements. |
| @AccessDate | date | Date of access to filter acknowledgements. |

### Logic Flow
1. Declare local variables for acknowledgement count and TVF attributes.  
2. Create three temporary tables: `#TMP_Station`, `#TMP_TVF`, and `#TMP_TVF_ToUpdate`.  
3. Create `#TMP_OCCTVF_Ack` to hold the final result set.  
4. If `@Line` equals 'DTL':  
   1. Count rows in `TAMS_TVF_Acknowledge` where `OperationDate` matches `@OperationDate`.  
   2. If the count is greater than zero:  
      1. Populate `#TMP_Station` with active DTL stations, concatenating `stationcode` and `StationName`.  
      2. Insert into `#TMP_OCCTVF_Ack` a row for each station, using a right join to include stations even when no acknowledgement exists for the given dates.  
         - `SNO` is a row number ordered by `tvf.ID`.  
         - `ID`, `AccessDate`, `OperationDate`, `TVFDirection1`, `TVFDirection2`, `TVFMode`, `TVFOnTime`, `AcknowledgedOn`, `VerifiedOn` are taken directly from `TAMS_TVF_Acknowledge`.  
         - `StationId` and `StationName` come from `#TMP_Station`.  
         - `AcknowledgedBy`, `OperatedBy`, and `VerifiedBy` are resolved to user names via sub‑queries on `TAMS_User`.  
      3. Return the contents of `#TMP_OCCTVF_Ack` ordered by `StationId`.  
5. Drop the temporary tables `#TMP_Station`, `#TMP_OCCTVF_Ack`, and `#TMP_TVF_ToUpdate` (the latter is never populated).

### Data Interactions
* **Reads:**  
  - `TAMS_TVF_Acknowledge`  
  - `TAMS_Station`  
  - `TAMS_User`  

* **Writes:**  
  - Temporary tables: `#TMP_Station`, `#TMP_TVF`, `#TMP_TVF_ToUpdate`, `#TMP_OCCTVF_Ack` (no permanent tables are modified).