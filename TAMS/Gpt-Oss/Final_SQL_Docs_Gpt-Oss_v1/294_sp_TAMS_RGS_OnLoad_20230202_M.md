# Procedure: sp_TAMS_RGS_OnLoad_20230202_M

### Purpose
Generate a detailed RGS (Request for Grid Service) report for a specified line, including possession and protection status, electrical sector details, and cancellation information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., 'DTL', 'NEL') to filter TAR and TOA records |

### Logic Flow
1. **Temporary tables creation**  
   - `#TmpRGS` holds the final report rows.  
   - `#TmpRGSSectors` is used to accumulate sector‑level data during processing.

2. **Date and time setup**  
   - Current date/time captured.  
   - `@CutOff` set to 06:00:00; if current time is after this, `@OperationDate` is today and `@AccessDate` is tomorrow; otherwise, `@OperationDate` is yesterday and `@AccessDate` is today.

3. **Parameter lookup**  
   - Retrieve background colour codes for possession, protection, and cancelled states from `TAMS_Parameters` based on `@Line`.

4. **Count existing possession records**  
   - `@lv_PossessionCtr` counts TAR/TOA pairs with `AccessType = 'Possession'`, `TOAStatus` not 0 or 6, and matching `@Line` and `@AccessDate`.

5. **Main cursor (`@Cur01`)**  
   - Iterates over all TAR/TOA pairs for the chosen line and access date where `TOAStatus` ≠ 0.  
   - For each pair, initialise local variables and fetch related data:
     - Electrical sector string via `dbo.TAMS_Get_ES_NoBufferZone`.
     - Parties list via `dbo.TAMS_Get_TOA_Parties`.
     - Contact string concatenating mobile and radio numbers.

6. **Sector processing**  
   - If `@Line = 'DTL'`:  
     - Cursor `@Cur02` loops over sector IDs from `TAMS_TAR_Sector` where the sector is not a gap and not a buffer.  
     - For each sector, three queries populate `#TmpRGSSectors` to determine:
       - Authorization status (`OCCAuthStatusId` 10 or 7 with buffer flag).  
       - Power‑off time (`PowerOffTime`).  
       - Circuit‑break time (`RackedOutTime`).  
     - Flags `@lv_IsTOAAuth`, `@lv_IsPowerOff`, `@lv_IsCircuitBreak` and corresponding times are set based on query results.
   - Else (`@Line` not 'DTL'):  
     - Cursor `@Cur02` loops over power‑sector IDs from `TAMS_TAR_Power_Sector` where `IsBuffer = 0`.  
     - Similar three queries populate `#TmpRGSSectors` to set authorization, power‑off, and circuit‑break flags and times, using `OCCAuthStatusId = 8`.

7. **Remarks construction**  
   - For 'DTL': remarks = trimmed `@ARRemark` + line break + trimmed `@TVFMode`.  
   - For other lines:  
     - If a rack‑out requirement exists (`OperationRequirement = 27`), prepend "Rack Out" to remarks.  
     - If an SCD application requirement exists, prepend "SCD".  
   - Append TVF stations string from `dbo.TAMS_Get_TOA_TVF_Stations`.  
   - If remarks remain empty, use the TVF stations string alone.

8. **Colour code and TOA enable logic**  
   - If `AccessType = 'Possession'`:  
     - Use possession background colour.  
     - Adjust `@lv_PossessionCtr` based on `TOAStatus` and `ProtTimeLimit`.  
     - Set `@lv_IsGrantTOAEnable = 1`.  
   - Else:  
     - Use protection background colour.  
     - Set `@lv_IsGrantTOAEnable` to 1 if `TOAStatus = 6`; otherwise, disable if `@lv_PossessionCtr > 0`.  

9. **Callback time**  
   - If `TOANo` is empty, clear callback time; otherwise set to 04:00.

10. **Cancellation handling**  
    - If `TOAStatus = 6`, change colour to cancelled background and append cancel remark to remarks.

11. **Insert into `#TmpRGS`**  
    - Populate all columns with the computed values for the current record.

12. **Finalize**  
    - After cursor loop, close and deallocate cursors.

13. **Output**  
    - Select all rows from `#TmpRGS` ordered by `Sno`.  
    - Select a cancel list of TAR/TOA pairs where `TOAStatus` not in (0,5,6).  
    - Return formatted `OperationDate` and `AccessDate`.  
    - Drop temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TOA`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Sector`  
  - `TAMS_OCC_Auth`  
  - `TAMS_Traction_Power_Detail`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_Power_Sector`  
  - `TAMS_TAR_AccessReq`  
  - `TAMS_Access_Requirement`  

* **Writes:**  
  - Temporary tables `#TmpRGS` and `#TmpRGSSectors` (created and dropped within procedure).  

---