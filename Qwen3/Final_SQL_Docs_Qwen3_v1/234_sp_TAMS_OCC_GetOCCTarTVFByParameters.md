# Procedure: sp_TAMS_OCC_GetOCCTarTVFByParameters

### Purpose
This stored procedure retrieves and updates TVF (Traffic Volume Forecast) data for a specified station and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @StationId | int | The ID of the station to retrieve TVF data for. |
| @AccessDate | date | The access date to filter TVF data by. |

### Logic Flow
1. The procedure starts by clearing temporary tables #TMP_TVF and #TMP_TAR_TVF.
2. It then inserts data from TAMS_TAR, TAMS_TAR_TVF, and TAMS_TOA tables into the temporary tables based on the specified station ID and access date.
3. A cursor is created to iterate through the data in #TMP_TVF.
4. For each row in the cursor, it checks if a corresponding record exists in #TMP_TAR_TVF with the same ID. If not, it inserts a new record into #TMP_TAR_TVF based on the TVF direction ('XB' or 'BB').
5. If a corresponding record does exist in #TMP_TAR_TVF, it updates the existing record by setting the appropriate bit for the TVF direction.
6. Finally, it selects all records from #TMP_TAR_TVF and deallocates the cursor.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_TVF, TAMS_TOA tables
* **Writes:** #TMP_TVF, #TMP_TAR_TVF tables