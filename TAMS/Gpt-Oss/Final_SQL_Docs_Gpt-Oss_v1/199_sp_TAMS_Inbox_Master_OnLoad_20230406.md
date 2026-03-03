# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406

### Purpose
Retrieves sector lists for a specified line, filtered by user access and pending workflow status, and returns two ordered result sets of sectors grouped by direction.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier for sector selection |
| @AccessDate | NVARCHAR(20) | Optional filter for TAR access date |
| @TARType | NVARCHAR(20) | Optional filter for TAR type |
| @LoginUser | NVARCHAR(50) | User login used to resolve UserID and role permissions |

### Logic Flow
1. Resolve the numeric UserID for the supplied @LoginUser from TAMS_USER.  
2. Determine the current date in DD/MM/YYYY format and store it in @CurrDate.  
3. Create three temporary tables: #TmpSector, #TmpInbox, #TmpInboxList.  
4. Truncate the temp tables to ensure they are empty.  
5. Populate #TmpSector with active sectors for the specified @Line whose effective and expiry dates encompass @CurrDate.  
   * Convert the Direction field to 1 for 'BB' or 'NB', otherwise 2.  
6. Populate #TmpInbox with TAR records that meet the following criteria:  
   * Linked to a sector via TAMS_TAR_Sector.  
   * Workflow status contains 'Pending'.  
   * Sector is not a gap and the workflow has no assigned UserId.  
   * Endorser role matches one of the roles assigned to the resolved UserID.  
   * Optional filters on @AccessDate and @TARType are applied.  
   * Sector buffer flag is 0.  
   * A second UNION query adds records where the workflow UserId equals the resolved UserID, applying the same optional filters.  
7. Open a cursor (Cur01) over #TmpInbox ordered by TARID and SectorID.  
8. For each row from Cur01:  
   * Check if any workflow record for the TAR has a status other than 'Pending'.  
   * If none exist, insert the row into #TmpInboxList.  
   * If such records exist, open a second cursor (Cur02) over those workflow records.  
   * Count how many of those records have ActionBy equal to the resolved UserID.  
   * If the count is zero, insert the row into #TmpInboxList.  
9. Close and deallocate both cursors.  
10. Return two result sets:  
    * First set selects distinct sectors from #TmpSector where Direction = 1, grouped and ordered by SectorOrder.  
    * Second set selects distinct sectors from #TmpSector where Direction = 2, grouped and ordered by SectorOrder.  
11. Drop the temporary tables.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role  
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList (temporary tables only)