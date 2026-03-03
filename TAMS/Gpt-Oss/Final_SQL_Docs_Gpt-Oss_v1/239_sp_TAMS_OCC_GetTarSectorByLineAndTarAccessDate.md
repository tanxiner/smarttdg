# Procedure: sp_TAMS_OCC_GetTarSectorByLineAndTarAccessDate

### Purpose
Retrieve tariff sector details for a specified line (DTL or NEL) and access date.

### Parameters
| Name        | Type          | Purpose |
| :---        | :---          | :--- |
| @Line       | nvarchar(10)  | Line identifier; expected values are DTL or NEL. |
| @AccessDate | nvarchar(50)  | Date string to be converted to datetime for filtering. |

### Logic Flow
1. The procedure checks the value of **@Line**.  
2. **If @Line = 'DTL'**  
   - Joins `tams_tar`, `TAMS_TAR_Sector`, and `TAMS_Traction_Power_Detail`.  
   - Filters on `TARStatusId = 8`, matching `Line` and the converted `AccessDate`.  
   - Returns columns: `s.id, tarid, d.tractionpowerid, s.sectorid, isbuffer, colourcode, isaddedbuffer, t.poweron`.  
   - Orders the result set by `d.tractionpowerid` ascending.  
3. **Else if @Line = 'NEL'**  
   - Joins `tams_tar`, `TAMS_TAR_Power_Sector`, and `TAMS_Power_Sector`.  
   - Filters on `TARStatusId = 9`, matching `Line` and the converted `AccessDate`.  
   - Returns columns: `s.id, tarid, d.PowerSection as tractionpowerid, s.powersectorid as sectorid, isbuffer, '' as colourcode, '' as isaddedbuffer, t.poweron`.  
   - Orders the result set by `s.powersectorid` ascending.  
4. If **@Line** is neither DTL nor NEL, the procedure returns no rows.  
5. Commented sections contain legacy or alternate queries that are not executed.

### Data Interactions
* **Reads:**  
  - `tams_tar`  
  - `TAMS_TAR_Sector`  
  - `TAMS_Traction_Power_Detail`  
  - `TAMS_TAR_Power_Sector`  
  - `TAMS_Power_Sector`  

* **Writes:** None.