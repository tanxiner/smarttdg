# Procedure: sp_TAMS_Depot_Inbox_Child_OnLoad
**Type:** Stored Procedure

This procedure performs a child inbox load for depot operations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter by. |
| @SectorID | INT | The sector ID to filter by. |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Inserts into the Audit table.
3. Returns the ID.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList

# Procedure: sp_TAMS_Depot_Inbox_Master_OnLoad
**Type:** Stored Procedure

This procedure performs a master inbox load for depot operations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter by. |

### Logic Flow
1. Checks if the user exists in the TAMS_USER table.
2. Filters the sector data based on the line and track type.
3. Inserts into the #TmpSector table.
4. Filters the TAR data based on the access date, TAR type, and sector ID.
5. Inserts into the #TmpInbox table.
6. Iterates through the #TmpInbox table to check if the user is assigned to any actions.
7. If not, inserts into the #TmpInboxList table.
8. Returns the filtered sector data.

### Data Interactions
* Reads: TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList