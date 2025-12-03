# Procedure: sp_TAMS_Get_UserInfo_by_ID

### Purpose
Retrieve a user’s profile, associated company, department queries, and all active role permissions across multiple lines, modules, and track types for a given UserID.

### Parameters
| Name     | Type          | Purpose |
| :------- | :------------ | :------ |
| @UserID  | NVARCHAR(100) | Identifier of the user whose information is requested; may be NULL to return no rows. |

### Logic Flow
1. **User Profile Retrieval**  
   - Query the `TAMS_User` table for the row where `UserID` matches the supplied parameter.  
   - Return all columns of that user record.

2. **Company Information Retrieval**  
   - Determine the `CompanyID` belonging to the user from `TAMS_User`.  
   - Query `TAMS_Company` for the company whose `ID` equals that `CompanyID`.  
   - Return all columns of the company record.

3. **User Query Department Retrieval**  
   - Select all rows from `TAMS_User_QueryDept` where `UserID` equals the supplied parameter.  
   - Return every column of those rows.

4. **Role Permission Retrieval – DTL Line**  
   - For the **DTL** line and **TAR** module, join `TAMS_Role` with `TAMS_User_Role` on `RoleID`.  
   - Filter to roles that are active, not marked as “All”, and where the user’s role assignment matches the DTL line.  
   - Return the role’s `ID`, `RoleDesc`, `Line`, `TrackType`, `Module`, `Role`, and `UserID`.  
   - Repeat the same pattern for the **DTL** line and **OCC** module.

5. **Role Permission Retrieval – NEL Line**  
   - For the **NEL** line and **TAR** module, apply the same join and filters, ensuring the role’s `TrackType` is `mainline`.  
   - Return the same set of columns.  
   - Repeat for the **NEL** line and **OCC** module.

6. **Role Permission Retrieval – NEL Depot**  
   - For the **NEL** line with `TrackType` `Depot`, retrieve permissions for the **TAR** module.  
   - Return the same columns.  
   - Repeat for the **NEL** line with `TrackType` `Depot` and **DCC** module.

7. **Commented Sections**  
   - The procedure contains commented-out blocks that would retrieve permissions for a **SPLRT** line (both TAR and OCC modules). These are currently inactive and do not affect the output.

### Data Interactions
* **Reads:**  
  - `TAMS_User`  
  - `TAMS_Company`  
  - `TAMS_User_QueryDept`  
  - `TAMS_Role`  
  - `TAMS_User_Role`

* **Writes:**  
  - None. The procedure performs only SELECT operations.