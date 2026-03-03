# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20231009

### Purpose
Approve a user registration module, update its workflow status to *Approved*, create a user record if missing, log the action, and send an approval notification email.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | Identifier of the registration module record to approve |
| @UpdatedBy | INT | User ID performing the approval |

### Logic Flow
1. **Start Transaction** – All subsequent operations are wrapped in a single transaction to ensure atomicity.  
2. **Determine External Flag** – Retrieve `IsExternal` from the registration that belongs to the module identified by `@RegModID`.  
3. **Load Module Details** – Fetch `RegID`, `Line`, `TrackType`, `Module`, `IsExternal`, and current `RegStatus` from the module and its registration.  
4. **Set Workflow Type** –  
   * If the registration is external, set `WorkFlowType` to `ExtUser`.  
   * Otherwise, set it to `TARIntUser` when the module is `TAR`; otherwise set to `OCCIntUser`.  
5. **Identify Next Stage** – Query `TAMS_WFStatus` for the status record where `WFType` is `UserRegStatus`, the line matches the module’s line, and the status is `Approved`. Store its `WFStatusId` and `WFStatus`.  
6. **Find Current Workflow** – Locate the active workflow in `TAMS_Workflow` that matches the module’s line, the determined `WorkFlowType`, and whose effective date range includes today.  
7. **Determine Next Endorser** – From `TAMS_Endorser`, select the record whose `Level` is one greater than the level of the current status, ensuring it is active and within its effective dates. Capture its `WFStatusID`, `RoleID`, and `ID` as the next endorser.  
8. **Process Module Record** – If a module record exists for `@RegModID`:  
   a. **Insert New Module Entry** – Add a new row to `TAMS_Reg_Module` with the same `RegID`, `Line`, `TrackType`, `Module`, the next stage ID, workflow ID, endorser ID, status `Approved`, the retrieved `WFStatus`, current timestamps, and the updater.  
   b. **Update Existing Record** – Set its `WFStatus` to `Approved`, update timestamps, and updater.  
   c. **Create User if Needed** –  
      * Check if a user with the registration’s `LoginID` exists in `TAMS_User`.  
      * If not, insert a new user:  
        - For internal registrations, copy fields from `TAMS_Registration`, set `IsExternal` to 0, `IsActive` to 1, and timestamps.  
        - For external registrations, copy all fields, preserve `IsExternal`, `Password`, `CompanyID`, contact person details, set `IsActive` to 1, and timestamps.  
   d. **Audit Log** – Insert a record into `TAMS_Action_Log` noting the line, module, action type `UserReg-Registration`, the registration ID, a descriptive message, current timestamp, and updater.  
   e. **Prepare Email Notification** –  
      * Retrieve the registration’s email as the recipient list.  
      * Set sender, system ID, subject, system name, greeting, and empty CC/BCC lists.  
      * Build the email body with a message that the user can now access TAMS, a link to the login page (different for external users), and a standard footer.  
      * Call `EAlertQ_EnQueue` to enqueue the email with the constructed parameters.  
9. **Commit Transaction** – Finalize all changes.  
10. **Error Handling** – If any step fails, roll back the transaction to leave the database unchanged.

### Data Interactions
* **Reads:**  
  - `TAMS_Registration`  
  - `TAMS_Reg_Module`  
  - `TAMS_WFStatus`  
  - `TAMS_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_User` (existence check)  

* **Writes:**  
  - `TAMS_Reg_Module` (insert & update)  
  - `TAMS_User` (insert)  
  - `TAMS_Action_Log` (insert)  
  - `EAlertQ_EnQueue` (procedure call for email)