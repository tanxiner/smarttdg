# Procedure: sp_TAMS_GetSectorsByLineAndDirection

### Purpose
Retrieve active sector records for a specified line and direction that are currently effective.

### Parameters
| Name        | Type          | Purpose |
| :---        | :---          | :--- |
| @Line       | nvarchar(10)  | The line identifier to filter sectors (e.g., 'DTL' or 'NEL'). |
| @Direction  | nvarchar(10)  | The direction identifier to filter sectors. |

### Logic Flow
1. The procedure receives @Line and @Direction values.  
2. It checks if @Line equals 'DTL'.  
   - If true, it selects sector rows from TAMS_Sector where:  
     - Line matches @Line,  
     - Direction matches @Direction,  
     - IsActive is 1,  
     - EffectiveDate is on or before the current date, and  
     - ExpiryDate is on or after the current date.  
   - The result set is ordered by the [Order] column ascending.  
3. If @Line is not 'DTL', it checks if @Line equals 'NEL'.  
   - If true, it performs the same selection and ordering logic as in step 2.  
4. If @Line is neither 'DTL' nor 'NEL', the procedure returns no rows.

### Data Interactions
* **Reads:** TAMS_Sector  
* **Writes:** None