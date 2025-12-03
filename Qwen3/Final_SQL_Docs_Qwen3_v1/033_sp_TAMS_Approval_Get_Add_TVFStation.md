# Procedure: sp_TAMS_Approval_Get_Add_TVFStation

### Purpose
This stored procedure retrieves information about TVF stations associated with a given TAR ID, including station names and directions, as well as the TVF run mode.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to retrieve TVF station information for. |

### Logic Flow
1. The procedure starts by selecting data from two tables: TAMS_Station and TAMS_TAR_TVF.
2. It joins these tables based on the ID of the TVF station and the TAR ID provided as a parameter.
3. The selected data is ordered by the ID of the TVF station.
4. Next, it retrieves the TVF run mode from the TAMS_TAR table where the ID matches the TAR ID provided as a parameter.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_TVF, and TAMS_TAR tables.
* **Writes:** None