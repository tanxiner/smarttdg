# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL_bak20230728
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and update data from the TAMS OCC Auth Preview table based on input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Specifies the line for which to retrieve data. |

### Logic Flow
1. The procedure checks if the input line is 'NEL'.
2. If it is, it creates a temporary table #TMP_OCCAuthPreview and inserts data from the TAMS OCC Auth table.
3. It then declares two cursors: one to iterate over the rows in the temporary table and another to retrieve workflow status information for each row.
4. For each row in the temporary table, it fetches the corresponding workflow status information using the second cursor.
5. Based on the workflow status, it updates the relevant columns in the temporary table with the current time and user name.
6. Finally, it returns the updated data from the temporary table.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_User]
* **Writes:** [TAMS_OCCAuthPreview]