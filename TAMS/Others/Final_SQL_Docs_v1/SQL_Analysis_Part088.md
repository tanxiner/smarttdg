# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process OCC Auth preview data for a specific line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line parameter used to filter the data. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TMP_OCCAuthPreview]