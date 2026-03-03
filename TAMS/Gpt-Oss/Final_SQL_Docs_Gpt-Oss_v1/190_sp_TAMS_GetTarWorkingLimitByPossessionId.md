# Procedure: sp_TAMS_GetTarWorkingLimitByPossessionId

### Purpose
Retrieve working limit records for a specified possession.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Identifier used to filter records by possession |

### Logic Flow
1. Accepts an integer `@PossessionId` (defaults to 0 if not supplied).  
2. Executes a SELECT that retrieves `id`, `possessionid`, and `redflashinglampsloc` from `TAMS_Possession_WorkingLimit`.  
3. Filters rows where `possessionid` equals the supplied `@PossessionId`.  
4. Orders the result set by `id` in ascending order.  
5. Returns the resulting rows to the caller.

### Data Interactions
* **Reads:** TAMS_Possession_WorkingLimit  
* **Writes:** None