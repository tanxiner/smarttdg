# Procedure: sp_TAMS_Approval_Proceed_To_App_20220930
**Type:** Stored Procedure

The purpose of this stored procedure is to approve a TAR (Technical Approval Request) and update its status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being approved. |
| @TARWFID | INTEGER | The current workflow ID for the TAR. |
| @EID | INTEGER | The current endorser ID. |
| @ELevel | INTEGER | The current endorser level. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approval (mandatory for reject, optional for approved or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(50) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_TAR_Workflow, TAMS_Sector, TAMS_Role
* **Writes:** TAMS_Audit, TAMS_TAR, TAMS_TAR_Workflow