# Procedure: sp_TAMS_Inbox_Child_OnLoad
**Type:** Stored Procedure

### Purpose
This stored procedure performs a batch load of TAR (Trade Agreement) records from the TAMS database, filtering out records that are already loaded or have been cancelled/withdrawn.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by |
| @TrackType | NVARCHAR(50) | The track type to filter by |
| @AccessDate | NVARCHAR(20) | The access date to filter by (optional) |
| @TARType | NVARCHAR(20) | The TAR type to filter by (optional) |
| @LoginUser | NVARCHAR(50) | The login user ID to filter by |
| @SectorID | INT | The sector ID to filter by |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table based on the provided login user ID.
2. Retrieves the current date and time using GETDATE().
3. Removes any TAR records with a status of 'Cancel' or 'Withdrawn' for the specified line number and track type.
4. Creates temporary tables to store sector data, TAR records, and their corresponding list items.
5. Truncates the temporary tables to ensure they are empty before loading new data.
6. Loads TAR records into the #TmpInbox table based on the provided filter criteria (line number, track type, access date, TAR type, login user ID, sector ID).
7. Iterates through the loaded TAR records and checks if there is a corresponding workflow record with a status other than 'Pending'. If so, it sets a flag to indicate that an action by has been performed.
8. For each TAR record without a corresponding workflow record, inserts a new item into the #TmpInboxList table.
9. Finally, selects the loaded TAR records from the #TmpInboxList table and groups them by their sector ID.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList