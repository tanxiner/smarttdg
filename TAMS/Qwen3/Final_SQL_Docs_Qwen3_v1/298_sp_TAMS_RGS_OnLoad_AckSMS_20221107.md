# Procedure: sp_TAMS_RGS_OnLoad_AckSMS_20221107

### Purpose
This stored procedure retrieves and formats specific data from the TAMS_TOA and TAMS_TAR tables to acknowledge SMS notifications for a given TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Target Access Record) for which to retrieve acknowledgement data. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA and TAMS_TAR tables.
2. It filters the results based on the provided TARID, ensuring that only matching records are returned.
3. The selected data is then formatted into a readable format for acknowledgement purposes.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR