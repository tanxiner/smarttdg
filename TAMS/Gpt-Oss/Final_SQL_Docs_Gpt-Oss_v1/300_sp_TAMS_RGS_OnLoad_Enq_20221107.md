# Procedure: sp_TAMS_RGS_OnLoad_Enq_20221107

### Purpose
Generate a line‑specific RGS enquiry list for a specified operation date, including TAR and TOA details, status flags, timing information, and calculated fields such as possession counters and grant TOA enablement.

### Parameters
| Name   | Type          | Purpose |
| :----- | :------------ | :------ |
| @Line  | NVARCHAR(20)  | Target line identifier (e.g., 'DTL' or 'NEL'). |
| @OPDate| NVARCHAR(20)  | Operation date in DD/MM/YYYY format; if NULL, current date is used. |

### Logic Flow
1. **Temp Table Setup**  
   - Create `#TmpRGS` for the final result set.  
   - Create `#TmpRGSSectors` for intermediate sector‑level data.  
   - Truncate both tables (they are new each run).

2. **Date Determination**  
   - Capture current date/time.  
   - Define a 06:00:00 cutoff.  
   - If current time is after the cutoff, set `@OperationDate` to today and `@AccessDate` to tomorrow; otherwise set `@OperationDate` to yesterday and `@AccessDate` to today.  
   - Override both dates with `@OPDate` if supplied.

3. **Parameter Retrieval**  
   - From `TAMS_Parameters` fetch:  
     * `@TOACallBackTime` (callback time for TOA).  
     * `@RGSPossBG` (colour code for possession).  
     * `@RGSProtBG` (colour code for protection).  

4. **Possession Counter**  
   - Count existing possession records for the line on `@AccessDate` where `TOAStatus` is not 0 or 6; store in `@lv_PossessionCtr`.

5. **Cursor @Cur01 – TAR/TOA Loop**  
   - Open a cursor over `TAMS_TAR` joined to `TAMS_TOA` for the line and `@AccessDate`, excluding `TOAStatus` 0.  
   - For each record:  
     a. Initialize local variables (Sno, flags, times, remarks).  
     b. Retrieve electrical sector string via `dbo.TAMS_Get_ES(@TARID)`.  
     c. Retrieve parties name via `dbo.TAMS_Get_TOA_Parties(@TOAID)`.  
     d. Build `@lv_ContactNo` from mobile and radio numbers.  

6. **Sector Processing (Cursor @Cur02)**  
   - **DTL line**:  
     * Cursor over sectors linked to the TAR (`TAMS_TAR_Sector`) that are not gaps or buffers.  
     * For each sector:  
       - Insert OCCAuth records for the sector and operation/access dates where status is 10 (or buffer 7).  
       - If none, set `@lv_IsTOAAuth` to 0.  
       - Insert power‑off times; if none, set `@lv_IsPowerOff` to 0.  
       - Insert racked‑out times; if none, set `@lv_IsCircuitBreak` to 0.  
   - **NEL line**:  
     * Cursor over power sectors linked to the TAR (`TAMS_TAR_Power_Sector`) that are not buffers.  
     * For each sector: perform the same three inserts as above, but filter OCCAuth status 7 and use power‑sector tables.  

7. **Remarks & Colour Code**  
   - For DTL: concatenate `ARRemark` and `TVFMode`.  
   - For NEL: if a rack‑out requirement exists, prepend “Rack Out” to remarks; otherwise omit racked‑out time.  
   - Retrieve TVF stations via `dbo.TAMS_Get_TOA_TVF_Stations(@TOAID)` and append to remarks.  
   - Set `@lv_ColourCode` to `@RGSPossBG` for possession access, otherwise to `@RGSProtBG`.  

8. **Possession Counter & Grant TOA Enable**  
   - If access type is possession:  
     * Adjust `@lv_PossessionCtr` based on `TOAStatus` and `ProtTimeLimit`.  
     * Set `@lv_IsGrantTOAEnable` to 1.  
   - If access type is not possession:  
     * Set `@lv_IsGrantTOAEnable` to 1 unless a possession counter remains >0 and `TOAStatus` ≠ 6.  

9. **Insert into #TmpRGS**  
   - Populate all columns (Sno, TARNo, ElectricalSections, times, parties, contact, TOANo, callback, radio, line clear, remarks, status, flags, colour, grant flag, QTS time, access type, ack times, limits, IDs, in‑charge NRIC).  
   - Use `@TOACallBackTime` for callback only when a TOANo exists.

10. **Finalize**  
    - Close and deallocate `@Cur01`.  
    - Return the ordered result set from `#TmpRGS`.  
    - Return formatted `OperationDate` and `AccessDate` (MM/DD/YYYY).  
    - Drop the temporary tables.

### Data Interactions
**Reads**
- `TAMS_TAR` – TAR records for the specified line and access date.  
- `TAMS_TOA` – TOA records linked to TARs, filtered by status.  
- `TAMS_Parameters` – line‑specific configuration values.  
- `TAMS_TAR_Sector` – sector links for DTL TARs.  
- `TAMS_Sector` – sector details for DTL.  
- `TAMS_OCC_Auth` – OCC authorization records for sectors or power sectors.  
- `TAMS_Traction_Power_Detail` – power‑off and racked‑out timestamps.  
- `TAMS_TAR_Power_Sector` – power‑sector links for NEL TARs.  
- `TAMS_Power_Sector` – power‑sector details for NEL.  
- `TAMS_TAR_AccessReq` & `TAMS_Access_Requirement` – rack‑out requirement checks for NEL.  
- `TAMS_Access_Requirement` – requirement definitions.  

**Functions Used**
- `dbo.TAMS_Get_ES(@TARID)` – returns electrical sector string.  
- `dbo.TAMS_Get_TOA_Parties(@TOAID)` – returns parties name string.  
- `dbo.TAMS_Get_TOA_TVF_Stations(@TOAID)` – returns TVF station list.  

**Writes**
- Only to the temporary tables `#TmpRGS` and `#TmpRGSSectors`; no permanent tables are modified.