# Procedure: sp_TAMS_Depot_GetTarSectorsByTarId

### Purpose
Retrieve all non‑buffer sectors associated with a specific TAR, ordered by the TAR’s internal sequence and sector name.

### Parameters
| Name   | Type    | Purpose |
| :----- | :------ | :------ |
| @TarId | integer | Identifier of the TAR whose sectors are requested; defaults to 0 if omitted. |

### Logic Flow
1. Accept the @TarId parameter.  
2. Join the sector table with the TAR‑sector mapping table on matching sector IDs.  
3. Join the resulting set with the TAR table on matching TAR IDs.  
4. Apply a filter to keep only rows where the mapping’s TARId equals the supplied @TarId and the mapping’s IsBuffer flag is not set to 1.  
5. Return the selected columns (ID, Line, Direction, Sector, TARNo, AccessDate, AccessType, SectorId, IsBuffer, ColourCode, IsGap).  
6. Order the output first by the mapping’s Order column, then by the sector name ascending.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR  
* **Writes:** None