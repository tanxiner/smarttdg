# Procedure: sp_TAMS_TOA_Get_Station_Name

### Purpose
Retrieve the station code for a specified line and station name.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line identifier to filter stations. |
| @StationName | NVARCHAR(20) | The name of the station to locate. |

### Logic Flow
1. Accept the line and station name parameters.  
2. Query the `TAMS_Station` table for a row where the `Line` column equals the supplied line and the `StationName` column equals the supplied station name.  
3. Return the `StationCode` value from the matching row(s).

### Data Interactions
* **Reads:** `TAMS_Station`  
* **Writes:** None