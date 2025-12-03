# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELRemark
**Type:** Stored Procedure

The procedure updates the OCCAuthorisationNELRemark field in the TAMS_OCC_Auth table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user updating the record. |
| @OCCAuthID | int | The ID of the OCCAuthorisationNEL to be updated. |
| @Line | nvarchar(10) | The line number associated with the update. |
| @TrackType | nvarchar(50) | The type of track being performed. |
| @Remarks | nvarchar(100) | The new remark value for the OCCAuthorisationNEL. |

### Logic Flow
1. Checks if a record exists in the TAMS_OCC_Auth table with the specified ID (@OCCAuthID).
2. If a record is found, updates the Remark field with the new value from @Remarks.
3. Updates the UpdatedOn field with the current date and time using GETDATE().
4. Updates the UpdatedBy field with the user ID from @UserID.
5. Returns no output.

### Data Interactions
* **Reads:** TAMS_OCC_Auth table (ID column)
* **Writes:** TAMS_OCC_Auth table (Remark, UpdatedOn, UpdatedBy columns)