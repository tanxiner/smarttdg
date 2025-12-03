# Procedure: sp_TAMS_GetTarOtherProtectionByPossessionId

### Purpose
Retrieves all other protection records linked to a specific possession.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Identifier of the possession whose protection records are requested |

### Logic Flow
1. Accepts an integer `@PossessionId` (defaults to 0 if not supplied).  
2. Queries the `TAMS_Possession_OtherProtection` table for rows where the `possessionid` column matches the supplied `@PossessionId`.  
3. Returns the columns `id`, `possessionid`, and `otherprotection` for each matching row.  
4. Results are ordered by `id` in ascending order.

### Data Interactions
* **Reads:** TAMS_Possession_OtherProtection  
* **Writes:** None