# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL_bak20230728

The purpose of this stored procedure is to retrieve and preview the OCC Auth data for a specific line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter the OCC Auth data. |

### Logic Flow

1. The procedure starts by creating a temporary table #TMP_OCCAuthPreview to store the initial OCC Auth data.
2. It then checks if the input line is 'NEL'. If true, it inserts the relevant data into the temporary table based on the operation date and access date.
3. A cursor is created to iterate through the OCC Auth IDs in the temporary table.
4. For each OCC Auth ID, another cursor is used to retrieve the corresponding endorser ID, workflow status, action time, and action by user.
5. Based on the endorser ID, the procedure updates the relevant columns in the temporary table with the appropriate data from the TAMS_OCC_Auth_Workflow table.
6. The procedure repeats steps 4-5 for each OCC Auth ID until all records have been processed.
7. Finally, the temporary table is selected and displayed.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow]
* **Writes:** [TAMS_OCCAuthPreview]