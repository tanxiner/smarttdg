### Procedure: EAS_Admin_MenuRole_Insert

### Purpose
This procedure inserts a new role within the EAS Menu Role table, handling both initial insertion and updates based on existing role configurations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RoleCode | VARCHAR(50) | The unique identifier for the role. |
| @MenuID | VARCHAR(50) | The ID of the menu to which the role is assigned. |
| @SysID | VARCHAR(10) | The system identifier for the menu and role. |
| @Active | SMALLINT = 1 | Indicates whether the role is active. |
| @LoginID | VARCHAR(50) | The ID of the user making the change. |
| @Sel | VARCHAR(5) |  Determines whether to insert a new role or update an existing one. |
| @P_ErrorMsge | varchar(225) | Output parameter to store any error messages. |

### Logic Flow
1.  **Initialization:** Sets the output error message parameter to an empty string.
2.  **Transaction Start:** Begins a database transaction to ensure atomicity (all operations succeed or none do).
3.  **Conditional Insertion/Update:**
    *   **If @Sel = 'Y':**  This block attempts to insert a new role.
        *   **Check for Existing Role:** Checks if a role with the same `MenuID` and `Role` already exists.
            *   **If Role Exists:** Updates the existing role with the provided `Active` status, `Updatedby`, and `UpdatedOn`.
            *   **If Role Does Not Exist:** Inserts a new row into the `EAS_Menu_Role` table with the provided `SysID`, `MenuID`, `Role`, `Active` status, `CreatedBy`, `CreatedOn`, `UpdatedBy`, and `UpdatedOn`.
            *   **Parent Menu Check:** Checks if the parent menu exists and if the role is associated with the parent menu. If not, it inserts a new row into the `EAS_Menu_Role` table with the provided `SysID`, `MenuID`, `Role`, `Active` status, `CreatedBy`, `CreatedOn`, `UpdatedBy`, and `UpdatedOn`.
    *   **If @Sel = 'N':** This block attempts to delete the role.
        *   **Delete Existing Role:** Deletes the role from the `EAS_Menu_Role` table based on the `MenuID` and `Role`.
        *   **Parent Menu Check:** Checks if the parent menu exists and if the role is associated with the parent menu. If not, it deletes the role from the `EAS_Menu_Role` table based on the `MenuID` and `Role`.
4.  **Transaction Commit/Rollback:** If all operations succeed, the transaction is committed. If any error occurs, the transaction is rolled back, and the output error message parameter is populated with the error message.
5.  **Error Handling:** Catches any errors that occur during the transaction and sets the output error message parameter with the error message.
6.  **Output:** Sets the output error message parameter to the value stored in the error message parameter.

### Data Interactions
* **Reads:** `EAS_Menu_Role`, `EAS_Menu`
* **Writes:** `EAS_Menu_Role`