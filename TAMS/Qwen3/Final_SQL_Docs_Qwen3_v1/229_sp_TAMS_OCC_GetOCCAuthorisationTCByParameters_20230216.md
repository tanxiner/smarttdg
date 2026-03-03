# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216

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
1. The procedure starts by creating temporary tables to store intermediate results.
2. It then checks if the specified line is 'DTL' and retrieves the workflow ID from the TAMS_Workflow table based on this condition.
3. If the line is 'DTL', it inserts data into the #TMP_Endorser table, which contains endorser information for the specified workflow ID.
4. The procedure then creates a cursor to iterate over the OCCAuthID column in the #TMP_OCCAuthTC table and retrieves the corresponding data from this table.
5. For each OCCAuthID retrieved, it iterates over the #TMP_Endorser table again to retrieve endorser information for that specific OCCAuthID.
6. Based on the endorser ID, it updates the TrainClearCert, AuthForTrackAccess, LineClearCertTOA, and AuthForTrainInsert columns in the #TMP_OCCAuthTC table with the corresponding values from the TAMS_OCC_Auth_Workflow table.
7. After iterating over all OCCAuthIDs, it closes the cursors and deallocates memory for the temporary tables.

### Data Interactions
* **Reads:**
	+ [TAMS_Workflow]
	+ [TAMS_Endorser]
	+ [TAMS_Traction_Power_Detail]
	+ [TAMS_Station]
	+ [TAMS_Traction_Power]
	+ [TAMS_OCC_Auth]
	+ [TAMS_OCC_Auth_Workflow]
* **Writes:**
	+ #TMP
	+ #TMP_Endorser
	+ #TMP_OCCAuthTC