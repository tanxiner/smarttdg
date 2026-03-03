# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters

### Purpose
Retrieve a list of stations and their TVF acknowledgement status for a specified line, operation date and access date, optionally calculating direction flags when no acknowledgements exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user invoking the procedure (unused in logic). |
| @Line | nvarchar(10) | Line identifier; only 'DTL' is processed. |
| @TrackType | nvarchar(50) | Filter for track type when building TVF data. |
| @OperationDate | date | Date of the operation to match acknowledgements. |
| @AccessDate | date | Date of the access to match acknowledgements. |

### Logic Flow
1. **Initial Setup**  
   - Declare variables for counting acknowledgements and holding TVF attributes.  
   - Create four temporary tables: `#TMP_Station`, `#TMP_TVF`, `#TMP_TVF_ToUpdate`, and `#TMP_OCCTVF_Ack`.

2. **Process Only for Line 'DTL'**  
   - If `@Line` equals 'DTL', continue; otherwise the procedure ends after dropping temp tables.

3. **Check Existing Acknowledgements**  
   - Count rows in `TAMS_TVF_Acknowledge` where `AccessDate` equals `@AccessDate`.  
   - If the count is zero, the procedure must compute direction flags; otherwise it simply retrieves existing data.

4. **When No Acknowledgements Exist**  
   a. **Prepare TVF Data**  
      - Truncate `#TMP_TVF_ToUpdate`.  
      - Insert into `#TMP_TVF` all records from `TAMS_TAR` joined with `TAMS_TAR_TVF` where `AccessDate` matches `@AccessDate`, `TrackType` matches `@TrackType`, and `TVFMode` is not null or 'N.A.'.  
   b. **Cursor Loop to Build Direction Flags**  
      - Open a cursor over `#TMP_TVF` ordered by `TVFStationId` and `TVFMode`.  
      - For each row, if the station is not yet in `#TMP_TVF_ToUpdate`, insert a new record with `TVFDirection1` or `TVFDirection2` set according to `TVFDirection` ('XB' or 'BB').  
      - If the station already exists, update its `TVFMode` and adjust direction bits: for 'Emergency' mode set both bits appropriately; for other modes set only the bit corresponding to the current direction.  
   c. **Load Station List**  
      - Insert into `#TMP_Station` all active stations on line 'DTL' with `IsStation = 1`, ordering by `[Order]`.  
   d. **Build Acknowledgement Result Set**  
      - Insert into `#TMP_OCCTVF_Ack` a row for each station, right‑joining `TAMS_TVF_Acknowledge` on `StationId`, `OperationDate`, and `AccessDate`.  
      - Populate fields such as `AcknowledgedBy`, `OperatedBy`, and `VerifiedBy` by selecting the user name from `TAMS_User`.  
      - Generate a sequential `SNO` using `ROW_NUMBER`.  
   e. **Apply Calculated Flags**  
      - Update `#TMP_OCCTVF_Ack` rows with the direction bits and mode from `#TMP_TVF_ToUpdate` where station IDs match.  
   f. **Return Result**  
      - Select all rows from `#TMP_OCCTVF_Ack` to return to the caller.

5. **When Acknowledgements Exist**  
   - Load the station list into `#TMP_Station` as in step 4c.  
   - Build `#TMP_OCCTVF_Ack` by right‑joining `TAMS_TVF_Acknowledge` to the station list, populating user names and generating `SNO`.  
   - Return the ordered result set by `StationId`.

6. **Cleanup**  
   - Drop all temporary tables: `#TMP_Station`, `#TMP_OCCTVF_Ack`, and `#TMP_TVF_ToUpdate`.

### Data Interactions
* **Reads:**  
  - `TAMS_TVF_Acknowledge`  
  - `TAMS_TAR`  
  - `TAMS_TAR_TVF`  
  - `TAMS_Station`  
  - `TAMS_User`

* **Writes:**  
  - None to permanent tables; all writes are to temporary tables created within the procedure.