# Procedure: EAS_Form_Check_Action_Access_Lists

### Purpose
This procedure determines if a user is authorized to view a specific form, considering their role, supervisor, and form approval levels.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |
| @P_UserID | varchar(15) | The unique identifier for the user. |
| @P_ErrorMsg | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure initializes the output error message parameter to an empty string.
2.  It retrieves the `userid` from the `EAS_Form_Approve_Lvl` table, filtering for the provided `@P_Guid` and associating it with a user from the `EAS_USER` table where the `sysid` is 'RPEAS' and the `active` flag is set to 1. This `userid` is stored in the `@p_Supervisorid` variable.
3.  It counts the number of rows in the `EAS_Form_Approve_Lvl` table where the `formguid` matches the input `@P_Guid` and the `userid` matches the input `@P_UserID`. This count is stored in the `@pcnt` variable.
4.  It counts the number of users whose `userid` matches the input `@P_UserID` and who are present in the `EAS_PA_Supervisor` table, where the `supervisorid` matches the `@p_Supervisorid` and the `active` flag is set to 1. This count is stored in the `@pPACnt` variable.
5.  It checks if both `@pcnt` and `@pPACnt` are zero. If they are, it sets the `@P_ErrorMsg` to 'You Are Not Authorised To View This Page.' and immediately exits the procedure.

### Data Interactions
* **Reads:** `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None