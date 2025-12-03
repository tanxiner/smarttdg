# Procedure: sp_TAMS_OCC_GetTarSectorByLineAndTarAccessDate

The procedure retrieves data from the TAMS database for a specific line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve data for. Can be either 'DTL' or 'NEL'. |
| @AccessDate | nvarchar(50) | The access date to filter results by. |

### Logic Flow
1. The procedure first checks if the provided line is 'DTL'.
2. If it is, the procedure retrieves data from the TAMS database for the specified line and access date.
3. The retrieved data includes sector IDs, traction power IDs, and other relevant information.
4. The results are ordered by traction power ID in ascending order.
5. If the provided line is not 'DTL', the procedure checks if it is 'NEL'.
6. If it is, the procedure retrieves data from the TAMS database for the specified line and access date.
7. The retrieved data includes sector IDs, power sector IDs, and other relevant information.
8. The results are ordered by power sector ID in ascending order.

### Data Interactions
* **Reads:** tams_tar, TAMS_TAR_Sector, TAMS_Traction_Power_Detail, TAMS_TAR_Sector_reno, TAMS_Power_Sector