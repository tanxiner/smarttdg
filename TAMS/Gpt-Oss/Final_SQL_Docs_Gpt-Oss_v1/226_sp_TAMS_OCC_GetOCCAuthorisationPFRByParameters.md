# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters

### Purpose
Retrieve and enrich OCC authorisation PFR records for the DTL line, incorporating endorser workflow status and timestamps.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting data (unused in logic). |
| @Line | nvarchar(10) | Target line; only 'DTL' triggers processing. |
| @TrackType | nvarchar(50) | Track type filter for traction power and duty roster look‑ups. |
| @OperationDate | date | Date of the operation to match OCC authorisation records. |
| @AccessDate | date | Date of access to match OCC authorisation records. |

### Logic Flow
1. **Variable Declaration** – Local variables are defined for workflow, authorisation, endorser details, status, timestamps, and station names.  
2. **Temporary Tables Creation** – Three temp tables are created:  
   * #TMP for traction power IDs and concatenated station names.  
   * #TMP_Endorser for endorser IDs, levels, roles, and titles.  
   * #TMP_OCCAuthPFR for the final result set, initially populated with base OCC authorisation data.  
3. **DTL Line Check** – If @Line equals 'DTL', the procedure proceeds; otherwise it exits without output.  
4. **Workflow Identification** – The workflow ID for the DTL line and specified track type is retrieved from TAMS_Workflow.  
5. **Endorser Population** – #TMP_Endorser is filled with endorser records that belong to the DTL line, the identified workflow, and have RoleId 14.  
6. **Traction Power Population** – #TMP is populated with traction power IDs and a semicolon‑separated list of station names linked to each traction power.  
7. **Base OCC Authorisation Load** – #TMP_OCCAuthPFR is filled by joining TAMS_Traction_Power, #TMP, and TAMS_OCC_Auth. Only active authorisations matching the operation and access dates are included. The duty roster is filtered for shift 3 on the operation date.  
8. **Cursor over OCCAuthIDs** – A cursor iterates through each OCCAuthID in #TMP_OCCAuthPFR.  
9. **Inner Cursor over Endorsers** – For each OCCAuthID, another cursor iterates through all endorser records in #TMP_Endorser.  
10. **Endorser‑Specific Logic** – For each endorser ID (100, 101, 102, 103, 108, 109, 111, 113, 114) the procedure:  
    * Retrieves the workflow status, action timestamp, and, for endorser 114, the FISTestResult from TAMS_OCC_Auth_Workflow.  
    * Depending on the status value (Pending, Completed, N.A.), updates the corresponding column in #TMP_OCCAuthPFR with either the status text, the formatted action time, or a composite string that includes the station name when applicable.  
    * Resets temporary status variables after each update.  
11. **Cursor Cleanup** – Both cursors are closed and deallocated.  
12. **Result Output** – All rows from #TMP_OCCAuthPFR are selected and returned to the caller.  
13. **Temp Table Drop** – The three temporary tables are dropped.

### Data Interactions
* **Reads:**  
  * TAMS_Workflow  
  * TAMS_Endorser  
  * TAMS_Traction_Power_Detail  
  * TAMS_Station  
  * TAMS_Traction_Power  
  * TAMS_OCC_Auth  
  * TAMS_OCC_Duty_Roster  
  * TAMS_OCC_Auth_Workflow  
* **Writes:** None to permanent tables; only temporary tables are created, populated, and dropped.