# Procedure: sp_TAMS_Check_UserExist

### Purpose
This stored procedure checks if a user exists in the TAMS_User table based on either their LoginID or SAPNo.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SapNo | NVARCHAR(100) | The SAP number of the user to check for existence. |
| @LoginID | NVARCHAR(200) | The login ID of the user to check for existence. |

### Logic Flow
The procedure first checks if both @LoginID and @SapNo are provided. If they are, it checks if a record exists in the TAMS_User table where LoginID matches @LoginID and SAPNo matches @SapNo. If this condition is met, it returns 1 (indicating existence). 

If only @LoginID is provided, it checks if a record exists in the TAMS_User table where LoginID matches @LoginID. If this condition is met, it returns 1.

If neither @LoginID nor @SapNo are provided, the procedure does not perform any checks and returns no result.

### Data Interactions
* **Reads:** TAMS_User