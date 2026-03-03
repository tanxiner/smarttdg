# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters

### Purpose
This stored procedure updates the OCC Authorisation PFR status for a given set of parameters, including user ID, OCC Auth ID, OCC level, line, track type, remarks PFR, selection value, and station name.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user performing the update. |
| @OCCAuthID | int | The ID of the OCC Auth to be updated. |
| @OCCLevel | int | The level of the OCC Auth being updated. |
| @Line | nvarchar(10) | The line number associated with the OCC Auth. |
| @TrackType | nvarchar(50) | The type of track for the OCC Auth. |
| @RemarksPFR | nvarchar(1000) | The remarks PFR for the OCC Auth. |
| @SelectionValue | nvarchar(50) | The selection value for the OCC Auth. |
| @StationName | nvarchar(50) | The name of the station associated with the OCC Auth. |

### Logic Flow
The procedure follows a hierarchical structure based on the OCC level, updating the status and remarks accordingly.

1. For OCC levels 4-6, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
2. For OCC levels 7-12, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
3. For OCC level 13, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
4. For OCC levels 15-17, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
5. It also updates the PFRRemark field in TAMS_OCC_Auth for all OCC levels.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_OCC_Auth_Workflow_Audit, TAMS_Station.
* Writes: TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_OCC_Auth_Workflow_Audit.