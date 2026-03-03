# Procedure: sp_TAMS_OCC_GetOCCTarTVFByParameters

### Purpose
Return a list of tariff records for a given station and access date, indicating whether each tariff has an outbound (XB) or inbound (BB) TVF direction.

### Parameters
| Name          | Type | Purpose |
| :---          | :--- | :--- |
| @StationId    | int  | Identifier of the TVF station to filter records. |
| @AccessDate   | date | Date of tariff access to filter records. |

### Logic Flow
1. **Setup** – Declare local variables and create two temporary tables: `#TMP_TVF` (raw TVF data) and `#TMP_TAR_TVF` (aggregated direction flags).  
2. **Reset Temp Tables** – Truncate both temporary tables to ensure they are empty before use.  
3. **Populate Raw Data** – Insert into `#TMP_TVF` all tariff rows that match the supplied station and access date.  
   - Join `TAMS_TAR` with `TAMS_TAR_TVF` on `TARID`.  
   - Left‑join `TAMS_TOA` (unused in the insert but included in the original query).  
   - Capture `Id`, `TarNo`, `PersonInCharge`, `TVFDirection`, and `TVFMode`.  
4. **Cursor Processing** – Open a cursor over `#TMP_TVF` ordered by `Id`.  
   - For each row, check if the `Id` already exists in `#TMP_TAR_TVF`.  
   - **If not present**:  
     - Insert a new record into `#TMP_TAR_TVF`.  
     - Set `TVFDirection1` to 1 and `TVFDirection2` to 0 when `TVFDirection` is `'XB'`.  
     - Set `TVFDirection1` to 0 and `TVFDirection2` to 1 when `TVFDirection` is `'BB'`.  
   - **If present**:  
     - Update the existing record’s direction bit to 1 based on the current `TVFDirection`.  
5. **Finalize** – Close and deallocate the cursor.  
6. **Return Result** – Select all rows from `#TMP_TAR_TVF`, providing the aggregated direction flags for each tariff.  
7. **Cleanup** – Drop the temporary tables `#TMP_TVF` and `#TMP_TAR_TVF`.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_TAR_TVF`, `TAMS_TOA`  
* **Writes:** `#TMP_TVF`, `#TMP_TAR_TVF` (temporary tables only)