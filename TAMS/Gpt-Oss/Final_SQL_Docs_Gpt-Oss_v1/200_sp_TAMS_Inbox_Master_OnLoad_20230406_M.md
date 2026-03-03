# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406_M

### Purpose
Retrieves and filters inbox items for a specified line, access date, and TAR type, returning sector‑ordered lists of pending or user‑eligible TARs for the logged‑in user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Target line identifier (e.g., “DTL”, “NEL”). |
| @AccessDate | NVARCHAR(20) | Date filter for TAR access; empty string means no date filter. |
| @TARType | NVARCHAR(20) | TAR type filter; empty string means all types. |
| @LoginUser | NVARCHAR(50) | Username of the caller; used to resolve UserID and role membership. |

### Logic Flow
1. Resolve the numeric UserID for the supplied @LoginUser from TAMS_USER.  
2. Capture the current date in a datetime variable @CurrDate.  
3. Create three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList.  
4. Populate #TmpSector with active sectors for the requested @Line whose effective period includes @CurrDate.  
   * Sector direction is coded as 1 for “BB” or “NB”, otherwise 2.  
5. Populate #TmpInbox with TAR records that meet all of the following:  
   * Linked to a sector via TAMS_TAR_Sector.  
   * Associated workflow is in a “Pending” state.  
   * Sector is not a gap and workflow has no assigned UserId.  
   * Endorser role matches one of the caller’s roles.  
   * AccessDate matches @AccessDate if supplied.  
   * TARType matches @TARType if supplied.  
   * The TAR is not a buffer sector.  
   * Two UNIONed queries are used: one for workflows with no assigned UserId, and one for workflows where the assigned UserId equals the caller’s UserID.  
6. Iterate over each record in #TmpInbox using a cursor (Cur01). For each TAR:  
   * If the TAR has no workflow records with a status other than “Pending”, add it to #TmpInboxList.  
   * Otherwise, collect all ActionBy values from non‑pending workflows.  
   * If the caller’s UserID is not among those ActionBy values, add the TAR to #TmpInboxList.  
7. After cursor processing, output the contents of #TmpInbox and #TmpInboxList for debugging.  
8. Produce two result sets that list sectors in ascending order of SectorOrder, one for direction 1 and one for direction 2.  
   * These result sets currently only return sector metadata; the commented JOIN to #TmpInboxList indicates future expansion to include TAR details.  
9. Drop the temporary tables and end the procedure.

### Data Interactions
* **Reads:**  
  * TAMS_USER – to resolve UserID.  
  * TAMS_Sector – to fetch active sectors for the line.  
  * TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role – to assemble the inbox list based on workflow status, role membership, and sector linkage.  

* **Writes:**  
  * #TmpSector – temporary sector list.  
  * #TmpInbox – temporary inbox candidate list.  
  * #TmpInboxList – temporary final inbox list after filtering.  

No permanent tables are modified.