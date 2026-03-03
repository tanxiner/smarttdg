# Procedure: sp_TAMS_OCC_GetTractionsPowerByLine

### Purpose
Retrieve active traction power records for a specified line within the current effective date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Optional line identifier to filter results; if null, no line filter is applied. |

### Logic Flow
1. Accept an optional line identifier.  
2. Query the `TAMS_Traction_Power` table.  
3. Apply a filter where the `Line` column matches the supplied `@Line` value.  
4. Ensure the current date falls between `EffectiveDate` and `ExpiryDate`.  
5. Include only rows marked as active (`IsActive = 1`).  
6. Return the columns `ID`, `Line`, `TractionPowerSection`, `HSCBName`, `TC`, `Train`, and `Order`.  
7. Order the result set by the `Order` column in ascending order.

### Data Interactions
* **Reads:** `dbo.TAMS_Traction_Power`  
* **Writes:** None