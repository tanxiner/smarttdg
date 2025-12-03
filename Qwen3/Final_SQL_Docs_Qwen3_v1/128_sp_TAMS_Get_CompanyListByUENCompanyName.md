# Procedure: sp_TAMS_Get_CompanyListByUENCompanyName

### Purpose
This stored procedure retrieves a list of companies from the TAMS_Company table based on a search for UENNo and CompanyName.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SearchUEN | NVARCHAR(100) | The UENNo to search for in the company names. |
| @SearchCompanyName | NVARCHAR(200) | The CompanyName to search for in the UENNo values. |

### Logic Flow
1. The procedure starts by selecting all columns (*) from the TAMS_Company table.
2. It then applies two conditions to filter the results:
   - The company name must match the @SearchUEN parameter (case-insensitive).
   - The UENNo value must match the @SearchCompanyName parameter (case-sensitive).
3. If both conditions are met, the procedure returns the selected columns for the matching company.

### Data Interactions
* **Reads:** TAMS_Company table