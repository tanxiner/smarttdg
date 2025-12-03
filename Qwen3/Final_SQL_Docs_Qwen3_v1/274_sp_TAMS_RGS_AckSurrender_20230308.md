# Procedure: sp_TAMS_RGS_AckSurrender_20230308

### Purpose
This stored procedure acknowledges a surrender for a RGS (Remote Gateway Server) and updates the relevant records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Test Access Record) to be acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain a message if an error occurs. |

### Logic Flow
The procedure follows these steps:

1. It checks if there is already a transaction in progress and sets `@IntrnlTrans` to 1 if not.
2. It retrieves the user ID from the TAMS_User table based on the provided login ID.
3. It updates the TOAStatus, AckSurrenderTime, UpdatedOn, and UpdatedBy fields for the specified TARID in the TAMS_TOA table.
4. It inserts a new record into the TAMS_TOA_Audit table with the current user ID and timestamp.
5. It retrieves various fields from the TAMS_TAR and TAMS_TOA tables based on the provided TARID, line, and access date.
6. If the line is 'DTL', it checks if there are any OCCAuthStatusId values that need to be updated or inserted into the TAMS_OCC_Auth table. It also checks for buffer zone records and updates them accordingly.
7. If the line is not 'DTL', it performs similar checks as above but for NEL (Network End).
8. After completing these checks, it sets a message based on the line and sends an SMS using the sp_api_send_sms stored procedure.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_TOA_Audit