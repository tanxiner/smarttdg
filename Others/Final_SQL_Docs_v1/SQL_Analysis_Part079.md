# Procedure: sp_TAMS_Insert_InternalUserRegistration
**Type:** Stored Procedure

### Purpose
This stored procedure inserts a new internal user registration into the database, including relevant details such as user name, email, and office number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SapNo | NVARCHAR(20) | SAP Number |
| @Name | NVARCHAR(200) | User Name |
| @UserName | NVARCHAR(200) | User Email |
| @Email | NVARCHAR(500) | User Email |
| @Mobile | NVARCHAR(20) | User Mobile Number |
| @OfficeNo | NVARCHAR(20) | Office Number |
| @Dept | NVARCHAR(100) | Department |
| @ValidTo | NVARCHAR(100) | Valid To Date |
| @Purpose | NVARCHAR(MAX) | Purpose |

### Logic Flow
1. The procedure checks if the user exists and inserts into the Audit table.
2. It then retrieves the next stage in the workflow for the given line, track type, and module.
3. Based on the retrieved next stage ID, it inserts a new record into the TAMS_Reg_Module table with relevant details.
4. An audit log is inserted to track the user registration submission.
5. An email is sent to the system approvers with a link to access TAMS.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log
* Writes: TAMS_Registration, TAMS_Reg_Module, TAMS_Action_Log