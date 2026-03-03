# Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule_20231009

### Purpose
This stored procedure performs the business task of inserting a new external user registration module into the TAMS system, including sending an email to approvers for approval or rejection.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |
| @Line | NVARCHAR(20) | The line number in the workflow. |
| @TrackType | NVARCHAR(50) | The type of track for the registration. |
| @Module | NVARCHAR(20) | The module associated with the registration. |

### Logic Flow
The procedure follows these steps:

1. It checks if a company is registered and, based on that, determines the level in the workflow to insert.
2. It retrieves the next stage ID and endorser ID from the TAMS system based on the line number and track type.
3. It inserts a new record into the TAMS_Reg_Module table with the provided data.
4. It inserts an audit log entry for the user registration submission.
5. If the level is 3, it sends an email to approvers with a link to access the TAMS system for approval or rejection.

### Data Interactions
* Reads: TAMS_Company, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log
* Writes: TAMS_Reg_Module