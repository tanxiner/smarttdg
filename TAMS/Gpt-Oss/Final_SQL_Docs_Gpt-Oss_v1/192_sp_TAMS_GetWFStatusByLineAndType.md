# Procedure: sp_TAMS_GetWFStatusByLineAndType

### Purpose
Retrieve active workflow status records for a specified line, track type, and workflow type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Filter by line identifier |
| @TrackType | nvarchar(50) | Filter by track type |
| @Type | nvarchar(50) | Filter by workflow type |

### Logic Flow
1. Accept optional parameters @Line, @TrackType, and @Type.  
2. Query the TAMS_WFStatus table for rows where:
   - Line equals @Line  
   - TrackType equals @TrackType  
   - WFType equals @Type  
   - IsActive equals 1  
3. Return the columns ID, Line, WFType, WFDescription, WFStatus, WFStatusId, and [Order].  
4. Order the result set by [Order] in ascending order.

### Data Interactions
* **Reads:** TAMS_WFStatus  
* **Writes:** None