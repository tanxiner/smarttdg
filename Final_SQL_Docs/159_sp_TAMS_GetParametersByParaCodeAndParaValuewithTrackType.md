# Procedure: sp_TAMS_GetParametersByParaCodeAndParaValuewithTrackType

### Purpose
Retrieve active parameter records that match a specific code, value, and track type, ordered by priority.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaCode | nvarchar(50) | Filter by the parameter code. |
| @ParaValue | nvarchar(350) | Filter by the primary parameter value. |
| @TrackType | nvarchar(50) | Filter by the secondary parameter value that represents the track type. |

### Logic Flow
1. The procedure receives three optional string inputs: a parameter code, a primary value, and a track type.  
2. It queries the `TAMS_Parameters` table for rows where:
   - `ParaCode` equals the supplied `@ParaCode`.  
   - `ParaValue1` equals the supplied `@ParaValue`.  
   - `ParaValue2` equals the supplied `@TrackType`.  
   - The current date falls between `EffectiveDate` and `ExpiryDate` (inclusive).  
3. The matching rows are returned with the columns `ID, ParaType, ParaCode, ParaDesc, ParaValue1, ParaValue2, ParaValue3, ParaDatetime, ParaDate, ParaTime, [Order]`.  
4. Results are sorted ascending by the `[Order]` column to reflect priority.

### Data Interactions
* **Reads:** `TAMS_Parameters`  
* **Writes:** None

---