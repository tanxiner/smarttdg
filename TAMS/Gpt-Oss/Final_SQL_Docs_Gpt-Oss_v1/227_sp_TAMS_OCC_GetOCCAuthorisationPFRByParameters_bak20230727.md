# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters_bak20230727

### Purpose
Retrieves detailed OCC authorisation and PFR status information for the DTL line based on the supplied operation and access dates, incorporating workflow approvals from multiple endorsers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting the data (unused in logic). |
| @Line | nvarchar(10) | Target line; logic only executes when this equals 'DTL'. |
| @TrackType | nvarchar(50) | Track type filter applied to traction power records. |
| @OperationDate | date | Date of the operation; used to match OCC authorisation records. |
| @AccessDate | date | Date of access; used to match OCC authorisation records. |

### Logic Flow
1. **Variable Declaration** – Local variables for workflow, authorisation, endorser details, status, timestamps, and station names are declared.  
2. **Temp Table Creation** – Three temporary tables are created:  
   * `#TMP` holds traction power IDs and concatenated station names.  
   * `#TMP_Endorser` stores endorser IDs, line, level, role, and title.  
   * `#TMP_OCCAuthPFR` will contain the final result set with columns for each PFR field.  
3. **DTL Branch** – The procedure proceeds only if `@Line` equals 'DTL':  
   a. **Workflow Lookup** – The active workflow ID for DTL and the specified track type is retrieved from `TAMS_Workflow`.  
   b. **Endorser Load** – Endorsers with role ID 14 for the DTL line and the identified workflow are inserted into `#TMP_Endorser`.  
   c. **Traction Power Load** – For each traction power record on the DTL line and given track type, the associated station names are concatenated and stored in `#TMP`.  
   d. **Authorisation Load** – A join between traction power, the temp traction power table, and `TAMS_OCC_Auth` populates `#TMP_OCCAuthPFR`. Only active authorisations matching the operation and access dates, and whose TC code appears in the duty roster for shift 3, are included.  
4. **Workflow Status Update Loop** –  
   a. A cursor iterates over each `OCCAuthID` in `#TMP_OCCAuthPFR`.  
   b. For each authorisation, a nested cursor iterates over every endorser in `#TMP_Endorser`.  
   c. Depending on the endorser ID, the procedure queries `TAMS_OCC_Auth_Workflow` for the current status (`WFStatus`) and action timestamp (`ActionOn`).  
   d. If the status is 'Pending', the corresponding PFR field in `#TMP_OCCAuthPFR` is set to the status string.  
   e. If the status is 'Completed' (or 'N.A.' where applicable), the field is updated with the converted time value from `ActionOn`.  
   f. Special handling for endorser 103 includes retrieving the station name from `TAMS_Station` and storing it in the `PermanentClosingVLD_Station` column.  
   g. Endorser 114 additionally stores the `FISTestResult` value in the `MainlineTractionCurrentSwitchOn_FISTestResult` column.  
   h. After processing all endorsers for an authorisation, the cursor moves to the next `OCCAuthID`.  
5. **Result Return** – After all cursors close, the procedure selects all rows from `#TMP_OCCAuthPFR`, delivering the enriched PFR dataset.  
6. **Cleanup** – The three temporary tables are dropped.

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
  - Temporary tables `#TMP`, `#TMP_Endorser`, `#TMP_OCCAuthPFR` (inserted and updated within the procedure). No permanent tables are modified.