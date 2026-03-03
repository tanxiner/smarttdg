# Procedure: sp_TAMS_Depot_Inbox_Child_OnLoad

### Purpose
This stored procedure populates the inbox for a specific depot by retrieving TARs that are pending and have not been processed yet, based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter TARs by. |
| @TrackType | NVARCHAR(50) | The track type to filter TARs by. |
| @AccessDate | NVARCHAR(20) | The access date to filter TARs by. |
| @TARType | NVARCHAR(20) | The TAR type to filter TARs by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter TARs by. |
| @SectorID | INT | The sector ID to filter TARs by. |

### Logic Flow
1. The procedure starts by selecting the current date and time.
2. It then truncates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList.
3. Next, it inserts data into #TmpSector from TAMS_Sector table based on the provided line number and track type.
4. After that, it inserts data into #TmpInbox from TAMS_TAR table based on the provided TAR type, access date, and sector ID. The data is filtered to include only TARs with a pending status and not processed yet.
5. The procedure then creates two cursors: @Cur01 and @Cur02. 
6. The first cursor fetches all TARs from #TmpInboxList that have not been processed yet (i.e., ActionByChk = 0).
7. For each TAR, the procedure checks if the user ID matches the provided login user ID. If it does, it increments the ActionByChk counter.
8. If ActionByChk is still 0 after checking all actions for a TAR, it inserts the TAR into #TmpInboxList.
9. The second cursor fetches the action by which a TAR should be processed from TAMS_TAR_Workflow table based on the TAR ID.
10. For each action, the procedure checks if the user ID matches the provided login user ID. If it does, it increments the ActionByChk counter.
11. After checking all actions for a TAR, the procedure inserts the TAR into #TmpInboxList only if ActionByChk is still 0.
12. Finally, the procedure selects and groups the data from #TmpInboxList based on the sector ID and returns the result.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role, TAMS_USER
* Writes: #TmpSector, #TmpInbox, #TmpInboxList