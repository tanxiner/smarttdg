# Procedure: sp_Get_TypeOfWorkByLine

### Purpose
This stored procedure retrieves data from the TAMS_Type_Of_Work table based on a specified line and track type, filtering for active records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @TrackType | nvarchar(50) | The track type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Type_Of_Work table.
2. It filters the results based on the provided @Line and @TrackType parameters, ensuring only active records are returned.
3. The filtered data is then ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Type_Of_Work