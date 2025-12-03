# Procedure: sp_TAMS_RGS_AckSurrender_20221107

### Purpose
This stored procedure acknowledges a surrender for a TAMS (Technical Assistance Management System) record and sends an SMS notification to the relevant party.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Technical Assistance Record) being surrendered. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It then retrieves the ID of the user performing the action from the TAMS_User table based on their login ID.
3. The procedure updates the TOAStatus to 5 (Acknowledged) in the TAMS_TOA table for the specified TARID.
4. It then checks if all acknowledgments are complete by iterating through the TOAStatus of each TOA record associated with the TARID. If any status is not 5, it sets a flag indicating that not all acknowledgments are complete.
5. Based on the line (DTL or NEL) of the TAR record, it performs different actions:
	* For DTL lines, it updates the OCCAuthStatusId to 11 and inserts a new workflow into TAMS_OCC_Auth_Workflow for each OCC Auth record with status 10. It also updates the OCCAuthStatusId to 13 for each OCC Auth record with status 7.
	* For NEL lines, it updates the OCCAuthStatusId to 9 and inserts a new workflow into TAMS_OCC_Auth_Workflow for each OCC Auth record with status 7.
6. After completing these actions, it constructs an SMS message based on the TOANo and sends it via the sp_api_send_sms stored procedure.

### Data Interactions
* Reads: TAMS_User, TAMS_TOA, TAMS_TAR, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA