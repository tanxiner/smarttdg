# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLine

### Purpose
Retrieve sector information for a specified line and access date, applying line‑specific status filters and propagating colour codes across matching sectors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The date on which access is evaluated. |
| @Line | nvarchar(10) | Identifier of the line (e.g., 'DTLD', 'NELD'); defaults to NULL. |

### Logic Flow
1. **Create a temporary table (#TMP)** to hold the result set with columns for sector details, access metadata, and visual attributes.  
2. **Conditional data loading**  
   - If @Line equals 'DTLD':  
     - Insert rows from `TAMS_Sector` joined with `TAMS_TAR_Sector` and `TAMS_TAR`.  
     - Apply filters: `AccessDate` matches @AccessDate, `TARStatusId` = 8, `AccessType` is 'Possession' or `isExclusive` = 1, `IsActive` = 1, and the sector’s effective period covers the current date.  
   - Else if @Line equals 'NELD':  
     - Similar insert logic but with `TARStatusId` = 9.  
   - Both branches order the inserted rows by `[Order]` ascending.  
3. **Propagate colour codes**  
   - Update each row in #TMP where `SameSector` is not null, `TarNo` is not null, and `ColourCode` is not null.  
   - Set its `ColourCode` to the value found in any row that satisfies the same non‑null conditions, effectively copying the colour code across matching sectors.  
4. **Return the populated set**  
   - Select all rows from #TMP ordered by `[Order]` ascending.  
5. **Cleanup**  
   - Drop the temporary table #TMP.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR`  
* **Writes:** Temporary table `#TMP` (inserted, updated, then dropped)