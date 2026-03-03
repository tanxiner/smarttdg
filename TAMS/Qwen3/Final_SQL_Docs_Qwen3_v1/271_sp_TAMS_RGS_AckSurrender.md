# Procedure: sp_TAMS_RGS_AckSurrender

### Purpose
This stored procedure acknowledges a surrender request for a Traction Asset Management System (TAMS) resource, updating the status and sending an SMS notification to the relevant stakeholders.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Traction Asset Resource) being surrendered. |
| @UserID | NVARCHAR(500) | The ID of the user performing the surrender action. |
| @Message | NVARCHAR(500) | An output parameter to store the acknowledgement message. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal flag (`@IntrnlTrans`) accordingly.
2. It retrieves the `Userid` from the `TAMS_User` table based on the provided `@UserID`.
3. It checks the current status of the TAR being surrendered (`@TOAStatusChk`) and updates it to 5 (Acknowledged) if it's not already in this state.
4. If the TAR has been acknowledged, it:
	* Retrieves the Traction Power ID from the `TAMS_Traction_Power_Detail` table based on the TAR ID.
	* Checks if all OCC (OCC Auth) requests for the Traction Power ID have been completed and sends an SMS notification to the relevant stakeholders using the `sp_api_send_sms` procedure.
	* Updates the OCC Auth status of the Traction Power ID to 9 (Completed).
5. If the TAR has not been acknowledged, it:
	* Retrieves the Traction Power ID from the `TAMS_Traction_Power_Detail` table based on the TAR ID.
	* Checks if all OCC requests for the Traction Power ID have been completed and sends an SMS notification to the relevant stakeholders using the `sp_api_send_sms` procedure.
	* Updates the OCC Auth status of the Traction Power ID to 9 (Completed).
6. If any errors occur during the process, it sets the `@Message` parameter to an error message and either commits or rolls back the transaction depending on whether an internal transaction was started.

### Data Interactions
* **Reads:** `TAMS_User`, `TAMS_TAR`, `TAMS_TOA`, `TAMS_Traction_Power_Detail`
* **Writes:** `TAMS_TOA` (updated TAR status), `TAMS_OCC_Auth` (OCC Auth status updates), `TAMS_OCC_Auth_Workflow` (OCC Auth workflow updates)