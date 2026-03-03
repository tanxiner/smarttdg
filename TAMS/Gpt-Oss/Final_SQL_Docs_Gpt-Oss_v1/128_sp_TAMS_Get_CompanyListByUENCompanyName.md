# Procedure: sp_TAMS_Get_CompanyListByUENCompanyName

### Purpose
Retrieve all company records that match a specified UEN pattern and company name pattern.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SearchUEN | NVARCHAR(100) | Pattern used to filter the UENNo column. |
| @SearchCompanyName | NVARCHAR(200) | Pattern used to filter the Company column. |

### Logic Flow
1. The procedure receives two search patterns: one for UENNo and one for Company.  
2. It executes a SELECT statement that returns every row from the TAMS_Company table where the UENNo column matches the @SearchUEN pattern and the Company column matches the @SearchCompanyName pattern.  
3. The result set is returned to the caller.

### Data Interactions
* **Reads:** TAMS_Company  
* **Writes:** None

---