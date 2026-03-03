# Procedure: sp_TAMS_GetParametersByParaCode

### Purpose
This stored procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode, filtering by effective and expiry dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | nvarchar(50) | The code of the parameter to retrieve |

### Logic Flow
1. The procedure starts by selecting all columns from the TAMS_Parameters table.
2. It filters the results to only include rows where the ParaCode matches the provided @ParaCode.
3. Additionally, it applies two date-based filters: EffectiveDate must be less than or equal to the current date, and ExpiryDate must be greater than or equal to the current date.
4. The final result is ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters table