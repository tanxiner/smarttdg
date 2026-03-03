# Procedure: sp_TAMS_GetSectorsByLineAndDirection

### Purpose
This stored procedure retrieves sectors from the TAMS_Sector table based on a specified line and direction, filtering by active status and effective dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @Direction | nvarchar(10) | The direction to filter by. |

### Logic Flow
1. The procedure checks if the provided line is 'DTL' or 'NEL'.
2. If either condition is met, it selects data from the TAMS_Sector table where the specified line and direction match.
3. The selected data is filtered to only include active records with effective dates within the current date range (EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE).
4. The results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Sector table