# Procedure: sp_TAMS_Approval_Proceed_To_App_20220930

### Purpose
This stored procedure performs the approval process for a TAR (Technical Approval Request) form. It checks if the current endorser has approved or rejected the request, and updates the TAR status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (mandatory for reject, optional for approved or endorse) |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not |
| @UserLI | NVARCHAR(50) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1.
2. It then retrieves the current endorser's details from the TAMS_User table based on the provided User Login ID.
3. Next, it retrieves the TAR details from the TAMS_TAR table and updates the TAR Status ID if necessary.
4. The procedure then creates two temporary tables, #TmpExc and #TmpExcSector, to store the exception TARs (sector conflicts) for each sector.
5. It iterates through the sectors and checks if there are any exceptions. If so, it inserts them into the temporary tables.
6. After that, it retrieves the next level endorser's details from the TAMS_Endorser table based on the current endorser's ID and level.
7. If the next level endorser is not found, it updates the TAR status to 'Approved' or 'Rejected' based on the current endorser's decision.
8. The procedure then checks if there are any late TARs that need to be approved. If so, it sends an email notification to the relevant users and updates the TAR status accordingly.
9. Finally, it commits or rolls back the transaction depending on whether an error occurred during the execution of the procedure.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_TAR_Workflow, TAMS_Sector, TAMS_Role
* Writes: TAMS_TAR, TAMS_TAR_Workflow