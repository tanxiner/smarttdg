# Procedure: sp_TAMS_RGS_OnLoad_20250128

### Purpose
Retrieves and formats a list of active and cancelled TOA requests for a specified line and track type, applying business rules for possession, protection, and cancellation status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Filters records by the railway line (e.g., DTL, NEL). |
| @TrackType | NVARCHAR(50) | Filters records by the track type (e.g., mainline). |

### Logic Flow
1. **Date Determination**  
   - Capture current date and time.  
   - If the time is after 06:00:00, set the operation date to today and the access date to tomorrow; otherwise, set the operation date to yesterday and the access date to today.  
   - Override dates with hard‑coded values for 2024‑08‑01 (operation) and 2024‑08‑30 (access).

2. **Parameter Retrieval**  
   - Query `TAMS_Parameters` three times to obtain background colour codes for possession, protection, and cancellation, keyed by the supplied line.

3. **Possession Control Flag**  
   - Evaluate whether all possession TOAs for the line and track type on the access date have an acknowledgement protection limit time set.  
   - Set a bit flag (`@possession_ctrl`) to 1 if the count of possession TOAs with a set limit equals the total possession TOAs; otherwise 0.

4. **Main Result Set Construction**  
   - Join `TAMS_TAR` and `TAMS_TOA` on TARId.  
   - Apply filters: access date, track type, line, and TOA status not equal to 0.  
   - For each record, compute:  
     - Electrical section count via `TAMS_Get_ES_NoBufferZone`.  
     - Power‑off time, racked‑out time, and circuit‑break‑out time using nested selects that reference `TAMS_OCC_Auth`, `TAMS_Traction_Power_Detail`, and related power‑sector tables.  
     - Parties name via `TAMS_Get_TOA_Parties`.  
     - Call‑back time, radio message time, line‑clear message time, and grant TOA enable flag.  
     - Colour code based on TOA status and access type.  
     - Grant TOA enable flag, updated QTS time, and acknowledgement times.  
     - Decrypted in‑charge NRIC.  
   - Determine whether the TOA is authorised (`IsTOAAuth`) by checking the existence of relevant OCC authorisations for the line and track type.  
   - Order the result set by access type, TOA status descending, and TAR Id.

5. **Cancelled List**  
   - Select TAR Id and TAR number for TOAs whose status is not 0, 5, or 6, matching the same line, track type, and access date.

6. **Date Output**  
   - Return the operation and access dates in dd/mm/yyyy format.

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

* **Writes:** None. The procedure only performs SELECT operations.