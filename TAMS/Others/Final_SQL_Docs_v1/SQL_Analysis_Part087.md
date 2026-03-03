# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters
**Type:** Stored Procedure

The procedure retrieves and updates data from various tables to provide an overview of OCC authentication details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number for which the data is required. |
| @TrackType | nvarchar(50) | The track type for which the data is required. |
| @OperationDate | date | The operation date for which the data is required. |
| @AccessDate | date | The access date for which the data is required. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_Station], [TAMS_User]
* **Writes:** [TAMS_OCC_Auth_Workflow]