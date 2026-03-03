# Procedure: sp_TAMS_Depot_GetTarSectorsByAccessDateAndLine

### Purpose
Retrieve and prepare sector‑tar information for the depot line “NEL” on a specified access date, then propagate colour codes across matching sectors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The date used to filter records by AccessDate. |
| @Line | nvarchar(10) | Optional line identifier; only triggers data retrieval when equal to “NEL”. |

### Logic Flow
1. A temporary table `#TMP` is created to hold the result set.  
2. If the supplied `@Line` equals “NEL”, a SELECT statement pulls rows from `TAMS_Sector`, left‑joined with `TAMS_TAR_Sector` and `TAMS_TAR`.  
   * The join conditions enforce that the sector’s ID matches the sector ID in the tar‑sector table, and that the tar ID matches the tar table.  
   * Filters applied:  
     - `AccessDate` equals the supplied `@AccessDate`.  
     - `TARStatusId` equals 9.  
     - `AccessType` is either “Possession” or “Protection” with `isExclusive` set to 1.  
     - The sector’s line matches `@Line`.  
     - The sector’s track type is “Depot”.  
     - The sector is active (`IsActive = 1`).  
     - The current date falls between the sector’s `EffectiveDate` and `ExpiryDate`.  
   * The resulting rows are inserted into `#TMP` and ordered by the `[Order]` column ascending.  
3. An UPDATE statement runs on `#TMP`. For each row where `SameSector` is not null, the statement copies the `ColourCode` from any row in `#TMP` that has the same `SameSector`, a non‑null `TarNo`, and a non‑null `ColourCode`.  
4. The final SELECT returns all rows from `#TMP`, ordered by `[Order]` ascending.  
5. The temporary table `#TMP` is dropped.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR`  
* **Writes:** None (only temporary table operations)