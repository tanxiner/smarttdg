### Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule
**Type:** Stored Procedure

This procedure performs the task of inserting a new external user registration into the system. It checks if the company is registered, and based on that, it determines the next stage in the workflow.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registration to be inserted |
| @Line | NVARCHAR(20) | The line number of the registration |
| @TrackType | NVARCHAR(50) | The type of track for the registration |
| @Module | NVARCHAR(20) | The module associated with the registration |

### Logic Flow
1. Checks if the user exists in the system.
2. Inserts into the Audit table to log the action.
3. Retrieves the next stage in the workflow based on the line number and track type.
4. Retrieves the endorser ID for the current level of the workflow.
5. Retrieves the WFStatus from the TAMS_WFStatus table.
6. Inserts a new record into the TAMS_Reg_Module table with the retrieved values.
7. If the level is 3, sends an email to the approvers.

### Data Interactions
* Reads: TAMS_Company, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User, TAMS_User_Role
* Writes: TAMS_Reg_Module, TAMS_Action_Log