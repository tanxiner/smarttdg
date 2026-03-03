# Procedure: sp_TAMS_Get_RegistrationCompanyInformationbyRegID

This procedure retrieves registration company information for a given registration ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The unique identifier of the registration to retrieve information for. |

### Logic Flow
1. The procedure checks if there exists a record in the TAMS_Reg_Module table where the RegID matches the input parameter and the RegStatus is either 1, 8, or 15.
2. If such a record exists, it means the registration ID has reached a specific stage (Applicant Company Registration Stage) and the procedure proceeds to retrieve the corresponding registration information from the TAMS_Registration table where the ID matches the input parameter.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration