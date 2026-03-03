# Procedure: sp_TAMS_TOA_QTS_Chk

### Purpose
Determine whether a person’s qualification is currently valid for a specified line and date, returning the qualification status along with personal details.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @nric     | NVARCHAR(50)  | Person’s access identifier (NRIC) to look up. |
| @qualdate | NVARCHAR(20)  | Date of qualification to validate against. |
| @line     | NVARCHAR(20)  | Rail line code used to filter personnel and qualifications. |
| @QualCode | NVARCHAR(20)  | Specific qualification code to check. |

### Logic Flow
1. Initialise counters and a return value placeholder.  
2. Create a temporary table `#tmpqtsqc` to hold decrypted access IDs and qualification dates.  
3. Retrieve the person’s name string from `QTS_Personnel` where the decrypted access ID matches `@nric`.  
4. Populate `#tmpqtsqc` by joining `QTS_Personnel_Qualification`, `QTS_Qualification`, and `QTS_Personnel` on matching IDs, filtering by line and qualification code, and decrypting the access ID.  
   - Compute a suspension end date (`suspened_till`) based on `pq_suspend_to` and `pq_reinstate_eff` relative to the current timestamp.  
5. Count rows in `#tmpqtsqc` for the given access ID.  
   - If zero rows, set status to **InValid**.  
   - If rows exist, fetch the first row’s dates into local variables.  
6. Evaluate suspension: if a suspension date exists and is in the future, set status to **InValid**.  
7. If not suspended, compare the supplied qualification date (`@qualdate`) to the qualification’s valid‑from and valid‑to dates.  
   - If the date is before both valid‑from and valid‑to, set status to **Valid**; otherwise **InValid**.  
8. Return a single row containing trimmed values of NRIC, name string, line, qualification date, qualification code, and the determined status.  
9. Drop the temporary table.

### Data Interactions
* **Reads:**  
  - `QTS_Personnel`  
  - `QTS_Personnel_Qualification`  
  - `QTS_Qualification`  

* **Writes:**  
  - None (only temporary table usage).