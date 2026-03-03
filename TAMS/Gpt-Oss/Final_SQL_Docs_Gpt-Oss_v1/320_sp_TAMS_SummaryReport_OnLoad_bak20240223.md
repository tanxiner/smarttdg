# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20240223

### Purpose
Generate a summary of TAR and TOA counts, cancellation lists, and extended counts for a specified line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line (e.g., DTL, NEL). |
| @TrackType | NVARCHAR(50) | Type of track to filter records. |
| @StrAccDate | NVARCHAR(20) | String representation of the target access date (format 103). |

### Logic Flow
1. **Current Date/Time Capture**  
   - Retrieve the current date and time.  
   - Convert the current time to a TIME value for comparison.

2. **Determine Access Date**  
   - Query `TAMS_Parameters` for the cutoff time (`ParaTime`) that matches the supplied line and track type.  
   - If the current time is earlier than the cutoff, set `@AccessDate` to the previous calendar day; otherwise, set it to today.

3. **Validate Requested Date**  
   - Convert `@StrAccDate` to a DATE.  
   - If `@AccessDate` is earlier than this date, return a single row with `ErrStr = 'Err'` to indicate the report is not ready.

4. **Initialize Counters and Strings**  
   - Set all numeric counters (`@TARPossCtr`, `@TARProtCtr`, `@TOAPossCtr`, `@TOAProtCtr`, `@CancelPossCtr`, `@CancelProtCtr`, `@ExtPossCtr`, `@ExtProtCtr`) to zero.  
   - Set cancellation strings (`@CancelPoss`, `@CancelProt`) to empty.

5. **Count TAR Records**  
   - Count records in `TAMS_TAR` where `AccessDate` matches the target date, `AccessType` is 'Possession', line conditions (`PowerOn` or `NEL`), status id based on line, and matching line and track type. Store in `@TARPossCtr`.  
   - Repeat the same logic for `AccessType` 'Protection' and store in `@TARProtCtr`.

6. **Count TOA Records**  
   - Join `TAMS_TAR` with `TAMS_TOA` on `Id = TARId`.  
   - Count records where `AccessType` is 'Possession' and store in `@TOAPossCtr`.  
   - Count records where `AccessType` is 'Protection' and store in `@TOAProtCtr`.

7. **Build Cancellation Lists**  
   - **Protection Cancellations**:  
     - Open a cursor over distinct `TAMS_TAR` records with `AccessType` 'Protection' that have no related `TAMS_TOA` record with `TOAStatus <> 0`.  
     - For each record, increment `@CancelProtCtr` and append the `TARNo` to `@CancelProt`, separating entries with '; '.  
   - **Possession Cancellations**:  
     - Repeat the same cursor logic for `AccessType` 'Possession', updating `@CancelPossCtr` and `@CancelPoss`.

8. **Count Extended Records**  
   - Count `TAMS_TAR` joined with `TAMS_TOA` where `TOAStatus` is 3 or (status 4 and `SurrenderTime` later than 04:00:00). Store in `@ExtPossCtr`.  
   - Repeat the same logic for `AccessType` 'Protection' and store in `@ExtProtCtr`.

9. **Return Result Set**  
   - Output all counters and cancellation strings as a single row:  
     `TARPossCtr, TARProtCtr, TOAPossCtr, TOAProtCtr, CancelPossCtr, CancelProtCtr, CancelPoss, CancelProt, ExtPossCtr, ExtProtCtr`.

### Data Interactions
* **Reads:** `TAMS_Parameters`, `TAMS_TAR`, `TAMS_TOA`
* **Writes:** None

---