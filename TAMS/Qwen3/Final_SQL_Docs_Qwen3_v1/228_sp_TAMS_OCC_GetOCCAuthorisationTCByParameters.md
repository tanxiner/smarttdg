# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters

### Purpose
This stored procedure retrieves OCC authorisation data for a specified track type and operation date, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (optional). |
| @OperationDate | date | The operation date to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. The procedure starts by creating temporary tables to store intermediate results.
2. It then selects the workflow ID from the TAMS_Workflow table where the line number matches the input parameter and the workflow type is 'OCCAuth' and the effective date is less than or equal to the current date and the expiry date is greater than or equal to the current date.
3. If a line number is provided, it inserts data into the #TMP_Endorser table from the TAMS_Endorser table where the line number matches the input parameter and the workflow ID matches the selected workflow ID.
4. It then selects the traction power IDs from the TAMS_Traction_Power table where the line number matches the input parameter and the track type matches the input parameter, groups by the traction power ID, and stores the results in the #TMP table.
5. The procedure then selects data from the TAMS_OCC_Auth table where the operation date matches the input parameter and the access date matches the input parameter, and joins it with the #TMP table on the traction power ID.
6. It then loops through each OCC authorisation record in the #TMP_OCCAuthTC table and updates the corresponding records in the #TMP_OCCAuthTC table based on the endorser ID.
7. Finally, it selects all data from the #TMP_OCCAuthTC table.

### Data Interactions
* **Reads:** 
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_Traction_Power
	+ TAMS_OCC_Auth
* **Writes:** None