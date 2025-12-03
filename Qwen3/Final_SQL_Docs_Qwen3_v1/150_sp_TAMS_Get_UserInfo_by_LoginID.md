# Procedure: sp_TAMS_Get_UserInfo_by_LoginID

### Purpose
This stored procedure retrieves user information from the TAMS_User table based on a provided LoginID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The unique identifier for the user to retrieve information for. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_User table with the specified LoginID.
2. If a matching record is found, it selects all columns from the TAMS_User table where the LoginID matches the provided value.

### Data Interactions
* **Reads:** TAMS_User