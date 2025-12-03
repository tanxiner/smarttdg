# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID

### Purpose
This stored procedure is used to reject a user registration request based on the status of the corresponding module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the module that needs to be rejected. |
| @UpdatedBy | INT | The ID of the user who is updating the registration request. |

### Logic Flow
The procedure follows these steps:
1. It retrieves the current status and details of the module with the given ID.
2. If the status is 'Pending Company Registration' or 'Pending Company Approval', it rejects the entire request by setting the status to 'Rejected'.
3. If the status is 'Pending System Admin Approval' or 'Pending System Approver Approval', it also rejects the request but moves to a different stage.
4. It sends an email notification to the registered user with the rejection reason.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration, TAMS_Action_Log, EAlertQ_EnQueue