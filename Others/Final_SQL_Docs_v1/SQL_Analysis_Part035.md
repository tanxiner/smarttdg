# Procedure: sp_TAMS_Depot_UpdateDTCAuth
**Type:** Stored Procedure

The purpose of this stored procedure is to update the DTCAuth status for a given user and workflow.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | The username of the user being updated. |
| @authid | int | The ID of the authentication being updated. |
| @workflowid | int | The ID of the workflow being updated. |
| @statusid | int | The current status ID of the DTCAuth. |
| @val | bit | The new value for the DTCAuth (NULL for no change). |
| @valstr | nvarchar(50) | The new string value for the DTCAuth (NULL for no change). |
| @powerzoneid | int | The ID of the power zone being updated. |
| @success | bit | Output parameter indicating success or failure. |
| @type | int | Type of update (1 for checkbox, 2 for dropdown). |
| @spksid | int | The ID of the SPK being updated. |
| @Message | nvarchar(500) | Output parameter containing error message. |

### Logic Flow
1. Checks if user exists in the TAMS_Endorser table.
2. If user does not exist, sets @access to 1 and throws an exception.
3. If user exists, checks if they have access to update the DTCAuth for the given workflow.
4. If they do not have access, sets @access to 1 and throws an exception.
5. Checks if the workflow is already updated.
6. If it is, throws an error.
7. Updates the current workflow with the new values.
8. Inserts a new workflow into the DTCAuth table.
9. Updates the power zone or SPK being updated based on the workflow ID.
10. If the workflow ID is 137, updates the status ID of the DTCAuth and inserts a new workflow.
11. If the workflow ID is not 137, updates the status ID of the DTCAuth and returns success.

### Data Interactions
* **Reads:** TAMS_Endorser, TAMS_User_Role, TAMS_User, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone
* **Writes:** TAMS_Depot_Auth_Workflow