# Procedure: sp_TAMS_RGS_OnLoad_20221118_M

### Purpose
Generate a daily RGS (Request for Grid Service) report for a specified line, including possession and protection details, and provide a list of cancellations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., 'DTL' or 'NEL') to filter data; defaults to NULL |

### Logic Flow
1. **Setup temporary tables**  
   - `#TmpRGS` holds the final report rows.  
   - `#TmpRGSSectors` is used for intermediate sector‑level calculations.

2. **Determine operation and access dates**  
   - Current date/time is captured.  
   - If the current time is after 06:00, the operation date is today and the access date is tomorrow; otherwise the operation date is yesterday and the access date is today.  
   - These dates are later overridden to fixed values for debugging (`2022‑11‑17` / `2022‑11‑18`).

3. **Retrieve background colours**  
   - `RGSPossessionBG` and `RGSProtectionBG` are fetched from `TAMS_Parameters` for the given line.

4. **Count active possessions**  
   - `@lv_PossessionCtr` counts TAR/TOA pairs where the TOA status is not 0 or 6, the line matches, the access type is ‘Possession’, and the access date matches the calculated access date.

5. **Cursor over TAR/TOA pairs**  
   - A cursor (`@Cur01`) iterates over all TAR/TOA records for the access date and line where the TOA status is not 0.  
   - For each pair, variables are initialized and helper functions retrieve:
     - Electrical sector list (`dbo.TAMS_Get_ES_NoBufferZone`).
     - TOA parties (`dbo.TAMS_Get_TOA_Parties`).
     - Contact string (mobile + radio).

6. **Sector‑level processing**  
   - If the line is `DTL`, sectors are obtained from `TAMS_TAR_Sector`; otherwise from `TAMS_TAR_Power_Sector`.  
   - For each sector, three queries populate `#TmpRGSSectors` to determine:
     - Whether the sector is authorised (`OCCAuthStatusId` 10 or 7 with buffer).  
     - Whether power is off (`PowerOffTime` present).  
     - Whether a circuit break is recorded (`RackedOutTime` present).  
   - Flags and times (`@lv_IsTOAAuth`, `@lv_PowerOffTime`, `@lv_CircuitBreakTime`) are set based on the presence of rows.

7. **Build remarks**  
   - For `DTL`, remarks combine the AR remark and TVF mode.  
   - For other lines, remarks may include “Rack Out” if a power rack‑out requirement exists, and “SCD” if an SCD application requirement exists.  
   - TVF stations are appended to the remarks.

8. **Colour and TOA enable logic**  
   - If the access type is ‘Possession’, the colour is set to the possession background; otherwise to the protection background.  
   - The `@lv_IsGrantTOAEnable` flag is set based on TOA status, possession counter, and protection time limits.  
   - The possession counter is adjusted according to TOA status and protection limits.

9. **Callback time**  
   - If a TOA number exists, the callback time is set to 04:00; otherwise it is blank.

10. **Insert into `#TmpRGS`**  
    - All calculated fields are inserted as a new row.

11. **After cursor loop**  
    - The cursor is closed and deallocated.

12. **Return report data**  
    - The final RGS list is selected from `#TmpRGS`, ordered by the row number.  
    - A cancellation list is produced by selecting TAR/TOA pairs whose TOA status is not 0, 5, or 6 for the access date and line.  
    - The operation and access dates are returned as formatted strings.

12. **Cleanup**  
    - Temporary tables are dropped.

### Data Interactions
- **Read‑only tables**  
  - `TAMS_TAR` – holds TAR records.  
  - `TAMS_TOA` – holds TOA records linked to TARs.  
  - `TAMS_Access_Requirement` – used to identify rack‑out and SCD application requirements.  
  - `TAMS_TAR_AccessReq` – provides requirement selections for a TAR.  
  - `TAMS_Parameters` – supplies background colour values.  
  - `TAMS_TAR_Sector` – sector list for DTL.  
  - `TAMS_TAR_Power_Sector` – sector list for other lines.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – used for counting rack‑out and SCD requirements.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – used for counting possession requirements.  

- **Temporary tables**  
  - `#TmpRGS` – final report rows.  
  - `#TmpRGSSectors` – intermediate sector calculations.  

- **Functions called**  
  - `dbo.TAMS_Get_ES_NoBufferZone` – electrical sector list.  
  - `dbo.TAMS_Get_TOA_Parties` – parties list.  
  - `dbo.TAMS_Get_TOA_TVF_Stations` – TVF station list.  
  - `dbo.TAMS_Get_TOA_TVF_Stations` – TVF station list.  

The procedure outputs three result sets: the RGS report, the cancellation list, and the operation/access dates. All data is derived from the tables listed above and temporary structures.