# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406

### Purpose
Retrieves a list of TAR records that are pending action for a specific sector, filtered by line, access date, TAR type, and user role, while excluding cancelled TARs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier |
| @AccessDate | NVARCHAR(20) | Date to filter TARs by access date |
| @TARType | NVARCHAR(20) | TAR type filter |
| @LoginUser | NVARCHAR(50) | User login used to resolve UserID and role |
| @SectorID | INT | Sector identifier to limit final output |

### Logic Flow
1. Resolve the numeric UserID for the supplied @LoginUser from TAMS_USER.  
2. Determine the current date in `dd/MM/yyyy` format and store it in @CurrDate.  
3. Find the workflow status ID that represents a cancelled TAR for the given @Line.  
4. Create three temporary tables:  
   * #TmpSector – holds active sectors for the line with order and direction flags.  
   * #TmpInbox – will contain candidate TARs that meet workflow and role criteria.  
   * #TmpInboxList – final list of TARs that are eligible for the user.  
5. Populate #TmpSector with active sectors for @Line whose effective period includes @CurrDate, ordering by the sector order field.  
6. Populate #TmpInbox with TARs that satisfy:  
   * Associated with a sector in #TmpSector.  
   * Workflow status contains “Pending”.  
   * No assigned user (UserId = 0) **or** the assigned user is the current user.  
   * Endorser role matches one of the current user’s roles.  
   * AccessDate matches @AccessDate if supplied.  
   * TARType matches @TARType if supplied.  
   * Not a buffer sector.  
   * Not cancelled (TARStatusId ≠ @StatusId).  
   The query is executed twice: once for unassigned workflows and once for workflows assigned to the current user.  
7. Iterate over each record in #TmpInbox. For each TAR:  
   * If the TAR has no workflow entries with a status other than “Pending”, add it directly to #TmpInboxList.  
   * Otherwise, collect all ActionBy values from non‑pending workflows.  
   * If the current user is not listed among those ActionBy values, add the TAR to #TmpInboxList.  
8. After processing all records, select distinct TAR details from #TmpInboxList where SectorID equals @SectorID, grouping by TAR fields and ordering by TARID, TARNo, TARType, AccessDate, AccessType.  
9. Clean up temporary tables.

### Data Interactions
* **Reads:**  
  * TAMS_USER – to resolve UserID.  
  * TAMS_WFStatus – to find cancelled status ID.  
  * TAMS_Sector – to load active sectors.  
  * TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role – to assemble candidate TARs.  
* **Writes:**  
  * Temporary tables #TmpSector, #TmpInbox, #TmpInboxList – used only within the procedure. No permanent tables are modified.