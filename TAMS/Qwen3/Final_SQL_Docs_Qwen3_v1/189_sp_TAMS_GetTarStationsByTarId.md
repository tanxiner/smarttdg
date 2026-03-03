# Procedure: sp_TAMS_GetTarStationsByTarId

### Purpose
This stored procedure retrieves a list of stations associated with a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID for which to retrieve associated stations |

### Logic Flow
The procedure starts by joining the TAMS_Station table with the TAMS_TAR_Station table on two conditions: the station's ID matches the TAR Station ID, and the TAR ID in the join condition matches the provided @TarId parameter. It then selects specific columns from both tables and orders the results by a column named [Order] in ascending order.

### Data Interactions
* **Reads:** TAMS_Station table, TAMS_TAR_Station table