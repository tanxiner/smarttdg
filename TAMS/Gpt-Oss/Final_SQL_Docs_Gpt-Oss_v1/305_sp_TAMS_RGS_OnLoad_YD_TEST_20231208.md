# Procedure: sp_TAMS_RGS_OnLoad_YD_TEST_20231208

### Purpose
Generate a daily RGS (Railway Gate Service) report for a specified line and track type, applying possession and protection logic, and return the list of RGS entries along with any cancelled records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line identifier (default 'NEL') |
| @TrackType | NVARCHAR(50) | Track type (default 'mainline') |

### Logic Flow
1. **Setup temporary structures** – two temp tables are created to hold RGS data and sector details.  
2. **Determine dates** – the current date and time are captured. A cutoff time of 06:00 is used to decide whether the operation date is today or yesterday, and the access date is the following day. The dates are then hard‑coded to 2023‑12‑06 and 2023‑12‑07 for testing.  
3. **Load background colours** – three parameters (RGSPossessionBG, RGSProtectionBG, RGSCancelledBG) are fetched from TAMS_Parameters for the selected line.  
4. **Count existing possession records** – a counter is set by counting TAR/TOA pairs that are not cancelled and have a possession access type for the access date.  
5. **Cursor over TAR/TOA pairs** – a cursor iterates through all TAR/TOA records for the access date, line, and track type where the TOA status is not zero.  
   * For each pair:  
     * Initialise all output variables.  
     * Retrieve the ES number, parties list, and contact details via helper functions.  
     * **Line‑specific logic**  
       * **DTL** – evaluate OCC authorisations, power‑off, and circuit‑break times based on traction power details and sector relationships.  
       * **NEL** – perform similar checks but using power‑section relationships instead of sectors.  
     * Build remarks, colour code, and grant TOA enable flags based on possession status, TOA status, and protection limits.  
     * Adjust callback time if a TOA number exists.  
     * If the TOA status indicates cancellation, override colour and append cancel remarks.  
     * Insert the assembled record into the #TmpRGS table.  
6. **Return results** –  
   * The populated #TmpRGS table is selected and ordered by the sequence number.  
   * A separate list of cancelled TAR/TOA pairs (status not in 0,5,6) is returned.  
   * The operation and access dates are output as formatted strings.  
7. **Cleanup** – temporary tables are dropped.

### Data Interactions
* **Reads**  
  * TAMS_Parameters – for background colour codes.  
  * TAMS_TAR – for TAR details, access date, line, track type, and possession status.  
  * TAMS_TOA – for TOA details, status, times, and related IDs.  
  * TAMS_OCC_Auth – for OCC authorisation checks.  
  * TAMS_Traction_Power_Detail – for power‑off and circuit‑break information.  
  * TAMS_TAR_Sector – for sector relationships.  
  * TAMS_Sector – for sector gap and buffer flags.  
  * TAMS_TAR_AccessReq & TAMS_Access_Requirement – for power and SCD application checks.  
  * TAMS_TAR_Power_Sector – for power‑section relationships.  
  * Helper functions: dbo.TAMS_Get_ES_NoBufferZone, dbo.TAMS_Get_TOA_Parties, dbo.DecryptString, dbo.TAMS_Get_TOA_TVF_Stations.  

* **Writes**  
  * #TmpRGS – temporary table that holds the final RGS report rows.  
  * #TmpRGSSectors – temporary table used only for sector data (not populated in the current logic).  

No permanent tables are modified; all updates occur in temporary tables that are dropped at procedure completion.