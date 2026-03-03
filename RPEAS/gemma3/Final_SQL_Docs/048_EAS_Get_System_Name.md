# Procedure: EAS_Get_System_Name

### Purpose
This procedure retrieves the system name associated with a specified system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(30) | The unique identifier for the system. |
| @P_SysName | varchar(200) | The system name, populated by the procedure. |

### Logic Flow
1.  The procedure initializes the output parameter @P_SysName to an empty string.
2.  The procedure queries the EAS_PARAM_REF_DET table.
3.  The query filters the table based on the following criteria:
    *   The PARAM_REC_TYPE column must equal 'EAS_APPL'.
    *   The PARAM_TYPE column must equal 'APPL_NAME'.
    *   The PARAM_CODE column must match the input @P_SysID.
    *   The EFF_FROM_DATE and EFF_TO_DATE columns must contain the current date.
4.  If a matching record is found, the value from the PARAM_VAL_C1 column is assigned to the output parameter @P_SysName.
5.  If no matching record is found, the output parameter @P_SysName remains an empty string.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None