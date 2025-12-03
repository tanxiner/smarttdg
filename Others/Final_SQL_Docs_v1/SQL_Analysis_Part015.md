# Procedure: sp_TAMS_Approval_Proceed_To_App_20231009
**Type:** Stored Procedure

The purpose of this stored procedure is to approve a TAR (Technical Approval Request) and update its status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being approved. |
| @TARWFID | INTEGER | The ID of the current workflow associated with the TAR. |
| @EID | INTEGER | The ID of the current endorser. |
| @ELevel | INTEGER | The level of the current endorser. |
| @Remarks | NVARCHAR(1000) | Remarks for the TAR (optional). |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional). |
| @TVFRunModeUpdInd | NVARCHAR(5) | Indicator to update TVF run mode or not (optional). |
| @UserLI | NVARCHAR(100) | User login ID. |
| @Message | NVARCHAR(500) | Output message. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_TAR_Workflow, TAMS_Sector, TAMS_Role
* **Writes:** TAMS_TAR, TAMS_TAR_Workflow