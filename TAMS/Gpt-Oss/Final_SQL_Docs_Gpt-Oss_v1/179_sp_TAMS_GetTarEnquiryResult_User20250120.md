# Procedure: sp_TAMS_GetTarEnquiryResult_User20250120

### Purpose
Return a list of users who are authorized to view TAR records for a specified track type, optionally filtered by line, TAR type, access type, status, and access date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | ID of the user making the request |
| @Line | nvarchar(50) | Optional line filter; ignored if NULL, empty, or '-1' |
| @TrackType | nvarchar(50) | Track type to filter TAR records |
| @TarType | nvarchar(50) | Optional TAR type filter; ignored if NULL, empty, or '-1' |
| @AccessType | nvarchar(50) | Optional access type filter; ignored if NULL, empty, or '-1' |
| @TarStatusId | integer | Optional TAR status filter; ignored if 0, NULL, or '-1' |
| @AccessDateFrom | nvarchar(50) | Optional start of access date range; ignored if NULL or empty |
| @AccessDateTo | nvarchar(50) | Optional end of access date range; ignored if NULL or empty |

### Logic Flow
1. **Role Determination**  
   - Query the user‑role‑role tables to set three flags:  
     - `@IsAll` if the user holds any of the “view all” roles for the given track type.  
     - `@IsPower` if the user holds any of the “power” roles for the given track type.  
     - `@IsDep` if the user holds any of the “department” roles for the given track type.  

2. **Build Filter String**  
   - Initialize an empty condition string `@cond`.  
   - Append SQL fragments for each non‑empty filter parameter (`@Line`, `@TarType`, `@AccessType`, `@TarStatusId`, `@AccessDateFrom`, `@AccessDateTo`) using the appropriate column names and data types.  

3. **Construct Dynamic Query**  
   - Start a SELECT that will return a row number, the TAR creator’s ID, and the creator’s name.  
   - Depending on the role flags, build a sub‑query that selects distinct `createdBy` values from `TAMS_TAR` joined with `TAMS_WFStatus` on status and line, applying the track type and the previously built `@cond`.  
     - If `@IsAll` is set, no additional role restrictions are applied.  
     - If `@IsPower` is set, include records where `InvolvePower = 1` or the creator matches the requesting user.  
     - If `@IsDep` is set, include records where the TAR’s company matches the user’s department or the creator matches the requesting user.  
     - Otherwise, include only records created by the requesting user.  
   - Join the resulting set with `TAMS_User` to retrieve the creator’s name.  

4. **Execute**  
   - Print the constructed SQL for debugging.  
   - Execute the dynamic SQL to return the result set.

### Data Interactions
* **Reads:**  
  - `TAMS_User`  
  - `TAMS_User_Role`  
  - `TAMS_Role`  
  - `TAMS_TAR`  
  - `TAMS_WFStatus`  

* **Writes:** None.