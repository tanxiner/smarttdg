# Procedure: sp_TAMS_RGS_OnLoad

### Purpose
Retrieve and format all RGS (Railway Guard Service) records for a specified line and track type, including status, timing, and visual cues for the current operational day.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Target railway line (e.g., 'DTL', 'NEL') |
| @TrackType | NVARCHAR(50) | Target track type (e.g., 'mainline', 'branch') |

### Logic Flow
1. **Initialisation**  
   - Create a line break string `<br />`.  
   - Declare variables for background colours, callback time, and control flags.  
   - Capture current date and time; set a 6 AM cut‑off to decide whether the operation day is today or tomorrow.  
   - Determine `@OperationDate` (the day for which TOAs are authorised) and `@AccessDate` (the day for which TARs are accessed) based on the cut‑off.

2. **Retrieve Background Colours**  
   - Query `TAMS_Parameters` three times to obtain background colours for possession, protection, and cancelled states for the supplied line.

3. **Set TOA Callback Time**  
   - Hard‑code a 4 AM callback time for TOAs that are not yet cancelled.

4. **Possession Control Flag**  
   - Evaluate whether all possession TOAs for the line and track type on the access date have an acknowledgement protection limit time set.  
   - If every possession TOA has this time, set `@possession_ctrl` to 1; otherwise 0.

5. **Main Data Retrieval**  
   - Join `TAMS_TAR` and `TAMS_TOA` on `TARId`.  
   - Filter by access date, track type, line, and non‑zero TOA status.  
   - For each record, compute:
     - Row number for ordering.  
     - Electrical sections via `TAMS_Get_ES_NoBufferZone`.  
     - Power‑off time, racked‑out time, and circuit‑break‑out time using sub‑queries that reference `TAMS_OCC_Auth`, `TAMS_Traction_Power_Detail`, and related power‑sector tables.  
     - Parties’ names, number of persons, work description, and contact details.  
     - Callback time, radio message time, line‑clear message time, and TOA status.  
     - Comments via `SP_TAMS_RGS_Comments`.  
     - A flag indicating whether the TOA is authorised (`IsTOAAuth`) based on existence of relevant OCC authorisations.  
     - Colour code derived from TOA status and access type.  
     - A flag enabling the grant TOA button (`IsGrantTOAEnable`).  
     - Update time, acknowledgement times, and decrypted in‑charge NRIC.  
   - Order the result set by access type, TOA status, acknowledgement and grant times, and TAR ID.

6. **Cancel List Retrieval**  
   - Select TAR IDs and numbers for all records whose TOA status is not 0, 5, or 6 (i.e., active or pending) for the same line, track type, and access date.

7. **Return Dates**  
   - Output the formatted operation and access dates for reference.

### Data Interactions
* **Reads:**  
  - `TAMS_Parameters`  
  - `TAMS_TAR`  
  - `TAMS_TOA`  
  - `TAMS_OCC_Auth`  
  - `TAMS_Traction_Power_Detail`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Sector`  
  - `TAMS_TAR_AccessReq`  
  - `TAMS_Access_Requirement`  

* **Writes:**  
  - None

---