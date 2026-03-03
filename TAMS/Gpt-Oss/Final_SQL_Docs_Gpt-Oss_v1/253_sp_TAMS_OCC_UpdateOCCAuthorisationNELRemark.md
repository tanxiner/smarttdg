# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELRemark

### Purpose
Updates the remark for a specific OCC authorisation record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | Identifier of the user performing the update |
| @OCCAuthID | int | Identifier of the OCC authorisation record to update |
| @Line | nvarchar(10) | Unused in this procedure |
| @TrackType | nvarchar(50) | Unused in this procedure |
| @Remarks | nvarchar(100) | New remark text to store |

### Logic Flow
1. The procedure receives the user ID, the target OCC authorisation ID, and the new remark text.  
2. It executes an UPDATE statement on the `TAMS_OCC_Auth` table, setting the `Remark` column to the supplied remark, updating `UpdatedOn` to the current date/time, and recording the `UpdatedBy` user ID.  
3. The UPDATE is scoped to the row where `ID` equals the supplied `@OCCAuthID`.  
4. The procedure then ends.

### Data Interactions
* **Reads:** None  
* **Writes:** `TAMS_OCC_Auth` (updates `Remark`, `UpdatedOn`, `UpdatedBy` for a specific record)