# Procedure: sp_TAMS_Get_User_TrackType_Line

### Purpose
Retrieve the distinct track types assigned to a user on a specified line.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @Line    | nvarchar(100) | The line identifier to filter roles. |
| @UserId  | nvarchar(100) | The login ID of the user whose roles are queried. |

### Logic Flow
1. The procedure begins by selecting distinct values of the `TrackType` column.  
2. It joins the `TAMS_User_Role` table (`ur`) with the `TAMS_User` table (`u`) on the `UserID` field.  
3. The join condition ensures that only roles belonging to the user identified by `@UserId` are considered.  
4. An additional filter limits the results to rows where the `Line` column in `TAMS_User_Role` matches the supplied `@Line` parameter.  
5. The resulting set of unique track types is returned to the caller.

### Data Interactions
* **Reads:** `TAMS_User_Role`, `TAMS_User`  
* **Writes:** None