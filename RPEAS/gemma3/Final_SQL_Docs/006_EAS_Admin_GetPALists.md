# Procedure: EAS_Admin_GetPALists

### Purpose
This procedure retrieves a list of users and their associated PA counts for the specified role within the RPEAS environment.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | Varchar(50) | The role identifier to filter users by. |
| @RoleDesc | Varchar(200) | Output parameter containing the description of the role. |

### Logic Flow
1.  The procedure begins by retrieving the description for the role specified in the @Role parameter from the EAS_Role table, filtering for the RPEAS system and the provided role. This description is then assigned to the @RoleDesc output parameter.
2.  The procedure then selects user information from the EAS_User table, filtering for users within the RPEAS system that are marked as active.
3.  The selection further filters the users based on a subquery that retrieves all user IDs associated with the specified role from the EAS_User_ROLE table, again filtering for the RPEAS system and active users.
4.  Finally, the selected user data is ordered alphabetically by the user's name.

### Data Interactions
* **Reads:** EAS_Role, EAS_User, EAS_User_ROLE
* **Writes:** None