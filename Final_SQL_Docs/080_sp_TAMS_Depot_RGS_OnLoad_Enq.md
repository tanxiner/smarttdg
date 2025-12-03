# Procedure: sp_TAMS_Depot_RGS_OnLoad_Enq

### Purpose
Retrieves a detailed list of depot RGS (Railway Guard Service) access requests for a specified line and access date, including calculated status, timing, and visual cues for the front‑end display.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The depot line identifier to filter TAR records. |
| @TrackType | NVARCHAR(50) | Unused in the current logic; reserved for future filtering. |
| @accessDate | DATE | The date of the access request to retrieve records for. |

### Logic Flow
1. **Initialisation**  
   - Set a line‑break string `@NewLine` for formatting contact numbers.  
   - Declare variables for background colours (`@RGSPossBG`, `@RGSProtBG`, `@RGSCancBG`) and a callback time placeholder (`@TOACallBackTime`).  
   - Capture the current date and time into `@CurDate` and `@CurTime`.  
   - Define a cut‑off time of 06:00:00, though it is not used further.  
   - Assign `@OperationDate` to the current date (previous day logic is commented out).  

2. **Retrieve Colour Codes**  
   - Query `TAMS_Parameters` three times to obtain the background colour values for possession, protection, and cancelled states, keyed by the supplied `@Line`.  

3. **Main Data Retrieval**  
   - Perform a SELECT that joins `TAMS_TAR` (access request) with `TAMS_TOA` (transport order) on matching `TARId`.  
   - Filter rows where:  
     * `AccessDate` equals `@accessDate`.  
     * `TrackType` is 'DEPOT'.  
     * `TOAStatus` is not 0.  
     * `Line` equals `@Line`.  
   - For each row, compute:  
     * A sequential number (`Sno`).  
     * Electrical sections via `TAMS_Get_ES_NoBufferZone`.  
     * `PowerOffTime` – if the line is NEL and the power is on with possession access, leave blank; otherwise, fetch the latest `PowerOffTiming` from `TAMS_Depot_Auth_Powerzone` where the type is 'Completed'.  
     * `CircuitBreakOutTime` – the latest `RackedOutTiming` for the TAR where the access requirement ID 48 is selected and completed.  
     * Parties name and count via `TAMS_Get_TOA_Parties`.  
     * Contact information concatenated with a line break.  
     * Various timestamps (TOA callback, radio message, line clear, grant TOA, acknowledgement times) formatted as strings.  
     * `Remarks` from `SP_TAMS_RGS_Comments`.  
     * `IsTOAAuth` – a bit flag set if any depot auth record for the TAR has a status ≥ 8.  
     * `ColourCode` – chosen from the retrieved colour variables based on `TOAStatus` and `AccessType`.  
     * `IsGrantTOAEnable` – always set to true.  
     * Decrypted in‑charge NRIC.  
   - Order the result set by `AccessType` and `TARNo`.  

4. **Return Access Date**  
   - After the main result set, output a single row containing the formatted `@AccessDate`.  

### Data Interactions
* **Reads:**  
  - TAMS_Parameters  
  - TAMS_Depot_Auth  
  - TAMS_Depot_Auth_Powerzone  
  - TAMS_TAR_AccessReq  
  - TAMS_Access_Requirement  
  - TAMS_TAR  
  - TAMS_TOA  

* **Writes:**  
  - None (the procedure performs only SELECT operations).