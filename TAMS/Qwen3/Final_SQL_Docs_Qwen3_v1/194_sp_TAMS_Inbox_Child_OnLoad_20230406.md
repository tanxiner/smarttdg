# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406

### Purpose
This stored procedure performs a daily load of TAR (Trade Agreement) inbox data, removing any cancelled TARs and populating the #TmpInboxList table with the remaining TARs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to load TARs for. |
| @AccessDate | NVARCHAR(20) | The access date to filter TARs by. |
| @TARType | NVARCHAR(20) | The TAR type to filter TARs by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter TARs by. |
| @SectorID | INT | The sector ID to load TARs for. |

### Logic Flow
1. The procedure starts by selecting the current user ID from TAMS_USER based on the provided login user.
2. It then sets the current date and time, which is used to filter TARs by access date.
3. The procedure removes any cancelled TARs by checking if there are any workflows with a status other than 'Pending' for each TAR.
4. If no such workflows exist, the TAR is added to the #TmpInboxList table.
5. If workflows do exist, the procedure checks if the user ID matches the current user ID. If it does, the TAR is added to the #TmpInboxList table; otherwise, it skips this TAR.
6. The procedure repeats steps 4-5 for each TAR in the #TmpInbox table.
7. Finally, the procedure selects and groups the TARs from the #TmpInboxList table based on the sector ID.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList