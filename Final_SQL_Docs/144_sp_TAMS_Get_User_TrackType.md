# Procedure: sp_TAMS_Get_User_TrackType

### Purpose
Retrieve the distinct track types assigned to a user identified by their login ID.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @Loginid  | NVARCHAR(100) | The login identifier of the user whose track types are requested. |

### Logic Flow
1. Accept the optional @Loginid parameter.  
2. Perform an inner join between the tables TAMS_User_Role and TAMS_User on the UserID column.  
3. Filter the joined rows where the LoginID column in TAMS_User matches the supplied @Loginid.  
4. Select the TrackType column from the joined result set, ensuring each returned value is unique by applying DISTINCT.  
5. Return the list of unique track types.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User  
* **Writes:** None