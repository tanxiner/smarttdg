# Procedure: sp_TAMS_GetTarSectorsByTarId

### Purpose
Retrieve all non‑buffer sectors associated with a specific TAR, ordered by the TAR’s internal sequence and sector name.

### Parameters
| Name     | Type    | Purpose |
| :---     | :---    | :---    |
| @TarId   | integer | Identifier of the TAR whose sectors are requested |

### Logic Flow
1. Accept an integer `@TarId` (defaults to 0 if omitted).  
2. Query the `TAMS_Sector` table for sector details.  
3. Join `TAMS_TAR_Sector` on matching `SectorId` to link sectors to TARs.  
4. Join `TAMS_TAR` on matching `TARId` to confirm the TAR record.  
5. Apply a filter so that only rows where `c.TARId` equals the supplied `@TarId` are considered.  
6. Exclude any sector that is marked as a buffer (`c.IsBuffer <> 1`).  
7. Return the selected columns: `ID, Line, Direction, Sector, TARNo, AccessDate, AccessType, SectorId, IsBuffer, ColourCode, IsGap`.  
8. Order the result set first by the TAR’s internal `[Order]` field, then alphabetically by `Sector`.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR`  
* **Writes:** None