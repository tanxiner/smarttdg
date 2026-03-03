# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_20231009

### Purpose
Creates a new internal user registration module record, logs the action, and sends an approval request email to system approvers.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @RegID    | INT           | Identifier of the registration to be processed. |
| @Line     | NVARCHAR(20)  | Business line for which the registration applies. |
| @TrackType| NVARCHAR(50)  | Tracking category of the registration. |
| @Module   | NVARCHAR(20)  | Module code (e.g., TAR, OCC). |

### Logic Flow
1. **Begin Transaction** – All subsequent operations are wrapped in a single transaction to ensure atomicity.  
2. **Determine Workflow ID**  
   * If @Module equals ‘TAR’, query `TAMS_Workflow` for a workflow of type `TARIntUser`.  
   * Otherwise, query for type `OCCIntUser`.  
   * The selected workflow must match the supplied @Line, @TrackType, be effective for the current date, and be active.  
3. **Retrieve Next Stage Details** – From `TAMS_Endorser` fetch the first level endorser for the identified workflow:  
   * `WFStatusId` → @NextStageID  
   * `RoleID` → @NewWFRoleID  
   * `ID` → @EndorserID  
4. **Get Status Text** – From `TAMS_WFStatus` obtain the status description for @NextStageID and store it in @WFStatus.  
5. **Insert Registration Module Record** – Add a new row to `TAMS_Reg_Module` with:  
   * Registration ID, Line, TrackType, Module, NextStageID, WorkflowID, EndorserID, status ‘Pending’, @WFStatus, current timestamp, and audit flags.  
6. **Log Action** – Insert a descriptive entry into `TAMS_Action_Log` indicating that an internal user submitted a registration for the specified module.  
7. **Build Email Recipient List** –  
   * Open a cursor over users whose roles match `%SysApprover%` for the given Line, TrackType, and Module.  
   * Concatenate their email addresses into @ToList, separated by commas.  
8. **Compose Email Content** – Assemble an HTML body that:  
   * Informs the recipient to approve/reject the registration.  
   * Provides a link to the TAMS login page.  
   * Includes a standard footer.  
9. **Queue Email** – Call `EAlertQ_EnQueue` with the constructed parameters to enqueue the approval request email.  
10. **Commit Transaction** – Finalize all database changes.  
11. **Error Handling** – If any step fails, roll back the transaction to leave the database unchanged.

### Data Interactions
* **Reads:**  
  * `TAMS_Workflow`  
  * `TAMS_Endorser`  
  * `TAMS_WFStatus`  
  * `TAMS_User`  
  * `TAMS_User_Role`  
  * `TAMS_Role`  

* **Writes:**  
  * `TAMS_Reg_Module`  
  * `TAMS_Action_Log`  
  * (via procedure call) `EAlertQ_EnQueue` – enqueues an email for delivery.