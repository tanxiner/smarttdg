# Procedure: sp_TAMS_GetWFStatusByLine

### Purpose
Retrieve the active workflow status records for a specified line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Optional line identifier to filter the status records. |

### Logic Flow
1. The procedure accepts an optional @Line parameter.  
2. It queries the TAMS_WFStatus table for rows where the Line column matches @Line and IsActive equals 1.  
3. The selected columns are ID, Line, WFType, WFDescription, WFStatus, WFStatusId, and [Order].  
4. Results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_WFStatus 
* **Writes:** None