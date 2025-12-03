# Procedure: sp_TAMS_RGS_AckReg

### Purpose
This stored procedure acknowledges a registration request for a Train Access Management System (TAMS) and sends an SMS notification to the registered mobile number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Train Access Request) being acknowledged. |
| @UserID | NVARCHAR(500) | The ID of the user who initiated the registration request. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores the SMS message to be sent. |

### Logic Flow
1. The procedure checks if a transaction has already been started. If not, it starts one.
2. It retrieves the TOA status and track type from the TAMS_TAR and TAMS_TOA tables based on the provided TAR ID.
3. If the TOA status is 1 (pending), it updates the TOA status to 2 (acknowledged) in the TAMS_TOA table.
4. It checks if a Depot Auth record already exists for the given TAR ID. If yes, it returns without inserting a new record.
5. Otherwise, it inserts a new Depot Auth record into the TAMS_Depot_Auth table with the provided track type and user ID.
6. It also inserts records into the TAMS_Depot_Auth_Workflow and TAMS_Depot_DTCAuth_SPKS tables.
7. Based on the track type, it constructs an SMS message to be sent to the registered mobile number.
8. If the SMS message is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
9. Finally, it returns the constructed SMS message or an error message if any errors occur during execution.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_DTCAuth_SPKS
* Writes: TAMS_TOA (TOA status), TAMS_Depot_Auth (new record), TAMS_Depot_Auth_Workflow (workflow ID), TAMS_Depot_DTCAuth_SPKS (SPKSID)