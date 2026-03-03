# Procedure: sp_TAMS_GetTarApprovalsByTarId

### Purpose
This stored procedure retrieves a list of approvals for a specific TarId, including the ID, title, name, remark, and workflow status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the Tar to retrieve approvals for. |

### Logic Flow
1. The procedure starts by selecting data from three tables: TAMS_TAR_Workflow, TAMS_Endorser, and TAMS_User.
2. It filters the data based on the TARId, WorkflowId, ActionBy, and EndorserId columns.
3. The selected data is ordered by the ID column in ascending order.

### Data Interactions
* **Reads:** TAMS_TAR_Workflow, TAMS_Endorser, and TAMS_User