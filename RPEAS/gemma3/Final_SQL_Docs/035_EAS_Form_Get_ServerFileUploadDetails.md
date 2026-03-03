# Procedure: EAS_Form_Get_ServerFileUploadDetails

### Purpose
This procedure retrieves the server name and associated file path URL from a configuration table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FilePath | varchar(225) | Output parameter holding the server name. |
| @p_FilrURLPath | varchar(225) | Output parameter holding the file URL path. |

### Logic Flow
The procedure retrieves data from the `EAS_PARAM_REF_DET` table. It filters the table based on the `PARAM_REC_TYPE` being ‘EAS_FILE_PATH’, the `PARAM_TYPE` being ‘FILE_PATH’, and the `PARAM_CODE` being ‘SERVER_NAME’. The filtering also includes a date range check between `EFF_FROM_DATE` and `EFF_TO_DATE`. The retrieved server name is assigned to the output parameter `@p_FilePath`, and the associated file URL path is assigned to the output parameter `@p_FilrURLPath`.

### Data Interactions
* **Reads:** `EAS_PARAM_REF_DET`
* **Writes:** None