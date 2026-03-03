# Procedure: EAS_PARAM_GET_REF_DET

### Purpose
This procedure retrieves detailed information about parameters from the EAS_PARAM_REF_DET table, filtering based on provided parameter type and record type criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_ParamRecType | NVARCHAR(50) | Specifies the desired parameter record type. If NULL, it matches all record types. |
| @P_ParamType | NVARCHAR(50) | Specifies the desired parameter type. If NULL, it matches the parameter type defined in the table. |

### Logic Flow
The procedure first assigns a sequential number to each row in the EAS_PARAM_REF_DET table, ordered by parameter record type in ascending order, and then by parameter code in ascending order.  It then filters the table based on the input parameters. Specifically, it selects rows where the parameter record type matches the value provided in @P_ParamRecType, or where @P_ParamRecType is NULL.  Additionally, it selects rows where the parameter type matches the value provided in @P_ParamType, or where @P_ParamType is NULL. The resulting set of rows is then returned.

### Data Interactions
* **Reads:** dbo.EAS_PARAM_REF_DET
* **Writes:** None