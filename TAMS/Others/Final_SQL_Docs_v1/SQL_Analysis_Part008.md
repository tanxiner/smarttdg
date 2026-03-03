# Procedure: sp_TAMS_Approval_Endorse20250120
**Type:** Stored Procedure

The procedure performs the business task of approving a TAR (Technical Approval Request) form by an endorser.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR to be approved. |
| @TARWFID | INTEGER | The current workflow ID for the TAR. |
| @EID | INTEGER | The ID of the endorser who is approving the TAR. |
| @ELevel | INTEGER | The level of the endorser (e.g., 1, 2, etc.). |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approved TAR. Mandatory for Reject, Optional for Approved/Endorse. |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to Update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(100) = NULL | User Login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Action_Log
* Writes: TAMS_TAR_Workflow, TAMS_TAR