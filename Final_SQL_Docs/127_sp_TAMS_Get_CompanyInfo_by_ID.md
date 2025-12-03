# Procedure: sp_TAMS_Get_CompanyInfo_by_ID

### Purpose
Retrieve all columns for a company identified by @CompanyID, or return an empty result set if the company does not exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompanyID | NVARCHAR(100) | Identifier of the company to fetch; defaults to NULL |

### Logic Flow
1. Check if a row exists in TAMS_Company where ID equals @CompanyID.  
2. If a matching row is found, return that row’s data.  
3. If no matching row exists, return an empty result set by selecting from TAMS_Company with a condition that is always false (1=2).

### Data Interactions
* **Reads:** TAMS_Company  
* **Writes:** None