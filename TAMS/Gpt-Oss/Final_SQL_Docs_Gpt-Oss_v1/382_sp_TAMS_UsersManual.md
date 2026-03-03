# Procedure: sp_TAMS_UsersManual

### Purpose
Retrieve the current manual value for the TOAUM parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |

### Logic Flow
1. Query the `TAMS_Parameters` table.  
2. Filter rows where `ParaCode` equals `'TOAUM'`.  
3. Ensure the current date (`GETDATE()`) falls between `EffectiveDate` and `ExpiryDate`.  
4. Return the `ParaValue1` column as the result set column `UManual`.

### Data Interactions
* **Reads:** TAMS_Parameters  
* **Writes:** None  

---