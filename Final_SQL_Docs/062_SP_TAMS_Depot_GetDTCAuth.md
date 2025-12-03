# Procedure: SP_TAMS_Depot_GetDTCAuth

### Purpose
Retrieve all depot authorization records for a specified access date, including related workflow, remark, and user information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | Filters records to those whose AccessDate equals the supplied date |

### Logic Flow
1. Disable the automatic row‑count message to keep the result set clean.  
2. Execute a SELECT that pulls columns from the main authorization table and several related tables.  
3. The base table is TAMS_TAR; it is left‑joined to TAMS_Depot_Auth on TarID.  
4. TAMS_Depot_Auth is left‑joined to TAMS_Depot_Auth_Workflow on DTCAuthId.  
5. TAMS_Depot_Auth_Workflow is left‑joined to TAMS_WFStatus on WorkflowID.  
6. TAMS_Depot_Auth is left‑joined to TAMS_Depot_Auth_Remark on RemarkID.  
7. TAMS_User is left‑joined to the workflow table on LoginId = ActionBy.  
8. The WHERE clause limits rows to those where TAMS_Depot_Auth.AccessDate matches @accessDate.  
9. The result set is ordered by DepotAuthStatusId in ascending order.  
10. The procedure returns the selected columns: AuthID, TARNo, DepotAuthStatusId, WFStatus, ActionOn, ActionBy, WorkflowID, CheckBoxValue, Remark, and the workflow order.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Remark, TAMS_WFStatus, TAMS_User  
* **Writes:** None