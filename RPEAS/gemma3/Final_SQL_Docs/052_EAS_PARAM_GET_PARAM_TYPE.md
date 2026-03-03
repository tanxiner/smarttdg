# Procedure: EAS_PARAM_GET_PARAM_TYPE

### Purpose
This procedure retrieves a list of distinct PARAM_TYPE values based on a specified PARAM_REC_TYPE and the current date falls within the EFF_FROM_DATE and EFF_TO_DATE ranges.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Param_RecType | varchar(50) | The identifier for a record type. |

### Logic Flow
The procedure filters the EAS_PARAM_REF_DET table to identify records where the PARAM_REC_TYPE matches the input @P_Param_RecType.  It then restricts the selection to only those records where the current date falls between the EFF_FROM_DATE and EFF_TO_DATE columns. Finally, the procedure returns a distinct list of all values found in the PARAM_TYPE column for these filtered records.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None