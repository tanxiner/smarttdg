# Procedure: sp_TAMS_GetBlockedTarDates

### Purpose
This stored procedure retrieves blocked TAR dates for a specific line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve blocked TAR dates for. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Block_TARDate table.
2. It filters the data based on the provided line number, track type, and access date.
3. Only records with an IsActive flag set to 1 are included in the results.
4. The selected data is ordered by BlockDate in ascending order.

### Data Interactions
* **Reads:** TAMS_Block_TARDate table