# Procedure: EAS_Form_Get_ApproverLists

### Purpose
This procedure retrieves a list of user names and identifiers from the EAS_User table, excluding a specified user, and filtering for users with the PA role and those associated with the RPEAS system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_ExclUser | varchar(15) | User identifier to exclude from the results. |

### Logic Flow
1.  The procedure begins by selecting the userid and name columns from the EAS_User table.
2.  It filters the selection to include only users where the active flag is set to 1.
3.  It further restricts the selection to users associated with the RPEAS system, ensuring that only users linked to the RPEAS system are included.
4.  The procedure excludes a specified user identifier, @P_ExclUser, from the results.
5.  Finally, the results are ordered alphabetically by user name.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None