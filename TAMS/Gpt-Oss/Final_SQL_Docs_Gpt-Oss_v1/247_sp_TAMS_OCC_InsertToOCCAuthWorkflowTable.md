# Procedure: sp_TAMS_OCC_InsertToOCCAuthWorkflowTable

### Purpose
Insert rows from a table‑valued parameter into the TAMS_OCC_Auth_Workflow table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth_Workflow | [dbo].[TAMS_OCC_Auth_Workflow] READONLY | Source data to be inserted |

### Logic Flow
1. Receive a read‑only table‑valued parameter containing rows to be added.  
2. Execute an INSERT statement that copies each column (OCCAuthId, OCCAuthEndorserId, WFStatus, StationId, FISTestResult, ActionOn, ActionBy) from the parameter into the corresponding columns of the TAMS_OCC_Auth_Workflow table.  
3. Complete the transaction; no additional processing or validation occurs.

### Data Interactions
* **Reads:** @TAMS_OCC_Auth_Workflow  
* **Writes:** TAMS_OCC_Auth_Workflow  

---