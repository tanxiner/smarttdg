# Procedure: sp_TAMS_RGS_AckSurrender_OSReq
**Type:** Stored Procedure

The purpose of this stored procedure is to acknowledge a surrender request for an Order Status Request (OSR) and update the relevant tables accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Transaction Area Record) to be updated. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message	| NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain an error message if any errors occur during execution. |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets a flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the TOAStatus of the TAR record to 5 (Acknowledged) and sets the AckSurrenderTime to the current date and time.
4. Retrieves the relevant data from TAMS_TAR and TAMS_TOA tables based on the TAR ID and Line values.
5. Checks if all OCC Auth requests are acknowledged for the given Line value. If not, sets a flag to indicate that not all requests have been acknowledged.
6. For each Line value ('DTL' or 'NEL'), performs the following actions:
	* For 'DTL', updates the relevant OCC Auth records and inserts new workflow records into TAMS_OCC_Auth_Workflow table for each endorser level (10, 11, and 12).
	* For 'NEL', updates the relevant OCC Auth records and inserts new workflow records into TAMS_OCC_Auth_Workflow table for each endorser level (7).
7. If all OCC Auth requests are acknowledged, sets a message to be sent via SMS.
8. If any errors occur during execution, sets an error message in the @Message output parameter.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_TOA