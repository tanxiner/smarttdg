# Procedure: sp_TAMS_TB_Gen_Summary20250120

### Purpose
Generate a series of summary reports for TAMS TAR records filtered by line type, track type, access date range, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line category (DTL or NEL) to determine which set of queries to run. |
| @TrackType | NVARCHAR(50) | Filters records by the track type. |
| @AccessDateFrom | NVARCHAR(20) | Lower bound of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Upper bound of the access date range. |
| @AccessType | NVARCHAR(20) | Optional filter for the access type; if null or empty, all types are included. |

### Logic Flow
1. **Line Selection**  
   - If @Line equals 'DTL', execute the DTL block.  
   - If @Line equals 'NEL', execute the NEL block.

2. **DTL Block**  
   - Execute nine separate SELECT statements, each producing a distinct result set.  
   - All statements filter on:  
     - AccessDate between @AccessDateFrom and @AccessDateTo (converted to DATETIME).  
     - TARStatusId = 8.  
     - AccessType matches @AccessType or @AccessType is null/empty.  
     - Line = 'DTL'.  
     - TrackType = @TrackType.  
   - Additional filters vary per statement:  
     1. Join with TAMS_TAR_AccessReq and TAMS_Access_Requirement where OperationRequirement = 'Power Off With Rack Out / 22KV Isolation'.  
     2. Same join with OperationRequirement = 'Use of Tunnel Ventilation'.  
     3. Company LIKE '%DTL SIG%'.  
     4. Company LIKE '%DTL POWER%'.  
     5. Company LIKE '%DTL COMMS%' and use dbo.TAMS_Get_Station for Access Stations.  
     6. Company LIKE '%DTL COMMS%' and use dbo.TAMS_Get_ES_NoBufferZone for Electrical Section.  
     7. Company LIKE '%DTL Pway & FM%' OR '%DTL Pway & CS%' OR '%DTL FM%'.  
     8. Company LIKE '%DTL RS%'.  
     9. Company LIKE '%DTL Operations%' OR '%DTL Training%' OR '%DTL OPS%'.  
     10. Company NOT IN (SELECT ParaValue2 FROM TAMS_Parameters WHERE ParaType = 'S' AND ParaCode = 'Company' AND ParaValue1 = a.Line).  
   - Each SELECT returns columns: Access Date, TAR ID, Electrical Section or Access Stations, Nature of Work, Remarks.  
   - Results are ordered by AccessDate and TARNo.

3. **NEL Block**  
   - Execute six SELECT statements, each producing a distinct result set.  
   - All statements filter on:  
     - AccessDate between @AccessDateFrom and @AccessDateTo.  
     - TARStatusId = 9.  
     - AccessType matches @AccessType or @AccessType is null/empty.  
     - Line = 'NEL'.  
     - TrackType = @TrackType.  
   - Additional filters vary per statement:  
     1. Join with TAMS_TAR_AccessReq and TAMS_Access_Requirement where OperationRequirement = 'Power Off With Rack Out / 22KV Isolation'.  
     2. a.Is13ASocket = 1.  
     3. Join with OperationRequirement = 'Use of Tunnel Ventilation'.  
     4. Company = 'NEL Signalling'.  
     5. Company = 'NEL ISCS and Systems'.  
     6. Company = 'NEL Communications'.  
   - Each SELECT returns columns tailored to the report type, such as Date, Time ranges, TAR ID, Power Section, Activities, Stations, Direction, TVF Request, Remarks, etc.  
   - Results are ordered by AccessDate and TARNo.

4. **Result Delivery**  
   - The procedure returns multiple result sets in the order they are executed, one per SELECT statement.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Parameters  
* **Writes:** None
---