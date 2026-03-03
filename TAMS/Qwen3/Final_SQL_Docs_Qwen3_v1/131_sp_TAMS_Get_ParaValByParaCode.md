# Procedure: sp_TAMS_Get_ParaValByParaCode

### Purpose
This stored procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode and ParaValue1.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @paraCode | NVARCHAR(200) | The code of the parameter to retrieve. |
| @paraValue1 | NVARCHAR(200) | A value used to filter parameters with a specific ParaValue1. |

### Logic Flow
The procedure starts by selecting all columns from the TAMS_Parameters table where the ParaCode matches the provided @paraCode, and the EffectiveDate is within or before the current date, the ExpiryDate is within or after the current date, and the ParaValue1 matches the provided @paraValue1. The results are then ordered by ParaValue1, ParaValue2, and [Order].

### Data Interactions
* **Reads:** TAMS_Parameters table