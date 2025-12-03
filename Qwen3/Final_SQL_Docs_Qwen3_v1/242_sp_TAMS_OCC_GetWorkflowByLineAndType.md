# Procedure: sp_TAMS_OCC_GetWorkflowByLineAndType

### Purpose
This stored procedure retrieves workflow information for a specific line and type, filtering by effective date and active status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @Type | NVARCHAR(50) | The workflow type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Workflow table.
2. It filters the results based on the provided Line and Type parameters, ensuring that only records with matching values are returned.
3. The EffectiveDate and ExpiryDate columns are filtered to ensure that only records within the current date range (i.e., where EffectiveDate is less than or equal to the current date and ExpiryDate is greater than or equal to the current date) are included.
4. Finally, the procedure orders the results by the ID column.

### Data Interactions
* **Reads:** TAMS_Workflow table