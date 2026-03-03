# Procedure: sp_TAMS_TOA_GenURL

### Purpose
This stored procedure generates a URL for each station or depot in the TAMS_Station table, based on whether it is a station or a depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Not applicable |

### Logic Flow
The procedure starts by selecting data from the TAMS_Station table. It then applies a conditional logic to determine whether each station is marked as a station or a depot, and assigns 'Station' or 'Depot' accordingly. The selected data is then returned.

### Data Interactions
* **Reads:** TAMS_Station