# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_M

### Purpose
Creates OCC authorization records for a specified line and access date, determining buffer and power status from TAR sector data and preparing workflow entries.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., DTL, NEL) |
| @AccessDate | NVARCHAR(20) | Optional access date; if omitted, the current date is used with a 06:00:00 cutoff to decide operation and access dates |

### Logic Flow
1. **Determine Dates**  
   * If @AccessDate is not supplied, compare the current time to a 06:00:00 cutoff.  
   * If after the cutoff, set the operation date to today and the access date to tomorrow; otherwise set the operation date to yesterday and the access date to today.  
   * If @AccessDate is supplied, set the operation date to the day before the supplied date and the access date to the supplied date.

2. **Check Existing Authorizations**  
   * Count OCC authorization records for the chosen line and derived access date.  
   * If any exist, the procedure ends early (no new records are created).

3. **Retrieve Workflow Context**  
   * Find the active workflow ID for the line with type OCCAuth.  
   * From the endorser table, obtain the first‑level endorser ID and the current workflow status ID.

4. **Create Temporary Tables**  
   * #TmpTARSectors – holds sector details for the line.  
   * #TmpOCCAuth – holds candidate OCC authorization rows.  
   * #TmpOCCAuthWorkflow – holds workflow rows to be inserted.

5. **Populate #TmpTARSectors**  
   * For line DTL: select sectors from TAMS_TAR, TAMS_TAR_Sector, and TAMS_Traction_Power_Detail where TAR status is 8.  
   * For line NEL: select sectors from TAMS_TAR, TAMS_TAR_Power_Sector, and TAMS_Power_Sector where TAR status is 9.  
   * Order the results by traction power ID.

6. **If No Existing Authorizations and Sectors Exist**  
   a. **Insert Candidate Authorizations**  
      * Load #TmpOCCAuth with active traction power records for the line, setting default values for remarks, status, buffer, and power flags.  
   b. **Adjust Buffer and Power Flags**  
      * For each record in #TmpOCCAuth, look up matching sectors in #TmpTARSectors.  
      * If a matching sector exists, set IsBuffer and PowerOn based on the sector’s IsBuffer and PowerOn values.  
      * If no matching sector, set both flags to 0.  
   c. **Prepare Workflow Rows**  
      * For each existing OCC authorization record that matches the line, operation date, and access date, insert a row into #TmpOCCAuthWorkflow with status “Pending”, the endorser ID, and current timestamps.

7. **Output and Cleanup**  
   * Return the contents of #TmpOCCAuth and #TmpTARSectors for debugging or reporting.  
   * Drop the temporary tables.

### Data Interactions
* **Reads**  
  - TAMS_OCC_Auth  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_Traction_Power_Detail  
  - TAMS_Traction_Power  
  - TAMS_TAR_Power_Sector  
  - TAMS_Power_Sector  

* **Writes**  
  - (Intended) TAMS_OCC_Auth (commented out but logically inserted)  
  - (Intended) TAMS_OCC_Auth_Workflow (commented out but logically inserted)  
  - Temporary tables #TmpTARSectors, #TmpOCCAuth, #TmpOCCAuthWorkflow (created and dropped within the procedure)