# Procedure: sp_TAMS_Depot_TOA_QTS_Chk

### Purpose
Determine whether a person identified by NRIC holds a valid qualification for a specified line on a given date, returning the qualification status along with related details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | NRIC of the person to evaluate |
| @qualdate | NVARCHAR(20) | Date to test qualification validity (format DD/MM/YYYY) |
| @line | NVARCHAR(20) | Rail line identifier for which the qualification is checked |
| @QualCode | NVARCHAR(50) | Qualification code to filter on |

### Logic Flow
1. Initialise counters and a return value placeholder.  
2. Create a temporary table `#tmpqtsqc` to hold decrypted access data and validity periods.  
3. Retrieve the person's name from `QTS_Personnel` where the decrypted access ID matches `@nric`.  
4. Populate `#tmpqtsqc` with qualification records that match the supplied line and qualification code, decrypting the access ID and calculating any suspension end date.  
5. Count how many qualification rows were inserted.  
   * If zero, set `@QualStatus` to **InValid**.  
   * If one or more, fetch the first row’s dates into local variables.  
6. If a suspension end date exists (not null and not the default 1900‑01‑01), set `@QualStatus` to **InValid**.  
7. Otherwise, compare the supplied `@qualdate` (converted to DATETIME) against the qualification’s valid‑access and valid‑till dates.  
   * If the date is earlier than both, set `@QualStatus` to **Valid**.  
   * Otherwise, set it to **InValid**.  
8. Return a single row containing the NRIC, name, line, qualification date, qualification code, and the determined status.  
9. Drop the temporary table.

### Data Interactions
* **Reads:**  
  - `[flexnetskgsvr].[QTSDB].[dbo].QTS_Personnel`  
  - `[flexnetskgsvr].[QTSDB].[dbo].QTS_Personnel_Qualification`  
  - `[flexnetskgsvr].[QTSDB].[dbo].QTS_Qualification`  

* **Writes:**  
  - Temporary table `#tmpqtsqc` (created, truncated, dropped)  

---