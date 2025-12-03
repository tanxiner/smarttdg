# Procedure: sp_TAMS_GetBlockedTarDates

### Purpose
Retrieve active blocked TAR dates for a specific line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Line identifier to filter records |
| @TrackType | nvarchar(50) | Track type to filter records |
| @AccessDate | date | Date to match the BlockDate field |

### Logic Flow
1. Accepts three optional parameters: line, track type, and access date.  
2. Queries the `TAMS_Block_TARDate` table.  
3. Filters rows where `Line` equals the supplied line, `TrackType` equals the supplied track type, and `BlockDate` equals the supplied access date.  
4. Ensures only rows marked as active (`IsActive = 1`) are returned.  
5. Orders the resulting set by `BlockDate` in ascending order.  
6. Returns the columns `ID`, `Line`, `TrackType`, `BlockDate`, and `BlockReason`.

### Data Interactions
* **Reads:** TAMS_Block_TARDate  
* **Writes:** None  

---