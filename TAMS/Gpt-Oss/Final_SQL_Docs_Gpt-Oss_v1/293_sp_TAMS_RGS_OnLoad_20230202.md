# Procedure: sp_TAMS_RGS_OnLoad_20230202

### Purpose
Generate a daily report of RGS (Railway Grid Services) activities for a specified line, including possession and protection status, and provide a list of cancellations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Optional line identifier (e.g., 'DTL', 'NEL'); if omitted, all lines are processed |

### Logic Flow
1. **Setup temporary tables**  
   Two temp tables are created: `#TmpRGS` for the final report rows and `#TmpRGSSectors` for intermediate sector data.

2. **Determine operation and access dates**  
   Current date and time are captured.  
   If the current time is after 06:00, the operation date is today and the access date is tomorrow; otherwise the operation date is yesterday and the access date is today.  
   These dates are used to filter TAR (Task Action Request) records.

3. **Retrieve background colours**  
   Parameters `RGSPossessionBG` and `RGSProtectionBG` are read from `TAMS_Parameters` for the requested line.

4. **Count existing possession records**  
   A count of TAR/TOA pairs with status not 0 or 6, line matching, access type 'Possession', and matching access date is stored in `@lv_PossessionCtr`.

5. **Cursor over TAR/TOA pairs**  
   A cursor (`@Cur01`) iterates over all TAR/TOA pairs for the access date and line where TOA status is not 0.  
   For each pair:
   - Increment a serial number (`@lv_Sno`).
   - Initialise flags and placeholders for TOA authentication, power‑off, circuit‑break, colour, remarks, etc.
   - Retrieve the ES number via `dbo.TAMS_Get_ES_NoBufferZone`.
   - Retrieve parties list via `dbo.TAMS_Get_TOA_Parties`.
   - Build a contact string from mobile and radio numbers.

6. **Sector processing**  
   Depending on the line:
   - **DTL**:  
     - Cursor over sectors linked to the TAR (`TAMS_TAR_Sector`).  
     - For each sector, three queries populate `#TmpRGSSectors` to determine:  
       * Whether the sector is authorised (OCCAuthStatusId 10 or 7 with buffer).  
       * Whether power is off (PowerOffTime).  
       * Whether a circuit break has occurred (RackedOutTime).  
     - Flags and times are set based on the presence of rows in `#TmpRGSSectors`.
   - **Other lines**:  
     - Cursor over power sectors linked to the TAR (`TAMS_TAR_Power_Sector`).  
     - Similar three queries are executed, but the authorised status requires OCCAuthStatusId 8.  
     - Flags and times are set accordingly.

7. **Build remarks**  
   - For DTL, remarks consist of the trimmed ARRemark and TVFMode.  
   - For other lines, the presence of a rack‑out requirement (ID 27) adds a 'Rack Out' line.  
   - If an SCD application requirement is selected, a leading 'SCD' line is added.  
   - The TVF station list from `dbo.TAMS_Get_TOA_TVF_Stations` is appended; if remarks are still empty, the TVF list becomes the remarks.

8. **Colour and grant logic**  
   - If the access type is 'Possession':  
     * Colour is set to possession background.  
     * Grant TOA enable flag is set to 1.  
     * Possession counter is adjusted based on TOA status and protection time limit.  
   - If the access type is not 'Possession':  
     * Colour is set to protection background.  
     * Grant TOA enable flag is set to 1 if status is 6 or if no possession counter remains; otherwise it is set to 0.

9. **Callback time**  
   If a TOANo exists, a fixed callback time of 04:00 is used; otherwise the callback time is blank.

10. **Insert into `#TmpRGS`**  
    All computed values for the current TAR/TOA pair are inserted as a new row.

11. **After cursor completion**  
    - The cursor is closed and deallocated.
    - The final report is selected from `#TmpRGS`, ordered by the serial number.
    - A cancellation list is produced by selecting TAR/TOA pairs whose TOA status is not 0, 5, or 6.
    - The operation and access dates are returned as formatted strings.
    - Temporary tables are dropped.

### Data Interactions
- **Read**  
  - `TAMS_Parameters` (for background colours)  
  - `TAMS_TAR` (TAR records)  
  - `TAMS_TOA` (TOA records)  
  - `TAMS_TAR_Sector` (sector links for DTL)  
  - `TAMS_TAR_Power_Sector` (power sector links for other lines)  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` (to detect rack‑out and SCD application requirements)  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` (to detect power‑related access requirements)  

- **Write**  
  - `#TmpRGS` (temporary report rows)  
  - `#TmpRGSSectors` (temporary sector status rows)  

- **Functions called**  
  - `dbo.TAMS_Get_ES_NoBufferZone`  
  - `dbo.TAMS_Get_TOA_Parties`  
  - `dbo.TAMS_Get_TOA_TVF_Stations`  

The procedure outputs three result sets: the RGS list, the cancel list, and the operation/access dates.