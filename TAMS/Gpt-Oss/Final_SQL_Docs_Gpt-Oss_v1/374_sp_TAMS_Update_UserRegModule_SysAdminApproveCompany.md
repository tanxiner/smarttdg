# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany

### Purpose
Approve a user registration request at the company level, advance the workflow, notify approvers, register the company if needed, and log the action.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @RegModID | INT           | Identifier of the registration module record to process. |
| @UserID   | NVARCHAR(200) | Identifier of the system admin performing the approval. |

### Logic Flow
1. **Start Transaction** – All operations are wrapped in a single transaction to ensure atomicity.  
2. **Create Temporary Table** – `#TMP_RegModule` holds module rows that will be processed.  
3. **Validate Pending Status** – Check that the supplied `@RegModID` has a `RegStatus` equal to the active status code for *Pending Company Approval*. If not, the procedure exits without changes.  
4. **Retrieve Registration ID** – Load the `RegID` associated with the module.  
5. **Populate Temp Table** – Insert into `#TMP_RegModule` every module row for this `RegID` whose `WFStatus` is *Pending*.  
6. **Process Each Module Row** – Open a cursor over the temp table and iterate:
   - **Determine Next Workflow Stage** – Find the active workflow definition (`TAMS_Workflow`) matching the module’s `Line` and `TrackType`.  
   - **Select Next Endorser** – From `TAMS_Endorser`, pick the record whose `Level` is one greater than the current status level for the same workflow and line, within the effective date range.  
   - **Get New Status Text** – Retrieve the descriptive status string from `TAMS_WFStatus` for the new status ID.  
   - **Insert New Module Record** – Create a new `TAMS_Reg_Module` entry with the new status, workflow, endorser, and a *Pending* `WFStatus` flag.  
   - **Mark Original as Approved** – Update the original module row to set `WFStatus` to *Approved* and refresh `UpdatedOn`.  
   - **Build Email Recipient List** – Query `TAMS_User` joined with `TAMS_User_Role` to collect email addresses of users whose role matches the new workflow role ID.  
   - **Compose Email** – Assemble a multi‑part HTML body that includes a link to the TAMS login page.  
   - **Queue Email** – Call `EAlertQ_EnQueue` to enqueue the notification for the collected recipients.  
7. **Close Cursor** – Release resources used for the module loop.  
8. **Register Company** – If no `TAMS_Company` record exists for the UEN number found in `TAMS_Registration` for this `RegID`, insert a new company record using the registration details.  
9. **Update Registration with Company ID** – Set the `CompanyID` field in `TAMS_Registration` to the ID of the newly inserted or existing company.  
10. **Audit Log Entry** – Insert a record into `TAMS_Action_Log` documenting that the system admin approved the company registration for the user registration.  
11. **Commit Transaction** – Persist all changes.  
12. **Error Handling** – If any step fails, roll back the entire transaction.

### Data Interactions
* **Reads:**  
  - TAMS_Reg_Module  
  - TAMS_WFStatus  
  - TAMS_Workflow  
  - TAMS_Endorser  
  - TAMS_Company  
  - TAMS_Registration  
  - TAMS_User  
  - TAMS_User_Role  

* **Writes:**  
  - TAMS_Reg_Module (insert new rows, update existing)  
  - TAMS_Company (insert if missing)  
  - TAMS_Registration (update CompanyID)  
  - TAMS_Action_Log (insert audit record)