# Procedure: sp_TAMS_OCC_GetOCCAuthorisationCCByParameters

### Purpose
Retrieves OCC authorisation details for the DTL line, incorporating endorser workflow status and time stamps for various authorisation checkpoints.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting data (unused in logic). |
| @Line | nvarchar(10) | Target line; only 'DTL' triggers processing. |
| @TrackType | nvarchar(50) | Track type filter applied to traction power records. |
| @OperationDate | date | Operation date used to match OCC authorisation records. |
| @AccessDate | date | Access date used to match OCC authorisation records. |

### Logic Flow
1. **Variable Declaration** – Set up local variables for workflow, authorisation, endorser details, and status tracking.  
2. **Temp Table Creation** – Create three temporary tables:  
   - `#TMP` for traction power IDs and concatenated station names.  
   - `#TMP_Endorser` for endorser IDs, levels, and titles.  
   - `#TMP_OCCAuthCC` for the final authorisation result set.  
3. **DTL Line Check** – Proceed only if `@Line` equals `'DTL'`.  
4. **Workflow Identification** – Query `TAMS_Workflow` to obtain the active workflow ID for DTL OCC authorisation.  
5. **Endorser Loading** – Insert into `#TMP_Endorser` all endorser records for DTL with the retrieved workflow ID and `RoleId = 12`.  
6. **Traction Power & Stations** – Populate `#TMP` with traction power IDs and a semicolon‑separated list of associated station names, filtered by `@TrackType`.  
7. **Authorisation Record Assembly** – Insert into `#TMP_OCCAuthCC` rows that join traction power, the temporary traction‑station mapping, and `TAMS_OCC_Auth`.  
   - Apply date and status filters (`EffectiveDate`, `ExpiryDate`, `IsActive`).  
   - Match `OperationDate` and `AccessDate`.  
   - Restrict to train codes (`TC`) that appear in the duty roster for shift 3 on the operation date.  
   - Initialise all status columns to empty strings.  
8. **Cursor over Authorisations** – Open a cursor on `#TMP_OCCAuthCC` to iterate through each `OCCAuthID`.  
9. **Cursor over Endorsers** – For each authorisation, open a nested cursor over `#TMP_Endorser`.  
10. **Endorser‑Specific Processing** – For each endorser ID (98, 99, 104, 110, 112, 115):  
    - Retrieve `WFStatus` and `ActionOn` from `TAMS_OCC_Auth_Workflow`.  
    - If `WFStatus` is `'Pending'`, set the corresponding column in `#TMP_OCCAuthCC` to `'Pending'`.  
    - If `WFStatus` is `'Completed'`, set the column to the time part of `ActionOn`.  
    - Reset status variables.  
11. **Close Cursors** – After processing all endorsers for an authorisation, close and deallocate the inner cursor; then fetch the next authorisation.  
12. **Result Output** – After all cursors finish, select all rows from `#TMP_OCCAuthCC` to return the enriched authorisation data.  
13. **Cleanup** – Drop the three temporary tables.

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
  - Temporary tables `#TMP`, `#TMP_Endorser`, `#TMP_OCCAuthCC` (only in-memory, no permanent tables modified).