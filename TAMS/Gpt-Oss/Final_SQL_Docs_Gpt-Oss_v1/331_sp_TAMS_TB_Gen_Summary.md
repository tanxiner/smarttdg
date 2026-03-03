# Procedure: sp_TAMS_TB_Gen_Summary

### Purpose
Generate a series of summary reports for TAR records filtered by line, track type, date range and access type, returning multiple result sets.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line identifier (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Track type filter |
| @AccessDateFrom | NVARCHAR(20) | Start of access date range |
| @AccessDateTo | NVARCHAR(20) | End of access date range |
| @AccessType | NVARCHAR(20) | Access type filter (optional) |

### Logic Flow
1. **Line Check** – The procedure branches on the value of @Line.  
   * If `@Line = 'DTL'` it executes a sequence of ten SELECT statements (0‑9).  
   * If `@Line = 'NEL'` it executes a sequence of six SELECT statements (0‑5).

2. **DTL Branch** – Each SELECT in the DTL branch returns the same column set: Access Date, TAR ID, Electrical Section, Nature of Work, and Remarks.  
   * **0 & 1** – Join `TAMS_TAR`, `TAMS_TAR_AccessReq`, and `TAMS_Access_Requirement` to filter on specific `OperationRequirement` values:  
     * 0: `Power Off With Rack Out / 22KV Isolation`  
     * 1: `Use of Tunnel Ventilation`  
   * **2‑4** – Filter `TAMS_TAR` by `Company` patterns:  
     * 2: `%DTL SIG%`  
     * 3: `%DTL POWER%`  
     * 4: `UPPER(a.Company) LIKE '%DTL SYSTEMS%'` (also includes a commented out `%DTL COMMS%`)  
   * **5** – Same as 4 but uses `dbo.TAMS_Get_Station` to return Access Stations instead of Electrical Section.  
   * **6** – Filter by multiple `Company` patterns related to Permanent Way & Civil Structure, Facilities Management, etc.  
   * **7** – Filter by `Company LIKE '%DTL RS%'`.  
   * **8** – Filter by `Company` patterns for Operations, Training, or OPS.  
   * **9** – Exclude companies listed in `TAMS_Parameters` where `ParaType = 'S'`, `ParaCode = 'Company'`, and `ParaValue1 = a.Line`.  

   All DTL queries apply the same date range, `TARStatusId = 8`, optional `AccessType` match, and `TrackType` filter. Results are ordered by Access Date and TAR No.

3. **NEL Branch** – Each SELECT in the NEL branch returns a different column set tailored to the operation type.  
   * **0** – Join on `TAMS_TAR_AccessReq` and `TAMS_Access_Requirement` for `Power Off With Rack Out / 22KV Isolation`. Columns include Date, TAR ID, Power Section, From/To times, and Activities.  
   * **1** – Filter `TAMS_TAR` where `Is13ASocket = 1`. Columns include Date, Time From/To, TAR ID, Location From/To, and Activities.  
   * **2** – Join on `TAMS_TAR_AccessReq` and `TAMS_Access_Requirement` for `Use of Tunnel Ventilation`. Columns include TAR ID, Company, Activities, TVF Request, Direction, Date/Time ranges.  
   * **3** – Filter `Company = 'NEL Signalling'`. Columns include TAR No, Date, Stations, Nature of Work, Time range, and Remarks.  
   * **4** – Filter `Company = 'NEL ISCS and Systems'`. Columns include a row number, TAR No, Date, Nature of Work, Department, Stations, Track Sector, Time range, and Remarks.  
   * **5** – Filter `Company = 'NEL Communications'`. Columns are identical to query 4.  

   All NEL queries apply the same date range, `TARStatusId = 9`, optional `AccessType` match, and `TrackType` filter. Results are ordered by Access Date and TAR No.

4. **Result Sets** – The procedure returns each SELECT as a separate result set in the order they are executed.

### Data Interactions
* **Reads:**  
  * `TAMS_TAR`  
  * `TAMS_TAR_AccessReq`  
  * `TAMS_Access_Requirement`  
  * `TAMS_Parameters` (only in DTL query 9)

* **Writes:** None.