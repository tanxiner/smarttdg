# Procedure: sp_TAMS_Inbox_Child_OnLoad_20240925

### Purpose
This stored procedure loads child TARs into a temporary table, filtering out cancelled and pending TARs based on user access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID. |
| @SectorID | INT | The sector ID. |

### Logic Flow
1. The procedure starts by selecting the user ID from the TAMS_USER table based on the provided login user ID.
2. It then creates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList to store the filtered data.
3. The procedure truncates these temporary tables before inserting new data.
4. It selects the TARs from the TAMS_TAR table that match the provided line number, track type, access date, and TAR type, as well as the sector ID.
5. For each TAR, it checks if there are any workflows with a status other than 'Pending'. If not, it inserts the TAR into the #TmpInboxList table.
6. If there are workflows with a status other than 'Pending', it opens a cursor to retrieve the action by user ID and checks if the current user is the same as the action by user ID. If so, it increments a counter.
7. After checking all TARs, it selects the data from the #TmpInboxList table where the sector ID matches the provided sector ID and groups the results by TAR ID, TAR number, TAR type, access date, and access type.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList