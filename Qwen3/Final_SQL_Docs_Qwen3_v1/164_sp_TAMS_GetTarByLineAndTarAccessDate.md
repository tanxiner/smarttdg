# Procedure: sp_TAMS_GetTarByLineAndTarAccessDate

### Purpose
This stored procedure retrieves data from the TAMS_TAR table based on a specific line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @AccessDate | nvarchar(50) | The access date to filter by. |

### Logic Flow
1. The procedure starts by selecting all columns from the TAMS_TAR table.
2. It then filters the results based on two conditions:
	* The line number must match the value of the @Line parameter.
	* The access date must be equal to the converted datetime value of the @AccessDate parameter, using a specific format (103).
3. If both conditions are met, the procedure returns the corresponding row from the TAMS_TAR table.

### Data Interactions
* **Reads:** TAMS_TAR table