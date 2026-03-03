# Procedure: EAS_PARAM_GET_REF

### Purpose
This procedure retrieves parameter descriptions based on a provided parameter record type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_ParamRecType | varchar(50) | The parameter record type to filter by. |

### Logic Flow
The procedure searches the `EAS_PARAM_REF` table. It filters the results based on the value provided in the `@P_ParamRecType` parameter. If `@P_ParamRecType` is null, the procedure returns all records from the table. The results are ordered alphabetically by `PARAM_REC_TYPE`.

### Data Interactions
* **Reads:** `EAS_PARAM_REF`
* **Writes:** None