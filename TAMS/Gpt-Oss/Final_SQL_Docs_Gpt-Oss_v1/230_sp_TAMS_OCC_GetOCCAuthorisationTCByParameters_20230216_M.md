# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216_M

### Purpose
Retrieve OCC authorisation records for a specific user, line, operation date and access date, enriching each record with current workflow status for selected endorsers.

### Parameters
| Name           | Type      | Purpose |
| :------------- | :-------- | :------ |
| @UserID        | int       | Identifier of the user whose duty roster is queried. |
| @Line          | nvarchar(10) | Line code to filter records; only 'DTL' is processed. |
| @OperationDate | date      | Date of the operation for which authorisations are required. |
| @AccessDate    | date      | Date of access for which authorisations are required. |

### Logic Flow
1. **Initialisation** – Declare local variables and create three temporary tables:  
   * `#TMP` holds traction power IDs and concatenated station names.  
   * `#TMP_Endorser` holds endorser details for the line.  
   * `#TMP_OCCAuthTC` will store the final authorisation rows.

2. **Line Check** – If `@Line` equals `'DTL'`, continue; otherwise the procedure ends without output.

3. **Workflow Identification** – Retrieve the active workflow ID for the DTL line from `TAMS_Workflow`.

4. **Load Endorsers** – Insert into `#TMP_Endorser` all endorsers for the DTL line with `RoleId = 13` and the workflow ID obtained.

5. **Load Traction Power Details** – Populate `#TMP` with each traction power ID and a semicolon‑separated list of station names linked to that traction power.

6. **Select OCC Authorisations** – Insert into `#TMP_OCCAuthTC` all active OCC authorisation records that match:  
   * The traction power ID matches a record in `#TMP`.  
   * The operation date and access date match the supplied parameters.  
   * The TC code is present in the duty roster for the supplied user, shift 3, and is active.  
   Each inserted row includes a row number (`SNO`) and copies of fields from the authorisation record; several certification fields are initially set to empty strings.

7. **Process Each Authorisation** – Open a cursor over `#TMP_OCCAuthTC` to iterate through each `OCCAuthID`.  
   For each authorisation:
   * Open a second cursor over `#TMP_Endorser` to iterate through each endorser.
   * For each endorser, if the endorser ID matches one of the specific IDs (97, 105, 106, 107, 116), query `TAMS_OCC_Auth_Workflow` for the current workflow status and action time for that authorisation and endorser.
   * Depending on the status value:
     * If `'Pending'`, set the corresponding certification field in `#TMP_OCCAuthTC` to `'Pending'`.
     * If `'Completed'`, set the field to the time part of `ActionOn`.
     * For endorser 107, if status is `'Remove'` or `'N.A.'`, also set the field to the time part of `ActionOn`.
   * Reset the temporary status variables before moving to the next endorser.

8. **Finalize** – After all cursors are closed and deallocated, select all rows from `#TMP_OCCAuthTC` to return to the caller.

9. **Cleanup** – Drop the three temporary tables.

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
  - None to permanent tables; only temporary tables are created, populated, and dropped within the procedure.