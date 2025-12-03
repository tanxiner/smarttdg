# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_hnin

### Purpose
Retrieves a list of registration records that a user is responsible for reviewing or approving, based on the user’s system‑admin or system‑approver roles.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | Identifier of the user whose inbox is being generated |

### Logic Flow
1. **Temporary table creation** – A table named #RegistrationTable is created to hold the results. It contains columns for registration identifiers, line, track type, module, workflow status, user type, and registration details.

2. **Variable declaration** – Variables are set up to hold role information, registration identifiers, status, workflow identifiers, and the user who last updated a record.

3. **Role cursor** – A cursor named cur selects all roles assigned to the supplied @UserID that end with `_SysAdmin` or `_SysApprover`. For each role record, the following steps are performed:

   a. **SysAdmin role processing** – If the role ends with `_SysAdmin`, three separate queries are executed to insert into #RegistrationTable:
      - Registrations where the workflow status is “Pending Company Registration”.
      - Registrations where the workflow status is “Pending Company Approval”.
      - Registrations where the workflow status is “Pending System Admin Approval”.
      Each query joins the registration, module, and workflow status tables, filters by the current line, track type, module, and ensures the module status is “Pending”.

   b. **SysApprover role processing** – If the role ends with `_SysApprover`, a second cursor named cur1 is opened. This cursor selects registrations that are pending system approver approval for the current line, track type, and module. For each record returned:
      - The registration status is decremented by one to locate the previous status record.
      - The `UpdatedBy` field of that previous status record is retrieved.
      - If the `UpdatedBy` value does not match the current @UserID, the registration is inserted into #RegistrationTable using the same join logic as in the SysAdmin case.

4. **Cursor cleanup** – Both cursors are closed and deallocated after use.

5. **Result set** – A distinct list of rows from #RegistrationTable is selected and returned to the caller.

6. **Temporary table drop** – #RegistrationTable is dropped to clean up temporary storage.

### Data Interactions
* **Reads:**  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_Registration  
  - TAMS_Reg_Module  
  - TAMS_WFStatus  
  - (TAMS_Workflow is referenced in a commented section but not used in the active logic)

* **Writes:**  
  - #RegistrationTable (temporary table only)