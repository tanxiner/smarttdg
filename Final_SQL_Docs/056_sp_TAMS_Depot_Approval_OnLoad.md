# Procedure: sp_TAMS_Depot_Approval_OnLoad

### Purpose
Retrieve all data required to display a TAR approval screen, including TAR details, sector selections, access requirements, possession information, workflow status, buffer zones, and potential sector conflicts.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to load |
| @LogInUser | NVARCHAR(20) | Login ID of the user requesting the load |

### Logic Flow
1. **Variable Initialization** – Declare variables for TAR attributes, sector lists, and cursor control.
2. **Header Retrieval** – Load TAR header fields (Line, TrackType, AccessDate, etc.) into variables from `TAMS_TAR` where `ID = @TARID`.
3. **Table[0] – TAR Header** – Select the full TAR record for display.
4. **Sector List Construction**  
   - Build comma‑separated lists of non‑gap sectors, power sectors, and SPKS zones that belong to the TAR and are not buffers.  
   - Trim trailing commas.
5. **Table[1] – Sector Lists** – Return the three lists (`SelSectorNotGap`, `SelSectorGap`, `PowerZone`, `SPKSZone`).
6. **Table[2] – Selected Non‑Power Access Requirements** – Return selected access requirements where `IsPower = 0`, including attachment count.
7. **Table[3] – Selected Power Access Requirements** – Return selected access requirements where `IsPower = 1`.
8. **Possession Variables** – Retrieve `PossID`, `PowerOnOff`, and `TypeOfWork` from `TAMS_Possession` for the TAR.
9. **Table[4] – Possession Details** – Return all possession rows for the TAR.
10. **Table[5] – Possession Limits** – Return protection limits for the possession.
11. **Table[6] – Working Limits** – Return working limits for the possession.
12. **Table[7] – Other Protection** – Return other protection entries for the possession.
13. **Table[8] – Depot Sector Details** – Return depot sector rows for the possession.
14. **Table[9] – Type of Work** – Return the active type of work record matching `@TypeOfWork`.
15. **Workflow Counters** – Compute maximum workflow level, count of approved and pending workflow records for the TAR.
16. **Table[10] – Workflow Counters** – Return the three counters.
17. **Table[11] – Approved Workflow Records** – Return all workflow rows where `WFStatus <> 'Pending'`, enriched with endorser and user details.
18. **Current User Name** – Retrieve the name of `@LogInUser` from `TAMS_User`.
19. **Table[12] – Pending Workflow Records** – Return all workflow rows where `WFStatus = 'Pending'`, including the current user name.
20. **Table[13] – Additional Buffer Zones (Non‑TAR)** – Return sectors that are not part of the current TAR but match the same line, track type, date, time slot, and are active within the effective period.
21. **Table[14] – Additional Buffer Zones (TAR)** – Return sectors marked as buffers for the current TAR.
22. **Exception List Construction**  
    - Create temporary tables `#TmpExc` and `#TmpExcSector`.  
    - For each sector of the current TAR, query other TARs that share the same access date/time, status 8 or 9, and line, filtering by buffer flag.  
    - Insert matching TARs into `#TmpExcSector`.  
    - Iterate `#TmpExcSector` to populate `#TmpExc` with unique TARs, applying protection and exclusivity rules to avoid duplicate or conflicting entries.
23. **Table[15] – Exception List** – Return the distinct conflicting TARs from `#TmpExc`.
24. **Table[16] – Access Requirement List** – Depending on `@AccessType`, return the list of active access requirements that are power‑related and match the line and track type.

### Data Interactions
* **Reads:**  
  - `TAMS_TAR`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Sector`  
  - `TAMS_Power_Sector`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_SPKSZone`  
  - `TAMS_TAR_SPKSZone`  
  - `TAMS_TAR_AccessReq`  
  - `TAMS_Access_Requirement`  
  - `TAMS_Possession`  
  - `TAMS_Possession_Limit`  
  - `TAMS_Possession_WorkingLimit`  
  - `TAMS_Possession_OtherProtection`  
  - `TAMS_Possession_DepotSector`  
  - `TAMS_Type_Of_Work`  
  - `TAMS_TAR_Workflow`  
  - `TAMS_Endorser`  
  - `TAMS_User`  
  - Temporary tables `#TmpExc`, `#TmpExcSector`

* **Writes:**  
  - Creation and population of temporary tables `#TmpExc` and `#TmpExcSector` (no permanent table modifications)