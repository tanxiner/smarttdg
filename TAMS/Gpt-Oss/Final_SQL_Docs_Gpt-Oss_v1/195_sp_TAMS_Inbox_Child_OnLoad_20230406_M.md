# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406_M

### Purpose
Loads the list of TARs that a user can act on in the inbox, filtered by line, access date, TAR type, and sector, while excluding cancelled TARs and ensuring the user is not already an actioner for completed workflows.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier used to filter sectors and TARs |
| @AccessDate | NVARCHAR(20) | Date filter for TAR access dates |
| @TARType | NVARCHAR(20) | TAR type filter |
| @LoginUser | NVARCHAR(50) | User login used to resolve UserID and roles |
| @SectorID | INT | Intended sector filter (not applied in final output) |

### Logic Flow
1. Resolve the numeric @UserID for @LoginUser from TAMS_USER.  
2. Capture the current date in @CurrDate.  
3. Retrieve the workflow status ID for a cancelled TAR on the specified @Line.  
4. Create three temporary tables: #TmpSector, #TmpInbox, #TmpInboxList.  
5. Populate #TmpSector with active sectors for @Line whose effective period includes @CurrDate, ordering them and mapping Direction values to 1 (BB/NB) or 2 (others).  
6. Populate #TmpInbox with TARs that meet all of the following:  
   * Linked to a sector in #TmpSector.  
   * Have a pending workflow entry.  
   * Either unassigned (UserId null) and the endorser’s role matches one of the user’s roles, or assigned to @UserID.  
   * Match @AccessDate and @TARType if provided.  
   * Not a buffer sector and not cancelled.  
   The query is split into two UNION parts to handle unassigned and assigned workflows separately.  
7. Iterate over each row in #TmpInbox using a cursor. For each TAR:  
   * If the TAR has no workflow entries with a status other than Pending, add it to #TmpInboxList.  
   * Otherwise, open a second cursor to count how many non‑Pending workflow entries have ActionBy equal to @UserID.  
   * If that count is zero, add the TAR to #TmpInboxList.  
8. After processing all rows, select distinct TAR records from #TmpInboxList, grouping by TARID, TARNo, TARType, AccessDate, and AccessType, and order the result.  
9. Drop the temporary tables.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_WFStatus, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role  
* **Writes:** None (only temporary tables are created and dropped)