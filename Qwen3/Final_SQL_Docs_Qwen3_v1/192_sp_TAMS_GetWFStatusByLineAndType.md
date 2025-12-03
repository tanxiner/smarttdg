# Procedure: sp_TAMS_GetWFStatusByLineAndType

This procedure retrieves the workflow status information for a specific line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve workflow status for. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @Type | nvarchar(50) | The workflow type to filter by. |

### Logic Flow
1. The procedure starts by selecting the required columns from the TAMS_WFStatus table.
2. It filters the results based on the provided line number, track type, and workflow type.
3. Only records with an IsActive flag set to 1 are included in the results.
4. The results are ordered by the Order column in ascending order.

### Data Interactions
* **Reads:** TAMS_WFStatus table