# Procedure: sp_TAMS_Get_ParentMenuByUserRole

### Purpose
This stored procedure retrieves the parent menu for a given user role, considering whether the user is accessing the application from an internet connection.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve the parent menu for. |
| @IsInternet | NVARCHAR(1) | A flag indicating whether the user is accessing the application from an internet connection (0 = no, 1 = yes). |

### Logic Flow
The procedure first checks if a valid user exists with the provided ID and active status. If a valid user is found, it then determines whether to retrieve the parent menu based on the value of @IsInternet. If @IsInternet is 0, it retrieves the parent menu for all roles assigned to the user; if @IsInternet is 1, it retrieves the parent menu only for roles assigned to the user and accessible from an internet connection.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role