# Procedure: sp_TAMS_Approval_Reject

### Purpose
This stored procedure performs a rejection of a TAR (Task Assignment Record) form, updating its status and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (mandatory for Reject, optional for Approved/Endorse) |
| @UserLI | NVARCHAR(100) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It updates the TAR form's status to 'Rejected' and records the rejection remarks.
3. It retrieves the endorser title and current level from the TAMS_Endorser table based on the provided Endorser ID and Level.
4. Depending on the TAR type, it determines whether to send an urgent email or not. If urgent, it sets the TAR status to 'Rejected' and sends a notification using the sp_TAMS_Email_Urgent_TAR procedure.
5. It logs the rejection action in the TAMS_Action_Log table.
6. If any errors occur during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_Endorser, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Action_Log, TAMS_Parameters
* Writes: TAMS_TAR, TAMS_TAR_Workflow