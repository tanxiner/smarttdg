# Procedure: sp_TAMS_OCC_Generate_Authorization
**Type:** Stored Procedure

Purpose: This stored procedure generates an authorization for a TAMS OCC (Track and Manage System Operations Control) operation.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the operation. |
| @TrackType | NVARCHAR(50) | The type of track for the operation. |
| @AccessDate | NVARCHAR(20) | The access date for the operation (optional). |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_Traction_Power], [dbo].[TAMS_Workflow], [dbo].[TAMS_Endorser]
* **Writes:** [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_OCC_Auth_Workflow], [dbo].[TAMS_OCC_Auth_Audit]