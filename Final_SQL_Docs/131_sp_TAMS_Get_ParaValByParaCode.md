# Procedure: sp_TAMS_Get_ParaValByParaCode

### Purpose
Retrieve active parameter records that match a specified code and optional value pattern.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @paraCode | NVARCHAR(200) | The parameter code to filter by. |
| @paraValue1 | NVARCHAR(200) | Optional pattern for ParaValue1; supports SQL LIKE syntax. |

### Logic Flow
1. The procedure begins by selecting all columns from the `TAMS_Parameters` table.  
2. It filters rows where `ParaCode` equals the supplied `@paraCode`.  
3. It ensures the current date (`GETDATE()`) falls between `EffectiveDate` and `ExpiryDate`, inclusive, so only currently valid parameters are returned.  
4. It applies a `LIKE` comparison on `ParaValue1` using the supplied `@paraValue1` pattern, allowing partial matches.  
5. The resulting set is ordered first by `ParaValue1`, then by `ParaValue2`, and finally by the `[Order]` column.  

### Data Interactions
* **Reads:** `TAMS_Parameters`  
* **Writes:** None