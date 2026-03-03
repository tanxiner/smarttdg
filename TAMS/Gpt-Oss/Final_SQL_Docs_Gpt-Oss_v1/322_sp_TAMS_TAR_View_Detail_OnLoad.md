# Procedure: sp_TAMS_TAR_View_Detail_OnLoad

### Purpose
Retrieves all detail information for a specific TAR record, including its core data, sector selections, access requirements, possession details, workflow status, buffer zones, and exception sectors, for display on the client interface.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR record to load |
| @LogInUser | NVARCHAR(20) | Username of the person requesting the data (unused in current logic) |

### Logic Flow
1. **Initial Variable Setup** – Declares variables for line, access date, sector lists, entry stations, and gap status.  
2. **Retrieve Core TAR Metadata** – Loads the TAR’s line and access date into variables.  
3. **Return Main TAR Record** – Selects all columns from the TAR table for the given ID.  
4. **Build Sector Lists** –  
   - Concatenates non‑gap sectors selected for the TAR into `@SelSectorNotGap`.  
   - Concatenates gap sectors selected for the TAR into `@SelSectorGap`.  
   - Concatenates active entry stations for the TAR into `@EntryStation`.  
   - Trims trailing commas from each list.  
5. **Determine Gap Presence** – Sets `@IsGap` to “Yes” if any gap sector exists, otherwise “No”.  
6. **Return Sector Summary** – Returns the three sector lists and the gap flag.  
7. **Return Access Requirements** –  
   - Non‑power requirements where `IsSelected = 1` and `IsPower = 0`.  
   - Power requirements where `IsSelected = 1` and `IsPower = 1`.  
8. **Retrieve Possession Data** –  
   - Loads possession ID, power state, and work type for the TAR.  
   - Returns the possession record, limits, working limits, other protection, power sector, and work type description.  
9. **Compute Workflow Metrics** – Calculates maximum workflow level, count of approved steps, and count of pending steps for the TAR.  
10. **Return Workflow Details** –  
    - Approved workflow entries.  
    - Pending workflow entries.  
11. **Identify Buffer Zone Sectors** – Selects sectors on the same line that are not already linked to the TAR (or a TAR with the same status, date, and line) and are active within the access date range.  
12. **Prepare Exception Tables** – Creates two temporary tables for exception handling, truncates them, and selects all sector associations for the TAR (no further use shown).  
13. **End** – Procedure completes after loading all required data sets.

### Data Interactions
* **Reads:**  
  - TAMS_TAR  
  - TAMS_TAR_Sector  
  - TAMS_Sector  
  - TAMS_Station  
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
* **Writes:** None (only temporary table creation and truncation)