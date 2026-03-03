# Procedure: sp_TAMS_TOA_QTS_Chk_20230323

### Purpose
Validate a person’s qualification status for a specified line and date, returning the qualification status and name.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | Access identifier to check |
| @qualdate | NVARCHAR(20) | Date to evaluate qualification validity |
| @line | NVARCHAR(20) | Rail line code for qualification filtering |
| @AccessType | NVARCHAR(20) | Qualification code to be verified |

### Logic Flow
1. Initialise counters and temporary tables `#tmpnric` (holds input record) and `#tmpqtsqc` (holds qualification query results).  
2. Retrieve the parameter value `QTSQualCode` for the supplied line and date from `TAMS_Parameters`; the value is stored in `@QualCode` but not used further.  
3. Insert the supplied parameters into `#tmpnric`.  
4. Open a cursor over `#tmpnric` (only one row). For each row:  
   a. Look up the person’s name from `QTS_Personnel` where the decrypted access id matches `@nric`.  
   b. Clear `#tmpqtsqc`.  
   c. Populate `#tmpqtsqc` with qualification records that match:  
      - Same rail line (`@line`) for both person and qualification.  
      - Qualification code equals `@AccessType`.  
      - Exclude codes containing `EPIC`, `OSM`, or equal to `TTP`.  
      - Exclude qualifications with an access period of 99.  
      - Compute a suspension end date (`suspened_till`) based on suspend and reinstate fields.  
   d. Count rows in `#tmpqtsqc` for the current access id.  
   e. If no rows → set `qualstatus` to **InValid**.  
   f. If rows exist:  
      i. Count rows where `suspened_till` is NULL.  
      ii. If any such rows:  
         - Count rows where the supplied `@qualdate` is before both `pq_validaccess_date` and `pq_validtill_date`.  
         - If count > 0 → set `qualstatus` to **Valid**.  
         - Else → set `qualstatus` to **InValid**.  
      iii. If no rows with `suspened_till` NULL → set `qualstatus` to **InValid**.  
   g. Update `#tmpnric` with the determined `qualstatus` and retrieved name.  
5. After cursor processing, select all columns from `#tmpnric` (trimmed) as the procedure result set, ordered by the internal ID.  
6. Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `QTS_Personnel`  
  - `QTS_Personnel_Qualification`  
  - `QTS_Qualification`  

* **Writes:**  
  - None to permanent tables (only temporary tables are created and dropped).