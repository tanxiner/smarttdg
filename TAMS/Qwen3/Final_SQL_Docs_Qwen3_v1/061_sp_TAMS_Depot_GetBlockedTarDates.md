# Procedure: sp_TAMS_Depot_GetBlockedTarDates

### Purpose
This stored procedure retrieves blocked TAR dates for a specific line from the TAMS_Block_TARDate table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve blocked TAR dates for. |
| @AccessDate | date | The access date to filter blocked TAR dates by. |

### Logic Flow
1. The procedure starts by selecting the ID, Line, BlockDate, and BlockReason columns from the TAMS_Block_TARDate table.
2. It filters the results based on the provided Line (@Line) and AccessDate (@AccessDate).
3. Only records with IsActive = 1 are included in the results.
4. The results are ordered by BlockDate in ascending order.

### Data Interactions
* **Reads:** TAMS_Block_TARDate table