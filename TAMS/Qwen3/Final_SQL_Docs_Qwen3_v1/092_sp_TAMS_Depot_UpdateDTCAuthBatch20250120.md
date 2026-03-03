# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch20250120

### Purpose
This stored procedure updates the Depot Authorization module for a batch of users.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit | Output parameter indicating success or failure |
| @Message | NVARCHAR(500) | Output parameter containing error message if any |

### Logic Flow

1. The procedure starts by setting the transaction count to 0 and declaring a variable `@IntrnlTrans` to track whether an internal transaction is being performed.
2. It then checks if there are any open transactions, and if not, sets `@IntrnlTrans` to 1.
3. The procedure opens a cursor `C` that selects the required columns from the `TAMS_DTC_AUTH` table.
4. The cursor fetches each row one by one, and for each row:
   - It checks if the user has access to update the information by checking if they are in the roster role or have the necessary permissions.
   - If not, it sets an error message and skips to the next iteration of the loop.
   - It then updates the workflow status based on the current status ID.
   - Depending on the new status ID, it performs different actions such as updating the power zone status, setting the protect off timing, or inserting a new workflow.
5. If any errors occur during this process, the procedure rolls back the transaction and sets `@success` to 0.
6. Finally, if no errors occurred, the procedure commits the transaction, sets `@success` to 1, and returns.

### Data Interactions
* **Reads:** TAMS_DTC_AUTH, TAMS_WFStatus, TAMS_Roster_Role, TAMS_OCC_Duty_Roster, TAMS_User, TAMS_Endorser, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Depot_DTCAuth_SPKS
* **Writes:** TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Depot_DTCAuth_SPKS