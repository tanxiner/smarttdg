# Procedure: sp_TAMS_GetParametersByLineandTracktype

### Purpose
Retrieve active parameter records that match a specific ParaCode, Line, and TrackType, ordered by the defined priority.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaCode | nvarchar(50) | Optional filter for the parameter code. |
| @Line | nvarchar(350) | Optional filter for the first value field (ParaValue1). |
| @TrackType | nvarchar(350) | Optional filter for the third value field (ParaValue3). |

### Logic Flow
1. The procedure begins by selecting columns ID, ParaType, ParaCode, ParaDesc, ParaValue1, ParaValue2, ParaValue3, ParaDatetime, ParaDate, ParaTime, and [Order] from the TAMS_Parameters table.  
2. It applies a WHERE clause that requires:  
   - ParaCode equals the supplied @ParaCode.  
   - ParaValue1 equals the supplied @Line.  
   - ParaValue3 equals the supplied @TrackType.  
   - The current date (GETDATE()) is on or after EffectiveDate.  
   - The current date is on or before ExpiryDate.  
3. The result set is ordered ascending by the [Order] column.  
4. The procedure returns the filtered, ordered rows to the caller.

### Data Interactions
* **Reads:** TAMS_Parameters  
* **Writes:** None