# Procedure: sp_TAMS_SummaryReport_OnLoad

### Purpose
Generate summary counts of TAR records for a specified line, track type, and access date, categorised by possession/protection status and execution state.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., DTL, NEL) |
| @TrackType | NVARCHAR(50) | Track type filter |
| @StrAccDate | NVARCHAR(20) | Access date string in DD/MM/YYYY format |

### Logic Flow
1. **Current timestamp** – Capture today’s date and time.  
2. **Cut‑off retrieval** – Query `TAMS_Parameters` for `ParaTime` where `ParaCode='OpDateCutOffTime'` and the supplied line and track type.  
3. **Determine access date** –  
   * If current time is earlier than the cut‑off, set `@AccessDate` to yesterday.  
   * Otherwise set it to today.  
4. **Validate requested date** – Convert `@StrAccDate` to a date.  
   * If `@AccessDate` is earlier than this date, return a single row with `ErrStr='Err'`.  
   * Otherwise proceed.  
5. **Initialize counters and list variables** for each category (Booked, Executed, Not Executed, Cancelled, Extended).  
6. **Booked – Possession** –  
   * Cursor over distinct `TARNo` from `TAMS_TAR` where `AccessDate` matches, `AccessType='Possession'`, line and track type match, status id depends on line, and `PowerOn` condition for DTL.  
   * Increment `@TARPossCtr` and build a semicolon‑separated list `@TARPoss`.  
7. **Booked – Protection** – Same cursor logic with `AccessType='Protection'`, updating `@TARProtCtr` and `@TARProt`.  
8. **Executed – Possession** –  
   * Cursor over `TAMS_TAR` joined with `TAMS_TOA` where `TOAStatus` is 4 or 5 (surrendered or acknowledged).  
   * Update `@TOAPossCtr` and `@TOAPoss`.  
9. **Executed – Protection** – Same join logic with `AccessType='Protection'`, updating `@TOAProtCtr` and `@TOAProt`.  
10. **Not Executed – Protection** –  
    * Cursor over `TAMS_TAR` where no matching `TAMS_TOA` record exists with `TOAStatus` ≠ 0.  
    * Update `@TOAProtNotExecCtr` and `@TOAProtNotExec`.  
11. **Not Executed – Possession** – Same logic as step 10 but with `AccessType='Possession'`, updating `@TOAPossNotExecCtr` and `@TOAPossNotExec`.  
12. **Cancelled – Possession** –  
    * Cursor over `TAMS_TAR` joined with `TAMS_TOA` where `TOAStatus=6`.  
    * Update `@CancelPossCtr` and `@CancelPoss`.  
13. **Cancelled – Protection** – Same join logic with `AccessType='Protection'`, updating `@CancelProtCtr` and `@CancelProt`.  
14. **Extended – Possession** –  
    * Cursor over `TAMS_TAR` joined with `TAMS_TOA` where `TOAStatus` is 4 or 5 and `SurrenderTime` is after 04:00:00.  
    * Update `@ExtPossCtr` and `@ExtPoss`.  
15. **Extended – Protection** – Same join logic with `AccessType='Protection'`, updating `@ExtProtCtr` and `@ExtProt`.  
16. **Return result** – Select the counters for all categories; list columns are returned as empty strings.

### Data Interactions
* **Reads:** `TAMS_Parameters`, `TAMS_TAR`, `TAMS_TOA`  
* **Writes:** None

---