# Procedure: sp_TAMS_Inbox_Child_OnLoad_20240925

### Purpose
Retrieves a list of TAR records that are pending for the logged‑in user or unassigned, filtered by line, track type, access date, TAR type, and sector, and returns the distinct TARs for the specified sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier to scope sectors and TARs |
| @TrackType | NVARCHAR(50) | Track type filter for sectors and TARs |
| @AccessDate | NVARCHAR(20) | Optional date filter for TAR access dates |
| @TARType | NVARCHAR(20) | Optional filter for TAR type |
| @LoginUser | NVARCHAR(50) | Login ID of the user invoking the procedure |
| @SectorID | INT | Sector identifier to limit the final result set |

### Logic Flow
1. **User Identification** – Resolve the numeric @UserID from @LoginUser via TAMS_USER.  
2. **Current Date** – Store today’s date in @CurrDate for sector validity checks.  
3. **Cancelled Status** – Retrieve the workflow status ID that represents a cancelled TAR into @StatusId.  
4. **Temporary Tables** – Create #TmpSector, #TmpInbox, and #TmpInboxList; truncate them to ensure a clean state.  
5. **Sector List** – Populate #TmpSector with active sectors for the given @Line and @TrackType whose effective/expiry window includes @CurrDate. Direction is coded 1 for 'BB'/'NB', otherwise 2.  
6. **Inbox Candidates** – Insert into #TmpInbox all TARs that meet the following:  
   * Linked to a sector in #TmpSector.  
   * Have a pending workflow entry.  
   * Either unassigned (UserId null) or assigned to @UserID.  
   * Match optional @AccessDate and @TARType filters.  
   * Not cancelled (TARStatusId ≠ @StatusId).  
   * TrackType matches @TrackType.  
   The union of two SELECTs handles the unassigned and assigned cases separately.  
7. **Process Each Candidate** – Using cursor @Cur01 over #TmpInbox:  
   a. If the TAR has no workflow entries with a status other than 'Pending', add it to #TmpInboxList.  
   b. If there are non‑pending entries, open cursor @Cur02 to iterate over their ActionBy values.  
   c. Count how many of those ActionBy values equal @UserID.  
   d. If none match, add the TAR to #TmpInboxList.  
8. **Result Set** – Select distinct TARID, TARNo, TARType, AccessDate, AccessType from #TmpInboxList where SectorID equals @SectorID, grouping to eliminate duplicates and ordering by TAR fields.  
9. **Cleanup** – Drop the temporary tables.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_WFStatus, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role  
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList (temporary tables)