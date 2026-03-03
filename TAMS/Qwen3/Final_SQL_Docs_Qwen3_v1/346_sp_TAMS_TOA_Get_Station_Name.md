# Procedure: sp_TAMS_TOA_Get_Station_Name

### Purpose
This stored procedure retrieves the station code from the TAMS_Station table based on a given line and station name.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @StationName | NVARCHAR(20) | The station name to filter by. |

### Logic Flow
1. The procedure starts by selecting the StationCode column from the TAMS_Station table.
2. It filters the results based on two conditions: Line and StationName, which are passed as input parameters (@Line and @StationName).
3. If a match is found, the corresponding station code is returned.

### Data Interactions
* **Reads:** TAMS_Station