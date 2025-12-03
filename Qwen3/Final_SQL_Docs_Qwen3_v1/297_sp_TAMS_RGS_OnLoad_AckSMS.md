# Procedure: sp_TAMS_RGS_OnLoad_AckSMS

The procedure retrieves and formats data from TAMS_TOA and TAMS_TAR tables to display access type, grant time, protection limit time, TAR number, and TOANumber for a specific TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR to retrieve data for. |

### Logic Flow
1. The procedure starts by selecting data from TAMS_TOA and TAMS_TAR tables.
2. It filters the data based on the provided TARID, ensuring only relevant records are retrieved.
3. The selected data is then formatted into a readable format, including access type, grant time, protection limit time, TAR number, and TOANumber.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR