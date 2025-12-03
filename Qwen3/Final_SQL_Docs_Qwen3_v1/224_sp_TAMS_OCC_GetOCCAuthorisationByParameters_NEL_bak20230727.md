# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_bak20230727

### Purpose
This stored procedure retrieves OCC authorisation details based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user. |
| @Line | nvarchar(10) | The line number. |
| @TrackType | nvarchar(50) | The track type. |
| @OperationDate | date | The operation date. |
| @AccessDate | date | The access date. |
| @RosterCode | nvarchar(50) | The roster code. |

### Logic Flow
1. The procedure starts by selecting the workflow ID from the TAMS_Workflow table where the line, track type, and workflow type match the provided parameters.
2. It then inserts data into a temporary table #TMP_Endorser with endorser details based on the selected workflow ID and line number.
3. Next, it selects OCC authorisation details from the TAMS_OCC_Auth table and inserts them into another temporary table #TMP_OCCAuthNEL.
4. The procedure then declares two cursors: one for each temporary table.
5. It iterates through the cursors, updating the corresponding fields in #TMP_OCCAuthNEL based on the endorser ID and roster code.
6. Finally, it selects all data from #TMP_OCCAuthNEL.

### Data Interactions
* Reads:
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_OCC_Auth
* Writes: None