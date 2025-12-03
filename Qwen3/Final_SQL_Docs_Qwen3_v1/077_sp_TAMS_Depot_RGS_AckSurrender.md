# Procedure: sp_TAMS_Depot_RGS_AckSurrender

### Purpose
This stored procedure performs the business task of acknowledging a surrender for a TAR (TAR ID) and updating the relevant records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to be acknowledged. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain a message indicating the result of the operation. |

### Logic Flow
1. The procedure first checks if there is an open transaction. If not, it sets a flag to indicate that an internal transaction has been started.
2. It then retrieves the user ID from the TAMS_User table based on the provided @UserID parameter.
3. Next, it checks the TOA status of the TAR sector associated with the @TARID parameter. If the status is 4 (pending), it proceeds to update the TOA status to 5 (acknowledged) and sets the AckSurrenderTime to the current date and time.
4. It then inserts an audit record into the TAMS_TOA_Audit table for the updated TAR sector.
5. The procedure then checks if the line is 'NEL'. If so, it generates a message indicating that the surrender has been acknowledged by NEL DCC.
6. It then sends an SMS to the mobile number associated with the TAR sector using the sp_api_send_sms stored procedure.
7. If any errors occur during this process, the procedure will display an error message in the @Message output parameter.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_TOA_Audit
* Writes: TAMS_TOA (TOA status), TAMS_Depot_Auth_Workflow (workflow updates), TAMS_Depot_Auth (DepotAuthStatusId)