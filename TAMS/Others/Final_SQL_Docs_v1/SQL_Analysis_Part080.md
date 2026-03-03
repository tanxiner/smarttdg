### Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_20231009

**Type:** Stored Procedure

### Purpose
This stored procedure performs the business task of inserting a new user registration into the system, including sending an email for approval to system administrators.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user |
| @Line | NVARCHAR(20) | The line number associated with the registration |
| @TrackType | NVARCHAR(50) | The type of track for the registration |
| @Module | NVARCHAR(20) | The module associated with the registration |

### Logic Flow
1. Checks if a workflow exists for the given line and track type.
2. Retrieves the next stage in the workflow, including the ID and title.
3. Inserts a new record into the TAMS_Reg_Module table with the provided data.
4. Inserts an audit log entry for the user registration.
5. Sends an email to system administrators for approval.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User, TAMS_User_Role
* Writes: TAMS_Reg_Module, TAMS_Action_Log

---

### Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_bak20230112

**Type:** Stored Procedure

### Purpose
This stored procedure performs the business task of inserting a new user registration into the system, including sending an email for approval to system administrators.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user |
| @Line | NVARCHAR(20) | The line number associated with the registration |
| @Module | NVARCHAR(20) | The module associated with the registration |

### Logic Flow
1. Checks if a workflow exists for the given line and track type.
2. Retrieves the next stage in the workflow, including the ID and title.
3. Inserts a new record into the TAMS_Reg_Module table with the provided data.
4. Inserts an audit log entry for the user registration.
5. Sends an email to system administrators for approval.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_User, TAMS_User_Role
* Writes: TAMS_Reg_Module, TAMS_Action_Log

---

### Procedure: sp_TAMS_Insert_RegQueryDept_SysAdminApproval

**Type:** Stored Procedure

### Purpose
This stored procedure performs the business task of inserting a new query for department system administrators.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registered module |
| @RegRoleID | INT | The ID of the registered role |
| @Dept | NVARCHAR(200) | The department associated with the query |
| @UpdatedBy | INT | The user who updated the query |

### Logic Flow
1. Inserts a new record into the TAMS_Reg_QueryDept table with the provided data.

### Data Interactions
* Writes: TAMS_Reg_QueryDept