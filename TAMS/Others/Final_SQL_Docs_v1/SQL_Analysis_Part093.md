# Procedure: sp_TAMS_OCC_GetOCCAuthorisationCCByParameters
**Type:** Stored Procedure

The procedure retrieves OCC authorisation data for a specific user and parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve OCC authorisation data for. |

### Logic Flow
1. Checks if user exists.
2. Retrieves workflow ID from TAMS_Workflow table where Line = @Line and WorkflowType = 'OCCAuth' and IsActive = 1 and EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE().
3. Inserts endorser data into #TMP_Endorser table from TAMS_Endorser table where Line = 'DTL', WorkflowId = @WorkflowId, RoleId = 12.
4. Retrieves traction power data from TAMS_Traction_Power table where Line = 'DTL' and TrackType = @TrackType.
5. Inserts OCC authorisation data into #TMP_OCCAuthCC table from TAMS_OCC_Auth table where EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE() and IsActive = 1 and OperationDate = @OperationDate and AccessDate = @AccessDate.
6. Iterates through OCC authorisation data, updating fields based on endorser ID:
	* If endorser ID is 98, updates TrainClearCert field if WFStatus is 'Pending' or 'Completed'.
	* If endorser ID is 99, updates MainlineTractionCurrentSwitchOff field if WFStatus is 'Pending' or 'Completed'.
	* If endorser ID is 104, updates AuthForTrackAccess field if WFStatus is 'Pending' or 'Completed'.
	* If endorser ID is 110, updates LineClearCert field if WFStatus is 'Pending' or 'Completed'.
	* If endorser ID is 112, updates MainlineTractionCurrentSwitchOn field if WFStatus is 'Pending' or 'Completed'.
	* If endorser ID is 115, updates AuthForTrainInsertion field if WFStatus is 'Pending' or 'Completed'.
7. Returns OCC authorisation data from #TMP_OCCAuthCC table.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_Traction_Power, TAMS_OCC_Auth
* Writes: #TMP_Endorser, #TMP_OCCAuthCC