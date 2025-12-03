# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationTCByParameters

### Purpose
This stored procedure updates the OCC Authorisation status for a given Traction Centre (TC) based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user performing the update. |
| @OCCAuthID | int | The ID of the OCC Authorisation to be updated. |
| @OCCLevel | int | The level of the OCC Authorisation (1-20). |
| @Line | nvarchar(10) | The line number for the Traction Centre. |
| @TrackType | nvarchar(50) | The track type for the Traction Centre. |
| @SelectionValue | nvarchar(50) | The new status value for the OCC Authorisation (used for levels 11-20). |

### Logic Flow
1. Check if the line number is 'DTL'. If true, proceed with the update.
2. Begin a transaction to ensure data consistency.
3. Retrieve the workflow ID and endorser ID for the given line number and track type.
4. Update the OCC Authorisation status in the TAMS_OCC_Auth_Workflow table based on the provided level.
5. Insert a new record into the TAMS_OCC_Auth_Workflow_Audit table to log the update action.
6. If the level is 11 or higher, insert another record into the TAMS_OCC_Auth_Workflow_Audit table for the pending status.
7. Update the OCC Authorisation status in the TAMS_OCC_Auth table based on the new value.
8. Insert a record into the TAMS_OCC_Auth_Audit table to log the update action.
9. Commit the transaction.

### Data Interactions
* Reads: [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit]
* Writes: [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth]