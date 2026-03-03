# Procedure: sp_TAMS_Form_OnLoad

### Purpose
Retrieves configuration, requirement, user, sector, and power‑sector data for a form load based on line, track type, access date, access type, selected sectors, and power selection text.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Identifier of the line (e.g., 'DTL', 'NEL') |
| @TrackType | NVARCHAR(50) | Type of track for which data is requested |
| @AccessDate | NVARCHAR(20) | Date of access, used to filter parameter validity |
| @AccessType | NVARCHAR(20) | Determines which power requirements are returned ('Protection' or other) |
| @Sectors | NVARCHAR(2000) | Semicolon‑separated list of sector IDs selected by the user |
| @PowerSelTxt | NVARCHAR(100) | Text describing the desired power state (e.g., 'Traction Power ON') |

### Logic Flow
1. **Company Parameters** – Selects `ParaValue1` and `ParaValue2` from `TAMS_Parameters` where the code is 'Company', the value matches `@Line`, and the access date falls between `EffectiveDate` and `ExpiryDate`. Results are ordered by `[Order]`.

2. **Access Requirements (Non‑Power)** – Retrieves a numbered list of active, non‑power requirements for the specified line and track type. The list is ordered by `[Order]`.

3. **Power Requirements** –  
   * If `@AccessType` equals 'Protection', selects active power requirements where `OperationRequirement` is not 'Traction Power ON'.  
   * Otherwise, selects all active power requirements.  
   Results are ordered by `[Order]`.

4. **Type of Work** – Fetches active work types for the line and track type that are marked for selection, ordered by `[Order]`.

5. **Head‑of‑Department User** – Builds a role name by concatenating `@Line` with `_ApplicantHOD`. Retrieves the user ID, login ID, and name of the active user who holds this role for the line and track type.

6. **Sector Lists** –  
   * Splits `@Sectors` into individual IDs using the `SPLIT` function.  
   * Builds a comma‑separated list of sectors where `IsGap = 0` (`@SelSectorNotGap`).  
   * Builds a comma‑separated list of sectors where `IsGap = 1` (`@SelSectorGap`).  
   * Builds a comma‑separated list of entry station codes linked to the selected sectors (`@EntryStation`).  
   Each list is trimmed of trailing commas.

7. **Return Sector Information** – Outputs the three lists (`SelSectorNotGap`, `SelSectorGap`, `EntryStation`).

8. **Possible Power Sector Determination** –  
   * Creates a temporary table `#TmpPossPowSector`.  
   * Determines flags:  
     - `@StrPowerOnOff` is 'Y' if `@PowerSelTxt` equals 'Traction Power ON', otherwise 'N'.  
     - `@PowerOnInd` is 1 for 'Traction Power ON', otherwise 0.  
     - `@StrBreakerOut` is 'Y' if `@PowerSelTxt` contains 'With Rack Out', otherwise 'N'.  
   * If `@Line` is 'DTL': concatenates all selected sector names into `@DTLSelSectors` and inserts a single row into the temp table with the flags.  
   * If `@Line` is not 'DTL' (e.g., 'NEL'): selects power sectors from `TAMS_Sector`, `TAMS_Track_Power_Sector`, and `TAMS_Power_Sector` where the sector is active, the power sector is active, and the power on flag matches `@PowerOnInd` (or is null). Groups by `PowerSector` and inserts each into the temp table with the flags.

9. **Return Possible Power Sectors** – Selects `PowerSector`, `PowerOnOff`, `NoOFSCD`, and `BreakerOut` from the temporary table.

### Data Interactions
* **Reads:**  
  - TAMS_Parameters  
  - TAMS_Access_Requirement  
  - TAMS_Type_Of_Work  
  - TAMS_User  
  - TAMS_User_Role  
  - TAMS_Role  
  - TAMS_Sector  
  - TAMS_Station  
  - TAMS_Entry_Station  
  - TAMS_Track_Power_Sector  
  - TAMS_Power_Sector  

* **Writes:**  
  - Temporary table `#TmpPossPowSector` (inserted rows only, no permanent table updates)