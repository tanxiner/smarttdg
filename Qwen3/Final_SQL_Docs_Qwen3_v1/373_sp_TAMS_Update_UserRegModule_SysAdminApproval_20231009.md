# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval_20231009

### Purpose
This stored procedure is used to update a user registration module for system admin approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who is updating the registration module. |

### Logic Flow
1. The procedure starts by selecting the relevant data from the TAMS_Reg_Module and TAMS_Registration tables based on the provided @RegModID.
2. It then determines the next stage in the workflow for the selected registration module, taking into account the current status and any external factors.
3. If the registration module is already approved, it updates the WFStatus to 'Approved' and sets the UpdatedOn and UpdatedBy fields accordingly.
4. The procedure then inserts a new record into the TAMS_Reg_Module table with the updated data.
5. It also generates an email notification for system admin approval, including a link to access the registration module and instructions on how to proceed.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_Registration
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_WFStatus
	+ TAMS_User
	+ TAMS_User_Role
* **Writes:**
	+ TAMS_Reg_Module (new record)
	+ TAMS_Action_Log