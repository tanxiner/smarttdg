# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID_20231009
**Type:** Stored Procedure

The purpose of this stored procedure is to reject a user registration request based on the status of the corresponding module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the module that needs to be rejected. |
| @UpdatedBy | INT | The ID of the user who is updating the registration request. |

### Logic Flow
1. Checks if the user exists for the given module.
2. If the status is still at Pending Company Registration or Pending Company Approval, reject the entire request and sends an email to the registered users with a rejection message.
3. If the status is Pending System Admin Approval or Pending System Approver Approval, reject the request and sends an email to the registered users with a rejection message.
4. If none of the above conditions are met, move to the rejected by Line/Module stage.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration
* **Writes:** TAMS_Reg_Module (updated), TAMS_Action_Log