# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch

### Purpose
This stored procedure updates the status of a Depot Authorization batch.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit | Output parameter indicating success or failure |
| @Message | NVARCHAR(500) | Output parameter containing error message if any |

### Logic Flow
The procedure starts by checking the transaction count. If it's 0, it begins a new transaction. It then opens a cursor to iterate over the Depot Authorization data.

For each row in the cursor:
1. Check if the user has access to update the information.
2. Validate the workflow ID and status ID.
3. Check for conflicts with other TARs or power zones.
4. Update the workflow status based on the new values.
5. Insert a new workflow if necessary.
6. Update the Depot Authorization data.

If any errors occur during this process, the procedure rolls back the transaction and sets @success to 0. Otherwise, it commits the transaction and sets @success to 1.

### Data Interactions
* Reads: TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Track_Power_Sector, TAMS_Track_SPKSZone, TAMS_Power_Sector, TAMS_User, TAMS_Endorser
* Writes: TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone