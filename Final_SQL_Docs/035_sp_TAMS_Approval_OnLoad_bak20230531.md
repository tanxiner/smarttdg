# Procedure: sp_TAMS_Approval_OnLoad_bak20230531

### Purpose
Loads every data set required to display the approval screen for a specific TAR, including TAR details, sector selections, access requirements, possession information, workflow status, buffer zones, TVF stations, and a list of conflicting TARs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to load |
| @LogInUser | NVARCHAR(20) | Login ID of the user requesting the data |

### Logic Flow
1. **Retrieve TAR core attributes** – Line, AccessDate, TARType, AccessType, IsExclusive from TAMS_TAR for @TARID.  
2. **Return main TAR record** – Select all columns from TAMS_TAR for @TARID, formatting AccessDate as dd/mm/yyyy.  
3. **Build sector lists** –  
   * Concatenate non‑gap sector names where IsBuffer = 0 and IsGap = 0.  
   * Concatenate gap sector names where IsBuffer = 0 and IsGap = 1.  
   * Concatenate entry station codes where IsActive = 1.  
   * Determine if any gap sectors exist (`IsGap = 'Yes'` if gap list non‑empty).  
   * Return these three strings and the gap flag as Table[1].  
4. **Selected access requirements (non‑power)** – Return rows from TAMS_TAR_AccessReq joined with TAMS_Access_Requirement where IsSelected = 1, IsPower = 0, and the requirement is active, including an attachment count. Table[2].  
5. **Selected access requirements (power)** – Return rows where IsSelected = 1, IsPower = 1, and the requirement is active. Table[3].  
6. **Possession details** – Return all columns from TAMS_Possession for @TARID. Table[4].  
7. **Possession limits** – Return rows from TAMS_Possession_Limit where PossessionId = @PossID. Table[5].  
8. **Possession working limits** – Return rows from TAMS_Possession_WorkingLimit where PossessionId = @PossID. Table[6].  
9. **Possession other protection** – Return rows from TAMS_Possession_OtherProtection where PossessionId = @PossID. Table[7].  
10. **Possession power sector** – Return rows from TAMS_Possession_PowerSector where PossessionId = @PossID, adding a computed BreakerOut flag. Table[8].  
11. **Type of work description** – Return the TypeOfWork text from TAMS_Type_Of_Work for @TypeOfWork. Table[9].  
12. **Workflow metrics** – Compute maximum workflow level, count of approved and pending workflow entries for @TARID. Return as Table[10].  
13. **Approved workflow entries** – Return all workflow rows where WFStatus <> 'Pending', joined with endorser and user tables for names and roles. Table[11].  
14. **Pending workflow entries** – Return all workflow rows where WFStatus = 'Pending', joined with endorser and user tables, and include the current user name. Table[12].  
15. **Buffer zone sectors not in TAR** – Return sectors on the same line whose IDs are not present in any TAR for the same AccessDate and Line, and whose effective period covers AccessDate. Table[13].  
16. **Buffer zone sectors in current TAR** – Return sectors marked IsBuffer = 1 for @TARID. Table[14].  
17. **TVF stations for line** – Return all stations where IsStation = 1 and IsActive = 1 for @Line. Table[15].  
18. **TVF station assignments for TAR** – Return station name, TVF direction, and TVFID for @TARID. Table[16].  
19. **Build exception list** –  
    * Create temp tables #TmpExcSector and #TmpExc.  
    * For each sector of @TARID, insert into #TmpExcSector all other TARs that share the same AccessDate, status 8, active sector, and match buffer rules.  
    * Iterate over #TmpExcSector to populate #TmpExc with distinct TARs that conflict, applying special logic when AccessType = 'Protection' and exclusivity flags.  
    * Return the distinct list of conflicting TARs as Table[17].  
20. **Return power‑requirement list** – Depending on @AccessType, return active power access requirements for @Line, excluding 'Traction Power ON' when AccessType = 'Protection'. Table[18].

### Data Interactions
* **Reads:**  
  TAMS_TAR, TAMS_TAR_Sector, TAMS_Sector, TAMS_TAR_Station, TAMS_Station, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Possession, TAMS_Possession_Limit, TAMS_Possession_WorkingLimit, TAMS_Possession_OtherProtection, TAMS_Possession_PowerSector, TAMS_Type_Of_Work, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User, TAMS_TAR_TVF, TAMS_TAR, TAMS_TAR_Sector, TAMS_Sector, TAMS_TAR_TVF, TAMS_Station, TAMS_Access_Requirement.
* **Writes:**  
  Temporary tables #TmpExcSector and #TmpExc (inserted and truncated). No permanent table modifications.