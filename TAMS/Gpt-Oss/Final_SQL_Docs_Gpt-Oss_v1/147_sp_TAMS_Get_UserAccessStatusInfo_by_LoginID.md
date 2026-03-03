# Procedure: sp_TAMS_Get_UserAccessStatusInfo_by_LoginID

### Purpose
Return a list of line, track type, module and access status for a given login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | Login identifier used to locate the user and related registrations |

### Logic Flow
1. Create a temporary table #AccessStatus to hold the result rows.  
2. If a user exists with the supplied @LoginID, retrieve that user's UserID.  
3. Open a cursor over all active roles (excluding those with Line = 'All').  
4. For each role row (Line, TrackType, Module):  
   a. If the user has a role that matches the current Line and Module, insert a row into #AccessStatus with Status = 'Approved'.  
   b. Otherwise, check if the user has a registration record whose module matches the current Line, TrackType and Module and whose RegStatus is a workflow status that is active and not yet 'Approved' or 'Rejected'.  
   c. If such a registration exists, insert a row into #AccessStatus with Status = 'Pending Approval'.  
5. If no user exists for the supplied @LoginID, repeat step 3 but skip the role‑approval check; only insert rows for pending registrations as described in 4b.  
6. After the cursor loop, close and deallocate the cursor.  
7. Return all rows from #AccessStatus and drop the temporary table.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Role, TAMS_User_Role, TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus  
* **Writes:** #AccessStatus (temporary table)