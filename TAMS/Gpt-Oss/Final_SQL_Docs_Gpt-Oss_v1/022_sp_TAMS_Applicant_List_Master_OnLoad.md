# Procedure: sp_TAMS_Applicant_List_Master_OnLoad

### Purpose
Return two ordered lists of sectors for a specified line and track type, split by direction (BB/NB vs others).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier to filter sectors |
| @TrackType | NVARCHAR(50) | Track type to filter sectors |
| @ToAccessDate | NVARCHAR(20) | Intended filter for upper bound of access dates (currently unused) |
| @FromAccessDate | NVARCHAR(20) | Intended filter for lower bound of access dates (currently unused) |
| @TARType | NVARCHAR(20) | Intended filter for TAR type (currently unused) |

### Logic Flow
1. Capture the current date in `@CurrDate` (date only).  
2. Create a temporary table `#TmpSector` with columns for line, sector ID, sector string, order, and direction.  
3. Truncate `#TmpSector` to ensure it is empty.  
4. Populate `#TmpSector` with sectors from `TAMS_Sector` that match the supplied `@Line` and `@TrackType`, are active, and whose effective period includes `@CurrDate`.  
   - The `Direction` column is set to 1 when the sector’s direction is 'BB' or 'NB'; otherwise it is set to 2.  
5. Produce the first result set: select distinct sectors from `#TmpSector` where `Direction = 1`, grouped by all columns and ordered by `SectorOrder`.  
6. Produce the second result set: select distinct sectors from `#TmpSector` where `Direction = 2`, grouped by all columns and ordered by `SectorOrder`.  
7. Drop the temporary table `#TmpSector`.

### Data Interactions
* **Reads:** `TAMS_Sector`  
* **Writes:** Temporary table `#TmpSector` (created and truncated within the procedure)