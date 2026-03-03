# Procedure: sp_TAMS_RGS_Cancel

### Purpose
This stored procedure cancels a Request for Goods (RGS) on TAMS, updating the status and sending an SMS notification to the OCC contact.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR sector being cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @tracktype as nvarchar(50)='MAINLINE' | nvarchar(50) | The type of track to use (in this case, MAINLINE). |
| @Message	| NVARCHAR(500) | Output parameter that will contain an error message if any. |

### Logic Flow
1. Check if a transaction is already in progress and set the internal transaction flag accordingly.
2. Initialize the output parameter @Message with an empty string.
3. Retrieve the current status of the TAR sector being cancelled from TAMS_TOA.
4. Update the TOAStatus to 6 (cancelled) and CancelRemark to the provided value in TAMS_TOA.
5. Insert a new record into TAMS_TAMSAudit for the updated TAR sector.
6. Determine the ID of the user associated with the current login ID in TAMS_User.
7. Check if the track type is MAINLINE. If so, proceed with the cancellation logic.
8. For MAINLINE tracks:
	* Retrieve the list of traction power IDs from TAMS_Traction_Power_Detail that are associated with the TAR sector being cancelled.
	* Iterate through each traction power ID and perform the following actions:
		+ Update OCCAuthStatusId to 9 (cancelled) in TAMS_OCC_Auth for the current traction power ID.
		+ Insert a new record into TAMS_OCC_Auth_Workflow for the updated OCC Auth status.
		+ Insert a new record into TAMS_OCC_Auth_Audit for the updated OCC Auth status.
9. For NEL tracks:
	* Retrieve the list of traction power IDs from TAMS_Traction_Power_Detail that are associated with the TAR sector being cancelled.
	* Iterate through each traction power ID and perform the following actions:
		+ Update OCCAuthStatusId to 9 (cancelled) in TAMS_OCC_Auth for the current traction power ID.
		+ Insert a new record into TAMS_OCC_Auth_Workflow for the updated OCC Auth status.
		+ Insert a new record into TAMS_OCC_Auth_Audit for the updated OCC Auth status.
10. If all surrender records are found, update the DepotAuthStatusId in TAMS_Depot_Auth to reflect the new workflow ID.
11. Determine if there is an existing DepotAuthWorkFlow record with the same DTCAuthID and WorkflowID as the newly inserted record.
12. If so, update the isCancelled flag to 1 (true) in TAMS_Depot_Auth_Workflow.
13. Insert a new record into TAMS_Depot_Auth_Workflow for the updated Depot Auth status.
14. Update the DepotAuthStatusId in TAMS_Depot_Auth to reflect the new workflow ID.
15. If any errors occur during the cancellation process, set @Message to an error message and exit the procedure.

### Data Interactions
* Reads: TAMS_TOA, TAMS_Traction_Power_Detail, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow.
* Writes: TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow.