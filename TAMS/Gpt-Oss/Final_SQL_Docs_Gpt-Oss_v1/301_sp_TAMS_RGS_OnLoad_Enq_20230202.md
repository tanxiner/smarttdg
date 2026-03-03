# Procedure: sp_TAMS_RGS_OnLoad_Enq_20230202

### Purpose
Generate a detailed RGS (Railway Grid System) report for a specified line and operation date, including possession and protection status, electrical sector details, and TOA (Track Occupancy Authorization) information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target railway line identifier (e.g., DTL, NEL). |
| @OPDate | NVARCHAR(20) | Operation date in dd/mm/yyyy format; used to calculate access and operation dates. |

### Logic Flow
1. **Setup temporary tables**  
   - `#TmpRGS` holds the final report rows.  
   - `#TmpRGSSectors` is used for intermediate sector‑level calculations.

2. **Determine operation and access dates**  
   - If current time is after 06:00, operation date is today and access date is tomorrow; otherwise operation date is yesterday and access date is today.  
   - Override these dates with the supplied `@OPDate` (converted to date) and set access date to the next day.

3. **Load configuration parameters**  
   - Retrieve callback time, possession background colour, and protection background colour for the line from `TAMS_Parameters`.

4. **Count existing possession records**  
   - Count TAR records with possession access type that are not cancelled for the access date and line; used later to adjust possession counters.

5. **Iterate over TAR/TOA pairs**  
   - Cursor `@Cur01` selects all TAR–TOA combinations for the access date and line where TOA status is not zero.  
   - For each pair:
     - Initialise flags and counters.
     - Retrieve electrical sector string via `dbo.TAMS_Get_ES`.
     - Retrieve TOA parties string via `dbo.TAMS_Get_TOA_Parties`.
     - Build contact string from mobile and radio numbers.

6. **Sector‑level processing**  
   - If line is DTL, loop over sector IDs from `TAMS_TAR_Sector`; otherwise loop over power sector IDs from `TAMS_TAR_Power_Sector`.  
   - For each sector:
     - **Authorization check** – insert into `#TmpRGSSectors` rows where OCCAuthStatusId is 10 (or 7 with buffer) and `IsBuffer` is 0; if none, mark TOA as not authorised.  
     - **Power‑off time** – insert rows where `PowerOffTime` is not null; if none, clear power‑off flag and time.  
     - **Circuit‑break time** – insert rows where `RackedOutTime` is not null; if none, clear circuit‑break flag and time.  
     - The first non‑null time found for each category is stored for the report.

7. **Build remarks and colour code**  
   - For DTL, remarks combine AR remark and TVF mode.  
   - For NEL, if a rack‑out requirement exists, prepend “Rack Out” to remarks; otherwise omit circuit‑break time.  
   - Append TVF station list from `dbo.TAMS_Get_TOA_TVF_Stations`.  
   - Set colour code to possession or protection background based on access type.  
   - Adjust possession counter and grant TOA enable flag according to TOA status and protection limits.

8. **Insert row into `#TmpRGS`**  
   - Populate all columns, including calculated times, flags, and identifiers.

9. **Finalize**  
   - After cursor completion, output the ordered report from `#TmpRGS`.  
   - Return operation and access dates in dd.mm.yyyy format.  
   - Drop temporary tables.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters` (for callback, possession, protection colours)  
  - `TAMS_TAR` and `TAMS_TOA` (for TAR/TOA data)  
  - `TAMS_TAR_Sector`, `TAMS_Sector`, `TAMS_OCC_Auth`, `TAMS_Traction_Power_Detail` (for DTL sector logic)  
  - `TAMS_TAR_Power_Sector`, `TAMS_Power_Sector` (for NEL power‑sector logic)  
  - `TAMS_TAR_AccessReq`, `TAMS_Access_Requirement` (for rack‑out check)  
  - `TAMS_Access_Requirement` (for requirement ID 27)  

* **Writes:**  
  - Temporary tables `#TmpRGS` and `#TmpRGSSectors` (no permanent data is modified)  

* **Functions called:**  
  - `dbo.TAMS_Get_ES`  
  - `dbo.TAMS_Get_TOA_Parties`  
  - `dbo.TAMS_Get_TOA_TVF_Stations`  
  - `dbo.TAMS_Get_TOA_TVF_Stations` (again for remarks)  

No permanent tables are updated or deleted by this procedure.