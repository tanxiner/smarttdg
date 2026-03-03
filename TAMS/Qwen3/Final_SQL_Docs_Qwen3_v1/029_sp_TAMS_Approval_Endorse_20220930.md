# Procedure: sp_TAMS_Approval_Endorse_20220930

### Purpose
This stored procedure performs the approval and endorsement process for a TAR (Trade Agreement) form, updating its status to "Approved" and assigning an endorser.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR form being approved. |
| @TARWFID | INTEGER | The current workflow ID for the TAR form. |
| @EID | INTEGER | The ID of the endorser assigning approval. |
| @ELevel | INTEGER | The level of the endorser (e.g., 1, 2, etc.). |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approved TAR form (mandatory for reject, optional for approve or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(50) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets an internal transaction flag to 1.
2. It updates the TAR form's status to "Approved" and assigns the current endorser as the action by and on dates.
3. If the TVF Run Mode update indicator is set to 1, it updates the TAR form's TVF mode.
4. The procedure then selects the next level endorser based on the current endorser's level.
5. If there is no next level endorser (i.e., this is the last level), it updates the TAR form's status and sends an email to the NEL approved role if applicable.
6. Otherwise, it inserts a new workflow record for the next level endorser and updates the TAR form's status.
7. It then selects all emails where the role ID matches the next level endorser and sends an email to these roles using the sp_TAMS_Email_Apply_Late_TAR procedure.
8. The procedure logs the approval action in the TAMS_Action_Log table.
9. If any errors occur during execution, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Role, TAMS_Workflow
* Writes: TAMS_TAR, TAMS_TAR_Workflow