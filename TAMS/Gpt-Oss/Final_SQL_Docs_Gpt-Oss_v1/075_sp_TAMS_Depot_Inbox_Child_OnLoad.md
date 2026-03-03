# Procedure: sp_TAMS_Depot_Inbox_Child_OnLoad

### Purpose
Retrieve the list of TAR records that are pending for a specific sector, applying user‑specific and date filters, and return the distinct set of records for that sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Filter sectors by line identifier |
| @TrackType | NVARCHAR(50) | Filter sectors and TARs by track type |
| @AccessDate | NVARCHAR(20) | Optional date to limit TARs to a specific access date |
| @TARType | NVARCHAR(20) | Optional TAR type filter |
| @LoginUser | NVARCHAR(50) | User login used to resolve the current user ID |
| @SectorID | INT | Target sector ID for which the inbox list is required |

### Logic Flow
1. Resolve the numeric user ID for the supplied @LoginUser from TAMS_USER.  
2. Capture the current date in a datetime variable @CurrDate.  
3. Create three temporary tables: #TmpSector, #TmpInbox, #TmpInboxList.  
4. Populate #TmpSector with active sectors that match @Line, @TrackType, and whose effective/expiry window includes @CurrDate, ordered by the sector order field.  
5. Populate #TmpInbox with TAR records that satisfy:  
   * linked to a sector in #TmpSector,  
   * have a pending workflow status,  
   * either have no assigned user or the assigned user is the current user,  
   * match the optional @AccessDate or are future dates when @AccessDate is omitted,  
   * match the optional @TARType,  
   * are not buffer sectors,  
   * match @TrackType.  
   The query pulls TAR details, sector ID, and sector string.  
6. Iterate over each row in #TmpInbox (cursor @Cur01). For each TAR:  
   a. If the TAR has no workflow entries with a status other than 'Pending', add the row to #TmpInboxList.  
   b. If such entries exist, open a second cursor (@Cur02) to fetch the ActionBy user IDs for those entries.  
   c. Count how many of those ActionBy IDs equal the current user ID.  
   d. If the count is zero, add the TAR row to #TmpInboxList.  
7. After processing all rows, select distinct TAR rows from #TmpInboxList where SectorID equals @SectorID, grouping by all TAR fields and ordering by the same set.  
8. Drop the temporary tables and end the procedure.

### Data Interactions
* **Reads:**  
  - TAMS_USER  
  - TAMS_Sector  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_TAR_Workflow  
  - TAMS_Endorser  
  - TAMS_User_Role  

* **Writes:**  
  - #TmpSector (temporary)  
  - #TmpInbox (temporary)  
  - #TmpInboxList (temporary)