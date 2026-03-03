# Procedure: sp_TAMS_OCC_GetOCCAuthByLineAndAccessDate

### Purpose
This stored procedure retrieves data from the TAMS_OCC_Auth table based on a specified line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @AccessDate | nvarchar(50) | The access date to filter by. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_OCC_Auth table.
2. It filters the data based on the provided line and access date, using a case-sensitive comparison for the line number.
3. The access date is converted to a datetime format before being compared with the provided @AccessDate parameter.
4. The results are ordered by the ID column in ascending order.

### Data Interactions
* **Reads:** [dbo].[TAMS_OCC_Auth]