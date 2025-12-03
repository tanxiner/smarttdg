# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_20220303_M

### Purpose
Return a list of TAR applicants for a specified line, sector, and date range, including status and colour information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier |
| @ToAccessDate | NVARCHAR(20) | Upper bound of access date filter |
| @FromAccessDate | NVARCHAR(20) | Lower bound of access date filter |
| @TARType | NVARCHAR(20) | TAR type filter (optional) |
| @SectorID | INT | Sector identifier to limit results |

### Logic Flow
1. **Current Date Calculation** – Convert the current system date to a `DATETIME` value (`@CurrDate`) for use in date comparisons.  
2. **Temp Table Setup** – Create two temporary tables:  
   * `#TmpSector` holds sector metadata for the requested line.  
   * `#TmpAppList` holds applicant details that match the filters.  
   Both tables are truncated to ensure they start empty.  
3. **Sector Population** – Insert into `#TmpSector` all active sectors for the supplied line whose effective period includes `@CurrDate`.  
   * `Direction` is set to 1 for sectors marked ‘BB’ or ‘NB’, otherwise 2.  
4. **Applicant List Population** – Insert into `#TmpAppList` a cross‑join of `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector` where:  
   * The TAR is linked to a sector and a workflow status.  
   * The workflow type is ‘TARWFStatus’.  
   * The TAR’s line matches the supplied line and its status ID is non‑zero.  
   * The sector is active and its effective period includes `@CurrDate`.  
   * The TAR’s access date falls between the converted `@ToAccessDate` and `@FromAccessDate`.  
   * The TAR type matches `@TARType` if supplied.  
   * `Direction` is again mapped to 1 or 2 based on the sector’s direction value.  
   * Colour code is defaulted to an empty string if null.  
5. **Result Selection** – From `#TmpAppList`, select all columns except sector fields, filter by the supplied `@SectorID`, group by the unique applicant identifiers, and order by `TARID`.  
6. **Cleanup** – Drop the temporary tables `#TmpSector` and `#TmpAppList`.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`  
* **Writes:** Temporary tables `#TmpSector`, `#TmpAppList` (created, truncated, populated, then dropped)