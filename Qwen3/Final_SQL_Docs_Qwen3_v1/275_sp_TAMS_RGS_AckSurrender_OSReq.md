# Procedure: sp_TAMS_RGS_AckSurrender_OSReq

### Purpose
This stored procedure acknowledges a surrender request for an Operating System (OS) and sends a corresponding SMS message to the endorser.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Transaction Acknowledgement Request) being acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent as an SMS. |

### Logic Flow
1. Check if a transaction is already in progress. If not, set a flag and begin a new transaction.
2. Update the TOAStatus of the TAR being acknowledged to 5 (Acknowledged).
3. Set the AckSurrenderTime to the current date and time.
4. Retrieve the TAR and TOA IDs from the TAMS_TAR and TAMS_TOA tables based on the @TARID parameter.
5. Check if the line is 'DTL' or not. If it's 'DTL', proceed with the DTL logic; otherwise, proceed with the NEL logic.
6. For the DTL logic:
	* Retrieve the IDs of the endorser for each OCCAuth status (10, 11, and 12).
	* Update the OCCAuthStatusId in TAMS_OCC_Auth to reflect the new status.
	* Insert a new record into TAMS_OCC_Auth_Workflow with the updated status and endorser ID.
7. For the NEL logic:
	* Retrieve the IDs of the endorser for each OCCAuth status (7).
	* Update the OCCAuthStatusId in TAMS_OCC_Auth to reflect the new status.
	* Insert a new record into TAMS_OCC_Auth_Workflow with the updated status and endorser ID.
8. Construct the SMS message based on the line type ('DTL' or 'NEL') and the current date and time.
9. If an error occurs during the process, set the @Message parameter to indicate the error and exit the procedure.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA