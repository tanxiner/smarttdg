# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters

### Purpose
Generate a preview of OCC authorization details for the DTL line based on the supplied track type, operation date and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Line identifier; only 'DTL' triggers processing |
| @TrackType | nvarchar(50) | Filter for track type |
| @OperationDate | date | Operation date used to match OCC authorization records |
| @AccessDate | date | Access date used to match OCC authorization records |

### Logic Flow
1. Declare local variables and create two temporary tables:  
   * `#TMP` holds traction power IDs and concatenated station names for the selected line and track type.  
   * `#TMP_OCCAuthPreview` holds the preview rows with many columns initially empty.

2. If `@Line` equals `'DTL'`:
   * Populate `#TMP` by selecting traction power IDs from `TAMS_Traction_Power` where line is `'DTL'` and the track type matches `@TrackType`.  
   * For each traction power, build a semicolon‑separated list of station names from `TAMS_Traction_Power_Detail` and `TAMS_Station`.

3. Insert into `#TMP_OCCAuthPreview` a row for each combination of traction power and OCC authorization that satisfies:
   * Effective date ≤ current date and expiry date ≥ current date.  
   * Active flag is true.  
   * Operation date and access date match the supplied parameters.  
   * Line and track type match the supplied values.  
   * The row includes many columns set to empty strings; only core fields (e.g., `Line`, `IsBuffer`, `PowerOn`, `StationName`, `Remark`, `PFRRemark`) are populated from source tables.

4. Open a cursor over the `OCCAuthID` values in `#TMP_OCCAuthPreview`.  
   For each `OCCAuthID`:
   * Open a second cursor over `TAMS_OCC_Auth_Workflow` rows where `OCCAuthId` matches and `ActionBy` is not 1.  
   * For each workflow record, examine `OCCAuthEndorserId` (97‑116) and update the corresponding columns in `#TMP_OCCAuthPreview`:
     * Set timestamps using `@ActionOn` formatted as `HH:MM:SS`.  
     * Retrieve user names from `TAMS_User` using `@ActionBy`.  
     * Retrieve station names from `TAMS_Station` using `@StationID`.  
     * For certain endorser IDs, prepend `'N.A. (' + time + ')'` when `@WFStatus` equals `'N.A.'`.  
     * For endorser ID 114, set `MT_Traction_Current_On_FIS` to `@FISTestResult`.  
     * For endorser ID 111, copy the permanent closing station, time and name into the normalisation columns.

5. After all cursors are closed, select all rows from `#TMP_OCCAuthPreview` to return the preview.

6. Drop the temporary tables.

### Data Interactions
* **Reads:**  
  * `TAMS_Traction_Power`  
  * `TAMS_Traction_Power_Detail`  
  * `TAMS_Station`  
  * `TAMS_OCC_Auth`  
  * `TAMS_OCC_Auth_Workflow`  
  * `TAMS_User`  
  * (Commented out) `TAMS_OCC_Duty_Roster`

* **Writes:**  
  * Temporary tables `#TMP` and `#TMP_OCCAuthPreview` (no permanent table modifications)