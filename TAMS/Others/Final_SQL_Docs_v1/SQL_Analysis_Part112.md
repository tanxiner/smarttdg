# Procedure: sp_TAMS_RGS_AckSurrender
**Type:** Stored Procedure

The purpose of this stored procedure is to acknowledge a surrender for a Traction Power Detail (TPD) and update the relevant tables accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the Traction Power Detail (TPD) being surrendered. |
| @UserID | NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store a message to be sent via SMS. |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag and begins a new transaction.
3. Retrieves the user ID from the TAMS_User table based on the provided login ID.
4. Checks the TOA status for the specified TAR ID to ensure it's not already acknowledged (TOAStatus = 5).
5. If the TOA status is valid, updates the TOA status to acknowledge the surrender and sets the AckSurrenderTime and UpdatedOn fields accordingly.
6. Inserts an audit record into the TAMS_TOA_Audit table for the updated TOA status.
7. Retrieves the Traction Power ID from the TAMS_Traction_Power_Detail table based on the TAR ID.
8. Checks if all OCC Auths have been acknowledged (i.e., no outstanding requests with a status of 8). If so, updates the OCC Auth status to acknowledge and inserts an audit record into the TAMS_OCC_Auth_Audit table.
9. Sends an SMS message using the sp_api_send_sms stored procedure.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_Traction_Power_Detail, TAMS_OCC_Auth
* **Writes:** TAMS_TOA, TAMS_OCC_Auth