# Procedure: sp_TAMS_Approval_Proceed_To_App_20240920

### Purpose
This stored procedure performs the approval process for a TAR (Technical Approval Request) by checking if it has already been approved, updating the TAR status and workflow, and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (mandatory for Reject, optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not |
| @UserLI | NVARCHAR(100) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure checks if the TAR has already been approved by the current user, and if so, sets an error message.
2. It updates the TAR status to 'Approved' or 'Cancelled' based on the line value (@Line).
3. If @TVFRunModeUpdInd = 1, it updates the TVF mode in the TAMS_TAR table.
4. The procedure retrieves the current level endorser and checks if there are any sector conflicts (i.e., exceptions) that need to be addressed.
5. It creates two temporary tables (#TmpExc and #TmpExcSector) to store the exception TARs and their corresponding sector IDs.
6. The procedure iterates through the exception TARs, checking for sector conflicts and sending notifications to relevant parties.
7. If there are no sector conflicts, it updates the TAR status to 'Approved' and sends an email notification to the next level endorser.
8. If there are sector conflicts, it cancels the TAR and sends a notification to the current user.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Sector, TAMS_Parameters
* Writes: TAMS_TAR, TAMS_TAR_Workflow