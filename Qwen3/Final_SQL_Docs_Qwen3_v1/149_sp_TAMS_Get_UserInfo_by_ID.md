# Procedure: sp_TAMS_Get_UserInfo_by_ID

### Purpose
This stored procedure retrieves user information based on a provided user ID, including access details for different roles and modules.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve information for. |

### Logic Flow
The procedure follows these steps:
1. It first checks if a user exists with the provided ID in the TAMS_User table.
2. If a user is found, it then retrieves company information from the TAMS_Company table based on the user's CompanyID.
3. Next, it fetches user query department details for the specified user ID.
4. The procedure then breaks down the access rights into four categories:
   - DTL TAR: Retrieves role and module information for the 'DTL' line and 'TAR' module with a TrackType of 'mainline'.
   - DTL OCC: Retrieves role and module information for the 'DTL' line and 'OCC' module with a TrackType of 'mainline'.
   - NEL TAR: Retrieves role and module information for the 'NEL' line and 'TAR' module with a TrackType of 'mainline'.
   - NEL OCC: Retrieves role and module information for the 'NEL' line and 'OCC' module with a TrackType of 'mainline'.
5. Finally, it fetches depot access details for the user ID.

### Data Interactions
* Reads from:
	+ TAMS_User
	+ TAMS_Company
	+ TAMS_User_QueryDept
	+ TAMS_Role
	+ TAMS_User_Role
* Writes to: None