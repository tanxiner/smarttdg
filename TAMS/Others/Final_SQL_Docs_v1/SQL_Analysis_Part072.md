# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406_M
**Type:** Stored Procedure

### Purpose
This stored procedure performs a batch load of TAR (Trade Agreement) inbox data for a given sector, filtering out cancelled and pending TARs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter by. |
| @SectorID | INT | The sector ID to load data for. |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Retrieves the current date and time.
3. Removes cancelled TARs from the #TmpInbox table based on the provided line number, access date, TAR type, login user, and sector ID.
4. Iterates through the remaining TARs in the #TmpInbox table and checks if there are any workflows associated with each TAR.
5. If no workflows exist for a TAR, it is inserted into the #TmpInboxList table.
6. If workflows exist, it iterates through them to check if the user has been assigned as the action by.
7. If the user has not been assigned as the action by, the TAR is inserted into the #TmpInboxList table.
8. Finally, the procedure groups and orders the data in the #TmpInboxList table.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList