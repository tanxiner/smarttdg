# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_bak20230727
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve OCC (Operations Control Centre) authorizations for a specific user and parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user for whom to retrieve OCC authorizations. |
| @Line | nvarchar(10) | The line number for which to retrieve OCC authorizations. (Optional) |
| @TrackType | nvarchar(50) | The track type for which to retrieve OCC authorizations. (Optional) |
| @OperationDate | date | The operation date for which to retrieve OCC authorizations. |
| @AccessDate | date | The access date for which to retrieve OCC authorizations. |
| @RosterCode | nvarchar(50) | The roster code for which to retrieve OCC authorizations. |

### Logic Flow
1. Checks if the user exists in the TAMS_Workflow table with a matching line and track type.
2. Retrieves the workflow ID from the TAMS_Workflow table.
3. Inserts data into the #TMP_Endorser temporary table, which contains endorser information for each OCC authorization.
4. Inserts data into the #TMP_OCCAuthNEL temporary table, which contains OCC authorizations with their corresponding endorser information.
5. Iterates through the #TMP_OCCAuthNEL table and updates the train clear certifications based on the workflow status and roster code.
6. Iterates through the #TMP_OCCAuthNEL table and updates the line clear certifications based on the workflow status and roster code.
7. Iterates through the #TMP_OCCAuthNEL table and updates the mainline traction current switch-on requests based on the workflow status and roster code.
8. Iterates through the #TMP_OCCAuthNEL table and updates the train insert authorizations based on the workflow status and roster code.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth]