# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL_bak20230728

### Purpose
Generate a preview of OCC authorization records for the NEL line, populating time‑and‑name fields for each endorser action based on the supplied operation and access dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Line identifier; only 'NEL' triggers processing. |
| @OperationDate | date | Date of the operation to filter OCC authorisations. |
| @AccessDate | date | Date of the access to filter OCC authorisations. |

### Logic Flow
1. **Temporary table creation** – A table `#TMP_OCCAuthPreview` is defined to hold the preview rows, including columns for each endorser’s time and name.  
2. **Conditional processing** – If `@Line` equals `'NEL'`, the procedure proceeds.  
3. **Initial data load** – Rows are inserted into `#TMP_OCCAuthPreview` by joining `TAMS_Traction_Power` (`tp`) with `TAMS_OCC_Auth` (`oa`).  
   * Only active authorisations (`IsActive = 1`) whose effective and expiry dates encompass the current date are selected.  
   * The join is on `tp.ID = oa.TractionPowerId`.  
   * The `OperationDate`, `AccessDate`, and `Line` columns of `oa` must match the supplied parameters.  
   * All time‑and‑name columns are initially set to empty strings; `Remark` is copied from `oa`.  
4. **Cursor over preview rows** – A cursor iterates over each `OCCAuthID` present in the temporary table.  
5. **Inner cursor over workflow records** – For each `OCCAuthID`, a second cursor selects all rows from `TAMS_OCC_Auth_Workflow` where `ActionBy <> 1`.  
6. **Field updates per endorser** – Inside the inner loop, the procedure checks the `OCCAuthEndorserId` and updates the corresponding columns in `#TMP_OCCAuthPreview`:  
   * Endorser IDs 117–131 map to specific time and name columns (e.g., 117 → `TrainClearCert_TC_Time/Name`, 118 → `TrainClearCert_CC_Time/Name`, etc.).  
   * For endorser IDs 120, 121, 128, 129, the update depends on `WFStatus`:  
     * If `WFStatus = 'Completed'`, the time is set to the converted `ActionOn` value.  
     * If `WFStatus = 'N.A.'`, the time is set to the literal string `'N.A.'`.  
   * The name is always resolved by selecting `Name` from `TAMS_User` where `Userid = @ActionBy`.  
7. **Cursor cleanup** – After processing all workflow rows for an `OCCAuthID`, the inner cursor is closed and deallocated.  
8. **Result output** – Once all preview rows have been enriched, the procedure selects all rows from `#TMP_OCCAuthPreview` for the caller.  
9. **Temporary table drop** – The temporary table is dropped at the end of the procedure.

### Data Interactions
* **Reads:**  
  * `TAMS_Traction_Power` – source of traction power details.  
  * `TAMS_OCC_Auth` – source of OCC authorisation records.  
  * `TAMS_OCC_Auth_Workflow` – source of workflow actions per authorisation.  
  * `TAMS_User` – source of user names for action by IDs.  
* **Writes:**  
  * `#TMP_OCCAuthPreview` – temporary table created, rows inserted, and updated during processing. No permanent tables are modified.