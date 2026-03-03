# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20230712

### Purpose
Generate a summary of TAR and TOA counts and cancellation lists for a specified line, track type, and access date, returning the results or an error if the requested date is not yet available.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line (e.g., NEL) |
| @TrackType | NVARCHAR(50) | Type of track to filter records |
| @StrAccDate | NVARCHAR(20) | Access date string in DD/MM/YYYY format |

### Logic Flow
1. Capture the current system date and time.  
2. Retrieve the operation cut‑off time for the supplied line and track type from **TAMS_Parameters**.  
3. If the current time is earlier than the cut‑off, set the effective access date to the previous day; otherwise use the current day.  
4. Convert the supplied string date to a DATE value.  
5. If the effective access date is earlier than the supplied date, return a single row with `ErrStr = 'Err'` to indicate the report is not ready.  
6. Otherwise, initialize all counters and string accumulators to zero or empty.  
7. Count TAR records that match the access date, line, track type, possession/protection type, power‑off flag, and status (status 9 for NEL, otherwise 8). Store these counts in `@TARPossCtr` and `@TARProtCtr`.  
8. Count TOA records that join with TAR on `TARId` and satisfy the same filters, storing results in `@TOAPossCtr` and `@TOAProtCtr`.  
9. Build a list of TAR numbers for protection records that have no corresponding TOA record with a non‑zero status, using a cursor. Increment `@CancelProtCtr` and concatenate the TAR numbers into `@CancelProt`.  
10. Build a similar list for possession records, updating `@CancelPossCtr` and `@CancelPoss`.  
11. Count extended possession records where the linked TOA status is 3 or 4 with a surrender time later than 04:00, storing in `@ExtPossCtr`.  
12. Count extended protection records with the same TOA status and surrender time criteria, storing in `@ExtProtCtr`.  
13. Return a single row containing all counters and the two cancellation strings.

### Data Interactions
* **Reads:**  
  - TAMS_Parameters  
  - TAMS_TAR  
  - TAMS_TOA  

* **Writes:** None

---