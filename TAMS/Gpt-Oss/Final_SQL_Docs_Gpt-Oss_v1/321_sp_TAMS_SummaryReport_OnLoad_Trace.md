# Procedure: sp_TAMS_SummaryReport_OnLoad_Trace

### Purpose
Generate a daily summary of TAR and TOA activity for a specified line, including counts of possessions, protections, cancellations, and external transfers, and return the results.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line (e.g., NEL) for which the report is generated. |
| @StrAccDate | NVARCHAR(20) | Access date in string format (dd/MM/yyyy) for which the report is requested. |

### Logic Flow
1. **Initialize dates and times**  
   - Capture the current system date (`@CurDate`) and time (`@CurTime`).  
   - Retrieve the operation cut‑off time (`@CutOff`) for the requested line from `TAMS_Parameters`.  
   - Determine the effective access date (`@AccessDate`): if the current time is before the cut‑off, use the previous day; otherwise use the current day.

2. **Validate requested date**  
   - Convert `@StrAccDate` to a date.  
   - If the requested date is earlier than `@AccessDate`, return a single row with `ErrStr = 'Err'` to indicate the report is not ready.

3. **Initialize counters and strings**  
   - Set all count variables (`@TARPossCtr`, `@TARProtCtr`, `@TOAPossCtr`, `@TOAProtCtr`, `@CancelPossCtr`, `@CancelProtCtr`, `@ExtPossCtr`, `@ExtProtCtr`) to zero.  
   - Set cancellation strings (`@CancelPoss`, `@CancelProt`) to empty.

4. **Count TAR records**  
   - Count TAR possessions where `AccessType = 'Possession'`, `PowerOn = 0`, status matches line rule, and `Line = @Line`.  
   - Count TAR protections with the same filters but `AccessType = 'Protection'`.

5. **Count TOA records linked to TAR**  
   - Count TOA possessions by joining `TAMS_TAR` and `TAMS_TOA` on `TARId`, applying the same filters.  
   - Count TOA protections similarly.

6. **Build cancellation lists**  
   - **Protection cancellations**:  
     - Open a cursor over distinct TAR IDs and numbers where the record is a protection, not linked to any TOA with a non‑zero status.  
     - For each row, increment `@CancelProtCtr` and append the TAR number to `@CancelProt`, separating entries with `; `.  
   - **Possession cancellations**:  
     - Repeat the same cursor logic for possession records, updating `@CancelPossCtr` and `@CancelPoss`.

7. **Count external transfers**  
   - Count possessions where the linked TOA status is 3 or (status 4 and surrender time after 04:00).  
   - Count protections with the same external transfer criteria.

8. **Return results**  
   - Output all counters and the two cancellation strings as columns in a single result set.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TOA`

* **Writes:**  
  - None

---