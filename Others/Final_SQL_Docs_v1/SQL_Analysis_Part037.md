# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch20250120
**Type:** Stored Procedure

The procedure updates the Depot Authorization module for a batch of users.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit | Output parameter indicating success or failure |
| @Message | NVARCHAR(500) | Output parameter containing error message |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_WFStatus, TAMS_User, TAMS_Roster_Role, TAMS_OCC_Duty_Roster, TAMS_Track_Power_Sector, TAMS_Track_SPKSZone, TAMS_Power_Sector, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Depot_DTCAuth_SPKS
* **Writes:** TAMS_Depot_Auth, TAMS_WFStatus, TAMS_User, TAMS_Roster_Role, TAMS_OCC_Duty_Roster, TAMS_Track_Power_Sector, TAMS_Track_SPKSZone, TAMS_Power_Sector, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Depot_DTCAuth_SPKS