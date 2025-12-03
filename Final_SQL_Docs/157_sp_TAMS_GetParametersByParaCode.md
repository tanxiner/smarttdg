# Procedure: sp_TAMS_GetParametersByParaCode

### Purpose
Retrieve active parameter records for a given ParaCode.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaCode | nvarchar(50) | Optional filter to return only rows matching this ParaCode; if NULL, no rows are returned. |

### Logic Flow
1. The procedure receives an optional @ParaCode value.  
2. It queries the TAMS_Parameters table.  
3. The WHERE clause limits results to rows where ParaCode equals the supplied @ParaCode.  
4. It further restricts rows to those whose EffectiveDate is on or before the current date and whose ExpiryDate is on or after the current date, ensuring only currently valid parameters are returned.  
5. The selected columns are ID, ParaType, ParaCode, ParaDesc, ParaValue1, ParaValue2, ParaValue3, ParaDatetime, ParaDate, ParaTime, and [Order].  
6. Results are ordered ascending by the [Order] column.

### Data Interactions
* **Reads:** TAMS_Parameters
* **Writes:** None