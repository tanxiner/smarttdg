# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection_SameSector

### Purpose
Retrieve sector and tariff details for a specified line and direction on a given access date, applying different status filters for DTL and NEL lines, and propagate colour codes to sectors that share the same sector identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The date on which access is evaluated. |
| @Line | nvarchar(10) | Identifier of the line; determines which status filter to apply (DTL or NEL). |
| @Direction | nvarchar(10) | Direction of travel to filter sectors. |

### Logic Flow
1. **Create Temporary Table**  
   A table `#TMP` is created to hold intermediate results with columns for sector, tariff, access details, and flags.

2. **Conditional Data Insertion**  
   - If `@Line` equals `DTL`:  
     - Rows are inserted from `TAMS_Sector` joined with `TAMS_TAR_Sector` and `TAMS_TAR`.  
     - Filters applied: `AccessDate = @AccessDate`, `TARStatusId = 8`, access type is `Possession` or exclusive possession, `Line = @Line`, `Direction = @Direction`, active status, and effective date range covering today.  
   - Else if `@Line` equals `NEL`:  
     - Similar insertion logic but with `TARStatusId = 9`.  
   - (Commented code for alternate logic is ignored.)

3. **Colour Code Propagation**  
   - For rows where `SameSector` is not null, the `ColourCode` column is updated to the value found in any row of `#TMP` that has non‑null `SameSector`, `TarNo`, and `ColourCode`.  
   - This ensures all sectors sharing the same sector identifier receive the same colour code.

4. **Return Result Set**  
   - All rows from `#TMP` are selected and returned to the caller.

5. **Cleanup**  
   - The temporary table `#TMP` is dropped.

### Data Interactions
* **Reads:** `TAMS_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR`  
* **Writes:** Temporary table `#TMP` (insert, update, drop)