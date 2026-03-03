# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_001

### Purpose
Retrieves and compiles OCC authorisation status for a specific line and operation dates, applying endorser workflow logic to populate status fields for each authorisation record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user requesting data (used only in commented code). |
| @Line | nvarchar(10) | Target line for which authorisations are fetched. |
| @OperationDate | date | Date of the operation to filter authorisations. |
| @AccessDate | date | Date of access to filter authorisations. |
| @RosterCode | nvarchar(50) | Code indicating the roster type (e.g., TC, CC, PFR) used to determine which status fields are updated. |

### Logic Flow
1. **Workflow Identification**  
   - Determine the active workflow ID for the specified line where the workflow type is 'OCCAuth' and the current date falls between its effective and expiry dates.

2. **Endorser Preparation**  
   - Populate a temporary table with endorser details (ID, line, level, role, title) for the 'NEL' line and the identified workflow, ordered by level.

3. **Authorisation Record Assembly**  
   - Build a temporary table of authorisation records by joining traction power data with OCC authorisation data.  
   - Include base fields such as traction power ID, line, section, HSCB name, train, and flags.  
   - Initialise all status columns (e.g., TrainClearCert_TC, MainlineTractionCurrentSwitchOff_Request_CC, etc.) with empty strings.

4. **Cursor Processing of Authorisations**  
   - Iterate over each authorisation ID in the temporary authorisation table.

5. **Cursor Processing of Endorsers**  
   - For each authorisation, iterate over every endorser from the endorser temporary table.  
   - For each endorser, retrieve the workflow status and action timestamp from the workflow table where the authorisation ID and endorser ID match.  
   - Based on the endorser ID, roster code, and workflow status, update the corresponding status column in the authorisation temporary table:
     - If status is 'Pending' and the roster code matches the column’s roster type, set the column to 'Pending'.
     - If status is 'Pending' and the roster code does not match, clear the column.
     - If status is 'Completed', set the column to the time part of the action timestamp.
     - For specific endorser IDs (121, 125, 128, 129) also handle 'N.A.' status by writing the literal string 'N.A.' into the column.
   - Reset temporary status variables after each endorser.

6. **Finalize**  
   - After processing all endorsers for an authorisation, move to the next authorisation until all are processed.

7. **Result Output**  
   - Return the fully populated temporary authorisation table as the procedure result set.

8. **Cleanup**  
   - Drop the temporary tables used for endorsers and authorisations.

### Data Interactions
* **Reads:**  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_Traction_Power  
  - TAMS_OCC_Auth  
  - TAMS_OCC_Auth_Workflow  

* **Writes:**  
  - Inserts into temporary tables #TMP_Endorser and #TMP_OCCAuthNEL.  
  - Updates within #TMP_OCCAuthNEL based on workflow status.  
  - Drops temporary tables #TMP_Endorser and #TMP_OCCAuthNEL at completion.