# Procedure: sp_TAMS_GetParametersByParaCodeAndParaValue

### Purpose
Retrieve active parameter records that match a specified code and value.

### Parameters
| Name       | Type          | Purpose |
| :---       | :---          | :--- |
| @ParaCode  | nvarchar(50) | Code to filter parameters. |
| @ParaValue | nvarchar(350)| Value to filter parameters. |

### Logic Flow
1. Accepts optional @ParaCode and @ParaValue inputs.  
2. Queries the TAMS_Parameters table for rows where:  
   - ParaCode equals @ParaCode.  
   - ParaValue1 equals @ParaValue.  
   - EffectiveDate is on or before the current date.  
   - ExpiryDate is on or after the current date.  
3. Returns the columns ID, ParaType, ParaCode, ParaDesc, ParaValue1, ParaValue2, ParaValue3, ParaDatetime, ParaDate, ParaTime, and [Order].  
4. Results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters  
* **Writes:** None