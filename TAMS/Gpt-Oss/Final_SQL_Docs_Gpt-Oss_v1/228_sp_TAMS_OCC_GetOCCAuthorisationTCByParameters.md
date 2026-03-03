# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters

### Purpose
Retrieves and compiles the current authorisation status for a specified user’s train‑control authorisations on the DTL line, including endorser approvals and timestamps.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting the authorisation data. |
| @Line | nvarchar(10) | Target line; only ‘DTL’ is processed. |
| @TrackType | nvarchar(50) | Type of track to filter traction power records. |
| @OperationDate | date | Date of the operation for which authorisations are required. |
| @AccessDate | date | Date of the access request for the operation. |

### Logic Flow
1. **Initialisation** – Declare variables for workflow, authorisation, endorser details, status, and action timestamps.  
2. **Create Temporary Tables** –  
   * `#TMP` holds traction power IDs and concatenated station names.  
   * `#TMP_Endorser` stores endorser IDs, line, level, role, and title.  
   * `#TMP_OCCAuthTC` will contain the final authorisation rows with status fields.  
3. **Process Only DTL Line** – If `@Line` equals ‘DTL’, continue; otherwise exit.  
4. **Retrieve Workflow ID** – Query `TAMS_Workflow` for the active OCCAuth workflow applicable to DTL.  
5. **Populate Endorser List** – Insert into `#TMP_Endorser` all endorser records for DTL with role ID 13 (and the workflow ID).  
6. **Gather Traction Power Details** –  
   * For each traction power record on DTL with the specified `@TrackType`, collect its ID and a semicolon‑separated list of associated station names from `TAMS_Traction_Power_Detail` and `TAMS_Station`.  
   * Insert these into `#TMP`.  
7. **Build Authorisation Rows** –  
   * Join `TAMS_Traction_Power`, `#TMP`, and `TAMS_OCC_Auth` on traction power ID.  
   * Filter by effective dates, active flag, operation date, access date, and the user’s duty roster for shift 3.  
   * Insert the resulting rows into `#TMP_OCCAuthTC`, initializing status columns (`TrainClearCert`, `AuthForTrackAccess`, `LineClearCertTOA`, `LineClearCertSCD`, `AuthForTrainInsert`) as empty strings.  
8. **Iterate Over Each Authorisation** –  
   * Open a cursor over `#TMP_OCCAuthTC` to process each `OCCAuthID`.  
   * For each authorisation, open a nested cursor over `#TMP_Endorser` to evaluate each endorser.  
   * For endorser IDs 97, 105, 106, 107, 116:  
     * Retrieve the workflow status and action timestamp from `TAMS_OCC_Auth_Workflow`.  
     * If status is ‘Pending’, set the corresponding status column in `#TMP_OCCAuthTC` to ‘Pending’.  
     * If status is ‘Completed’ (or ‘Remove’/‘N.A.’ for endorser 107), convert the action timestamp to a TIME value and store it in the appropriate column.  
     * Reset temporary status variables before moving to the next endorser.  
   * Close the endorser cursor and continue with the next authorisation.  
9. **Return Result** – Select all rows from `#TMP_OCCAuthTC` to deliver the compiled authorisation data.  
10. **Cleanup** – Drop the three temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_Traction_Power_Detail`  
  - `TAMS_Station`  
  - `TAMS_Traction_Power`  
  - `TAMS_OCC_Auth`  
  - `TAMS_OCC_Duty_Roster`  
  - `TAMS_OCC_Auth_Workflow`  

* **Writes:**  
  - Temporary tables `#TMP`, `#TMP_Endorser`, `#TMP_OCCAuthTC` (no permanent tables are modified).