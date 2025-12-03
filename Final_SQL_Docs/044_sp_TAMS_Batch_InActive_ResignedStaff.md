# Procedure: sp_TAMS_Batch_InActive_ResignedStaff

### Purpose
Deactivates, archives, and removes user accounts for staff who have resigned within the last seven days.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | – | – |

### Logic Flow
1. Identify all users whose `LoginId` matches a `s_lanid` from the `ResignedStaff` table where the resignation effective date (`s_eff_day`) falls between yesterday’s date minus seven days and today’s date, and the `s_lanid` is not empty.  
2. Set `IsActive` to 0 for those users in `TAMS_User`.  
3. Copy the entire user record for each identified user from `TAMS_User` into the archive table `TAMS_User_InActive`.  
4. Delete the same user records from `TAMS_User`.

### Data Interactions
* **Reads:** `TAMS_User`, `VMSDBSVR.ACRS.dbo.ResignedStaff`  
* **Writes:** `TAMS_User` (UPDATE, DELETE), `TAMS_User_InActive` (INSERT)