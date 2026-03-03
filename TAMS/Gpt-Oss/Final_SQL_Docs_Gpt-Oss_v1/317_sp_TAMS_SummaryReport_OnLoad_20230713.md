# Procedure: sp_TAMS_SummaryReport_OnLoad_20230713

### Purpose
Generate a summary of TAR and TOA activity for a specified line and access date, including counts of possessions, protections, cancellations, and external cases, and return the results as a single row.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line (e.g., NEL) for which the report is generated. |
| @StrAccDate | NVARCHAR(20) | Access date in string format (dd/MM/yyyy) to be used as the reference day for the report. |

### Logic Flow
1. **Initialize dates and times**  
   - Capture the current system date and time.  
   - Convert the current time to a TIME value for comparison.

2. **Determine the cutoff time**  
   - Query `TAMS_Parameters` for the parameter `OpDateCutOffTime` that matches the supplied line.  
   - Store the returned time in `@CutOff`.

3. **Select the effective access date**  
   - If the current time is earlier than the cutoff, set `@AccessDate` to the previous calendar day.  
   - Otherwise, set `@AccessDate` to the current day.

4. **Validate the requested access date**  
   - Convert `@StrAccDate` to a DATE value.  
   - If this date is earlier than `@AccessDate`, return a single column row with the string `'Err'` to indicate the report is not ready for that date.

5. **Initialize counters and string accumulators**  
   - Set all numeric counters (`@TARPossCtr`, `@TARProtCtr`, `@TOAPossCtr`, `@TOAProtCtr`, `@CancelPossCtr`, `@CancelProtCtr`, `@ExtPossCtr`, `@ExtProtCtr`) to zero.  
   - Set the cancellation string variables (`@CancelPoss`, `@CancelProt`) to empty.

6. **Count TAR possessions**  
   - Count rows in `TAMS_TAR` where `AccessDate` matches the requested date, `AccessType` is `'Possession'`, `PowerOn` is 0, `TARStatusId` is 9 for NEL or 8 otherwise, and `Line` matches the supplied line.  
   - Store the result in `@TARPossCtr`.

7. **Count TAR protections**  
   - Same criteria as step 6 but with `AccessType` `'Protection'`.  
   - Store the result in `@TARProtCtr`.

8. **Count TOA possessions**  
   - Join `TAMS_TAR` and `TAMS_TOA` on `TARId`.  
   - Apply the same filters as step 6 and additionally require `a.Id = b.TARId`.  
   - Store the result in `@TOAPossCtr`.

9. **Count TOA protections**  
   - Same as step 8 but with `AccessType` `'Protection'`.  
   - Store the result in `@TOAProtCtr`.

10. **Build list of cancelled protections**  
    - Open a cursor over distinct `TARNo` values from `TAMS_TAR` where the record is a protection, has no matching TOA record with a non‑zero status, and meets the same filters as earlier steps.  
    - For each fetched row, increment `@CancelProtCtr` and append the `TARNo` to `@CancelProt`, separating entries with `; `.

11. **Build list of cancelled possessions**  
    - Repeat the cursor logic of step 10 but for `AccessType` `'Possession'`.  
    - Increment `@CancelPossCtr` and build `@CancelPoss`.

12. **Count external possessions**  
    - Join `TAMS_TAR` and `TAMS_TOA` as in step 8.  
    - Add a condition that `TOAStatus` is 3 or (4 and the surrender time is after 04:00).  
    - Store the count in `@ExtPossCtr`.

13. **Count external protections**  
    - Same as step 12 but with `AccessType` `'Protection'`.  
    - Store the count in `@ExtProtCtr`.

14. **Return the result set**  
    - Output a single row containing all counter values and the two cancellation string columns.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TOA`

* **Writes:**  
  - None

---