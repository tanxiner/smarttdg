# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216_M

### Purpose
This stored procedure retrieves OCC authorisation data for a given set of parameters, including user ID, line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the OCC authorisation data. |
| @Line | nvarchar(10) | The line for which to retrieve OCC authorisation data (optional). |
| @OperationDate | date | The operation date for which to retrieve OCC authorisation data. |
| @AccessDate | date | The access date for which to retrieve OCC authorisation data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the `@Line` parameter is 'DTL'. If it is, it retrieves the workflow ID from the `TAMS_Workflow` table where the line matches and the workflow type is 'OCCAuth' and the status is active.
2. It then inserts data into temporary tables `#TMP_Endorser` and `#TMP` based on the retrieved workflow ID and user ID.
3. The procedure then creates a cursor to iterate over the OCC authorisation IDs in the `#TMP_OCCAuthTC` table.
4. For each OCC authorisation ID, it iterates over the endorser IDs in the `#TMP_Endorser` table and updates the corresponding fields in the `#TMP_OCCAuthTC` table based on the endorser level and title.
5. The procedure then closes the cursor and deallocates the temporary tables.

### Data Interactions
* **Reads:** 
	+ [TAMS_Workflow]
	+ [TAMS_Endorser]
	+ [TAMS_Traction_Power_Detail]
	+ [TAMS_Station]
	+ [TAMS_Traction_Power]
	+ [TAMS_OCC_Auth]
	+ [TAMS_OCC_Auth_Workflow]
	+ [TAMS_OCC_Duty_Roster]
* **Writes:** 
	+ #TMP_Endorser
	+ #TMP
	+ #TMP_OCCAuthTC