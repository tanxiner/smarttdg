# Procedure: EAS_Form_Get_Prefix

### Purpose
This procedure retrieves the value associated with the document prefix parameter from the EAS_PARAM_REF_DET table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_DocPrefix | varchar(50) | Output parameter containing the retrieved document prefix value. |

### Logic Flow
The procedure initializes an output parameter, @P_DocPrefix, to an empty string. It then executes a query against the EAS_PARAM_REF_DET table. The query filters records where the PARAM_REC_TYPE is ‘EAS_DOC_PREFIX’, the PARAM_TYPE is ‘DOC_PREFIX’, and the PARAM_CODE is ‘PREFIX_NAME’.  The query further restricts the selection to records where the effective date falls between the EFF_FROM_DATE and EFF_TO_DATE. The value from the [PARAM_VAL_C1] column of the matching record is then assigned to the output parameter @P_DocPrefix.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None