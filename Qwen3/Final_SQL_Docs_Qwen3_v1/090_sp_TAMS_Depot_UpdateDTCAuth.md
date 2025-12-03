# Procedure: sp_TAMS_Depot_UpdateDTCAuth

### Purpose
This stored procedure updates the DTCAuth status for a given user and workflow ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | The username of the user being updated. |
| @authid | int | The ID of the authentication being updated. |
| @workflowid | int | The ID of the workflow being updated. |
| @statusid | int | The current status ID. |
| @val | bit | The new value for the DTCAuth status (NULL for no change). |
| @valstr | nvarchar(50) | The string representation of the new value for the DTCAuth status (NULL for no change). |
| @powerzoneid | int | The ID of the power zone being updated. |
| @success | bit | Output parameter indicating whether the update was successful. |
| @type | int | The type of update (1 for checkbox, 2 for dropdown). |
| @spksid | int | The ID of the SPKSID being updated. |
| @Message | nvarchar(500) | Output parameter containing any error messages. |

### Logic Flow
The procedure follows these steps:

1. It checks if the user has access to update the information by checking if the username exists in the TAMS_Endorser table with the specified workflow ID.
2. If the user does not have access, it sets an error message and skips the rest of the procedure.
3. It checks if the workflow is already updated by checking if there is a record in the TAMS_Depot_Auth_Workflow table with the same authentication ID and workflow ID.
4. If the workflow is not already updated, it updates the current workflow by setting the WFStatus field to the new value based on the @type parameter.
5. It gets the next status ID from the TAMS_WFStatus table based on the current status ID.
6. It inserts a new record into the TAMS_Depot_Auth_Workflow table with the updated workflow ID and authentication ID.
7. Depending on the workflow ID, it updates other tables such as TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone, or TAMS_Depot_Auth to update the status ID.

### Data Interactions
* Reads: TAMS_Endorser, TAMS_User_Role, TAMS_User, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone.
* Writes: TAMS_Depot_Auth_Workflow.