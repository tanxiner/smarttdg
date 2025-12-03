# Procedure: sp_TAMS_Approval_Proceed_To_App

### Purpose
This stored procedure performs the approval process for a TAR (Technical Approval Request) and updates the TAR status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) | New Column to be confirmed with Adeline (Optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Indicator to Update TVF Run Mode or Not (Optional) |
| @UserLI | NVARCHAR(100) | User Login ID |
| @Message | NVARCHAR(500) | Output message |

### Logic Flow
1. The procedure checks if the TAR has already been approved by the current user. If yes, it sets an error message and exits.
2. It updates the TVF Run Mode column in the TAR table if specified.
3. It retrieves the current level endorser's details from the TAMS_Endorser table.
4. It creates two temporary tables (#TmpExc and #TmpExcSector) to store exceptions (sector conflicts) for each TAR.
5. It iterates through the exceptions and checks if there are any sector conflicts. If yes, it inserts the exception into the #TmpExcSector table.
6. It retrieves the next level endorser's details from the TAMS_Endorser table.
7. If the next level endorser is not found or has already been approved, it updates the TAR status to 'Approved' and sends an email notification if required.
8. If the next level endorser is found and has not been approved, it inserts a new record into the TAMS_TAR_Workflow table.
9. It checks for any urgent after notifications and sends an email notification if required.
10. Finally, it updates the TAR status to 'Approved' and logs the approval action.

### Data Interactions
* Reads: TAMS_User, TAMS_Endorser, TAMS_TAR, TAMS_TAR_Workflow, TAMS Paramaters
* Writes: TAMS_TAR, TAMS_TAR_Workflow