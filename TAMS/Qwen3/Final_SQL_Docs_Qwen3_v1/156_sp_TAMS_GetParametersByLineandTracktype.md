# Procedure: sp_TAMS_GetParametersByLineandTracktype

This procedure retrieves parameters from the TAMS_Parameters table based on a specific ParaCode, Line value, and TrackType.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaCode | nvarchar(50) | The code of the parameter to retrieve. |
| @Line | nvarchar(350) | The line value associated with the parameter. |
| @TrackType | nvarchar(350) | The track type associated with the parameter. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Parameters table.
2. It filters the results based on the provided ParaCode, Line, and TrackType values.
3. The EffectiveDate and ExpiryDate columns are used to ensure that only parameters within their effective period are returned.
4. The results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters table