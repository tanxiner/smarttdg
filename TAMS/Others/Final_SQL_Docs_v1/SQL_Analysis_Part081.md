Here are the documented procedures:

# Procedure: sp_TAMS_Insert_RegQueryDept_SysOwnerApproval
**Type:** Stored Procedure

Purpose: This procedure inserts a new record into TAMS_Reg_QueryDept table and checks if user exists.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | ID of the registration module |
| @RegRoleID | INT | ID of the role |
| @Dept | NVARCHAR(200) | Department name |
| @UpdatedBy | INT | User ID who updated |

Logic Flow:
1. Checks if user exists by selecting UserID from TAMS_User table where LoginID is equal to the LoginID in TAMS_Registration table for the given registration module ID.
2. Inserts a new record into TAMS_Reg_QueryDept table with the provided values.
3. If the user does not exist, inserts a new record into TAMS_User_QueryDept table.

Data Interactions:
* Reads: TAMS_User, TAMS_Registration, TAMS_Reg_QueryDept
* Writes: TAMS_Reg_QueryDept