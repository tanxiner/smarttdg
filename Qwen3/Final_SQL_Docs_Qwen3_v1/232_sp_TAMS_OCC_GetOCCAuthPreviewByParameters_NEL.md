# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL

### Purpose
This stored procedure retrieves and previews the OCC authentication data for a specified line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line for which to retrieve OCC authentication data. |

### Logic Flow
1. The procedure starts by creating a temporary table #TMP_OCCAuthPreview to store the retrieved data.
2. It then checks if the input line is 'NEL'. If true, it proceeds with the logic for this line.
3. For each row in the TAMS_Traction_Power and TAMS_OCC_Auth tables where the operation date matches the input operation date and access date matches the input access date, and the line matches the input line, it inserts a new row into #TMP_OCCAuthPreview.
4. The procedure then creates a cursor to iterate over the OCC authentication IDs in #TMP_OCCAuthPreview.
5. For each OCC authentication ID, it opens another cursor to retrieve the corresponding data from the TAMS_OCC_Auth_Workflow table.
6. It updates the data in #TMP_OCCAuthPreview based on the workflow status and action by user for each OCC authentication ID.
7. Finally, it closes both cursors and deallocates them.

### Data Interactions
* **Reads:** 
	+ TAMS_Traction_Power
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
* **Writes:** None