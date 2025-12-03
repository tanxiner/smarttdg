# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_M
**Type:** Stored Procedure

### Purpose
This stored procedure generates an authorization for a Traction Power (TP) operation based on the provided Line and AccessDate parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TP operation. |
| @AccessDate | NVARCHAR(20) | The access date for the TP operation. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [dbo].[TAMS_Traction_Power], [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_Workflow], [dbo].[TAMS_Endorser]
* **Writes:** [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_OCC_AuthWorkflow]