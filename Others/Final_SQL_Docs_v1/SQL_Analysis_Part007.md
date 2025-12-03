# Procedure: sp_TAMS_Approval_Endorse
**Type:** Stored Procedure

The purpose of this stored procedure is to approve a TAR (Technical Approval Request) and update its status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being approved. |
| @TARWFID | INTEGER | The current workflow ID for the TAR. |
| @EID | INTEGER | The ID of the endorser approving the TAR. |
| @ELevel | INTEGER | The level of the endorser approving the TAR. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks or comments about the approval. (Optional for approved, mandatory for reject). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to Update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(100) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message indicating the result of the approval process. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Action_Log, TAMS_Parameters
* **Writes:** TAMS_TAR_Workflow, TAMS_TAR