# Procedure: sp_TAMS_Approval_Endorse20250120

### Purpose
This stored procedure is used to approve and endorse a TAR (Technical Approval Request) form, which involves updating the workflow status, assigning an endorser, and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) = NULL | New Column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to Update TVF Run Mode or Not |
| @UserLI | NVARCHAR(100) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure checks if the TAR has already been approved by the current user, and if so, it sets an error message and exits.
2. It updates the workflow status to 'Approved' and assigns the current user as the action by.
3. If the TVF Run Mode update indicator is set to 1, it updates the TAR's TVF mode.
4. The procedure retrieves the next endorser for the current level and checks if there are any pending approvals for that level. If not, it inserts a new workflow record with the next endorser assigned.
5. It updates the TAR status ID based on the line number (NEL or LRT).
6. If the TAR type is 'Urgent', it sends an urgent email to the current user and the next endorser.
7. The procedure logs the approval action in the TAMS_Action_Log table.
8. If any errors occur during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Parameters, TAMS_Workflow, TAMS_Role, TAMS_Action_Log
* **Writes:** TAMS_TAR_Workflow, TAMS_TAR