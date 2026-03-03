# Procedure: sp_TAMS_TOA_QTS_Chk_20230907

### Purpose
Validate a person’s qualification status for a specified line and qualification date against the QTS database, returning the person’s name and validity status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | Person’s access identifier to check |
| @qualdate | NVARCHAR(20) | Date of qualification to evaluate |
| @line | NVARCHAR(20) | Railway line for which the qualification applies |
| @AccessType | NVARCHAR(20) | Qualification code to be used in the check |

### Logic Flow
1. **Setup** – Initialise counters and create two temporary tables:  
   * `#tmpqtsqc` to hold qualification records for the current person.  
   * `#tmpnric` to hold the input record and later the result status.

2. **Retrieve QualCode** – Query `TAMS_Parameters` for the parameter `QTSQualCode` that matches the supplied `@line` and is effective on `@qualdate`. The value is stored in `@QualCode`.

3. **Insert Input Record** – Insert a single row into `#tmpnric` containing the supplied `@nric`, `@qualdate`, `@line`, and `@AccessType` (used as `qualcode`). `namestr` and `qualstatus` are left NULL.

4. **Process Each Record (Cursor)** –  
   a. Open a cursor over `#tmpnric` (only one row).  
   b. For the current row:  
      i. Retrieve the person’s name from `QTS_Personnel` where the decrypted `p_access_id` equals the current `nric`.  
      ii. Truncate `#tmpqtsqc`.  
      iii. Populate `#tmpqtsqc` with qualification rows that satisfy:  
          - Same line for personnel and qualification.  
          - Qualification code equals the current `qualcode`.  
          - Exclude codes containing `EPIC`, `OSM`, or equal to `TTP`, and exclude period 99.  
          - Compute `suspened_till` based on suspend and reinstate dates.  
   c. **Determine Status** –  
      - If `#tmpqtsqc` contains no rows for the current `nric`, set `qualstatus` to `InValid`.  
      - Else, count rows where `suspened_till` is NULL or the default date.  
        * If such rows exist, check if the supplied `qualdate` is before both `pq_validaccess_date` and `pq_validtill_date`.  
          - If true, set `qualstatus` to `Valid`.  
          - If false, set `qualstatus` to `InValid`.  
        * If no rows without suspension, set `qualstatus` to `InValid`.  
   d. Update `#tmpnric` with the determined `qualstatus` and the retrieved name.

5. **Return Result** – Select the final columns from `#tmpnric` (trimmed) and order by `ID`.

6. **Cleanup** – Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `[FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel`  
  - `[FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel_Qualification`  
  - `[FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Qualification`

* **Writes:**  
  - Insert into `#tmpnric`  
  - Insert into `#tmpqtsqc`  
  - Update `#tmpnric` (status and name)  

---