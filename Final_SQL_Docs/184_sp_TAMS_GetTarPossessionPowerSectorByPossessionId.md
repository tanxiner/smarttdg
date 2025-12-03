# Procedure: sp_TAMS_GetTarPossessionPowerSectorByPossessionId

### Purpose
Retrieves power sector details for a specified possession.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Identifier of the possession to query |

### Logic Flow
1. Execute a SELECT statement that retrieves `id`, `possessionid`, `powersector`, `noofscd`, and `breakerout` from `TAMS_Possession_PowerSector` where `possessionid` equals the supplied `@PossessionId`.  
2. Return the result set ordered by `id` ascending.

### Data Interactions
* **Reads:** TAMS_Possession_PowerSector  
* **Writes:** None