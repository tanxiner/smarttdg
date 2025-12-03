# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationCCByParameters

### Purpose
This stored procedure updates the OCC authorization status for a given ID, based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID performing the update. |
| @OCCAuthID | int | The ID of the OCC authorization to be updated. |
| @OCCLevel | int | The level of the OCC authorization (used for conditional updates). |
| @Line | nvarchar(10) | The line number associated with the OCC authorization. |
| @TrackType | nvarchar(50) | The track type associated with the OCC authorization (optional). |
| @RemarksCC | nvarchar(1000) | The remarks for the OCC authorization update (optional). |

### Logic Flow
1. Check if the line is 'DTL'. If true, proceed to the DTL logic block.
2. Within the DTL logic block:
   a. Begin a transaction.
   b. Retrieve the workflow ID and endorser ID associated with the OCC authorization.
   c. Update the OCC authorization status in the TAMS_OCC_Auth_Workflow table based on the OCC level.
   d. Insert a new record into the TAMS_OCC_Auth_Workflow_Audit table to log the update action.
   e. Insert a new record into the TAMS_OCC_Auth_Audit table to log the update details.
   f. Commit the transaction.

3. If the line is not 'DTL', skip to the end of the procedure.

### Data Interactions
* Reads: 
  * [TAMS_Workflow]
  * [TAMS_Endorser]
  * [TAMS_OCC_Auth]
  * [TAMS_OCC_Auth_Workflow]
  * [TAMS_OCC_Auth_Workflow_Audit]
  * [TAMS_OCC_Auth_Audit]
* Writes: 
  * [TAMS_OCC_Auth_Workflow]
  * [TAMS_OCC_Auth_Audit]