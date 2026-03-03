# Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule_20231009

### Purpose
Insert a new external user registration module record, log the action, and trigger an approval email when the registration originates from a company.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Identifier of the registration record |
| @Line | NVARCHAR(20) | Business line identifier |
| @TrackType | NVARCHAR(50) | Tracking type for the workflow |
| @Module | NVARCHAR(20) | Module name being registered |

### Logic Flow
1. Start a transaction.  
2. Initialise the workflow level to 1.  
3. Check if the registration belongs to a company by comparing the UENNo in the registration with any UENNo in the company table.  
   - If a match exists, set the level to 3 (skip the first two workflow stages).  
4. Declare variables for workflow status, next stage ID, workflow ID, and endorser ID.  
5. Retrieve the active workflow ID that matches the line, track type, and workflow type 'ExtUser'.  
6. Using the workflow ID and the determined level, fetch the next stage ID and the endorser ID from the endorser table.  
7. Look up the textual workflow status from the status table using the next stage ID.  
8. Insert a new record into the registration module table with the registration ID, line, track type, module, next stage ID, workflow ID, endorser ID, a status of 'Pending', the workflow status text, the current timestamp, and flags set to 1.  
9. Insert an audit log entry describing the submission of the external user registration.  
10. If the level is 3 (company registration), prepare to send an approval email:  
    - Build a comma‑separated list of email addresses for all users who hold a role containing 'SysApprover' for the given line, track type, and module.  
    - Construct an email body that includes a link to the TAMS login page and a standard footer.  
    - Queue the email using the EAlertQ_EnQueue procedure with the assembled parameters.  
11. Commit the transaction.  
12. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_Company, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User, TAMS_User_Role, TAMS_Role  
* **Writes:** TAMS_Reg_Module, TAMS_Action_Log

---