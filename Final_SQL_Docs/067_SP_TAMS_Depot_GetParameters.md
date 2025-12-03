# Procedure: SP_TAMS_Depot_GetParameters

### Purpose
Retrieve distinct parameter values for depot-related settings that are currently effective.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | – | – |

### Logic Flow
1. Disable row‑count messages to avoid extra result sets.  
2. Execute a SELECT that returns unique combinations of ParaValue1, ParaCode, ParaValue2, ParaValue3, and ParaTime from TAMS_Parameters.  
3. The SELECT filters rows where the current date falls between EffectiveDate and ExpiryDate and where ParaValue2 equals 'Depot'.

### Data Interactions
* **Reads:** TAMS_Parameters  
* **Writes:** None

---