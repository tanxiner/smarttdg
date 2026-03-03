# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters

### Purpose
This stored procedure retrieves and previews the OCC authentication data for a given set of parameters, including line, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @OperationDate | date | The operation date to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. The procedure creates two temporary tables, #TMP and #TMP_OCCAuthPreview.
2. It then inserts data from the TAMS_Traction_Power table into #TMP based on the provided line number and track type.
3. Next, it inserts data from the TAMS_OCC_Auth table into #TMP_OCCAuthPreview based on the operation date, access date, and other parameters.
4. The procedure then iterates through the OCC authentication IDs in #TMP_OCCAuthPreview and updates the corresponding records in #TMP_OCCAuthPreview with additional information based on the workflow status.
5. Finally, it returns all the data from #TMP_OCCAuthPreview.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TAMS_Traction_Power], [TAMS_OCC_Auth]