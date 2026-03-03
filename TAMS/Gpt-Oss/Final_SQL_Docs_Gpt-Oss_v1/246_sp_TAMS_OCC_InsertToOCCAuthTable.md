# Procedure: sp_TAMS_OCC_InsertToOCCAuthTable

### Purpose
Insert rows from a table‑valued parameter into the TAMS_OCC_Auth table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth | [dbo].[TAMS_OCC_Auth] READONLY | Source data to be inserted |

### Logic Flow
1. Receive a read‑only table‑valued parameter containing rows to be added.  
2. Execute an `INSERT INTO` statement that copies each column from the parameter into the corresponding column of the TAMS_OCC_Auth table.  
3. No additional processing or validation is performed; all rows are inserted as provided.

### Data Interactions
* **Reads:** @TAMS_OCC_Auth  
* **Writes:** TAMS_OCC_Auth  

---