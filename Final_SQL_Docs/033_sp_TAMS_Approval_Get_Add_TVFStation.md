# Procedure: sp_TAMS_Approval_Get_Add_TVFStation

### Purpose
Retrieve TVF station details and the TVF run mode for a specified TARID.

### Parameters
| Name   | Type   | Purpose |
| :----- | :----- | :------ |
| @TARID | BIGINT | Identifier for the TAR record whose TVF stations and mode are requested |

### Logic Flow
1. The procedure receives a TARID value.  
2. It performs a join between the station table and the TVF association table to gather all stations linked to the given TARID.  
   - For each matching record, it selects the station name, the TVF direction, and the TVF association ID.  
   - The results are ordered by the station ID.  
3. After returning the station list, the procedure queries the TAR table to obtain the TVF mode for the same TARID.  
4. The two result sets are returned to the caller.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_TVF, TAMS_TAR  
* **Writes:** None