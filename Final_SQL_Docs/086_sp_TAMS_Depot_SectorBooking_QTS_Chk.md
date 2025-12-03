# Procedure: sp_TAMS_Depot_SectorBooking_QTS_Chk

### Purpose
Determine the validity status of a person’s QTS qualification for a depot sector booking based on NRIC, qualification date, line, and track type.

### Parameters
| Name        | Type          | Purpose |
| :---        | :---          | :--- |
| @nric       | NVARCHAR(MAX) | NRIC of the person to check |
| @qualdate   | NVARCHAR(MAX) | Qualification date to evaluate |
| @line       | NVARCHAR(MAX) | Railway line identifier |
| @TrackType  | NVARCHAR(50)  | Track type (unused in logic) |

### Logic Flow
1. **Initialization** – Set counters and a return value placeholder; create three temporary tables: `#tmpqtsqc`, `#tmpnric`, and `#tmpqualcode`.  
2. **Parameter Retrieval** – Load the QTS qualification code that applies to the supplied line and date from `TAMS_Parameters` into `#tmpqualcode`.  
3. **NRIC Record Insertion** – Insert the supplied NRIC, qualification date, line, and empty status into `#tmpnric`.  
4. **Cursor Setup** – Open a cursor over `#tmpnric` to process each NRIC record (currently only one).  
5. **Per‑NRIC Processing**  
   - Retrieve the person’s name from `QTS_Personnel` where the decrypted access ID matches the NRIC.  
   - Clear `#tmpqtsqc`.  
   - Populate `#tmpqtsqc` with qualification records from `QTS_Personnel_Qualification`, `QTS_Qualification`, and `QTS_Personnel` that:  
     * belong to the same line,  
     * have a qualification code in `#tmpqualcode`,  
     * are not EPIC, OSM, or TTP, and  
     * have an access period other than 99.  
     The query also calculates a suspension end date (`suspened_till`) based on suspend and reinstate fields.  
   - Count how many qualification rows exist for the NRIC.  
     * If zero, mark the NRIC record as **InValid**.  
     * If at least one row exists without a suspension (`suspened_till IS NULL`):  
       - Check if the supplied qualification date falls between `pq_validaccess_date` and `pq_validtill_date`.  
       - If it does, set status to **Valid**; otherwise set to **InValid**.  
     * If all rows are suspended, set status to **InValid**.  
   - Update the `qualstatus` and `namestr` fields in `#tmpnric` accordingly.  
6. **Result Output** – Select and trim the NRIC, name, line, qualification date, qualification code, and status from `#tmpnric`, ordering by the temporary table ID.  
7. **Cleanup** – Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Personnel`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Personnel_Qualification`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Qualification`  
  - `FLEXNETSKGSVR.QTSDB.QTS_Personnel`  

* **Writes:**  
  - Temporary tables `#tmpqualcode`, `#tmpnric`, `#tmpqtsqc` (inserted, updated, truncated, and dropped within the procedure).