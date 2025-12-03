# Procedure: sp_TAMS_Approval_Endorse_20220930
**Type:** Stored Procedure

### Purpose
This stored procedure performs the business task of approving and endorsing a TAR (Task Assignment Record) by updating its status, assigning it to the next level of approval, and sending notifications to relevant users.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR record being approved. |
| @TARWFID | INTEGER | The current workflow ID associated with the TAR record. |
| @EID | INTEGER | The ID of the current endorser. |
| @ELevel | INTEGER | The level of approval for the current endorser. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approved TAR record (mandatory for reject, optional for approved or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(50) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output parameter for error messages. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Updates TAMS_TAR_Workflow table with approved status and assigns it to the next level of approval.
4. If TAR type is 'Late', sends an email notification to relevant users.
5. Updates TAMS_TAR table with new TAR status ID and updated by user information.
6. Inserts into TAMS_Action_Log table for audit purposes.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Role
* Writes: TAMS_TAR, TAMS_TAR_Workflow, TAMS_Action_Log