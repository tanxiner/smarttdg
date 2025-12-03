# Procedure: sp_TAMS_GetTarStationsByTarId

### Purpose
Retrieve all stations linked to a specified TAR ID, including station details and the TAR association.

### Parameters
| Name     | Type    | Purpose |
| :------- | :------ | :------ |
| @TarId   | integer | Identifier of the TAR for which station data is requested |

### Logic Flow
1. Accept an integer TAR ID, defaulting to 0 if none is supplied.  
2. Query the station table to obtain each station’s ID, line, code, name, and long name.  
3. Join this result with the TAR‑station mapping table on matching station IDs.  
4. Filter the joined rows to those whose TAR ID equals the supplied @TarId.  
5. Order the final list by the station’s defined order value in ascending sequence.  
6. Return the resulting set to the caller.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_Station  
* **Writes:** None