# Procedure: sp_TAMS_Get_RolesByLineModule

### Purpose
This stored procedure retrieves roles associated with a specific line, track type, and module from the TAMS_Role table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(100) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @Module | NVARCHAR(100) | The module to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Role table.
2. It filters the results based on the provided line number, track type, and module using LIKE operators with the input parameters.
3. The filtered data is then returned.

### Data Interactions
* **Reads:** TAMS_Role