# Procedure: EAS_Form_Get_UserLogid_Update

### Purpose
This procedure updates the active status of a user record in the EAS_User_login table based on provided system and GUID identifiers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(50) | System identifier of the user record. |
| @p_GUID | varchar(225) | Globally unique identifier associated with the user session. |

### Logic Flow
The procedure initiates by updating a record within the EAS_User_login table. Specifically, it sets the ‘active’ field to ‘N’ (inactive), records the current date and time in the ‘updatedon’ field, and assigns the ‘SYSTEM’ user as the user responsible for the update in the ‘updatedby’ field. The update is performed on records where the ‘SessionGUID’ matches the provided @p_GUID, the ‘sysid’ matches the provided @P_SysID, and the ‘active’ field is currently set to ‘Y’.

### Data Interactions
* **Reads:** EAS_User_login
* **Writes:** EAS_User_login