# Procedure: sp_TAMS_Approval_Proceed_To_App
**Type:** Stored Procedure

The purpose of this stored procedure is to approve a TAR (Technical Approval Request) and update its status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) | New Column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) | Indicator to Update TVF Run Mode or Not |
| @UserLI | NVARCHAR(100) | User Login ID |
| @Message | NVARCHAR(500) | Output message |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_TAR_Workflow, TAMS_Sector
* **Writes:** TAMS_Audit, TAMS_TAR, TAMS_TAR_Workflow