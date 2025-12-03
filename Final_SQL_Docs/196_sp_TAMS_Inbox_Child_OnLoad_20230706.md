# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230706

### Purpose
Return the list of TARs that are pending for a specific sector, filtered by line, access date, TAR type, and the current user’s role, while excluding cancelled TARs and those already processed by the user.

### Parameters
| Name        | Type          | Purpose |
| :---        | :---          | :--- |
| @Line       | NVARCHAR(10)  | Target line identifier. |
| @AccessDate | NVARCHAR(20)  | Date to filter TARs by AccessDate; empty string means no date filter. |
| @TARType    | NVARCHAR(20)  | TAR type to filter; empty string means all types. |
| @LoginUser  | NVARCHAR(50)  | Login ID of the user invoking the procedure. |
| @SectorID   | INT           | Sector identifier to return results for. |

### Logic Flow
1. **Identify the user** – look up the numeric UserID in TAMS_USER that matches @LoginUser.  
2. **Set the current date** – truncate the current system date to a day value.  
3. **Find the cancelled status ID** – retrieve the WFStatusId from TAMS_WFStatus where the line matches @Line, the workflow type is TARWFStatus, and the status is Cancel.  
4. **Prepare temporary tables** – create #TmpSector, #TmpInbox, and #TmpInboxList to hold intermediate data.  
5. **Load active sectors** – insert into #TmpSector all active sectors for @Line whose effective period includes the current date, ordering them and converting the Direction flag to 1 for BB/NB and 2 otherwise.  
6. **Load pending TARs** – insert into #TmpInbox two sets of TARs:  
   * a. TARs with a pending workflow entry that has no assigned UserId and where the endorser’s role matches the current user’s roles.  
   * b. TARs with a pending workflow entry that is already assigned to the current user.  
   Both sets are filtered by AccessDate (if supplied), TARType (if supplied), IsBuffer=0, and not having the cancelled status.  
7. **Process each TAR record** – iterate over #TmpInbox sorted by TARID and SectorID. For each record:  
   a. If the TAR has no workflow entries with a status other than Pending, add it to #TmpInboxList.  
   b. Otherwise, count how many non‑Pending workflow entries have ActionBy equal to the current user. If none, add the TAR to #TmpInboxList.  
8. **Return the sector‑specific list** – select distinct TARID, TARNo, TARType, AccessDate, and AccessType from #TmpInboxList where SectorID equals @SectorID, grouping and ordering by those fields.  
9. **Clean up** – drop the temporary tables.

### Data Interactions
* **Reads:**  
  - TAMS_USER  
  - TAMS_WFStatus  
  - TAMS_Sector  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_TAR_Workflow  
  - TAMS_Endorser  
  - TAMS_User_Role  

* **Writes:**  
  - #TmpSector  
  - #TmpInbox  
  - #TmpInboxList   (temporary tables only)