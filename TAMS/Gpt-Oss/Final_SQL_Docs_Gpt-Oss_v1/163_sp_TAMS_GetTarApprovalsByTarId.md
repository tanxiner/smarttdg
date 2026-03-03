# Procedure: sp_TAMS_GetTarApprovalsByTarId

### Purpose
Retrieve the approval workflow records for a specific TAR ID, including endorser details and user information.

### Parameters
| Name     | Type    | Purpose |
| :------- | :------ | :------ |
| @TarId   | integer | Identifier of the TAR whose approvals are requested. Defaults to 0 if not supplied. |

### Logic Flow
1. Accepts a TAR identifier (`@TarId`).  
2. Queries the `TAMS_TAR_Workflow` table for rows where `TARId` matches the supplied value.  
3. For each matching workflow row, joins to `TAMS_Endorser` on `WorkflowId` to obtain the endorser record.  
4. Joins to `TAMS_User` on `ActionBy` to retrieve the user who performed the action.  
5. Projects the workflow ID, title, endorser name, remark, and workflow status.  
6. Orders the result set by the workflow record ID in ascending order.

### Data Interactions
* **Reads:** `TAMS_TAR_Workflow`, `TAMS_Endorser`, `TAMS_User`  
* **Writes:** None