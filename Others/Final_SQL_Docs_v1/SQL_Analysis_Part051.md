# Procedure: sp_TAMS_GetTarByTarId
**Type:** Stored Procedure

The procedure retrieves a specific TAR record by its ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR record to retrieve |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_TAR
* **Writes:** Audit table