# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule

### Purpose
Creates a new internal user registration record, assigns the initial workflow stage, logs the action, and sends an approval request email to system approvers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Identifier of the registration to be processed |
| @Line | NVARCHAR(20) | Business line for which the registration applies |
| @TrackType | NVARCHAR(50) | Type of track (e.g., user category) |
| @Module | NVARCHAR(20) | Module code (TAR, DCC, or other) |

### Logic Flow
1. Begin a transaction to ensure atomicity.  
2. Determine the active workflow ID that matches the supplied `@Line`, `@TrackType`, and `@Module`.  
   * If `@Module` is `TAR`, look for workflow type `TARIntUser`.  
   * If `@Module` is `DCC`, look for workflow type `DCCIntUser`.  
   * Otherwise, look for workflow type `OCCIntUser`.  
   The workflow must be currently effective and active.  
3. Retrieve the first level endorser for that workflow: obtain the workflow status ID, role ID, and endorser ID.  
4. Resolve the human‑readable status text for the retrieved status ID.  
5. Insert a new record into `TAMS_Reg_Module` with the registration ID, line, track type, module, next stage ID, workflow ID, endorser ID, a status of `Pending`, the status text, timestamps, and a flag indicating active.  
6. Insert an audit entry into `TAMS_Action_Log` noting that the internal user submitted a registration for the specified module.  
7. Build a comma‑separated list of email addresses for all users who hold a role whose name contains `SysApprover` for the given line, track type, and module.  
8. Compose an email body that includes a link to the TAMS login page and a standard footer.  
9. Enqueue the email via `EAlertQ_EnQueue`, passing sender, system ID, subject, greetings, body, recipients, and separators.  
10. Commit the transaction.  
11. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** `TAMS_Workflow`, `TAMS_Endorser`, `TAMS_WFStatus`, `TAMS_User`, `TAMS_User_Role`, `TAMS_Role`  
* **Writes:** `TAMS_Reg_Module`, `TAMS_Action_Log` (and enqueues an email through `EAlertQ_EnQueue`)