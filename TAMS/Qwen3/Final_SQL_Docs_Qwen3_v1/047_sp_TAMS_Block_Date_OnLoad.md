# Procedure: sp_TAMS_Block_Date_OnLoad

### Purpose
This stored procedure retrieves data from the TAMS_Block_TARDate table based on specified parameters, filtering by line number, track type, and block date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(20) | The line number to filter by. If NULL, all lines are included. |
| @TrackType  | NVARCHAR(50) | The track type to filter by. If NULL, all track types are included. |
| @BlockDate	| NVARCHAR(20) | The block date to filter by. If NULL, all dates are included. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Block_TARDate table.
2. It filters the results based on the provided parameters: line number (@Line), track type (@TrackType), and block date (@BlockDate).
3. The filter conditions use OR operators to include rows that match any of the specified values, or NULL if no value is provided.
4. The procedure orders the filtered results by the block date in descending order (newest dates first).

### Data Interactions
* **Reads:** TAMS_Block_TARDate table