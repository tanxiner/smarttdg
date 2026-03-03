# Procedure: sp_TAMS_Get_SignUpStatusByLoginID

### Purpose
Retrieve the current sign‑up status for a user identified by a login ID, including workflow status, pending role, and notification timestamp for each line/module combination.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The user’s login identifier used to locate registration records. |

### Logic Flow
1. **Check for Registration** – Verify that at least one record exists in `TAMS_Registration` for the supplied `@LoginID`.  
2. **Identify Latest Registration** – If a record exists, capture the most recent registration entry (ordered by `CreatedOn` descending) and store its `ID` in a local variable.  
3. **Prepare Temporary Result Set** – Create a temporary table `#AccessStatus` with columns for line, module, status, pending role, and notification time.  
4. **Iterate Over Line/Module Pairs** – Open a cursor that selects distinct `Line` and `Module` values from the registration and module tables where the registration matches the login ID.  
5. **Process Each Pair**  
   - Retrieve the most recent module status (`RegStatus`), the last update time (`UpdatedOn`), the user type flag (`IsExternal`), and derive a user type string (`ExtUser` or `IntUser`).  
   - Determine the workflow status and its ID by querying `TAMS_WFStatus` for the current line, a workflow type of `UserRegStatus`, active status, and a status ID that appears in the module’s status list.  
   - If the user is internal (`IsExternal = 0`), prepend the module name to the user type string.  
   - If the workflow status is one of `Rejected`, `Company Rejected`, or `Approved`, set the pending role to `-`.  
   - Otherwise, look up the role name from the endorser, workflow, and role tables where the workflow matches the derived user type, is active, within its effective date range, and the endorser line matches.  
   - Insert a row into `#AccessStatus` containing the line, module, workflow status, pending role, and notification timestamp.  
6. **Finalize Cursor** – Close and deallocate the cursor.  
7. **Return Results** – Select all rows from `#AccessStatus`, ordered by line and module descending, then drop the temporary table.

### Data Interactions
* **Reads:** `TAMS_Registration`, `TAMS_Reg_Module`, `TAMS_WFStatus`, `TAMS_Endorser`, `TAMS_Workflow`, `TAMS_Role`  
* **Writes:** Temporary table `#AccessStatus` (created and dropped within the procedure)