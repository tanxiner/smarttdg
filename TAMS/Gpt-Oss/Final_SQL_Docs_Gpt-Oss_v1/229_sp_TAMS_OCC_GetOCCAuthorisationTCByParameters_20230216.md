# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216

### Purpose
Retrieve and enrich OCC authorisation details for a specific user, line, operation date and access date, including workflow status for each endorser.

### Parameters
| Name           | Type      | Purpose |
| :------------- | :-------- | :------ |
| @UserID        | int       | Identifier of the user requesting data. |
| @Line          | nvarchar(10) | Target line; defaults to NULL, only processed when 'DTL'. |
| @OperationDate | date      | Date of the operation for which authorisations are sought. |
| @AccessDate    | date      | Date of access for which authorisations are sought. |

### Logic Flow
1. **Initialisation** – Declare variables for workflow, authorisation, endorser details and status.  
2. **Create Temp Tables** –  
   - `#TMP` holds traction power IDs and concatenated station names.  
   - `#TMP_Endorser` holds endorser IDs, line, level, role and title.  
   - `#TMP_OCCAuthTC` holds the core authorisation data to be returned.  
3. **Process Only for Line 'DTL'** –  
   a. Retrieve the active workflow ID for line 'DTL' and workflow type 'OCCAuth'.  
   b. Populate `#TMP_Endorser` with endorser records for line 'DTL' that belong to the retrieved workflow and have RoleId = 13.  
   c. Populate `#TMP` with traction power IDs and a semicolon‑separated list of station names for line 'DTL'.  
   d. Insert into `#TMP_OCCAuthTC` the authorisation records that match the traction power ID, are active, fall within the current date range, and match the supplied operation and access dates.  
   e. Filter these records to only those whose TC code appears in the duty roster for the supplied operation date, shift = 3, active roster, and the supplied user ID.  
4. **Iterate Over Authorisations** – For each `OCCAuthID` in `#TMP_OCCAuthTC`:  
   a. Iterate over each endorser in `#TMP_Endorser`.  
   b. For each endorser, query `TAMS_OCC_Auth_Workflow` to obtain the current workflow status and action time.  
   c. Depending on the endorser ID, update the corresponding column in `#TMP_OCCAuthTC`:  
      - 97 → `TrainClearCert`  
      - 105 → `AuthForTrackAccess`  
      - 106 → `LineClearCertTOA`  
      - 107 → `LineClearCertSCD` (also handles 'Remove' or 'N.A.' statuses)  
      - 116 → `AuthForTrainInsert`  
      If status is 'Pending', set the column to the status string; if 'Completed' (or 'Remove'/'N.A.' for 107), set the column to the time part of `ActionOn`.  
   d. Reset temporary status variables before moving to the next endorser.  
5. **Return Result** – Select all rows from `#TMP_OCCAuthTC` to deliver the enriched authorisation data.  
6. **Cleanup** – Drop the temporary tables `#TMP`, `#TMP_Endorser`, and `#TMP_OCCAuthTC`.

### Data Interactions
* **Reads:**  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_Traction_Power_Detail  
  - TAMS_Station  
  - TAMS_Traction_Power  
  - TAMS_OCC_Auth  
  - TAMS_OCC_Duty_Roster  
  - TAMS_OCC_Auth_Workflow  

* **Writes:**  
  - #TMP (inserted)  
  - #TMP_Endorser (inserted)  
  - #TMP_OCCAuthTC (inserted and updated)  

---