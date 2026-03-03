# Procedure: sp_TAMS_SummaryReport_OnLoad_20240112_M

### Purpose
Generate a summary of TAR (Transport Asset Record) statuses for a specified line, track type, and access date, returning counts and comma‑separated lists for each status category.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target line identifier (e.g., DTL, NEL). |
| @TrackType | NVARCHAR(50) | Target track type. |
| @StrAccDate | NVARCHAR(20) | Access date in DD/MM/YYYY format. |

### Logic Flow
1. **Current timestamp capture** – Retrieve current date and time; determine the operational cut‑off time from `TAMS_Parameters` for the supplied line and track type.  
2. **Access date calculation** – If the current time is before the cut‑off, set the access date to the previous day; otherwise use the current day.  
3. **Date validation** – Compare the calculated access date with the supplied `@StrAccDate`. If the access date is earlier, return an error string; otherwise proceed.  
4. **Initialize counters and lists** – For each status category (Booked, Executed, Not Executed, Cancelled, Extended) and for both possession and protection types, set counters to zero and list strings to empty.  
5. **Booked (Possession & Protection)** –  
   * Open a cursor over `TAMS_TAR` filtered by access date, access type, line, track type, and status ID (8 for DTL, 9 for NEL).  
   * For each distinct TAR number, increment the counter and append the number to the list string, separated by semicolons.  
6. **Executed (Possession & Protection)** –  
   * Open a cursor over joined `TAMS_TAR` and `TAMS_TOA` where the TOA status is 4 or 5 (surrendered or acknowledged).  
   * Count and list distinct TAR numbers as in step 5.  
7. **Not Executed (Possession & Protection)** –  
   * Open a cursor over `TAMS_TAR` where no corresponding TOA record exists with a non‑zero status.  
   * Count and list distinct TAR numbers.  
8. **Cancelled (Possession & Protection)** –  
   * Open a cursor over joined `TAMS_TAR` and `TAMS_TOA` where the TOA status is 6 (cancelled).  
   * Count and list distinct TAR numbers.  
9. **Extended (Possession & Protection)** –  
   * Open a cursor over joined `TAMS_TAR` and `TAMS_TOA` where the TOA status is 4 or 5 and the surrender time is after 04:00:00.  
   * Count and list distinct TAR numbers.  
10. **Return results** – Output all counters and list strings as a single result set.

### Data Interactions
* **Reads:** `TAMS_Parameters`, `TAMS_TAR`, `TAMS_TOA`
* **Writes:** None

---