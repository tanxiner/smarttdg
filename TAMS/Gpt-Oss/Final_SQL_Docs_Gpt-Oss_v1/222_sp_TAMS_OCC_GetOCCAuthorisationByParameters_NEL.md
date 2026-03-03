# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL

### Purpose
Retrieves and compiles OCC authorisation details for the NEL line, applying endorser workflow statuses to each record before returning the result set.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting data (used in commented logic for duty roster filtering). |
| @Line | nvarchar(10) | Target line (e.g., 'NEL') to filter authorisation records. |
| @TrackType | nvarchar(50) | Track type used to locate the correct workflow and filter authorisations. |
| @OperationDate | date | Date of the operation; filters OCC authorisations. |
| @AccessDate | date | Date of access; filters OCC authorisations. |
| @RosterCode | nvarchar(50) | Code indicating the roster type (TC, CC, PFR) used to decide which workflow status to apply. |

### Logic Flow
1. **Workflow Identification**  
   - Query `TAMS_Workflow` for the active workflow matching the supplied line, track type, and type 'OCCAuth'.  
   - Store its ID in `@WorkflowId`.

2. **Endorser Loading**  
   - Insert into temporary table `#TMP_Endorser` all endorser rows from `TAMS_Endorser` that belong to line 'NEL' and the identified workflow.  
   - Order the rows by `EndorserLevel` to preserve processing priority.

3. **Authorisation Loading**  
   - Join `TAMS_OCC_Auth` with `TAMS_Traction_Power` on traction power ID.  
   - Apply filters: effective dates, active flag, operation date, access date, line, and track type.  
   - Insert the resulting rows into temporary table `#TMP_OCCAuthNEL`, initializing many status columns with empty strings.

3. **Status Application Loop**  
   - For each `OCCAuthID` in `#TMP_OCCAuthNEL`:  
     a. For each endorser in `#TMP_Endorser`:  
        i. Retrieve the workflow status (`WFStatus`) and action time (`@ActionTime`) from `TAMS_OCC_Auth_Workflow` for the current `OCCAuthID` and endorser ID.  
        ii. Depending on the endorser ID (117–131) and the supplied roster code, update the corresponding column in `#TMP_OCCAuthNEL` with:  
           - The status string if the status is 'Pending' and the roster code matches the endorser’s required code.  
           - The formatted action time if the status is 'Completed'.  
           - An empty string if the status is 'Pending' but the roster code does not match, or if the status is 'Completed' but the roster code does not match.  
           - For statuses 'Completed' or 'N.A.', the time is formatted as a string; otherwise the column remains empty.

4. **Result Return**  
   - After all loops, select all rows from `#TMP_OCCAuthNEL` to return to the caller.

5. **Cleanup**  
   - Drop the temporary tables `#TMP_Endorser` and `#TMP_OCCAuthNEL`.

### Data Interactions
* **Reads:**  
  - `TAMS_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_Traction_Power`  
  - `TAMS_OCC_Auth`  
  - `TAMS_OCC_Auth_Workflow`  

* **Writes:**  
  - Temporary table `#TMP_Endorser` (insert)  
  - Temporary table `#TMP_OCCAuthNEL` (insert, update)