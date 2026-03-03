# Procedure: sp_TAMS_Approval_Endorse_20230410

### Purpose
This stored procedure performs the approval and endorsement process for a TAR (Task Assignment Request) form. It updates the TAR status, assigns the next level of endorser, and sends notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR form being approved. |
| @TARWFID | INTEGER | The current workflow ID associated with the TAR form. |
| @EID | INTEGER | The ID of the current endorser. |
| @ELevel | INTEGER | The level of the current endorser. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approval process (mandatory for reject, optional for approved or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF run mode or not. |
| @UserLI | NVARCHAR(100) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If so, it sets an internal flag to 1 and begins a new transaction.
2. It updates the TAR form status to 'Approved' and assigns the current endorser's ID as the action by and on dates.
3. If the TVF run mode update indicator is set to 1, it updates the TAR form with the new TVF run mode value.
4. The procedure retrieves the next level of endorser from the TAMS_Endorser table based on the current endorser's level.
5. If there is no next level of endorser, it updates the TAR form status to a specific value (9 for NEL approved or 8 for DTL or LRT).
6. It sends an email notification to relevant parties (e.g., the next level of endorser) if the TAR form type is 'Urgent'.
7. The procedure logs the approval action in the TAMS_Action_Log table.
8. If any errors occur during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Role
* Writes: TAMS_TAR, TAMS_Action_Log