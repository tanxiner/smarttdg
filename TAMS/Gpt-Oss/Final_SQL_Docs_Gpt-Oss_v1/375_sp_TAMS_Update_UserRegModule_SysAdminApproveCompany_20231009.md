# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany_20231009

### Purpose
Approve a user registration that is pending company approval, advance its workflow, notify approvers, register the company if needed, and log the action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module record to process |
| @UserID | NVARCHAR(200) | Identifier of the system user performing the approval |

### Logic Flow
1. **Start Transaction** – All operations are wrapped in a single transaction to guarantee atomicity.  
2. **Temporary Table Creation** – A table `#TMP_RegModule` is created to hold the set of registration module rows that share the same `RegID` as the target record and are currently in the “Pending” status.  
3. **Eligibility Check** – The procedure verifies that the supplied `@RegModID` refers to a record whose `RegStatus` equals the workflow status ID for “Pending Company Approval”. If not, the procedure exits without making changes.  
4. **Load Related Records** – The `RegID` of the target record is retrieved. All rows in `TAMS_Reg_Module` that belong to this `RegID` and are in the “Pending” status are inserted into `#TMP_RegModule`.  
5. **Cursor Loop over Pending Rows** – For each row in `#TMP_RegModule` the following steps are performed:  
   a. **Determine Next Workflow Stage** –  
      - Find the active workflow definition (`TAMS_Workflow`) for the row’s `Line` and type “ExtUser”.  
      - Using that workflow, locate the next endorser record (`TAMS_Endorser`) whose level is one greater than the current status level.  
      - Retrieve the new workflow status ID and role ID from that endorser.  
      - Translate the status ID into a status text (`TAMS_WFStatus`).  
   b. **Create New Registration Module Record** – Insert a new row into `TAMS_Reg_Module` with the new status, workflow, and endorser information, marking it as “Pending”.  
   c. **Mark Current Row Approved** – Update the original row’s `WFStatus` to “Approved” and set its `UpdatedOn` timestamp.  
   d. **Email Notification** –  
      - Build a comma‑separated list of email addresses for users who hold the role identified in step 5a.  
      - Compose an email body that invites the approvers to log into TAMS and approve or reject the request.  
      - Queue the email via `EAlertQ_EnQueue`.  
6. **Company Registration** – After all pending rows are processed:  
   a. If a company record does not already exist for the UEN number found in `TAMS_Registration`, insert a new record into `TAMS_Company` using the registration details.  
   b. Retrieve the new company ID and update the `CompanyID` field of the corresponding `TAMS_Registration` row.  
7. **Audit Log** – Insert a record into `TAMS_Action_Log` describing the system‑admin approval action.  
8. **Commit Transaction** – Finalise all changes.  
9. **Error Handling** – If any error occurs, the transaction is rolled back.

### Data Interactions
* **Reads:**  
  - `TAMS_Reg_Module`  
  - `TAMS_WFStatus`  
  - `TAMS_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_User`  
  - `TAMS_User_Role`  
  - `TAMS_Registration`  
  - `TAMS_Company`  
  - `TAMS_Action_Log`  

* **Writes:**  
  - `TAMS_Reg_Module` (insert new rows, update status)  
  - `TAMS_Company` (insert if missing)  
  - `TAMS_Registration` (update CompanyID)  
  - `TAMS_Action_Log` (audit entry)  

---