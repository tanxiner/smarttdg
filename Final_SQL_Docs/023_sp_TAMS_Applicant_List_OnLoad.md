# Procedure: sp_TAMS_Applicant_List_OnLoad

### Purpose
Return a two‑pass list of TAR records grouped by sector for a specified line, filtered by access dates and sector activity, separating results by sector direction.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Identifier of the line to query. |
| @ToAccessDate | NVARCHAR(20) | Upper bound of the access date range (inclusive). |
| @FromAccessDate | NVARCHAR(20) | Lower bound of the access date range (inclusive). |
| @TARType | NVARCHAR(20) | Intended filter for TAR type (currently unused). |

### Logic Flow
1. **Current Date Calculation** – Convert the system date to a `DATETIME` value truncated to the day, stored in `@CurrDate`.  
2. **Temp Table Setup** – Create two temporary tables:  
   - `#TmpSector` to hold sector metadata for the requested line.  
   - `#TmpAppList` to hold TAR records that match the line, sector, status, and date criteria.  
3. **Clear Temp Tables** – Truncate both temp tables to ensure they are empty before use.  
4. **Populate Sector Temp Table** – Insert into `#TmpSector` all active sectors on the specified line where the current date falls between `EffectiveDate` and `ExpiryDate`.  
   - `Direction` is set to `1` for sectors marked ‘BB’ or ‘NB’, otherwise `2`.  
   - Results are ordered by the sector’s `[Order]` field.  
5. **Populate Applicant List Temp Table** – Insert into `#TmpAppList` all TAR records that:  
   - Belong to the specified line and track type ‘Mainline’.  
   - Have a non‑zero status ID and a matching workflow status of type ‘TARWFStatus’.  
   - Are linked to an active sector whose current date is within its validity window.  
   - Have an `AccessDate` between the converted `@ToAccessDate` and `@FromAccessDate`.  
   - Include sector information and translate sector direction to `1` or `2` as above.  
6. **First Result Set (Direction = 1)** – Perform a left outer join between `#TmpSector` and `#TmpAppList` on `SectorID`, filter for `Direction = 1`, and return the joined columns ordered by sector order.  
7. **Second Result Set (Direction = 2)** – Repeat the join, filtering for `Direction = 2`, and return the same column set ordered by sector order.  
8. **Cleanup** – Drop the temporary tables `#TmpSector` and `#TmpAppList`.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus  
* **Writes:** #TmpSector, #TmpAppList (temporary tables)