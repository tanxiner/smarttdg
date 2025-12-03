# Procedure: sp_TAMS_Inbox_Child_OnLoad

### Purpose
This stored procedure is used to load child TARs into a temporary table for further processing. It filters TARs based on various conditions such as status, type, and sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the sector to process |
| @TrackType | NVARCHAR(50) | The track type of the sector to process |
| @AccessDate | NVARCHAR(20) | The access date for the TARs to filter |
| @TARType | NVARCHAR(20) | The type of TAR to filter |
| @LoginUser | NVARCHAR(50) | The login user ID to filter |
| @SectorID | INT | The sector ID to process |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList.
3. It truncates the existing data in the temporary tables.
4. It inserts data into #TmpSector by selecting sectors that match the line number, track type, and are active with an effective date within the specified access date range.
5. It inserts data into #TmpInbox by selecting TARs that match the provided conditions such as status, type, sector, and endorser ID.
6. It creates a cursor to iterate through the #TmpInbox table and checks if the user ID is associated with any of the TARs in the current iteration.
7. If the user ID is not associated, it inserts the TAR into #TmpInboxList.
8. Finally, it selects the data from #TmpInboxList based on the sector ID.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList