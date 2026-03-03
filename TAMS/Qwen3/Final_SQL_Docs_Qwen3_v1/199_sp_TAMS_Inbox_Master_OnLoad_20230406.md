# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406

### Purpose
This stored procedure performs a master load of TAMS inbox data, including filtering and processing based on user access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter by. |
| @AccessDate | NVARCHAR(20) | Specifies the access date to filter by. |
| @TARType | NVARCHAR(20) | Specifies the TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | Specifies the login user ID for filtering and authorization. |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data, inbox data, and processed inbox list data, respectively.
3. It truncates the existing data in these temporary tables.
4. It inserts data from the TAMS_Sector table into the #TmpSector table based on the specified line and date range.
5. It inserts data from the TAMS_TAR table into the #TmpInbox table based on the specified TAR type, access date, and user ID.
6. It processes the #TmpInbox table by checking if there are any pending workflows for each TAR ID. If not, it adds the TAR ID to the #TmpInboxList table.
7. If there are pending workflows, it retrieves the action by from the TAMS_TAR_Workflow table and checks if the user is authorized to perform that action. If so, it updates the #TmpInboxList table with the action by.
8. It fetches the next record from the #TmpInbox table and repeats steps 6-7 until all records are processed.
9. Finally, it joins the #TmpSector table with the #TmpInboxList table based on sector ID and orders the results by sector order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_USER, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList