# Procedure: EAS_Admin_UserRole_Insert

### Purpose
This procedure allows an administrator to insert, update, or delete user role entries within the EAS system, managing access permissions based on user and role definitions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RoleCode | VARCHAR(50) | The unique identifier for the role being assigned. |
| @LanID | VARCHAR(50) | The unique identifier for the user to which the role is being assigned. |
| @Active | SMALLINT = 1 | A flag indicating whether the role is currently active. |
| @LoginID | VARCHAR(50) | The identifier of the user who is performing the operation. |
| @Sel | VARCHAR(5) |  A flag indicating whether to update an existing role or insert a new one. |
| @P_ErrorMsge | VARCHAR(225) | An output parameter to store any error messages that occur during the procedure execution. |

### Logic Flow
1.  The procedure initializes the `@P_ErrorMsge` output parameter to an empty string.
2.  It enters a TRY block to handle potential errors during the operation.
3.  Within the TRY block, a transaction is started to ensure atomicity.
4.  The procedure checks the value of the `@Sel` parameter.
    *   If `@Sel` is 'Y', it checks if a role with the specified `@RoleCode` and `@LanID` already exists in the `EAS_User_Role` table.
        *   If the role exists, it updates the existing record in `EAS_User_Role` with the new `@RoleCode`, `@Active` status, and the current timestamp for `UpdatedOn` and `UpdatedBy`.
        *   If the role does not exist, it inserts a new record into the `EAS_User_Role` table with the provided `@LanID`, `SYSID` ('RPEAS'), `@RoleCode`, `@Active` status, the current timestamp for `CreatedOn`, the `@LoginID` as `CreatedBy`, the current timestamp for `UpdatedOn`, and the `@LoginID` as `UpdatedBy`.
    *   If `@Sel` is not 'Y', it executes a deletion operation.
        *   It deletes records from the `EAS_User_Role` table where the `UserID` matches the provided `@LanID` and the `Role` matches the specified `@RoleCode`.
        *   If `@RoleCode` is 'PA', it also deletes records from the `EAS_PA_Supervisor` table where the `UserID` matches the provided `@LanID` and the `SYSID` is 'RPEAS'.
5.  If any error occurs within the TRY block, the transaction is rolled back, and the error message is captured and stored in the `@P_ErrorMsge` output parameter.
6.  Finally, the `@P_ErrorMsge` parameter is set to its current value.

### Data Interactions
*   **Reads:** `EAS_User_Role`, `EAS_PA_Supervisor`
*   **Writes:** `EAS_User_Role`, `EAS_PA_Supervisor`