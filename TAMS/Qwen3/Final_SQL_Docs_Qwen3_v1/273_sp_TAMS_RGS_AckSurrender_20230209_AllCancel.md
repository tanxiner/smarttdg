# Procedure: sp_TAMS_RGS_AckSurrender_20230209_AllCancel

### Purpose
This stored procedure acknowledges a surrender for all TAMS (Test and Measurement Systems) records with a specific status, updates the corresponding TOA (Test Operation Assignment) records, and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAMS record being acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has been started and sets an internal flag (`@IntrnlTrans`) accordingly.
2. It retrieves the user ID from the `TAMS_User` table based on the provided login ID.
3. It updates the corresponding TOA records in the `TAMS_TOA` table with the new status (5) and timestamp.
4. It inserts an audit record into the `TAMS_TOA_Audit` table for each updated TOA record.
5. It checks if all TAMS records have been acknowledged by iterating through the TOA records and checking their status.
6. If all records are acknowledged, it sends an SMS notification to the user with a success message.
7. If any record is not acknowledged, it sets an error message in the `@Message` output parameter.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_TOA_Audit
* **Writes:** TAMS_TOA