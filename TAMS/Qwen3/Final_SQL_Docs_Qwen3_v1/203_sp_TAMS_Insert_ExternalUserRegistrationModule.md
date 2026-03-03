# Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule

### Purpose
This stored procedure performs the business task of inserting a new external user registration module into the TAMS system, triggering an email notification to approvers for approval or rejection.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |
| @Line | NVARCHAR(20) | The line number associated with the registration. |
| @TrackType | NVARCHAR(50) | The type of track for the registration. |
| @Module | NVARCHAR(20) | The module name for the registration. |

### Logic Flow
The procedure follows these steps:

1. It determines the level of the workflow based on whether a company is registered or not.
2. It retrieves the next stage in the workflow, including the ID and title.
3. It inserts a new record into the TAMS_Reg_Module table with the provided data.
4. It inserts an audit log entry for the registration action.
5. If the level of the workflow is 3 (indicating that it's the final step), it sends an email notification to approvers with instructions on how to access and approve or reject the user registration.

### Data Interactions
* Reads: TAMS_Company, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log.
* Writes: TAMS_Reg_Module, TAMS_Action_Log.