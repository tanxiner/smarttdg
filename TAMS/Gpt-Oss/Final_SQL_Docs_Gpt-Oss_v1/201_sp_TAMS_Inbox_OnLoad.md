# Procedure: sp_TAMS_Inbox_OnLoad

### Purpose
Loads the inbox view for a user, returning sectors and pending TARs filtered by line, date, and type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier to filter sectors |
| @AccessDate | NVARCHAR(20) | Optional access date to filter TARs |
| @TARType | NVARCHAR(20) | Optional TAR type to filter TARs |
| @LoginUser | NVARCHAR(50) | User login used to determine UserID and role |

### Logic Flow
1. Resolve the numeric UserID for the supplied @LoginUser from TAMS_USER.  
2. Capture the current date (without time) into @CurrDate.  
3. Create three temporary tables: #TmpSector, #TmpInbox, #TmpInboxList.  
4. Populate #TmpSector with active sectors for the specified @Line whose effective/expiry window includes @CurrDate.  
   * Map sector direction: 'BB' or 'NB' → 1, otherwise → 2.  
   * Order sectors by the [Order] column.  
5. Populate #TmpInbox with TAR records that are pending in workflow and belong to the sectors in #TmpSector.  
   * Two UNIONed queries:  
     * First selects TARs where the workflow endorser role matches the current user’s roles and no UserId is assigned.  
     * Second selects TARs where the workflow UserId equals the current UserID.  
   * Apply optional filters for @AccessDate and @TARType.  
   * Exclude sectors marked as gaps or buffers.  
   * Convert AccessDate to string format 103 and map sector direction as in step 4.  
6. Iterate over each record in #TmpInbox using a cursor.  
   * For each TAR, check if any workflow entries exist with status other than 'Pending'.  
     * If none exist, insert the record into #TmpInboxList.  
     * If such entries exist, open a second cursor to fetch all ActionBy values from those workflow rows.  
       * (Commented code would increment a counter if the current user matches an ActionBy, but it is inactive.)  
   * After the second cursor, if the counter remains zero, insert the record into #TmpInboxList.  
7. Close and deallocate both cursors.  
8. Produce the first result set: left‑join #TmpSector to #TmpInboxList on SectorID, filter where Direction = 1, group by all selected columns, and order by SectorOrder.  
9. Produce the second result set: same join but filter where Direction = 2, group and order similarly.  
10. Drop the temporary tables.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role  
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList (temporary tables only)