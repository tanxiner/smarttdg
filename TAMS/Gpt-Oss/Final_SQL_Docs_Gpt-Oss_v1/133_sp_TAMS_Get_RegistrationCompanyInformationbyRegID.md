# Procedure: sp_TAMS_Get_RegistrationCompanyInformationbyRegID

### Purpose
Retrieve the registration record for a company when its registration status is in the applicant, pending, or approved stages.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Identifier of the registration record to retrieve |

### Logic Flow
1. Verify that a record exists in **TAMS_Reg_Module** where the `RegID` matches the supplied `@RegID` and the `RegStatus` is one of 1, 8, or 15.  
2. If such a record is found, return all columns from **TAMS_Registration** where the `ID` equals the supplied `@RegID`.  
3. If no matching record exists, the procedure completes without returning data.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration  
* **Writes:** None