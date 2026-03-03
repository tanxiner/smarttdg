# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_bak20230727

### Purpose
Retrieve the current OCC authorisation status for the NEL line, applying workflow rules for each endorser and roster code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting data (unused in logic) |
| @Line | nvarchar(10) | Target line (default NULL) |
| @TrackType | nvarchar(50) | Target track type (default NULL) |
| @OperationDate | date | Date of the operation to filter authorisations |
| @AccessDate | date | Date of the access to filter authorisations |
| @RosterCode | nvarchar(50) | Code of the roster (TC, CC, PFR, etc.) |

### Logic Flow
1. **Workflow Identification**  
   - Query `TAMS_Workflow` for the active workflow matching `@Line`, `@TrackType`, type `'OCCAuth'`, and current date between `EffectiveDate` and `ExpiryDate`.  
   - Store the workflow ID in `@WorkflowId`.

2. **Endorser List Creation**  
   - Populate temporary table `#TMP_Endorser` with endorsers from `TAMS_Endorser` where `Line = 'NEL'` and `WorkflowId` matches the one found.  
   - Order by `Level` ascending.

3. **Authorisation Record Assembly**  
   - Insert into `#TMP_OCCAuthNEL` a row for each active `TAMS_OCC_Auth` record that joins with `TAMS_Traction_Power` on `TractionPowerId`.  
   - Apply filters: `EffectiveDate`/`ExpiryDate` overlap current date, `IsActive = 1`, `OperationDate = @OperationDate`, `AccessDate = @AccessDate`, `Line = @Line`, `TrackType = @TrackType`.  
   - Populate columns such as `TractionPowerSection`, `HSCBName`, `Train`, and set all workflow‑dependent columns to empty strings initially.

4. **Workflow Status Application**  
   - For each `OCCAuthID` in `#TMP_OCCAuthNEL`, iterate over every endorser in `#TMP_Endorser`.  
   - For each endorser, read `WFStatus` and `ActionOn` from `TAMS_OCC_Auth_Workflow` where `OCCAuthId` matches and `OCCAuthEndorserId` equals the current endorser ID.  
   - Depending on the endorser ID, roster code, and status, update the corresponding column in `#TMP_OCCAuthNEL`:
     - **Pending**: set column to `'Pending'` if roster code matches the endorser’s required code; otherwise set to empty string.
     - **Completed**: set column to the time part of `ActionOn`.
     - **N.A.** (only for PFR endorsers 120 & 121): set column to `'N.A.'`.
   - Reset `@WFStatus` and `@ActionOn` after each endorser.

5. **Result Return**  
   - After all cursors finish, select all rows from `#TMP_OCCAuthNEL` to return the enriched authorisation data.

6. **Cleanup**  
   - Drop temporary tables `#TMP_Endorser` and `#TMP_OCCAuthNEL`.

### Data Interactions
* **Reads**  
  - `TAMS_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_Traction_Power`  
  - `TAMS_OCC_Auth`  
  - `TAMS_OCC_Auth_Workflow`

* **Writes**  
  - Temporary tables: `#TMP`, `#TMP_Endorser`, `#TMP_OCCAuthNEL` (no permanent table updates)