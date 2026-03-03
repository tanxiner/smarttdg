# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_PowerOnIssue
**Type:** Stored Procedure

The purpose of this stored procedure is to generate an authorization for a Traction Power (TP) operation.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TP operation. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_Power_Sector, TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_AuthWorkflow
* **Writes:** TAMS_TAR_Sector, TAMS_OCC_Auth, TAMS_OCC_AuthWorkflow