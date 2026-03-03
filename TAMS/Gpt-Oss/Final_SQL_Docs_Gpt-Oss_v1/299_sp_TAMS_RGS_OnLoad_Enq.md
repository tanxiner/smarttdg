# Procedure: sp_TAMS_RGS_OnLoad_Enq

### Purpose
Generate a list of RGS (Railway Gate Service) records for a specified line, track type and operation date, including calculated status, timing, and visual cues for the front‑end display.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target line identifier (e.g., DTL, NEL). |
| @TrackType | NVARCHAR(50) | Track classification (e.g., DEPOT). |
| @OPDate | NVARCHAR(20) | Operation date in dd/mm/yyyy format. |

### Logic Flow
1. **Temporary tables**  
   - `#TmpRGS` holds the final RGS rows.  
   - `#TmpRGSSectors` is created but never used in the current logic.

2. **Date and time setup**  
   - Current date/time captured.  
   - `@CutOff` set to 06:00:00.  
   - If current time is after the cutoff, `@OperationDate` is today and `@AccessDate` is tomorrow; otherwise, `@OperationDate` is yesterday and `@AccessDate` is today.  
   - For DEPOT track type, `@AccessDate` is forced to equal `@OperationDate`.  
   - `@OperationDate` is overridden by the supplied `@OPDate`.

3. **Parameter retrieval**  
   - `@TOACallBackTime`, `@RGSPossBG`, `@RGSProtBG`, `@RGSCancBG` are fetched from `TAMS_Parameters` based on line and track type.

4. **Possession counter**  
   - `@lv_PossessionCtr` counts existing possession records for the line, track type, and access date where TOA status is not 0 or 6.

5. **Main cursor (`@Cur01`)**  
   - Iterates over all TAR/TOA pairs for the line, track type, and access date where TOA status is not 0.  
   - For each record, local variables are initialized and populated:
     - **Electrical section** via `dbo.TAMS_Get_ES_NoBufferZone`.  
     - **Parties name** via `dbo.TAMS_Get_TOA_Parties`.  
     - **Contact number** concatenates mobile and radio numbers.

6. **Power and rack‑out logic**  
   - **DTL line**:  
     - Checks OCCAuth entries for the operation and access dates.  
     - Determines if TOA is authorized (`@lv_IsTOAAuth`) based on OCCAuth status and buffer flag.  
     - Retrieves power‑off and rack‑out times if all sectors have completed the respective actions.  
   - **NEL line**:  
     - Similar checks but against power sections instead of traction power sectors.  
     - Determines TOA authorization and action times accordingly.

7. **Remarks construction**  
   - For DTL, remarks combine AR remark and TVF mode.  
   - For NEL, remarks may include “Rack Out” if a rack‑out requirement exists, otherwise just AR remark and TVF mode.  
   - Adds SCD application remark if applicable.  
   - Appends TVF stations list from `dbo.TAMS_Get_TOA_TVF_Stations`.  
   - If no remarks exist, defaults to the TVF stations list.

8. **Colour code and TOA enable logic**  
   - **DTL**:  
     - Possession records receive `@RGSPossBG`; others receive `@RGSProtBG`.  
     - Possession counter is adjusted based on TOA status and protection time limit.  
     - Grant TOA enable flag is set according to possession priority rules.  
   - **NEL**:  
     - Colour code set based on possession or protection.  
     - Grant TOA enable flag is always true.  
   - **Cancelled records (TOA status 6)**:  
     - Colour code set to `@RGSCancBG`.  
     - Cancel remark appended to remarks.

9. **Insert into `#TmpRGS`**  
   - All calculated fields are inserted, including callback time formatting for DEPOT tracks.

10. **Result set**  
    - The procedure returns the ordered list from `#TmpRGS`.  
    - It also returns the formatted operation and access dates.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TOA`  
  - `TAMS_OCC_Auth`  
  - `TAMS_Traction_Power_Detail`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Sector`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_TAR_AccessReq`  
  - `TAMS_Access_Requirement`  
  - `TAMS_TAR_Sector` (via join)  
  - `TAMS_TAR` (for possession count)  

* **Writes:**  
  - Temporary tables `#TmpRGS` and `#TmpRGSSectors` (created and dropped within the procedure).  

No permanent tables are modified.