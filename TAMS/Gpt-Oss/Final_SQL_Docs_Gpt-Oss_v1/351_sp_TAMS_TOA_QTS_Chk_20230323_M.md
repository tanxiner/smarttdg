# Procedure: sp_TAMS_TOA_QTS_Chk_20230323_M

### Purpose
Validate a person’s qualification status for a specified rail line and access type by cross‑checking QTS personnel data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | Person’s identification number to be validated |
| @qualdate | NVARCHAR(20) | Date of the qualification to be checked |
| @line | NVARCHAR(20) | Rail line identifier for which the qualification applies |
| @AccessType | NVARCHAR(20) | Code representing the type of access/qualification being verified |

### Logic Flow
1. Initialise counters and a return value placeholder.  
2. Create two temporary tables:  
   * `#tmpqtsqc` – holds decrypted access IDs and qualification dates from QTS.  
   * `#tmpnric` – holds the input record and will store the resulting status.  
3. Retrieve the qualification code (`@QualCode`) from `TAMS_Parameters` that matches the supplied line, access type “Possession”, and is active for the supplied qualification date.  
4. Insert the input parameters into `#tmpnric`.  
5. Open a cursor over `#tmpnric` (only one row in this case). For each row:  
   a. Look up the person’s name (`@CurNameStr`) from `QTS_Personnel` where the decrypted access ID equals the NRIC.  
   b. Truncate `#tmpqtsqc`.  
   c. Populate `#tmpqtsqc` with all QTS qualification records that:  
      * belong to the same rail line,  
      * match the retrieved qualification code,  
      * are not generic codes (`EPIC`, `OSM`, `TTP`) and have a defined access period.  
      * calculate a suspension end date (`suspened_till`) based on suspend and reinstate fields.  
   d. Count records in `#tmpqtsqc` for the current NRIC.  
   e. If no records exist → set `qualstatus` to **InValid**.  
   f. If records exist:  
      i. Check for any record where `suspened_till` is null or the default date (`1900‑01‑01`).  
      ii. If such a record exists, compare the supplied qualification date against `pq_validaccess_date` and `pq_validtill_date`.  
          * If the date falls within the valid window → set `qualstatus` to **Valid**.  
          * Otherwise → set `qualstatus` to **InValid**.  
      iii. If no non‑suspended record exists → set `qualstatus` to **InValid**.  
   g. Update `#tmpnric` with the determined status and the retrieved name.  
6. After cursor processing, select all columns from `#tmpnric`, trimming spaces, and order by the internal ID.  
7. Drop the temporary tables and end the procedure.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `FLEXNETSKGSVR.QTSDB.dbo.QTS_Personnel`  
  - `FLEXNETSKGSVR.QTSDB.dbo.QTS_Personnel_Qualification`  
  - `FLEXNETSKGSVR.QTSDB.dbo.QTS_Qualification`  

* **Writes:**  
  - Temporary tables `#tmpqtsqc` and `#tmpnric` (no permanent data is modified).