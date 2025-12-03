# Procedure: sp_TAMS_OCC_GetTractionsPowerByLine

### Purpose
This stored procedure retrieves traction power data for a specified line, filtered by effective and expiry dates, and order status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve traction power data for. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Traction_Power table.
2. It filters the results based on the provided line number, ensuring that only records with an effective date within the current date range and an active status are included.
3. The results are ordered by the order status in ascending order.

### Data Interactions
* **Reads:** [dbo].[TAMS_Traction_Power]
* **Writes:** None