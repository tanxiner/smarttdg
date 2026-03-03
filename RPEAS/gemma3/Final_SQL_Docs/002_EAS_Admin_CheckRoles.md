# Procedure: EAS_Admin_CheckRoles

### Purpose
This procedure determines the number of records in the EAS_Role table that match a specified RoleCode.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | Varchar(50) | The RoleCode to search for. |
| @Count | int | The number of matching RoleCodes. |

### Logic Flow
1.  The procedure receives a RoleCode as input.
2.  It queries the EAS_Role table, searching for records where the Role column matches the provided RoleCode.
3.  The query counts all matching records.
4.  The count of matching records is assigned to the output parameter @Count.
5.  The value of @Count is then returned.

### Data Interactions
* **Reads:** EAS_Role
* **Writes:** None