# Procedure: sp_TAMS_Get_RegistrationInboxByUserID

### Purpose
Return the list of registration modules that a user must review, based on their SysAdmin or SysApprover roles.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | Identifier of the user whose inbox is being retrieved |

### Logic Flow
1. **Create a temporary table** `#RegistrationTable` to hold candidate registrations.  
2. **Declare variables** for role‑specific data and for iterating through records.  
3. **Open a cursor** that selects the user’s roles where the role name ends with `_SysAdmin` or `_SysApprover`.  
4. **Loop through each role** returned by the cursor:  
   - **If the role is a SysAdmin**  
     - Insert into the temp table all registrations that are:  
       * on the same line and track type as the role,  
       * have a workflow status of *Pending*,  
       * and whose current status matches one of the three pending statuses: *Pending Company Registration*, *Pending Company Approval*, or *Pending System Admin Approval*.  
   - **If the role is a SysApprover**  
     - Open a second cursor that selects registrations pending *System Approver Approval* for the same line, track type, and module.  
     - For each registration in this cursor:  
       * Decrement the status value by one to find the previous status.  
       * Retrieve the `UpdatedBy` value for that previous status.  
       * If the `UpdatedBy` user is not the current user, insert the registration into the temp table using the same criteria as for SysAdmin.  
5. **Close and deallocate** both cursors.  
6. **Select distinct rows** from the temp table to produce the final result set.  
7. **Drop the temporary table**.

### Data Interactions
* **Reads:**  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_Registration`  
  - `TAMS_Reg_Module`  
  - `TAMS_WFStatus`  

* **Writes:**  
  - Temporary table `#RegistrationTable` (inserted rows only; no permanent data is modified).