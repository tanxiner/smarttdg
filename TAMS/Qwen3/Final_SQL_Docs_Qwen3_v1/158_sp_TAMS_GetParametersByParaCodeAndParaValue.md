# Procedure: sp_TAMS_GetParametersByParaCodeAndParaValue

This procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode and ParaValue.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | nvarchar(50) | Specifies the ParaCode to filter by. |

### Logic Flow
1. The procedure starts by selecting all columns from the TAMS_Parameters table.
2. It filters the results based on the provided @ParaCode and @ParaValue, ensuring that both conditions are met.
3. Additionally, it applies date constraints: EffectiveDate must be less than or equal to the current date, and ExpiryDate must be greater than or equal to the current date.
4. The final step is to sort the results in ascending order by the [Order] column.

### Data Interactions
* **Reads:** TAMS_Parameters table