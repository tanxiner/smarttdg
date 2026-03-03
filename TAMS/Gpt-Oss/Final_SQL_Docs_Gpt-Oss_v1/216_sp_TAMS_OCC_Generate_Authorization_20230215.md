# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215

### Purpose
Creates new OCC authorization records for a specified line (DTL or NEL) for the appropriate operation and access dates, and initiates the corresponding workflow entries.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., 'DTL', 'NEL') for which authorizations are generated. |
| @AccessDate | NVARCHAR(20) | Optional date string; if omitted, the procedure derives the operation and access dates based on the current time and a 6 AM cutoff. |

### Logic Flow
1. **Initialize dates**  
   - Capture current date and time.  
   - Define a 6 AM cutoff.  
   - If @AccessDate is not supplied, determine `@DerOPDate` and `@DerAccessDate` by comparing the current time to the cutoff:  
     * After 6 AM → operation date is today, access date is tomorrow.  
     * Before 6 AM → operation date is yesterday, access date is today.  
   - If @AccessDate is supplied, set operation date to the day before the supplied date and access date to the supplied date.

2. **Check for existing authorizations**  
   - Count rows in `TAMS_OCC_Auth` where `Line` equals @Line and `AccessDate` equals `@DerAccessDate`.  
   - Store the count in `@OCCAuthCtr`.

3. **Retrieve workflow context**  
   - Find the active workflow ID for the line where `WorkflowType` is 'OCCAuth'.  
   - From `TAMS_Endorser`, obtain the first‑level endorser ID and the current workflow status ID for that workflow.

4. **Create temporary tables**  
   - `#TmpTARSectors` holds TAR sector details.  
   - `#TmpOCCAuth` holds candidate OCC authorization rows.  
   - `#TmpOCCAuthWorkflow` holds workflow rows to be inserted.

5. **Load TAR sector data**  
   - For DTL: select sectors from `TAMS_TAR`, `TAMS_TAR_Sector`, and `TAMS_Traction_Power_Detail` where `TARStatusId` is 8.  
   - For NEL: select sectors from `TAMS_TAR`, `TAMS_TAR_Power_Sector`, and `TAMS_Power_Sector` where `TARStatusId` is 9.  
   - All selections filter on the derived access date and the specified line.

6. **Generate base OCC authorizations (if none exist)**  
   - If `@OCCAuthCtr` is zero and there are TAR sectors, insert rows into `#TmpOCCAuth` from `TAMS_Traction_Power` for the line, setting default values (empty remarks, status from workflow, no buffer, power off).  
   - Order the inserts by the `Order` column.

7. **Adjust buffer and power flags**  
   - For each row in `#TmpOCCAuth`, check if a matching TAR sector exists with `IsBuffer = 1`.  
   - If a matching sector is found, update the OCC row’s `IsBuffer` and `PowerOn` flags based on the sector’s `IsBuffer` and `PowerOn` values.  
   - If no matching sector or the sector’s flags differ, set `IsBuffer` to 0 and `PowerOn` to 0.

8. **Persist OCC authorizations**  
   - Insert all rows from `#TmpOCCAuth` into `TAMS_OCC_Auth`, copying all columns except the auto‑generated `UpdatedOn` and `UpdatedBy`.

9. **Create workflow entries**  
   - For each newly inserted OCC authorization, insert a row into `#TmpOCCAuthWorkflow` with status 'Pending', station ID 0, and the current user (ID 1).  
   - After populating the temp table, insert all rows into `TAMS_OCC_Auth_Workflow`.

10. **Cleanup**  
    - Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_OCC_Auth` (count check)  
  - `TAMS_Workflow` (workflow lookup)  
  - `TAMS_Endorser` (endorser and status lookup)  
  - `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_Traction_Power_Detail` (DTL sector data)  
  - `TAMS_TAR_Power_Sector`, `TAMS_Power_Sector` (NEL sector data)  
  - `TAMS_Traction_Power` (base traction power rows)

* **Writes:**  
  - `TAMS_OCC_Auth` (new authorization records)  
  - `TAMS_OCC_Auth_Workflow` (workflow records for each authorization)