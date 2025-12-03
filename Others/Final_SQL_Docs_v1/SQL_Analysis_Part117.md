# Procedure: sp_TAMS_RGS_Cancel
**Type:** Stored Procedure

The purpose of this stored procedure is to cancel a RGS (Remote Gateway Server) and update the corresponding records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Terminal Access Record) to be cancelled. |
| @CancelRemarks | NVARCHAR(1000) | The remarks for the cancellation. |
| @UserID | NVARCHAR(500) | The ID of the user performing the cancellation. |
| @tracktype | nvarchar(50)='MAINLINE' | The type of track (mainline or not). |
| @Message | NVARCHAR(500) | The message to be sent to the user after cancellation. |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If no transaction, sets a flag and begins a new transaction.
3. Initializes a variable to store the internal transaction status.
4. Updates the TOAStatus of the TAR record to 6 (cancelled) and inserts into the TAMS_TOA_Audit table.
5. Retrieves the ID of the user from the TAMS_User table based on the provided @UserID.
6. Checks if the track type is 'MAINLINE'. If true, proceeds with the cancellation logic for mainline tracks.
7. For mainline tracks:
	* Iterates through all OCC (Occupancy Control) records associated with the TAR record and updates their status to 9 (cancelled).
	* Inserts into the TAMS_OCC_Auth_Audit table for each OCC record.
	* Updates the OCCAuthStatusId of the OCC records to 9 (cancelled).
8. For non-mainline tracks:
	* Iterates through all Traction Power Detail records associated with the TAR record and checks if any are in a 'Power On' state.
	* If no power on states, proceeds with the cancellation logic for NEL (Non-Electric Line) tracks.
9. For NEL tracks:
	* Iterates through all Depot Auth records associated with the TAR record and updates their status to 1 (cancelled).
	* Inserts into the TAMS_Depot_Auth_Workflow table for each Depot Auth record.
	* Updates the DepotAuthStatusId of the Depot Auth records to a new value based on the workflow ID.
10. Sends an SMS message to the user with the cancellation details.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_OCC_Auth, TAMS_User, TAMS_TAR, TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Traction_Power_Detail
* **Writes:** TAMS_TOA, TAMS_OCC_Auth, TAMS_Depot_Auth, TAMS_WFStatus