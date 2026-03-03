# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELRemark

### Purpose
This stored procedure updates the remark field for a specific OCC authorisation, along with the user ID and current date, in the TAMS_OCC_Auth table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user making the update. |
| @OCCAuthID | int | The ID of the OCC authorisation being updated. |
| @Line | nvarchar(10) | Not used in this procedure ( possibly a placeholder for future use). |
| @TrackType | nvarchar(50) | Not used in this procedure (possibly a placeholder for future use). |
| @Remarks | nvarchar(100) | The new remark to be stored. |

### Logic Flow
1. The procedure starts by updating the remark field of the specified OCC authorisation ID.
2. It also updates the user ID and current date fields with the provided values.

### Data Interactions
* **Reads:** None explicitly listed, but it is assumed that the system retrieves data from other tables as needed for this update operation.
* **Writes:** 
  * TAMS_OCC_Auth table: Updated with new remark value, updated on field, and updated by field.