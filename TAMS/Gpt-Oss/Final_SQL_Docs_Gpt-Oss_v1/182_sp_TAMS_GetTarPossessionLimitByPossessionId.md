# Procedure: sp_TAMS_GetTarPossessionLimitByPossessionId

### Purpose
Retrieve all protection limit records for a specified possession.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Identifier of the possession to filter records by |

### Logic Flow
1. Accept an integer `@PossessionId` (defaults to 0 if not supplied).  
2. Query the `TAMS_Possession_Limit` table for rows where the `possessionid` column equals the supplied `@PossessionId`.  
3. Return the columns `id`, `possessionid`, `typeofprotectionlimit`, and `redflashinglampsloc`.  
4. Order the result set by `id` in ascending order.

### Data Interactions
* **Reads:** TAMS_Possession_Limit  
* **Writes:** None  

---