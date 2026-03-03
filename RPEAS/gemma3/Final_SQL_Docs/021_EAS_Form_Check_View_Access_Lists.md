# Procedure: EAS_Form_Check_View_Access_Lists

### Purpose
This procedure determines if a user is authorized to view a specific form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) |  A unique identifier for the form. |
| @P_UserID | varchar(15) | The identifier for the user. |
| @P_ErrorMsg | varchar(500) | An output parameter to hold an error message if authorization is denied. |

### Logic Flow
1.  The procedure initializes an output parameter, @P_ErrorMsg, to an empty string.
2.  The procedure executes a query against the EAS_User table.
3.  The query checks if a user with the specified @P_UserID exists in the EAS_User table.
4.  The query also verifies that the user's active status is set to 1.
5.  If no user record is found matching the criteria, the procedure sets the @P_ErrorMsg to a predefined error message indicating the user is not authorized.
6.  The procedure then immediately returns, terminating execution.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None