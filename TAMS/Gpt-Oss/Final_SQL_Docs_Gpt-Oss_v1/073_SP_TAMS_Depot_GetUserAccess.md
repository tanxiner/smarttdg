# Procedure: SP_TAMS_Depot_GetUserAccess

### Purpose
Determine whether a specified username exists in the TAMS_User table and return the result as a bit flag.

### Parameters
| Name     | Type      | Purpose |
| :---     | :---      | :--- |
| @username | nvarchar(50) | Input username to check for existence. |
| @res      | bit OUTPUT   | Output flag: 1 if the user exists, 0 otherwise. |

### Logic Flow
1. Initialize the output flag `@res` to 0.  
2. Query the `TAMS_User` table for a row where `LoginId` matches the supplied `@username`.  
3. If a matching row is found, set `@res` to 1.  
4. If no matching row is found, leave `@res` as 0.  

### Data Interactions
* **Reads:** `TAMS_User`  
* **Writes:** None