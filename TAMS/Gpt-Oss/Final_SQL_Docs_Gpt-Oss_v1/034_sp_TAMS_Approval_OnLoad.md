# Procedure: sp_TAMS_Approval_OnLoad

### Purpose
Retrieve all data required to display a TAR approval screen, including TAR details, sector selections, access requirements, possession information, workflow status, buffer zones, TVF stations, and exception TARs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to load |
| @LogInUser | NVARCHAR(20) | Login ID of the user requesting the load |

### Logic Flow
1. **Load TAR core data** – Pull Line, AccessDate, TARType, AccessType, IsExclusive, TrackType from TAMS_TAR for the given @TARID.  
2. **Return TAR master record** – Select all columns from TAMS_TAR for @TARID, formatting AccessDate to dd/mm/yyyy.  
3. **Build sector strings** –  
   a. Concatenate non‑gap sectors (IsGap = 0) into @SelSectorNotGap.  
   b. Concatenate gap sectors (IsGap = 1) into @SelSectorGap.  
   c. Concatenate entry stations into @EntryStation.  
   d. Set @IsGap to “Yes” if @SelSectorGap is not empty, otherwise “No”.  
   e. Return these four values as Table[1].  
4. **Access requirements – non‑power** – Select selected, operation requirement, attachment flag, ID, and attachment count for the current TrackType where IsPower = 0. Return as Table[2].  
5. **Access requirements – power** – Same as step 4 but where IsPower = 1. Return as Table[3].  
6. **Possession data** –  
   a. Retrieve Possession ID, PowerOnOff, TypeOfWorkId for @TARID.  
   b. Return full possession record as Table[4].  
   c. Return possession limits, working limits, other protections, and power sector details (with BreakerOut flag) as Tables 5‑8.  
   d. Return the TypeOfWork description for the possession as Table 9.  
7. **Workflow counts** – Calculate maximum workflow level, approved count, and pending count for @TARID. Return as Table[10].  
8. **Workflow history – approved** – Return all non‑pending workflow entries with endorser details and actioner name as Table[11].  
9. **Workflow history – pending** – Return all pending workflow entries with endorser details, actioner name, and current user name as Table[12].  
10. **Buffer zone – additional** –  
    a. Return sectors not already used by the current TAR or by TARs with the same AccessDate/Line/TrackType that are in status 8 or 9, within effective dates, as Table[13].  
    b. Return sectors marked as buffer for the current TAR as Table[14].  
11. **TVF stations – additional** –  
    a. Return all active stations on the current Line as Table[15].  
    b. Return TVF stations linked to the current TAR as Table[16].  
12. **Exception TAR list – sector conflict** –  
    a. Create temporary tables #TmpExc and #TmpExcSector.  
    b. For each sector of the current TAR, insert into #TmpExcSector all TARs that share the same AccessDate, Line, and TrackType, are in status 8 or 9, and are not the current TAR.  
    c. For each record in #TmpExcSector, apply rules: if the current AccessType is “Protection” and the current TAR is not exclusive, only add a TAR to #TmpExc if its AccessType is not “Protection” or it is exclusive; otherwise add it.  
    d. Return the distinct exception TARs from #TmpExc as Table[17].  
13. **Exception TAR list – power requirement** –  
    a. If current AccessType is “Protection”, return all active power requirements where OperationRequirement is not “Traction Power ON”.  
    b. Otherwise return all active power requirements.  
    c. Return these as Table[18].

### Data Interactions
* **Reads:**  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_Sector  
  - TAMS_Station  
  - TAMS_TAR_Station  
  - TAMS_TAR_Attachment  
  - TAMS_TAR_AccessReq  
  - TAMS_Access_Requirement  
  - TAMS_Possession  
  - TAMS_Possession_Limit  
  - TAMS_Possession_WorkingLimit  
  - TAMS_Possession_OtherProtection  
  - TAMS_Possession_PowerSector  
  - TAMS_Type_Of_Work  
  - TAMS_TAR_Workflow  
  - TAMS_Endorser  
  - TAMS_User  
  - Temporary tables #TmpExc, #TmpExcSector  
* **Writes:** none (only SELECT statements)