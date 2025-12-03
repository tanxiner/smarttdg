# Procedure: sp_TAMS_RGS_Cancel_20250403

### Purpose
This stored procedure cancels a Request for Goods (RGS) on TAMS and sends an SMS notification to the OCC contact.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR sector being cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | The reason for cancellation. |
| @UserID	| NVARCHAR(500) | The user ID performing the cancellation. |
| @tracktype as nvarchar(50)='MAINLINE' | nvarchar(50) | The type of track (MAINLINE). |
| @Message	| NVARCHAR(500) | Output parameter to store the SMS message. |

### Logic Flow
1. Check if a transaction is already in progress.
2. If not, set an internal transaction flag and begin a new transaction.
3. Initialize an output parameter `@Message` to store the SMS message.
4. Retrieve the TAR sector ID from TAMS_TAR table based on the input `@TARID`.
5. Update the TOA status in TAMS_TOA table to 6 (cancelled) and set the cancellation remarks.
6. Insert a new record into TAMS_TOA_Audit table to log the cancellation.
7. Retrieve the user ID from TAMS_User table based on the input `@UserID`.
8. Check if the track type is MAINLINE. If so, proceed with the cancellation logic.
9. For MAINLINE tracks:
	* Declare a cursor to iterate through TAMS_OCC_Auth table and find records with a specific status (8 or 9).
	* Update these records in TAMS_OCC_Auth table to reflect the new status (9) and insert new records into TAMS_OCC_Auth_Workflow table.
	* Insert new records into TAMS_OCC_Auth_Audit table to log the changes.
10. If the track type is not MAINLINE, proceed with the cancellation logic for NEL tracks.
11. For NEL tracks:
	* Declare a cursor to iterate through TAMS_TAR_Power_Sector table and find records associated with the TAR sector being cancelled.
	* Check if all these records have cleared (i.e., their status is not 0, 5, or 6). If so, proceed with the cancellation logic.
12. For NEL tracks:
	* Cancel authorisation for any existing Depot Auth records associated with the TAR sector being cancelled.
	* Update the Depot Auth Status ID in TAMS_Depot_Auth table to reflect the new status (e.g., 'Line Clear Certification (TOA/SCD) (CC)' or 'Line Clear Certification (TOA/SCD) (DTC)').
13. Send an SMS notification to the OCC contact based on the track type and TAR sector ID.
14. If any errors occur during the procedure, roll back the transaction and return an error message.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth, TAMS_WFStatus.
* **Writes:** TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth.