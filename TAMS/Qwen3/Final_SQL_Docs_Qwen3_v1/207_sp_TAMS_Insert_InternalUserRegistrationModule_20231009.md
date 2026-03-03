# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_20231009

### Purpose
This stored procedure performs internal user registration for a given module, including updating workflow status and sending an email notification to approvers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |
| @Line | NVARCHAR(20) | The line number associated with the registration. |
| @TrackType | NVARCHAR(50) | The type of track for the registration. |
| @Module | NVARCHAR(20) | The module being registered (e.g., TAR or OCC). |

### Logic Flow
1. The procedure starts by checking if the module is 'TAR'. If it is, it retrieves the workflow ID from the TAMS_Workflow table based on the line number and track type.
2. If the module is not 'TAR', it retrieves the workflow ID from the TAMS_Workflow table based on the line number and track type, but with a different workflow type ('OCCIntUser').
3. The procedure then retrieves the next stage ID and other relevant information (e.g., endorser ID, workflow status) from the TAMS_Endorser and TAMS_WFStatus tables.
4. It inserts a new record into the TAMS_Reg_Module table with the provided registration details.
5. An audit log is inserted to track the registration activity.
6. The procedure sends an email notification to approvers (identified by their email addresses) with a link to access the TAMS system and approve/reject the user registration.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_User_Role, TAMS_Action_Log
* Writes: TAMS_Reg_Module