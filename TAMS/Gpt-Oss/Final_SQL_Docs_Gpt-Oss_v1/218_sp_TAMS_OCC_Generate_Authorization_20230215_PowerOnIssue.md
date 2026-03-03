# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_PowerOnIssue

### Purpose
Creates OCC authorization records and associated workflow entries for a specified line (DTL or NEL) when no authorization exists for the calculated access date, using TAR sector information to determine buffer and power‑on status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier to process (e.g., 'DTL' or 'NEL'). |
| @AccessDate | NVARCHAR(20) | Optional explicit access date; if omitted, the date is derived from the current time relative to a 06:00:00 cutoff. |

### Logic Flow
1. **Date Determination**  
   - Capture current date and time.  
   - If @AccessDate is not supplied, decide operation and access dates based on whether the current time is after 06:00:00.  
     * After 06:00:00: operation date = today, access date = tomorrow.  
     * Before 06:00:00: operation date = yesterday, access date = today.  
   - If @AccessDate is supplied, set operation date to the day before the supplied date and access date to the supplied date.

2. **Existing Authorization Check**  
   - Count rows in TAMS_OCC_Auth where Line equals @Line and AccessDate equals the derived access date.  
   - Store the count in @OCCAuthCtr.

3. **Workflow Context Retrieval**  
   - Find the active workflow for the line with type 'OCCAuth' and store its ID in @WorkflowID.  
   - From TAMS_Endorser, retrieve the first‑level endorser ID and current workflow status ID for that workflow, storing them in @EndorserID and @WFStatusId.

4. **Temporary Tables Creation**  
   - Create three in‑memory tables: #TmpTARSectors, #TmpOCCAuth, and #TmpOCCAuthWorkflow to hold intermediate data.

5. **Populate TAR Sectors**  
   - If @Line is 'DTL', insert into #TmpTARSectors rows from TAMS_TAR, TAMS_TAR_Sector, and TAMS_Traction_Power_Detail where TARStatusId = 8, Line matches, and AccessDate matches the derived access date.  
   - If @Line is 'NEL', insert from TAMS_TAR, TAMS_TAR_Power_Sector, and TAMS_Power_Sector where TARStatusId = 9, Line matches, and AccessDate matches.

6. **Authorization Generation (only if none exist)**  
   - If @OCCAuthCtr = 0 and at least one TAR sector was found:  
     a. Insert into #TmpOCCAuth all active traction power records for the line, setting default values for remarks, status, buffer, power‑on, timestamps, and creator.  
     b. For each record in #TmpOCCAuth, look up matching TAR sectors by TractionPowerId.  
        - If a match exists, set IsBuffer and PowerOn in #TmpOCCAuth based on the sector’s IsBuffer and PowerOn flags.  
        - If no match, set both flags to 0.  
     c. Insert the finalized rows from #TmpOCCAuth into TAMS_OCC_Auth, preserving all fields except UpdatedOn/UpdatedBy.

7. **Workflow Entry Creation**  
   - For each newly inserted OCC authorization record, create a corresponding workflow row in #TmpOCCAuthWorkflow with status 'Pending', station ID 0, and the endorser ID retrieved earlier.  
   - Insert all rows from #TmpOCCAuthWorkflow into TAMS_OCC_Auth_Workflow.

8. **Cleanup**  
   - Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - TAMS_OCC_Auth  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_Traction_Power_Detail  
  - TAMS_TAR_Power_Sector  
  - TAMS_Power_Sector  
  - TAMS_Traction_Power  

* **Writes:**  
  - TAMS_OCC_Auth  
  - TAMS_OCC_Auth_Workflow