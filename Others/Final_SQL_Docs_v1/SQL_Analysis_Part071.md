# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406
**Type:** Stored Procedure

### Purpose
This stored procedure loads TARs into the inbox based on user access and sector ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line number for filtering sectors |
| @AccessDate | NVARCHAR(20) | Access date filter (optional) |
| @TARType | NVARCHAR(20) | TAR type filter (optional) |
| @LoginUser | NVARCHAR(50) | Login user ID for access control |
| @SectorID | INT | Sector ID for filtering |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Retrieves the current date and time.
3. Removes cancelled TARs by checking the WFStatus column in the TAMS_WFStatus table.
4. Truncates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList.
5. Inserts data into #TmpSector from the TAMS_Sector table based on the line number and sector ID.
6. Inserts data into #TmpInbox from the TAMS_TAR table based on the TARID, TARNo, TARType, AccessDate, AccessType, SectorID, SectorStr, and Direction columns.
7. Checks if there are any workflows for the current TAR by querying the TAMS_TAR_Workflow table.
8. If no workflows exist, inserts the data into #TmpInboxList.
9. If workflows exist, checks if the user is assigned to the workflow by comparing the @LoginUser with the EndorserId in the TAMS_TAR_Workflow table.
10. If the user is not assigned, inserts the data into #TmpInboxList.
11. Fetches the next record from #TmpInbox and repeats steps 7-10 until all records are processed.
12. Finally, selects the TARID, TARNo, TARType, AccessDate, and AccessType columns from #TmpInboxList where SectorID matches the input @SectorID.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_WFStatus, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList