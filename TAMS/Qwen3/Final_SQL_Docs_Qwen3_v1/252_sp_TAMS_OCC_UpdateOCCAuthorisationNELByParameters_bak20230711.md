# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELByParameters_bak20230711

### Purpose
This stored procedure updates the OCC Authorisation for a given NEL by processing the specified workflow level and endorser ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID performing the update. |
| @OCCAuthID | int | The ID of the OCC Authorisation to be updated. |
| @OCCLevel | int | The workflow level to process (1-12). |
| @Line | nvarchar(10) | The line number for which the update is being performed. |
| @Remarks | nvarchar(100) | Optional remarks for the update. |
| @SelectionValue | nvarchar(50) | The new status value for OCC Auth workflow level 15. |

### Logic Flow
The procedure follows these steps:

1. Check if the line number matches 'NEL'. If true, proceed with the update.
2. Begin a transaction to ensure data consistency.
3. Declare variables to store endorser IDs and workflow IDs.
4. For each OCC Level (1-12), perform the following actions:
	* Retrieve the workflow ID for the specified level.
	* Update the corresponding OCC Auth workflow status to 'Completed' if it's not already set.
	* Insert a new OCC Auth workflow record with the next endorser ID and pending status.
	* Update the OCC Auth record with the new status ID, remarks, and updated timestamps.
5. If the line number matches 'NEL', also perform additional updates:
	* Insert an audit record for each OCC Auth workflow update.
	* Insert another audit record for each OCC Auth update with a specific action type ('I' or 'U').
6. Commit the transaction if all updates are successful.

### Data Interactions
* Reads: [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit], and [TAMS_OCC_Auth_Audit].
* Writes: [TAMS_OCC_Auth_Workflow] and [TAMS_OCC_Auth].