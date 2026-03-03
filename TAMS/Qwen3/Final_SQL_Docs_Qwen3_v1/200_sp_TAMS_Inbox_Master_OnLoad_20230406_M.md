# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406_M

### Purpose
This stored procedure performs a master load of TAMS inbox data, including filtering and processing based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| AS NVARCHAR(10) | Specifies the line number to filter by |
| @AccessDate	| AS NVARCHAR(20) | Specifies the access date to filter by |
| @TARType	| AS NVARCHAR(20) | Specifies the TAR type to filter by |
| @LoginUser	| AS NVARCHAR(50) | Specifies the login user ID |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates temporary tables (#TmpSector and #TmpInbox) to store sector data and inbox data, respectively.
3. It truncates the existing data in the temporary tables.
4. It inserts data into the temporary tables by selecting relevant data from the TAMS_Sector and TAMS_TAR tables based on the provided line number, access date, TAR type, and user ID.
5. It creates a cursor (@Cur01) to iterate through the inbox data in the #TmpInbox table.
6. For each row in the inbox data, it checks if there are any pending workflows associated with the corresponding TAMS_TAR record. If not, it inserts the data into the #TmpInboxList table.
7. If there are pending workflows, it creates another cursor (@Cur02) to retrieve the action by user ID from the TAMS_TAR_Workflow table.
8. It checks if the current user ID matches the action by user ID retrieved from the cursor. If not, it skips the data insertion.
9. After processing all rows in the inbox data, it closes both cursors and deallocates them.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_User, TAMS_Endorser tables.
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList tables.