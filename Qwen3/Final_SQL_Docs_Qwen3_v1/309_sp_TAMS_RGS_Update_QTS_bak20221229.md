# Procedure: sp_TAMS_RGS_Update_QTS_bak20221229

### Purpose
This stored procedure updates the qualification status of a TAR (Target Area Record) based on the user's input and checks for any errors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC (National Registration Identity Card) number of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the update. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | An output parameter to store the updated QTS (Qualification and Standards) code. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | An output parameter to store the updated QTS line number. |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets an internal flag (`@IntrnlTrans`) to 1 and begins a new transaction.
2. It creates a temporary table (`#tmpnric`) to store the in-charge person's details.
3. The procedure truncates the temporary table and then inserts a record into it using a dynamic SQL command (`sp_TAMS_TOA_QTS_Chk`).
4. It selects the in-charge person's name and status from the temporary table.
5. Based on the in-charge person's status, the procedure checks if the TAR record is valid or not. If it's invalid, it updates the QTS code to 'InValid' and sets `@QTSFinStatus` to 'InValid'. If it's valid, it updates the QTS code to the corresponding value.
6. The procedure then updates the TAR record with the new QTS code and inserts an audit record into the `TAMS_TOA_Audit` table.
7. Finally, it checks for any errors that may have occurred during the update process and returns an error message if necessary.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit
* **Writes:** TAMS_TOA