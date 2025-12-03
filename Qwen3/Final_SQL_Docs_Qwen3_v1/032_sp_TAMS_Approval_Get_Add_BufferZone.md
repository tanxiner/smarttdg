# Procedure: sp_TAMS_Approval_Get_Add_BufferZone

The purpose of this stored procedure is to retrieve additional buffer zone information for a given TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TARID for which to retrieve the buffer zone information |

### Logic Flow
1. The procedure starts by selecting data from two tables: TAMS_Sector and TAMS_TAR_Sector.
2. It filters the results to only include rows where the sector ID matches the TARID's associated sector ID, and the IsBuffer flag is set to 1.
3. The results are ordered by the sector ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector