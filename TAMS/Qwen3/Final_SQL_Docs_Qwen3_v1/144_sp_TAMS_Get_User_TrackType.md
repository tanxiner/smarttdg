# Procedure: sp_TAMS_Get_User_TrackType

### Purpose
This stored procedure retrieves a list of unique track types associated with a specific user, based on their login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Loginid | NVARCHAR(100) | The login ID of the user to retrieve track types for. |

### Logic Flow
1. The procedure starts by selecting distinct track types from the TAMS_User_Role table.
2. It joins this table with the TAMS_User table on the UserID column, ensuring that only roles associated with a specific user are considered.
3. The procedure then filters the results to include only rows where the LoginID matches the provided @Loginid parameter.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User