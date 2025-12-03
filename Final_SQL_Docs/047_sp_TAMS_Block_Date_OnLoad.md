# Procedure: sp_TAMS_Block_Date_OnLoad

### Purpose
Retrieve block date records for a specified line, track type, and block date, returning the most recent entries first.

### Parameters
| Name       | Type          | Purpose |
| :---       | :---          | :--- |
| @Line      | NVARCHAR(20)  | Filter by line; if NULL or empty, all lines are returned. |
| @TrackType | NVARCHAR(50)  | Filter by track type; if NULL or empty, all track types are returned. |
| @BlockDate | NVARCHAR(20)  | Filter by block date; if NULL or empty, all dates are returned. |

### Logic Flow
1. Convert the @BlockDate parameter from a string to a DATE using style 103 (dd/mm/yyyy).  
2. Select rows from TAMS_Block_TARDate where:  
   - The Line column equals @Line, or @Line is NULL/empty.  
   - The TrackType column equals @TrackType, or @TrackType is NULL/empty.  
   - The BlockDate column equals the converted @BlockDate, or @BlockDate is NULL/empty.  
3. Return the columns ID, Line, TrackType, BlockDate (formatted as NVARCHAR(20) dd/mm/yyyy), BlockReason, and IsActive.  
4. Order the result set by the BlockDate column in descending order.

### Data Interactions
* **Reads:** TAMS_Block_TARDate  
* **Writes:** None