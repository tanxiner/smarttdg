# Procedure: EAS_Get_UserInfo

### Purpose
This procedure retrieves user information from the EAS_User table based on a provided user identifier and system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_uid | nvarchar(100) | The unique identifier for the user. |
| @p_sysid | varchar(30) | A system identifier associated with the user record. |

### Logic Flow
The procedure retrieves data from the EAS_User table. It selects specific columns including UserID, Name, Email, Designation, BusinessArea, Department, and Section. The selection is filtered based on two criteria: the UserID must match the value provided in the @p_uid parameter, and the sysid must match the value provided in the @p_sysid parameter.  The procedure also includes a filter to ensure that only active user records are returned.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None