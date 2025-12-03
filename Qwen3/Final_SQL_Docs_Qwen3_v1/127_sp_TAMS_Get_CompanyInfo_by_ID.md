# Procedure: sp_TAMS_Get_CompanyInfo_by_ID

### Purpose
This stored procedure retrieves company information from the TAMS_Company table based on a provided CompanyID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompanyID | NVARCHAR(100) | The ID of the company to retrieve information for. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_Company table with the specified CompanyID.
2. If a record is found, it selects all columns from the TAMS_Company table where the ID matches the provided CompanyID.
3. If no record is found, it returns an empty result set (i.e., no data is returned).

### Data Interactions
* **Reads:** TAMS_Company