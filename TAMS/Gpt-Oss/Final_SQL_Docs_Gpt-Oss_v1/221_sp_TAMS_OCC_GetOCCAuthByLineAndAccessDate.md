# Procedure: sp_TAMS_OCC_GetOCCAuthByLineAndAccessDate

### Purpose
Retrieves all authorization records for a specified production line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Filters records by the production line identifier. |
| @AccessDate | nvarchar(50) | Filters records by the access date; input is converted to datetime. |

### Logic Flow
1. Accepts optional @Line and @AccessDate parameters.  
2. Converts @AccessDate from string to datetime using style 103 (dd/mm/yyyy).  
3. Queries the TAMS_OCC_Auth table for rows where the Line column matches @Line and the AccessDate column equals the converted datetime.  
4. Returns the selected columns: ID, Line, OperationDate, AccessDate, TractionPowerId, Remark, PFRRemark, OCCAuthStatusId, IsBuffer, PowerOn, PowerOffTime, RackedOutTime.  
5. Orders the result set by ID in ascending order.

### Data Interactions
* **Reads:** [dbo].[TAMS_OCC_Auth]  
* **Writes:** None