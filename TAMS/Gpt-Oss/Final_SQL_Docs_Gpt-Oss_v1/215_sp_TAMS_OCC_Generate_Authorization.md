# Procedure: sp_TAMS_OCC_Generate_Authorization

### Purpose
Creates OCC authorization records for a specified line and track type, generates associated workflow entries, and logs audit information based on the current or supplied access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target line identifier (e.g., 'DTL', 'NEL') |
| @TrackType | NVARCHAR(50) | Target track type |
| @AccessDate | NVARCHAR(20) | Optional access date; if omitted, the procedure derives dates from the current time |

### Logic Flow
1. **Date Determination**  
   - Capture current date and time.  
   - If @AccessDate is empty:  
     - If current time > 06:00, set operation date to today and access date to tomorrow.  
     - Otherwise set operation date to yesterday and access date to today.  
   - If @AccessDate is supplied, set operation date to the day before the supplied date and access date to the supplied date.

2. **Existing Authorization Check**  
   - Count records in TAMS_OCC_Auth for the given line, track type, and derived access date.  
   - If a count exists, the procedure exits without further action.

3. **Workflow Context Retrieval**  
   - Find the active workflow ID for the line and track type where WorkflowType = 'OCCAuth'.  
   - Retrieve the level‑1 endorser ID and workflow status ID from TAMS_Endorser for that workflow.

4. **Temporary Tables Creation**  
   - Create #TmpTARSectors, #TmpOCCAuth, and #TmpOCCAuthWorkflow to hold intermediate data.

5. **Sector Data Loading**  
   - For line 'DTL': join TAMS_TAR, TAMS_TAR_Sector, and TAMS_Traction_Power_Detail where TARStatusId = 8, matching line, track type, and access date.  
   - For line 'NEL': join TAMS_TAR, TAMS_TAR_Power_Sector, TAMS_Power_Sector, and TAMS_Traction_Power_Detail where TARStatusId = 9, matching line, track type, and access date.  
   - Store the resulting sector records in #TmpTARSectors.

6. **Authorization Record Generation**  
   - If no existing authorizations and sectors exist:  
     - Insert into #TmpOCCAuth from TAMS_Traction_Power for the line and track type, selecting active and effective records, ordered by Order.  
     - Set default values: operation date, access date, workflow status ID, and initial flags.

7. **Sector Flag Application**  
   - For each record in #TmpOCCAuth:  
     - Find matching sectors by TractionPowerId.  
     - If any sector exists, pick the one with the highest PowerOn and IsBuffer values.  
     - Update the authorization record’s IsBuffer and PowerOn flags according to the sector’s flags:  
       * Buffer = 1 & PowerOn = 1 → set both to 1.  
       * Buffer = 0 & PowerOn = 1 → set Buffer = 0, PowerOn = 1.  
       * Otherwise → set both to 0.

8. **Persist Authorizations**  
   - Insert the finalized #TmpOCCAuth records into TAMS_OCC_Auth.

9. **Workflow Entry Creation**  
   - For each inserted authorization, insert a pending workflow record into #TmpOCCAuthWorkflow with the retrieved endorser ID, status 'Pending', station 0, and current timestamp.  
   - Persist these records into TAMS_OCC_Auth_Workflow.

10. **Audit Logging**  
    - Insert audit entries for each new authorization into TAMS_OCC_Auth_Audit with action 'I'.  
    - Insert audit entries for each new workflow record into TAMS_OCC_Auth_Workflow_Audit with action 'I'.

11. **Cleanup**  
    - Drop the temporary tables.

### Data Interactions
* **Reads**  
  - TAMS_OCC_Auth  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_Traction_Power_Detail  
  - TAMS_TAR_Power_Sector  
  - TAMS_Power_Sector  
  - TAMS_Traction_Power  

* **Writes**  
  - TAMS_OCC_Auth  
  - TAMS_OCC_Auth_Workflow  
  - TAMS_OCC_Auth_Audit  
  - TAMS_OCC_Auth_Workflow_Audit