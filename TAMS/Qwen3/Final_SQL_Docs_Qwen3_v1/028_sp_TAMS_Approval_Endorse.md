# Procedure: sp_TAMS_Approval_Endorse

### Purpose
This stored procedure is used to endorse a TAR (Technical Approval Request) and update its status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being endorsed. |
| @TARWFID | INTEGER | The current workflow ID associated with the TAR. |
| @EID | INTEGER | The ID of the endorser who is endorsing the TAR. |
| @ELevel | INTEGER | The level of the endorser who is endorsing the TAR. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the TAR (optional). |
| @TVFRunMode | NVARCHAR(50) = NULL | New TVF run mode value (optional). |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF run mode or not (optional). |
| @UserLI | NVARCHAR(100) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. The procedure checks if a transaction is already in progress and sets an internal transaction flag accordingly.
2. It retrieves the user's ID and name from the TAMS_User table based on the provided login ID.
3. It checks if the TAR has already been approved by another user with the same workflow ID, and if so, it sets an error message and exits the procedure.
4. If not, it updates the TAR's workflow status to 'Approved', sets the action by and action on fields, and inserts a new record into the TAMS_TAR_Workflow table.
5. It then checks the next level of endorser for the TAR and performs actions based on the TAR type (Urgent or Not Urgent).
6. If the TAR is urgent, it sends an email to the current endorser and any additional recipients specified in the TAMS_Parameters table.
7. After completing all steps, it logs the action in the TAMS_Action_Log table.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS Paramaters
* Writes: TAMS_TAR, TAMS_TAR_Workflow