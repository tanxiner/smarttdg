# Procedure: sp_TAMS_UsersManual

### Purpose
This stored procedure retrieves user manual data from the TAMS_Parameters table based on a specific parameter code and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | The parameter code to filter results |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Parameters table.
2. It filters the data based on the ParaCode column, which must match 'TOAUM'.
3. Additionally, it applies a date range filter using the EffectiveDate and ExpiryDate columns, ensuring that the data is only returned for dates within this period.
4. The filtered data is then retrieved and returned as part of the procedure's output.

### Data Interactions
* **Reads:** TAMS_Parameters table