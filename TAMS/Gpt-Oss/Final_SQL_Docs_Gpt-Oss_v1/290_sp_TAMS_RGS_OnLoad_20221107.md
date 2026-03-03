# Procedure: sp_TAMS_RGS_OnLoad_20221107

### Purpose
Generate a list of RGS records for a specified line, including status flags, times, and remarks, and provide a cancel list and operation/access dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., DTL or NEL) used to filter records and fetch line‑specific parameters. |

### Logic Flow
1. **Temp tables**  
   Create `#TmpRGS` for the final RGS list and `#TmpRGSSectors` for intermediate sector data.

2. **Date calculation**  
   - Get current date/time.  
   - If current time is after 06:00, set `@OperationDate` to today and `@AccessDate` to tomorrow; otherwise set `@OperationDate` to yesterday and `@AccessDate` to today.

3. **Parameter lookup**  
   Retrieve `RGSPossessionBG` and `RGSProtectionBG` values for the line from `TAMS_Parameters`.

4. **Possession counter**  
   Count existing possession records for the line on `@AccessDate` where `TOAStatus` is not 0 or 6; store in `@lv_PossessionCtr`.

5. **Cursor over TAR/TOA**  
   Open a cursor (`@Cur01`) selecting TAR and TOA rows for the line and `@AccessDate` where `TOAStatus` ≠ 0, ordered by `AccessType`, `TOAStatus` descending, and `Id`.

6. **Process each row**  
   For each fetched record:
   - Initialize variables and counters.  
   - Retrieve ES number (`dbo.TAMS_Get_ES_NoBufferZone`) and parties name (`dbo.TAMS_Get_TOA_Parties`).  
   - Build contact string from mobile and radio numbers.  
   - **Sector handling**  
     *If line is DTL*: iterate over sectors linked to the TAR via `TAMS_TAR_Sector`.  
     *If line is NEL*: iterate over power sectors linked via `TAMS_TAR_Power_Sector`.  
     For each sector:  
     - Check OCCAuth records to set `IsTOAAuth`.  
     - Check for `PowerOffTime` to set `IsPowerOff` and `PowerOffTime`.  
     - Check for `RackedOutTime` to set `IsCircuitBreak` and `CircuitBreakTime`.  
   - **Remarks**  
     *DTL*: concatenate `ARRemark` and `TVFMode`.  
     *NEL*: if a rack‑out requirement exists, prepend “Rack Out”; otherwise use the same concatenation.  
   - Append TVF stations (`dbo.TAMS_Get_TOA_TVF_Stations`) to remarks.  
   - Determine colour code and grant TOA enable flag based on `AccessType`, `TOAStatus`, possession counter, and protection time limit.  
   - If `TOANo` is empty, clear `TOACallBackTime`.  
   - Insert the assembled row into `#TmpRGS`.

7. **Finalize**  
   Close and deallocate the cursor.

8. **Output result sets**  
   - **RGS List**: select all rows from `#TmpRGS` ordered by `Sno`.  
   - **Cancel List**: select TAR records where `TOAStatus` is not 0, 5, or 6 for the line and `@AccessDate`.  
   - **Dates**: return formatted `OperationDate` and `AccessDate`.

9. **Cleanup**  
   Drop the temporary tables.

### Data Interactions
* **Reads**  
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
  - Functions: `dbo.DecryptString`, `dbo.TAMS_Get_ES_NoBufferZone`, `dbo.TAMS_Get_TOA_Parties`, `dbo.TAMS_Get_TOA_TVF_Stations`

* **Writes**  
  - Temporary tables `#TmpRGS` and `#TmpRGSSectors` (created and dropped within the procedure)