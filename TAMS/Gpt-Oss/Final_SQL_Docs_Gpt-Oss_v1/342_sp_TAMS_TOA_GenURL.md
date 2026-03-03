# Procedure: sp_TAMS_TOA_GenURL

### Purpose
Generate a list of stations and depots with their line and type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | None | No parameters required |

### Logic Flow
1. Execute a SELECT statement that retrieves data from the TAMS_Station table.  
2. For each row, return three columns:  
   - `PLine`: the value of the `Line` column.  
   - `PLoc`: the value of the `StationName` column.  
   - `PType`: a string that is `'Station'` when `IsStation` equals 1, otherwise `'Depot'`.  
3. The result set is returned to the caller.

### Data Interactions
* **Reads:** TAMS_Station  
* **Writes:** None