# Procedure: EAS_Form_Get_Company

### Purpose
This procedure retrieves a company name from a parameter reference table, filtering by effective dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PARAM_VAL_C1 | VARCHAR | The company name to retrieve. |

### Logic Flow
The procedure selects a value from the EAS_PARAM_REF_DET table. The selection is based on the criteria that the parameter record type is ‘EAS_COMP_NAME’, the parameter type is ‘COMP_NAME’, and the effective date falls within a specified range (EFF_FROM_DATE to EFF_TO_DATE). The selected value is aliased as Company.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None