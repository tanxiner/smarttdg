# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_20231009

### Purpose
Retrieves the registration inbox entries that a user is authorized to view, based on their System Admin or System Approver roles, filtering by pending workflow statuses.

### Parameters
| Name     | Type | Purpose |
| :------- | :--- | :------ |
| @UserID  | INT  | Identifier of the user whose inbox is being queried |

### Logic Flow
1. **Temporary Table Creation**  
   A table `#RegistrationTable` is created to hold registration records that match the user’s role‑based permissions.

2. **Role Retrieval**  
   A cursor iterates over the roles assigned to `@UserID` that end with `_SysAdmin` or `_SysApprover`. For each role the variables `@Line`, `@TrackType`, `@Module`, and `@Role` are set.

3. **System Admin Processing**  
   If the role ends with `_SysAdmin`, three separate inserts populate `#RegistrationTable` with registrations that are:
   - Pending Company Registration  
   - Pending Company Approval  
   - Pending System Admin Approval  
   Each insert joins `TAMS_Registration`, `TAMS_Reg_Module`, and `TAMS_WFStatus`, ensuring the workflow type is `UserRegStatus`, the line and track type match the role, and the registration status ID corresponds to the pending status. The `WFStatus` column is set to the status name from `TAMS_WFStatus`, and `UserType` is derived from `TAMS_Registration.IsExternal`.

4. **System Approver Processing**  
   If the role ends with `_SysApprover`, a second cursor selects registrations that are pending System Approver Approval. For each record:
   - The `RegStatus` is decremented by one to locate the previous status step.  
   - The `UpdatedBy` field of that previous step is retrieved.  
   - If `UpdatedBy` is not the current user, the registration is inserted into `#RegistrationTable` using the same join logic as in the admin case, but limited to the specific registration ID.

5. **Result Retrieval**  
   After all cursors close, a distinct list of records from `#RegistrationTable` is returned, containing registration identifiers, workflow status, user type, and registration details.

6. **Cleanup**  
   The temporary table is dropped.

### Data Interactions
* **Reads:**  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_Registration`  
  - `TAMS_Reg_Module`  
  - `TAMS_WFStatus`  
  - `TAMS_Workflow` (referenced in commented logic but not executed)

* **Writes:**  
  - Temporary table `#RegistrationTable` (created, populated, then dropped)