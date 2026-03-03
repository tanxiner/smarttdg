# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection

### Purpose
Retrieves sector information for a specified line and access date, enriches it with TAR details, and propagates colour codes across related sectors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The date on which access is evaluated. |
| @Line | nvarchar(10) | Identifier of the line (e.g., DTL, NEL). |
| @TrackType | nvarchar(50) | Type of track to filter sectors. |
| @Direction | nvarchar(10) | Direction of travel (currently unused in filtering). |

### Logic Flow
1. A temporary table `#TMP` is created to hold sector and TAR data.  
2. If `@Line` equals `DTL`, rows are inserted into `#TMP` by selecting from `TAMS_Sector` joined with `TAMS_TAR_Sector` and `TAMS_TAR`.  
   - Only sectors where `AccessDate` matches `@AccessDate`, `TARStatusId` is 8, and the access type is either 'Possession' or the TAR is exclusive are included.  
   - Additional filters: sector line equals `@Line`, sector track type equals `@TrackType`, sector is active, and the current date falls between the sector’s effective and expiry dates.  
   - Results are ordered by the `[Order]` column.  
3. If `@Line` equals `NEL`, a similar insertion occurs, but `TARStatusId` is 9 instead of 8.  
4. After insertion, an `UPDATE` statement sets the `ColourCode` for rows whose `SameSector` value matches a row that already has a non‑null `ColourCode`.  
5. The procedure selects all rows from `#TMP`, ordering them by `[Order]`.  
6. Finally, the temporary table is dropped.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR`  
* **Writes:** Temporary table `#TMP` (insert, update, drop)