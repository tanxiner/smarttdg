# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID_20231009

### Purpose
This stored procedure is used to reject a user registration request based on the status of the corresponding company registration module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the company registration module. |
| @UpdatedBy | INT | The ID of the user who updated the registration request. |

### Logic Flow
The procedure follows these steps:

1. It retrieves the current status of the company registration module associated with the provided `@RegModID`.
2. If the status is 'Pending Company Registration' or 'Pending Company Approval', it rejects the entire request and sends an email to all registered users.
3. If the status is 'Pending System Admin Approval' or 'Pending System Approver Approval', it rejects the request and sends an email to the user who submitted the registration request.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration
* **Writes:** TAMS_Reg_Module (updates RegStatus), TAMS_Action_Log