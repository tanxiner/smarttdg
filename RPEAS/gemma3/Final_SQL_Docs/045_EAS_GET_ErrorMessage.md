# Procedure: EAS_GET_ErrorMessage

### Purpose
This procedure retrieves the corresponding error message from the EAS_ERROR_MSG table based on a provided error code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_ErrorCode | integer | The error code to search for. |
| @p_Errormsg | Varchar(500) | The error message, populated by the procedure. |

### Logic Flow
1.  The procedure initializes the `@p_Errormsg` variable to an empty string.
2.  It checks if there exists at least one row in the `EAS_ERROR_MSG` table where the `ERROR_CODE` matches the input `@p_ErrorCode`.
3.  If a matching row is found, the procedure constructs the error message by concatenating the `ERROR_CODE` (converted to a string) with a hyphen and the `ERROR_TEXT` from the matching row. This constructed message is then assigned to the `@p_Errormsg` parameter.
4.  If no matching row is found in the `EAS_ERROR_MSG` table, the procedure sets `@p_Errormsg` to the string '9999 - Error Message not defined in EAS_ERROR_MSG table.' and immediately exits the procedure.

### Data Interactions
* **Reads:** `EAS_ERROR_MSG`
* **Writes:** None