# Procedure: SP_TAMS_Depot_SaveDTCAuthComments

### Purpose
This stored procedure saves comments for a given authentication ID in the TAMS Depot Authorization module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @str | TAMS_DTC_AUTH_COMMENTS | A table variable containing the comments to be saved. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then checks if a transaction is already in progress and sets an internal transaction flag accordingly.
3. If no transaction is active, it begins a new transaction.
4. The procedure then opens a cursor on the @str table variable, which contains the comments to be saved.
5. It fetches each row from the cursor and processes it:
	* For each comment, it checks if a remark ID already exists in the TAMS_Depot_Auth table for the corresponding authentication ID.
	* If a remark ID exists, it updates the remark in the TAMS_Depot_Auth_Remark table with the new comment.
	* If no remark ID exists, it inserts a new record into the TAMS_Depot_Auth_Remark table with the comment and sets the remark ID for the corresponding authentication ID in the TAMS_Depot_Auth table.
6. After processing all comments, the procedure closes the cursor and deallocates its resources.
7. If any errors occur during the process, it rolls back the transaction and sets a success flag to 0.
8. Otherwise, it commits the transaction, sets the success flag to 1, and returns.

### Data Interactions
* **Reads:** TAMS_DTC_AUTH_COMMENTS (table variable)
* **Writes:** TAMS_Depot_Auth_Remark (table), TAMS_Depot_Auth (table)