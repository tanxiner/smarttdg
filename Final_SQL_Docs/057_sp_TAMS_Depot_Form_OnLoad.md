# Procedure: sp_TAMS_Depot_Form_OnLoad

### Purpose
Loads all data required to display the depot form, including company settings, access requirements, work types, user roles, sector details, power zone information, and available timeslots based on the requested access type and date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Identifier of the railway line. |
| @TrackType | NVARCHAR(50) | Type of track (e.g., Depot, DTL). |
| @AccessDate | NVARCHAR(20) | Date of the requested access. |
| @AccessType | NVARCHAR(20) | Either 'Protection' or 'Possession'. |
| @Sectors | NVARCHAR(2000) | Semicolon‑separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(100) | Text describing the power selection (e.g., 'Traction Power ON'). |

### Logic Flow
1. **DW‑Only Check**  
   * Retrieve the list of DW sectors for the given line and access date from `TAMS_Parameters`.  
   * Compare the supplied `@Sectors` list with the DW list.  
   * If every sector in `@Sectors` is in the DW list and vice versa, set `@isDWONLY` to 1; otherwise 0.

2. **Company Parameters**  
   * Select all `ParaValue1` and `ParaValue2` rows from `TAMS_Parameters` where `ParaCode = 'Company'`, the line matches, and the access date falls between `EffectiveDate` and `ExpiryDate`.  
   * Results are ordered by `[Order]`.

3. **Access Requirements – Non‑Power**  
   * Retrieve rows from `TAMS_Access_Requirement` where `Line`, `TrackType`, `IsPowerReq = 0`, and `IsActive = 1`.  
   * Return `Sno`, `ID`, `OperationRequirement`, and `IsAttachment`, ordered by `[Order]`.

4. **Access Requirements – Power**  
   * If `@AccessType = 'Protection'`, fetch only the requirement where `OperationRequirement = 'Traction Power ON'`.  
   * Otherwise, fetch all power requirements (`IsPowerReq = 1`, `IsActive = 1`).  
   * Return `ID` and `OperationRequirement`, ordered by `[Order]`.

5. **Type of Work Options**  
   * Select `ID`, `TypeOfWork`, and `ColourCode` from `TAMS_Type_Of_Work` where the line and track type match, `ForSelection = 1`, and `IsActive = 1`.  
   * Order by `[Order]`.

6. **Head‑of‑Department User**  
   * Build a role name `@Line + '_ApplicantHOD'`.  
   * Join `TAMS_User`, `TAMS_User_Role`, and `TAMS_Role` to find the active user whose role matches the constructed HOD role for the line and track type.  
   * Return `Userid`, `LoginId`, and `EmpName`, ordered by name.

7. **Sector, Power Zone, and SPKS Zone Lists**  
   * Build a comma‑separated list of selected sectors that are not gaps (`@SelSectorNotGap`).  
   * Build a comma‑separated list of power sectors (`@PowerZone`) linked to the selected sectors via `TAMS_Track_Power_Sector`.  
   * Build a comma‑separated list of SPKS zones (`@SPKSZone`) linked via `TAMS_Track_SPKSZone`.  
   * Trim trailing commas from each list.

8. **Temporary Power Sector Table**  
   * Create `#TmpPossPowSector` with columns for power sector, power on/off flag, number of SCDs, and breaker status.  
   * Determine `@StrPowerOnOff` (`'N'` if power selection is 'Traction Power ON', else `'Y'`).  
   * Determine `@StrBreakerOut` (`'Y'` if power selection contains 'With Rack Out', else `'N'`).  
   * Insert a row for each selected sector with the derived flags and `NoOFSCD = 0`.

9. **Day and Holiday Determination**  
   * Convert `@AccessDate` to a date and extract the three‑letter day name (`@DayName`).  
   * Check `TAMS_Calendar` for a holiday on the current system date; set `@PHInd` to `'1'` if a holiday exists, otherwise `'0'`.

10. **Timeslot Availability Calculation**  
    * Depending on `@AccessType` and whether the day is a weekend, public holiday, or weekday, choose the appropriate parameter set (`AccessTimeSlot_Weekend`, `AccessTimeSlot_Weekday_DW`, or `AccessTimeSlot_Weekday`).  
    * For each timeslot, evaluate whether any approved TAR (`TARStatusId = 9`) exists for the selected sectors (excluding buffer sectors for protection).  
    * Return the timeslot value and a `DDLEnable` flag (`'false'` if an approved TAR exists, otherwise `'true'`).  
    * The logic differs slightly for protection (buffer sectors ignored) versus possession (all sectors considered).

11. **End of Procedure**  
    * All result sets are returned to the caller; no permanent data is modified.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_Access_Requirement`  
  - `TAMS_Type_Of_Work`  
  - `TAMS_User`  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_Sector`  
  - `TAMS_Power_Sector`  
  - `TAMS_Track_Power_Sector`  
  - `TAMS_SPKSZone`  
  - `TAMS_Track_SPKSZone`  
  - `TAMS_Calendar`  
  - `TAMS_TAR`  
  - `TAMS_TAR_Sector`  

* **Writes:**  
  - Temporary table `#TmpPossPowSector` (created, truncated, and populated).