# Procedure: sp_TAMS_Batch_InActive_ResignedStaff

### Purpose
This stored procedure updates the status of active users to inactive and moves them to a separate table for inactive staff, based on their last login date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |

### Logic Flow
1. The procedure starts by updating the `IsActive` column in the `TAMS_User` table to 0 (inactive) for users who are currently active and have a login ID present in the `ResignedStaff` table.
2. It then inserts new records into the `TAMS_User_InActive` table, which includes all the columns from the original `TAMS_User` table, but with some differences (e.g., `ValidFrom`, `ValidTo`, `IsExternal`, etc.).
3. Finally, it deletes users from the `TAMS_User` table who have a login ID present in the `ResignedStaff` table.

### Data Interactions
* **Reads:** VMSDBSVR.ACRS.dbo.ResignedStaff
* **Writes:** TAMS_User, TAMS_User_InActive