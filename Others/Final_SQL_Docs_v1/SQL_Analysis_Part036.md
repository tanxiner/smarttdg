# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch
**Type:** Stored Procedure

The procedure updates the status of a Depot Authorization batch.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit | Output parameter indicating success or failure |
| @Message | NVARCHAR(500) | Output parameter containing error message if any |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Track_Power_Sector, TAMS_Track_SPKSZone, TAMS_Power_Sector, TAMS_User, TAMS_Endorser
* **Writes:** TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone