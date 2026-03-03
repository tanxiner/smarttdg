# Procedure: sp_TAMS_SectorBooking_QTS_Chk

### Purpose
Validate a personnel’s qualification status for a specified line and date by cross‑checking QTS qualification records and return the qualification status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The personnel identifier to be checked. |
| @qualdate | NVARCHAR(MAX) | The date on which the qualification validity is evaluated. |
| @line | NVARCHAR(MAX) | The rail line for which the qualification is relevant. |
| @TrackType | NVARCHAR(50) | Not used within the procedure. |

### Logic Flow
1. Initialise counters and a return value placeholder.  
2. Create two temporary tables: `#tmpqtsqc` for holding qualification query results and `#tmpnric` for holding the input record and its evaluation outcome.  
3. Retrieve the qualification code (`@QualCode`) from `TAMS_Parameters` that matches the supplied line, the mainline possession flag, and the qualification date range.  
4. Insert the supplied NRIC, qualification date, line, and the retrieved qualification code into `#tmpnric`.  
5. Open a cursor over `#tmpnric` (currently only one row). For each row:  
   a. Look up the personnel’s name from `QTS_Personnel` where the decrypted access ID matches the NRIC.  
   b. Clear `#tmpqtsqc`.  
   c. Populate `#tmpqtsqc` by joining `QTS_Personnel_Qualification`, `QTS_Qualification`, and `QTS_Personnel` on matching IDs, filtering by line, qualification code, and excluding codes containing EPIC, OSM, or equal to TTP.  
   d. Determine the number of qualification records for the NRIC.  
   e. If none exist, mark the status as **InValid**.  
   f. If records exist, count those without suspension (`suspened_till IS NULL`).  
      - If any such records exist, check whether the supplied qualification date falls before both the valid access date and the valid till date.  
        * If it does, set status to **Valid**.  
        * If it does not, set status to **InValid**.  
      - If no non‑suspended records exist, set status to **InValid**.  
   g. Update the `qualstatus` and `namestr` fields in `#tmpnric` accordingly.  
6. After cursor processing, select the final NRIC, name, line, qualification date, qualification code, and status from `#tmpnric` ordered by ID.  
7. Drop the temporary tables and end the procedure.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Personnel`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Personnel_Qualification`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Qualification`  

* **Writes:**  
  - Temporary tables `#tmpnric` and `#tmpqtsqc` (insert, update, truncate, drop).