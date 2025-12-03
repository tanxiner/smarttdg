# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule

### Purpose
This stored procedure performs internal user registration by submitting a new registration request to the system, which then triggers a workflow for approval and notification of relevant users.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Unique identifier for the registered user. |
| @Line | NVARCHAR(20) | Line number associated with the registration request. |
| @TrackType | NVARCHAR(50) | Track type (e.g., TAR, DCC, OCC) indicating the workflow to be triggered. |
| @Module | NVARCHAR(20) | Module name (e.g., TAR, DCC, OCC) used for tracking and notification purposes. |

### Logic Flow
1. The procedure starts by checking if a specific module (@Module) is provided. Based on this, it determines the corresponding workflow ID (@WorkflowID) to be triggered.
2. It then retrieves the next stage in the workflow (e.g., @NextStageID, @WFStatus) for the given line number (@Line) and track type (@TrackType).
3. The procedure inserts a new record into the TAMS_Reg_Module table with the provided registration details.
4. An audit log entry is created to track the submission of the user registration request.
5. If the module is TAR, an email is sent to relevant users (sys approvers) for approval and notification purposes.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_User_Role, TAMS_Action_Log
* Writes: TAMS_Reg_Module