# Procedure: sp_TAMS_Depot_GetBlockedTarDates

### Purpose
Retrieve active block records for a specific line and date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line identifier to filter blocks. |
| @AccessDate | date | The date to filter block records. |

### Logic Flow
1. Accept optional @Line and @AccessDate parameters.  
2. Query the TAMS_Block_TARDate table for rows where:  
   - Line equals @Line,  
   - BlockDate equals @AccessDate,  
   - IsActive equals 1.  
3. Return the columns ID, Line, BlockDate, BlockReason for matching rows, ordered by BlockDate ascending.

### Data Interactions
* **Reads:** TAMS_Block_TARDate  
* **Writes:** None