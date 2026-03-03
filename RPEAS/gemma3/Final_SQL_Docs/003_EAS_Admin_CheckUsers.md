# Procedure: EAS_Admin_CheckUsers

### Purpose
This procedure counts the number of users in the EAS_User table matching a specified UserID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | Varchar(10) | The UserID to search for. |
| @Count | int | The count of users matching the @User. |

### Logic Flow
1.  The procedure receives a UserID as input.
2.  The procedure queries the EAS_User table.
3.  The query filters the table to include only rows where the UserID matches the provided @User.
4.  The COUNT aggregate function calculates the total number of rows that satisfy the filtering criteria.
5.  The calculated count is assigned to the output parameter @Count.
6.  The value of @Count is then returned.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None