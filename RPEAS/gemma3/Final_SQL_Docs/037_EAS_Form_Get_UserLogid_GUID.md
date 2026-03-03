# Procedure: EAS_Form_Get_UserLogid_GUID

### Purpose
This procedure generates a unique identifier and creates a new record in the EAS_User_login table, associating it with a specified user and session.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(50) |  System Identifier |
| @p_UserID | varchar(10) | User Identifier |
| @p_GUID | varchar(225) | Output: Unique Session Identifier |

### Logic Flow
1.  A new unique identifier is generated using the NEWID() function and stored in the @pNewGuiD variable.
2.  The value stored in @pNewGuiD is assigned to the output parameter @p_GUID.
3.  A new record is inserted into the EAS_User_login table.
4.  The record includes the provided system identifier (@P_SysID), the user identifier (@p_UserID), the current date and time for the start and end times, the newly generated unique identifier (@pNewGuiD) as the SessionGUID, a value of 'Y' for the Active flag, the current date and time for the CreatedOn timestamp, and the user identifier (@p_UserID) as the CreatedBy.

### Data Interactions
* **Reads:** None
* **Writes:** [dbo].[EAS_User_login]