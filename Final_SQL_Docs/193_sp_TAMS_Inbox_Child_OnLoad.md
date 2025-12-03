# Procedure: sp_TAMS_Inbox_Child_OnLoad

### Purpose
Retrieve the list of pending TAR records for a specific sector and user, excluding cancelled or withdrawn TARs, and ensuring the user is not already assigned to the workflow.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line identifier to filter sectors and status records. |
| @TrackType | NVARCHAR(50) | The track type used to filter sectors and TARs. |
| @AccessDate | NVARCHAR(20) | Optional date to filter TARs by access date. |
| @TARType | NVARCHAR(20) | Optional TAR type to filter the result set. |
| @LoginUser | NVARCHAR(50) | The login identifier of the user invoking the procedure. |
| @SectorID | INT | The sector identifier used to return only TARs belonging to this sector. |

### Logic Flow
1. **User Identification** – Look up the numeric UserID for the supplied @LoginUser from TAMS_USER.  
2. **Current Date** – Store the current system date in @CurrDate.  
3. **Status Retrieval** – Find the workflow status IDs for “Cancel” and “Withdraw” for the given @Line from TAMS_WFStatus.  
4. **Temp Table Setup** – Create three temporary tables: #TmpSector, #TmpInbox, #TmpInboxList.  
5. **Sector Population** – Insert into #TmpSector all active sectors for the specified @Line and @TrackType whose effective period includes @CurrDate.  Each row records the sector’s ID, name, order, and a direction flag (1 for ‘BB’ or ‘NB’, otherwise 2).  
6. **Inbox Population** – Insert into #TmpInbox the TAR records that satisfy:
   * The TAR is linked to a sector in #TmpSector.  
   * The workflow status is pending.  
   * The workflow is either unassigned (UserId = 0) or assigned to the current user.  
   * The endorser’s role matches one of the current user’s roles.  
   * The TAR’s access date matches @AccessDate if supplied.  
   * The TAR’s type matches @TARType if supplied.  
   * The sector is not a buffer.  
   * The TAR’s status is neither the cancelled nor the withdrawn status.  
   * The TAR’s track type matches @TrackType.  
   Two UNIONed SELECTs handle the unassigned and assigned cases separately.  
7. **First Cursor (Cur01)** – Iterate over #TmpInbox sorted by TARID and SectorID.  
   * For each TAR, check if any workflow entries exist with a status other than pending.  
   * If none exist, add the TAR to #TmpInboxList.  
   * If such entries exist, open a second cursor (Cur02) to count how many of those entries have ActionBy equal to the current user.  
   * If the count is zero, add the TAR to #TmpInboxList.  
8. **Result Selection** – Return the distinct set of TARs from #TmpInboxList that belong to the requested @SectorID, grouped and ordered by TARID, TARNo, TARType, AccessDate, and AccessType.  
9. **Cleanup** – Drop the temporary tables.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_WFStatus, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role.  
* **Writes:** Temporary tables #TmpSector, #TmpInbox, #TmpInboxList (no permanent data is modified).