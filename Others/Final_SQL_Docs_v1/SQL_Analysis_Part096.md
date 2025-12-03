# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters
**Type:** Stored Procedure

Purpose:
This stored procedure retrieves OCC authorisation data for a specified user, line, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve OCC authorisation data for. |
| @Line | nvarchar(10) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (optional). |
| @OperationDate | date | The operation date to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Retrieves OCC authorisation data from the database based on the provided parameters.
4. Iterates through each OCC authorisation record and updates the corresponding fields in the #TMP_OCCAuthTC table based on the endorser ID.
5. Returns all OCC authorisation records.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power_Detail], [TAMS_Station], [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** #TMP, #TMP_Endorser, #TMP_OCCAuthTC