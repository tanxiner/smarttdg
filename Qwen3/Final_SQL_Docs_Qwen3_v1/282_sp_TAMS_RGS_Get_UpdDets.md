# Procedure: sp_TAMS_RGS_Get_UpdDets

This procedure retrieves and decrypts specific data from the TAMS_TOA table based on a provided TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TARID to filter the data by |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA table.
2. It filters the results based on the provided TARID, if specified.
3. The selected columns are then decrypted using a function named dbo.DecryptString.

### Data Interactions
* **Reads:** TAMS_TOA