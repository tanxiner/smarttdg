# Procedure: sp_TAMS_Approval_Reject_20220930

### Purpose
This stored procedure performs a rejection of a TAR (Task Assignment Request) form, updating its status and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @UserLI | NVARCHAR(50) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It retrieves the user's details from TAMS_User based on the provided User Login ID.
3. The procedure updates the TAR form's status to 'Rejected' and sets the remark field with the provided remarks.
4. It selects the endorser title, TAR type, line, email, company, and access date from TAMS_TAR based on the TAR ID.
5. If the TAR type is 'Late', it sends a rejection email using sp_TAMS_Email_Late_TAR.
6. The procedure updates the TAR form's status to reflect the current level endorser title.
7. It checks if the workflow type is 'LateAfter' and involves power 1 with the current endorser level being 2. If true, it sends an email using sp_TAMS_Email_Late_TAR_OCC.
8. The procedure commits or rolls back the transaction based on whether any errors occurred during execution.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_Workflow, TAMS_Role, TAMS_User_Role
* Writes: TAMS_TAR (status and remark fields)