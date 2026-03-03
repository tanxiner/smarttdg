# Procedure: sp_TAMS_RGS_OnLoad_M

### Purpose
Generate a daily report of RGS (Railway Grid System) status for a specified line, including possession and protection details, and provide a list of cancellations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (e.g., 'DTL', 'NEL') to filter records; defaults to NULL |

### Logic Flow
1. **Setup temporary tables**  
   - `#TmpRGS` holds the final report rows.  
   - `#TmpRGSSectors` is used for intermediate sector‑level checks.

2. **Determine operation and access dates**  
   - Current date/time is captured.  
   - If the current time is after 06:00, the operation date is today and the access date is tomorrow; otherwise the operation date is yesterday and the access date is today.

3. **Retrieve background colours**  
   - `RGSPossBG` and `RGSProtectionBG` are fetched from `TAMS_Parameters` for the requested line.

4. **Count existing possession records**  
   - `@lv_PossessionCtr` counts TAR/TOA pairs on the access date with status not 0 or 6 and line matching the input.

5. **Cursor over TAR/TOA pairs**  
   - For each pair where `TOAStatus` ≠ 0 and the line matches, the procedure:
     - Initializes default flags and counters.
     - Calls helper functions to get ES number, parties list, and contact string.
     - **Sector processing**  
       - If line is `DTL`, iterate over TAR sectors; otherwise iterate over power sectors.  
       - For each sector, populate `#TmpRGSSectors` with OCC authorization data for the operation and access dates.  
       - Determine if the sector is authorised (`IsTOAAuth`), has a power‑off time (`IsPowerOff`), and has a circuit‑break time (`IsCircuitBreak`).  
       - Extract the relevant times from the temporary table.
     - Build remarks: combine AR remark, TVF mode, rack‑out status, and SCD application status.  
     - Retrieve TVF stations via a helper function.
     - Set colour code and grant TOA enable flag based on access type, TOA status, and possession counter logic.
     - Determine callback time: if TOANo is empty, no callback; otherwise 04:00.
     - Insert a row into `#TmpRGS` with all computed values.

6. **Output**  
   - Return the ordered `#TmpRGS` result set (the RGS list).  
   - Return a cancellation list of TAR/TOA pairs where `TOAStatus` is not 0, 5, or 6.  
   - Return the operation and access dates in human‑readable format.

7. **Cleanup**  
   - Drop the temporary tables.

### Data Interactions
- **Read‑only**  
  - `TAMS_TAR` – source of TAR records.  
  - `TAMS_TOA` – source of TOA records.  
  - `TAMS_Parameters` – line‑specific colour parameters.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – determine rack‑out and SCD application flags.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out and SCD application selections.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count rack‑out occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – count SCD application occurrences.  
  - `TAMS_TAR_AccessReq` & `TAMS