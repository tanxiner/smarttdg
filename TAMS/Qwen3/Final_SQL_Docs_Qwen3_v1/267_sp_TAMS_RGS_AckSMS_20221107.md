# Procedure: sp_TAMS_RGS_AckSMS_20221107

### Purpose
This stored procedure sends an SMS acknowledgement to a TAMS user when their protection limit or grant time has been updated.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The TAR ID of the TAMS record being updated. |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it begins a new transaction.
2. It retrieves the necessary data from the `TAMS_TAR` and `TAMS_TOA` tables based on the provided TAR ID.
3. Depending on the access type (Possession or Not), it updates the corresponding grant or protection limit time in the `TAMS_TOA` table.
4. If the SMS message is not empty, it sends an SMS using the `sp_api_send_sms` procedure.
5. If any errors occur during the process, it sets a message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA