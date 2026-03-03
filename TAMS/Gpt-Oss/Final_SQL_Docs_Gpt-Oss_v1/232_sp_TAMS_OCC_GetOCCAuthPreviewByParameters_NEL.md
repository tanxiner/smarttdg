# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL

### Purpose
Generate a preview of OCC authorization details for the NEL line, populating time stamps and approver names for each workflow step based on the supplied operation and access dates.

### Parameters
| Name           | Type   | Purpose |
| :------------- | :----- | :------ |
| @Line          | nvarchar(10) | Line identifier; only processed when equal to 'NEL'. |
| @OperationDate | date   | Date of the operation to filter OCC authorizations. |
| @AccessDate    | date   | Date of the access to filter OCC authorizations. |

### Logic Flow
1. **Initialisation**  
   - Declare local variables for workflow processing.  
   - Create a temporary table `#TMP_OCCAuthPreview` with columns for all preview fields, initially empty.

2. **Conditional Execution**  
   - If `@Line` equals `'NEL'`, proceed; otherwise the procedure ends without output.

3. **Base Data Load**  
   - Insert into `#TMP_OCCAuthPreview` a row for each active OCC authorization that matches:  
     - `TAMS_Traction_Power.ID = TAMS_OCC_Auth.TractionPowerId`  
     - Current date between `EffectiveDate` and `ExpiryDate`  
     - `IsActive = 1`  
     - `OperationDate = @OperationDate`  
     - `AccessDate = @AccessDate`  
     - `Line = @Line`  
   - The inserted row contains the traction power details and the authorization remark; all time‑stamp and name columns are initially empty strings.

4. **Workflow Processing**  
   - Open a cursor over the `OCCAuthID` values in the temporary table.  
   - For each `OCCAuthID`:  
     - Open a second cursor over `TAMS_OCC_Auth_Workflow` rows where `OCCAuthId = @OCCAuthID` and `ActionBy <> 1`.  
     - For each workflow row, read `OCCAuthEndorserId`, `WFStatus`, `ActionOn`, `ActionBy`.  
     - Depending on `OCCAuthEndorserId`, update the corresponding columns in `#TMP_OCCAuthPreview` for that `OCCAuthID`:  
       - **117** → `TrainClearCert_TC_Time`, `TrainClearCert_TC_Name`  
       - **118** → `TrainClearCert_CC_Time`, `TrainClearCert_CC_Name`  
       - **119** → `MT_Traction_Current_Off_Req_CC_Time/Name` (status‑dependent: `'Completed'` uses time, `'N.A.'` prefixes with `N.A.`)  
       - **120** → `MT_Traction_Current_Off_PFR_Time/Name` (status‑dependent)  
       - **121** → `MT_Traction_Current_Off_RackOut_PFR_Time/Name` (status‑dependent)  
       - **122** → `AuthForTrackAccess_CC_Time/Name`  
       - **123** → `AuthForTrackAccess_TC_Time/Name`  
       - **124** → `LineClearCert_TOA_TC_Time/Name`  
       - **125** → `LineClearCert_SCD_TC_Time/Name`  
       - **126** → `LineClearCert_CC_Time/Name`  
       - **127** → `MT_Traction_Current_On_Req_CC_Time/Name` (status‑dependent)  
       - **128** → `MT_Traction_Current_On_RackIn_PFR_Time/Name` (status‑dependent)  
       - **129** → `MT_Traction_Current_On_PFR_Time/Name` (status‑dependent)  
       - **130** → `AuthForTrainInsert_CC_Time/Name`  
       - **131** → `AuthForTrainInsert_TC_Time/Name`  
     - Each update pulls the approver’s name from `TAMS_User` using `UserId = @ActionBy`.  
     - Time values are formatted as `TIME` or `varchar` with 24‑hour format (`108`).  
   - Close and deallocate the inner cursor after processing all workflow rows for the current `OCCAuthID`.

5. **Result Return**  
   - After all cursors are closed, select all rows from `#TMP_OCCAuthPreview` to return the preview dataset.

6. **Cleanup**  
   - Drop the temporary table `#TMP_OCCAuthPreview`.

### Data Interactions
* **Reads**  
  - `TAMS_Traction_Power`  
  - `TAMS_OCC_Auth`  
  - `TAMS_OCC_Auth_Workflow`  
  - `TAMS_User`

* **Writes**  
  - Temporary table `#TMP_OCCAuthPreview` (created, populated, updated, then dropped). No permanent tables are modified.