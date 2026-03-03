# Procedure: sp_TAMS_OCC_Generate_Authorization_Trace

### Purpose
Generate OCC authorization records and associated workflow entries for a specified line and access date, applying buffer and power‑on rules derived from TAR sector data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Identifier of the line (e.g., DTL, NEL) for which authorizations are created. |
| @AccessDate | NVARCHAR(20) | Optional date string; if omitted, the procedure derives the operation and access dates based on the current time and a 06:00:00 cutoff. |

### Logic Flow
1. **Date Determination**  
   - Capture the current date and time.  
   - If @AccessDate is not supplied, compare the current time to a 06:00:00 cutoff.  
   - If after the cutoff, set the operation date to today and the access date to tomorrow; otherwise set the operation date to yesterday and the access date to today.  
   - If @AccessDate is supplied, set the operation date to the day before the supplied date and the access date to the supplied date.

2. **Existing Authorization Check**  
   - Count how many OCC authorization records already exist for the chosen line and derived access date.  
   - If none exist, the procedure exits without further action.

3. **Workflow Context Retrieval**  
   - Find the active workflow definition for the line where the workflow type is OCCAuth.  
   - From that workflow, obtain the current status ID and the ID of the first‑level endorser.

4. **Temporary Tables Creation**  
   - Create three in‑memory tables: one for TAR sectors, one for pending OCC authorizations, and one for workflow actions.

5. **Populate TAR Sectors**  
   - For line DTL: select TAR sectors where the TAR status is 8 and the access date matches the derived access date.  
   - For line NEL: select TAR sectors where the TAR status is 9 and the access date matches the derived access date.  
   - Store each sector’s ID, TAR ID, traction power ID, sector ID, buffer flag, colour code, added‑buffer flag, and power‑on flag.

6. **Prepare OCC Authorization Records**  
   - If there are existing authorizations and at least one TAR sector, insert into the temporary OCC auth table all traction power rows for the line that are currently effective and active.  
   - Each inserted row receives the derived operation and access dates, the workflow status ID, and default values for remarks and flags.

7. **Apply Buffer and Power‑On Logic**  
   - Iterate over each temporary OCC auth row.  
   - For the row’s traction power ID, check if a matching TAR sector exists.  
   - If a sector exists, set the auth row’s buffer and power‑on flags based on the sector’s buffer and power‑on values:  
     * If the sector is a buffer and power‑on, set both flags to 1.  
     * If the sector is not a buffer but power‑on, set buffer to 0 and power‑on to 1.  
     * Otherwise set both flags to 0.

8. **Persist Authorizations**  
   - Insert all rows from the temporary OCC auth table into the permanent TAMS_OCC_Auth table, preserving all fields except the update columns.

9. **Create Workflow Actions**  
   - For each newly inserted OCC authorization, insert a corresponding workflow action row into the temporary workflow table with status “Pending”, station ID 0, and the current user ID (1).  
   - After all actions are prepared, insert them into the permanent TAMS_OCC_Auth_Workflow table.

10. **Cleanup**  
    - Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - TAMS_OCC_Auth  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_Traction_Power_Detail  
  - TAMS_Traction_Power  
  - TAMS_TAR_Power_Sector  
  - TAMS_Power_Sector  

* **Writes:**  
  - TAMS_OCC_Auth  
  - TAMS_OCC_Auth_Workflow