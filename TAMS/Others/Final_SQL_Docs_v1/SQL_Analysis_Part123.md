# Procedure: sp_TAMS_RGS_GrantTOA_001
**Type:** Stored Procedure

Purpose: This stored procedure grants a TAR (Track and Record) to an operator, updates the TOA (Track and Record Assignment) status, and sends an SMS notification.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR being granted. |
| @EncTARID | NVARCHAR(250) | The encrypted ID of the TAR being granted. |
| @UserID | NVARCHAR(500) | The ID of the user granting access. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

Logic Flow:
1. Checks if a transaction is already in progress.
2. If not, sets an internal transaction flag and begins a new transaction.
3. Retrieves the TAR details from the TAMS_TAR table based on the provided @TARID.
4. Generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA procedure.
5. Updates the TOA status in the TAMS_TOA table with the generated reference number and current date/time.
6. Inserts an audit record into the TAMS_TOA_Audit table with the user ID, current date/time, and 'U' (update) action.
7. Sets the SMS message based on the @AccessType parameter.
8. Sends an SMS notification to the operator's mobile number using the sp_api_send_sms procedure.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA

# Procedure: sp_TAMS_RGS_GrantTOA_20221107
**Type:** Stored Procedure

Purpose: This stored procedure grants a TAR (Track and Record) to an operator, updates the TOA (Track and Record Assignment) status, and sends an SMS notification.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR being granted. |
| @EncTARID | NVARCHAR(250) | The encrypted ID of the TAR being granted. |
| @UserID | NVARCHAR(500) | The ID of the user granting access. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

Logic Flow:
1. Checks if a transaction is already in progress.
2. If not, sets an internal transaction flag and begins a new transaction.
3. Retrieves the TAR details from the TAMS_TAR table based on the provided @TARID.
4. Generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA procedure.
5. Updates the TOA status in the TAMS_TOA table with the generated reference number and current date/time.
6. Inserts an audit record into the TAMS_TOA_Audit table with the user ID, current date/time, and 'U' (update) action.
7. Sets the SMS message based on the @AccessType parameter.
8. Sends an SMS notification to the operator's mobile number using the sp_api_send_sms procedure.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA

# Procedure: sp_TAMS_RGS_GrantTOA_20221214
**Type:** Stored Procedure

Purpose: This stored procedure grants a TAR (Track and Record) to an operator, updates the TOA (Track and Record Assignment) status, and sends an SMS notification.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR being granted. |
| @EncTARID | NVARCHAR(250) | The encrypted ID of the TAR being granted. |
| @UserID | NVARCHAR(500) | The ID of the user granting access. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

Logic Flow:
1. Checks if a transaction is already in progress.
2. If not, sets an internal transaction flag and begins a new transaction.
3. Retrieves the TAR details from the TAMS_TAR table based on the provided @TARID.
4. Generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA procedure.
5. Updates the TOA status in the TAMS_TOA table with the generated reference number and current date/time.
6. Inserts an audit record into the TAMS_TOA_Audit table with the user ID, current date/time, and 'U' (update) action.
7. Sets the SMS message based on the @AccessType parameter.
8. Sends an SMS notification to the operator's mobile number using the sp_api_send_sms procedure.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA