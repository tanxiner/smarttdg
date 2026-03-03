# Procedure: sp_TAMS_OCC_GetTractionPowerDetailsByIdAndType

### Purpose
This stored procedure retrieves traction power details by ID and type, filtering for active records with a specific sector type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | int | The ID of the traction power detail to retrieve. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Traction_Power_Detail table.
2. It filters the records based on the provided ID, ensuring only matching records are returned.
3. Additionally, it filters for records with a specific sector type ('Sector') and ensures they are active (IsActive = 1).
4. The results are ordered by the ID in ascending order.

### Data Interactions
* **Reads:** TAMS_Traction_Power_Detail