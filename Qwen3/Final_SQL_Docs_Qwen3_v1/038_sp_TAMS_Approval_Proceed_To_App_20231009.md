# Procedure: sp_TAMS_Approval_Proceed_To_App_20231009

### Purpose
This stored procedure performs the business task of proceeding with a TAR (Technical Approval Request) approval process. It checks for any exceptions, updates the TAR status, and sends notifications as required.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) | New Column to be confirmed with Adeline (Optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Indicator to Update TVF Run Mode or Not (Optional) |
| @UserLI | NVARCHAR(100) | User Login ID |
| @Message | NVARCHAR(500) | Output message |

### Logic Flow
1. The procedure starts by checking if the transaction count is 0, indicating a new transaction.
2. It then checks for any exceptions in the TAR workflow and updates the TAR status accordingly.
3. If there are no exceptions, it proceeds with the approval process.
4. For each level of endorsement, it checks if the next level's endorser has been approved or not.
5. If the next level's endorser is not approved, it sends an email notification to the relevant stakeholders.
6. Once all levels have been checked and exceptions handled, it updates the TAR status to 'Approved' and inserts a new record into the TAMS_TAR_Workflow table.
7. Finally, it commits or rolls back the transaction based on whether any errors occurred during the procedure.

### Data Interactions
* Reads: TAMS_User, TAMS_Endorser, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Sector, TAMS_Role
* Writes: TAMS_TAR, TAMS_TAR_Workflow