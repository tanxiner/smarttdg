# Procedure: SP_TAMS_Depot_GetDTCAuthSPKS

### Purpose
Retrieve DTC authorization and SPKS details for a specified access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date used to filter authorization records |

### Logic Flow
1. Disable the automatic row‑count message to keep the result set clean.  
2. Execute a SELECT that pulls the authorization ID, SPKS ID, protection types and timings, status ID, and the names of the users who performed the protect‑off and protect‑on actions.  
3. Join the authorization table to the SPKS table on the authorization ID.  
4. Join to the workflow status table where the workflow type is “DTCAuth” to obtain the workflow ID.  
5. Join twice to the user table to resolve the login IDs for the protect‑off and protect‑on action by fields.  
6. Filter the combined rows so only those whose access date matches the supplied @accessDate are returned.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, TAMS_WFStatus, TAMS_User  
* **Writes:** None