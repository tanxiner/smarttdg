# Procedure: sp_TAMS_GetParametersByParaCodeAndParaValuewithTrackType

### Purpose
This stored procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode, ParaValue, and TrackType.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | nvarchar(50) | Specifies the ParaCode to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Parameters table.
2. It filters the results based on the provided @ParaCode, ensuring that only rows with matching values are returned.
3. Additionally, it filters by the value of @TrackType, which must match a specific column in the table.
4. The results are further filtered to include only records where the EffectiveDate is less than or equal to the current date and the ExpiryDate is greater than or equal to the current date.
5. Finally, the results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters table