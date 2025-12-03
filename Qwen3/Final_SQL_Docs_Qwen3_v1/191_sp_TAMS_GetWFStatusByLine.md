# Procedure: sp_TAMS_GetWFStatusByLine

### Purpose
This stored procedure retrieves the workflow status information for a specific line from the TAMS_WFStatus table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve workflow status information for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_WFStatus table.
2. It filters the results to only include rows where the Line column matches the input @Line parameter and the IsActive flag is set to 1.
3. The selected columns are then ordered in ascending order based on the [Order] column.

### Data Interactions
* **Reads:** TAMS_WFStatus table