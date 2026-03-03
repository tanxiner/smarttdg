# Procedure: sp_TAMS_Inbox_Child_OnLoad_20240925
**Type:** Stored Procedure

### Purpose
This stored procedure loads TARs into the inbox based on the provided parameters.

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
1. Checks if the user exists in the TAMS_USER table based on the provided login user ID.
2. Removes Cancelled TARs from the #TmpInbox table by checking the WFStatus column in the TAMS_WFStatus table.
3. Truncates the #TmpSector, #TmpInbox, and #TmpInboxList tables to ensure they are empty before loading new data.
4. Inserts TARs into the #TmpInbox table based on the provided parameters (Line, TrackType, AccessDate, TARType, LoginUser, SectorID).
5. Checks if there are any pending TARs for the current user and sector ID. If not, it inserts the TAR into the #TmpInboxList table.
6. If there are pending TARs, it checks which action by (Endorser) needs to be taken on each TAR. If no action is required, it inserts the TAR into the #TmpInboxList table.
7. Finally, it selects and groups the TARs in the #TmpInboxList table based on the SectorID.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_WFStatus, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList