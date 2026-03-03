# Procedure: sp_TAMS_Depot_GetPossessionDepotSectorByPossessionId

### Purpose
Retrieve all depot sector records associated with a specific possession.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Identifier of the possession to filter depot sectors |

### Logic Flow
1. Accept an integer `@PossessionId` (default 0).  
2. Query the table `TAMS_Possession_DepotSector`.  
3. Return rows where `possessionid` equals the supplied `@PossessionId`.  
4. Order the result set by `ID` in ascending order.

### Data Interactions
* **Reads:** `TAMS_Possession_DepotSector`  
* **Writes:** None