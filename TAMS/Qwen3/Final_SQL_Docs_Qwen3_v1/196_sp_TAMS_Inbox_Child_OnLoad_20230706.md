# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230706

### Purpose
This stored procedure loads child TARs into a temporary inbox table, filtering out cancelled and pending TARs based on user access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to load TARs for. |
| @AccessDate | NVARCHAR(20) | The access date filter (optional). |
| @TARType | NVARCHAR(20) | The TAR type filter (optional). |
| @LoginUser | NVARCHAR(50) | The login user ID. |
| @SectorID | INT | The sector ID to load TARs for. |

### Logic Flow
1. The procedure starts by selecting the current user ID from the TAMS_USER table based on the provided login user ID.
2. It then sets a cursor to retrieve all TARs in the temporary inbox table, ordered by TAR ID and sector ID.
3. For each TAR in the inbox table:
   1. If there are no workflow records for the current TAR with a status other than 'Pending', it is inserted into the temporary inbox list table.
   2. If there are workflow records for the current TAR with a status other than 'Pending', it checks if the user ID of the endorser matches the current user ID. If not, it skips to the next iteration.
4. After processing all TARs in the inbox table, the procedure groups and orders the temporary inbox list table by TAR ID, sector ID, TAR type, access date, and access type.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList