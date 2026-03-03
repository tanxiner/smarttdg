# Procedure: sp_TAMS_Get_RolesByLineModule

### Purpose
Retrieves role information from TAMS_Role that matches specified line, track type, and module criteria.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @Line     | NVARCHAR(100) | Filter roles by line using a LIKE comparison. |
| @TrackType| NVARCHAR(50)  | Filter roles by track type using a LIKE comparison. |
| @Module   | NVARCHAR(100) | Filter roles by module using a LIKE comparison. |

### Logic Flow
1. The procedure receives three optional string parameters: @Line, @TrackType, and @Module.  
2. It constructs a SELECT statement that retrieves the columns ID, Line, TrackType, Module, Role, and RoleDesc from the TAMS_Role table.  
3. The WHERE clause applies three LIKE predicates, each comparing the corresponding column to the supplied parameter.  
4. Because the parameters default to NULL, a NULL value results in a LIKE comparison that matches any value, effectively acting as a wildcard for that field.  
5. The query returns all rows that satisfy all three LIKE conditions, providing a filtered list of roles.

### Data Interactions
* **Reads:** TAMS_Role  
* **Writes:** None