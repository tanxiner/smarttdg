# Procedure: sp_TAMS_Approval_Endorse

### Purpose
Approve a TAR record, advance the workflow to the next level or complete the approval chain, and send the appropriate email notifications.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | Identifier of the TAR being processed |
| @TARWFID | INTEGER | Current workflow record ID |
| @EID | INTEGER | Current endorser user ID |
| @ELevel | INTEGER | Current endorser level in the workflow |
| @Remarks | NVARCHAR(1000) | Comment supplied by the endorser (required for rejection, optional otherwise) |
| @TVFRunMode | NVARCHAR(50) | New TVF run mode value (optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Flag indicating whether to update TVF run mode |
| @UserLI | NVARCHAR(100) | Login ID of the user executing the procedure |
| @Message | NVARCHAR(500) OUTPUT | Result code or error message |

### Logic Flow
1. **Transaction Setup** – If no outer transaction exists, start a new one and mark that the procedure owns the transaction.
2. **User Identification** – Retrieve the internal user ID and name for the supplied login ID.
3. **Duplicate Approval Check** –  
   * Count how many times the current user has already approved this TAR.  
   * If the count is greater than zero, set message `1001` and exit.
4. **Workflow Record Validation** –  
   * If the supplied workflow record is already marked `Approved`, set message `1001` and exit.
5. **Approve Current Workflow Record** – Update the workflow record