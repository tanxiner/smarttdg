# Procedure: EAS_Admin_Role_Update

### Purpose
This procedure updates information for a specific role within the EAS system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The new name for the role. |
| @OrginRole | VARCHAR(250) | The current name of the role to be updated. |
| @RoleDesc | VARCHAR(250) | The new description for the role. |
| @Active | VARCHAR(5) |  Indicates whether the role is active or inactive. |
| @CreatedBy | VARCHAR(50) | The user who initiated the update. |
| @P_ErrorMsg | Varchar(250) |  Variable to store any error messages that occur during the process. |

### Logic Flow
1.  The procedure begins with a `TRY` block to handle potential errors during the update process.
2.  A transaction is started within the `TRY` block to ensure atomicity – either all changes are committed, or none are.
3.  The `EAS_Role` table is updated. The `Role` column is set to the value provided in the `@Role` parameter, the `RoleDesc` column is set to the value provided in the `@RoleDesc` parameter, the `Active` column is set to the value provided in the `@Active` parameter, and the `UpdatedBy` column is set to the value provided in the `@CreatedBy` parameter. The `UpdatedOn` column is automatically populated with the current date and time using `GETDATE()`. The update is performed where the `Role` column matches the value provided in the `@OrginRole` parameter.
4.  If the update is successful, the transaction is committed, finalizing the changes.
5.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
6.  The `ROLLBACK TRANSACTION` command is executed, undoing any changes made during the transaction.
7.  An error message is retrieved from the system and stored in the `@P_ErrorMsg` parameter.
8.  The `@P_ErrorMsg` parameter is set to an empty string if it is null.

### Data Interactions
* **Reads:** [EAS_Role]
* **Writes:** [EAS_Role]