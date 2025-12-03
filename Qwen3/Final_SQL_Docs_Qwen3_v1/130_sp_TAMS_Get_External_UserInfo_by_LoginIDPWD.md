# Procedure: sp_TAMS_Get_External_UserInfo_by_LoginIDPWD

### Purpose
This stored procedure retrieves external user information from the TAMS database based on a provided login ID and password.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID of the user to retrieve information for. |
| @LoginPWD | NVARCHAR(200) | The encrypted password of the user to verify. |

### Logic Flow
The procedure first checks if a TAMS User record exists with an active and external status matching the provided LoginID. If such a record is found, it then decrypts the stored password using the dbo.DecryptString function and compares it to the provided LoginPWD. If the decryption and comparison are successful, the procedure returns all columns from the TAMS_User table where the LoginID matches.

### Data Interactions
* **Reads:** TAMS_User table