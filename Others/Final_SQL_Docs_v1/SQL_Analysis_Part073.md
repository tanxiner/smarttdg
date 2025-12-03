# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230706
**Type:** Stored Procedure

### Purpose
This stored procedure loads TARs (Tender and Award) into the inbox for a given sector, taking into account various filters such as access date, type, and user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter TARs by. |
| @AccessDate | NVARCHAR(20) | The access date to filter TARs by. |
| @TARType | NVARCHAR(20) | The type of TAR to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter TARs by. |
| @SectorID | INT | The sector ID to load TARs for. |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Retrieves the current date and time.
3. Removes cancelled TARs from the #TmpInbox table based on the WFStatusId.
4. Truncates the #TmpSector, #TmpInbox, and #TmpInboxList tables.
5. Inserts TAR data into the #TmpInbox table from the TAMS_TAR table, filtering by sector ID, access date, type, user ID, and other conditions.
6. Iterates through the #TmpInbox table to check if each TAR has been processed by the current user.
7. If a TAR has not been processed, it is inserted into the #TmpInboxList table.
8. Finally, the procedure returns the loaded TARs for the specified sector.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList