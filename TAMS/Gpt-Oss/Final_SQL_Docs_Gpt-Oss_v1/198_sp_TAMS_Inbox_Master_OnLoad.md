# Procedure: sp_TAMS_Inbox_Master_OnLoad

### Purpose
Loads sector lists for a user’s inbox view, filtering sectors and TAR records by line, track type, access date, TAR type, and workflow status, and returns two ordered lists of sectors (direction 1 and direction 2).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier for sector selection. |
| @TrackType | NVARCHAR(50) | Track type filter applied to sectors and TAR records. |
| @AccessDate | NVARCHAR(20) | Date used to match TAR access dates; empty string means no date filter. |
| @TARType | NVARCHAR(20) | TAR type filter; empty string means no type filter. |
| @LoginUser | NVARCHAR(50) | User login name used to resolve the user’s ID and role. |

### Logic Flow
1. Resolve the numeric user ID from the login name.  
2. Capture the current date in `@CurrDate`.  
3. Create three temporary tables: `#TmpSector`, `#TmpInbox`, and `#TmpInboxList`.  
4. Truncate the temp tables to ensure they are empty.  
5. Populate `#TmpSector` with active sectors for the specified line and track type whose effective period includes `@CurrDate`.  
   * Direction is set to 1 for ‘BB’ or ‘NB’, otherwise 2.  
6. Populate `#TmpInbox` with TAR records that meet the following criteria:  
   * Linked to a sector, not a gap, not a buffer, and matching the specified track type.  
   * Workflow status contains ‘Pending’.  
   * Either the workflow has no assigned user (`UserId` = 0) and the endorser’s role matches the current user’s roles, **or** the workflow’s assigned user equals the current user.  
   * Optional filters on access date and TAR type are applied if supplied.  
   * Direction is derived from the sector’s direction flag.  
7. Open a cursor over `#TmpInbox` ordered by TARID and SectorID.  
8. For each inbox record:  
   * If no workflow entries exist with a status other than ‘Pending’, add the record to `#TmpInboxList`.  
   * Otherwise, open a second cursor over the non‑pending workflow entries for that TAR.  
   * Count how many of those entries have `ActionBy` equal to the current user.  
   * If the count is zero, add the inbox record to `#TmpInboxList`.  
9. Close and deallocate both cursors.  
10. Return two result sets:  
    * First set lists sectors with `Direction` = 1, grouped and ordered by `SectorOrder`.  
    * Second set lists sectors with `Direction` = 2, grouped and ordered by `SectorOrder`.  
11. Drop the temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_USER` (to obtain Userid)  
  - `TAMS_Sector` (to retrieve sector details)  
  - `TAMS_TAR` (to retrieve TAR records)  
  - `TAMS_TAR_Sector` (to link TARs to sectors)  
  - `TAMS_TAR_Workflow` (to evaluate workflow status and assignments)  
  - `TAMS_Endorser` (to match endorser roles)  
  - `TAMS_User_Role` (to determine user roles)  

* **Writes:**  
  - Temporary tables `#TmpSector`, `#TmpInbox`, `#TmpInboxList` (no permanent tables are modified).