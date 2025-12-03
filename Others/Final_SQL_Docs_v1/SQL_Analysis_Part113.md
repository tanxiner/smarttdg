# Procedure: sp_TAMS_RGS_AckSurrender_20221107
**Type:** Stored Procedure

The procedure acknowledges a surrender for a TAMS RGS (Request for Goods and Services) by updating the TOA status, inserting into the Audit table, and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Task Assignment Record) to be acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user who is acknowledging the surrender. |
| @Message	| NVARCHAR(500) = NULL OUTPUT | The message to be sent via SMS notification. |

### Logic Flow
1. Checks if a transaction has been started.
2. If not, sets a flag and begins a new transaction.
3. Retrieves the ID of the user from the TAMS_User table based on the provided login ID.
4. Updates the TOA status in the TAMS_TOA table to 5 (Acknowledged) for the specified TAR ID.
5. Retrieves additional information about the TAR, including the TOA status and access date.
6. Checks if all TOAs have been acknowledged by verifying that none of them have a status other than 5.
7. If all TOAs are acknowledged, updates the OCCAuthStatusId in the TAMS_OCC_Auth table for each relevant record.
8. Inserts into the TAMS_OCC_Auth_Workflow table to track the workflow status.
9. Sends an SMS notification with the TOA number and acknowledgement message.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_TOA, TAMS_OCC_Auth