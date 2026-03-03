# Procedure: SP_TAMS_Depot_GetDTCAuthEndorser

### Purpose
Retrieve DTC authorization endorser records for a specified access date and LAN ID, indicating whether the user has access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date used to filter effective periods and duty roster operation dates. |
| @lanid | nvarchar(50) | The login identifier used to determine if the user is listed in the duty roster for the given date. |

### Logic Flow
1. Disable row‑count messages to keep the result set clean.  
2. Declare a variable to hold the workflow ID.  
3. Retrieve the workflow ID where `WorkflowType` is `'OCCAuth'` and `TrackType` is `'Depot'`.  
4. Select endorser information joined with workflow status where:  
   - The workflow ID matches the one found in step 3.  
   - The endorser is active.  
   - The workflow status type is `'DTCAuth'`.  
   - The supplied access date falls between the endorser’s `EffectiveDate` and `ExpiryDate`.  
5. For each selected row, compute an `Access` flag:  
   - Set to 1 if the supplied `@lanid` appears in the duty roster for the same `RoleId`, on the same `@accessDate`, with `TrackType` `'Depot'` and `Line` `'NEL'`.  
   - Otherwise set to 0.  
6. Return the workflow ID, title, role ID, access flag, and status ID for each qualifying endorser.

### Data Interactions
* **Reads:** `TAMS_Workflow`, `TAMS_Endorser`, `TAMS_WFStatus`, `TAMS_OCC_Duty_Roster`, `TAMS_Roster_Role`, `TAMS_User`  
* **Writes:** None