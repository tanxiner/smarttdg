# Procedure: SP_TAMS_Depot_GetParameters

### Purpose
This stored procedure retrieves specific parameters from the TAMS_Parameters table based on a date range and parameter value.

### Parameters
| Name | Type | Purpose |
| @EffectiveDate | datetime | The start of the date range to filter parameters. |
| @ExpiryDate | datetime | The end of the date range to filter parameters. |
| @ParamValue2 | nvarchar(50) | The specific parameter value to filter by. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects distinct values from the TAMS_Parameters table where the EffectiveDate is between the specified date range and ParaValue2 equals 'Depot'.
3. The selected parameters are returned based on these conditions.

### Data Interactions
* **Reads:** TAMS_Parameters
* **Writes:** None