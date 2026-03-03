# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval

### Purpose
This stored procedure updates a user registration module for system admin approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the user registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who is updating the module. |

### Logic Flow
1. The procedure starts by selecting relevant data from the TAMS_Reg_Module and TAMS_Registration tables based on the provided @RegModID.
2. It then determines the next stage in the workflow for the selected module, taking into account the module's type and the current registration status.
3. If the module is external, it sets the work flow type to 'ExtUser'. Otherwise, it sets the work flow type based on the module's type (TAR, DCC, or OCC).
4. The procedure then selects the workflow ID, new WF status ID, and endorser ID for the selected module.
5. It updates the registration module with the new values and inserts an audit log entry.
6. Finally, it sends an email to the registered users with a link to access TAMS and approve/reject the user registration.

### Data Interactions
* Reads: TAMS_Reg_Module, TAMS_Registration
* Writes: TAMS_Reg_Module (updated), TAMS_Action_Log