# Procedure: EAS_Admin_GET_Roles

### Purpose
This procedure retrieves role information from the EAS_Role table based on specified criteria, including role code, role description, and active status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RoleCode | VARCHAR(50) | The role code to search for. |
| @RoleDesc | VARCHAR(250) | The role description to search for. |
| @Active | SMALLINT | The active status to filter by. |
| @LoginID | VARCHAR(10) | The login ID to determine if the user is an IT_ADMIN. |

### Logic Flow
The procedure first checks if the provided @LoginID corresponds to an IT_ADMIN user. If it does, it executes a search for roles where the Role is 'IT_ADMIN'.  If the @LoginID does not correspond to an IT_ADMIN, the procedure proceeds to search for roles based on the provided input parameters.

The procedure then selects role details from the EAS_Role table. The selection is filtered based on the @RoleCode, @RoleDesc, and @Active parameters. The Role column is filtered using an `OR` condition, allowing a search by @RoleCode or if @RoleCode is null. The RoleDesc column is filtered using a `LIKE` operator with a wildcard character (`%`) to perform a partial match against the @RoleDesc parameter. The Active column is filtered based on the @Active parameter. The results are ordered by the CreatedOn column in descending order.
 

### Data Interactions
* **Reads:** EAS_Role
* **Writes:** None