# Procedure: sp_TAMS_Insert_UserQueryDeptByUserID

### Purpose
Insert a new user‑department query record when none exists for the specified user and department.

### Parameters
| Name      | Type      | Purpose |
| :-------- | :-------- | :------ |
| @UserID   | INT       | Identifier of the user. |
| @Dept     | NVARCHAR(100) | Department name to associate. |
| @UpdatedBy| INT       | Identifier of the user performing the update. |

### Logic Flow
1. Begin a transaction.  
2. Check if a record already exists in **TAMS_User_QueryDept** with the given @UserID and @Dept.  
3. If no such record exists:  
   1. Retrieve the department line from **TAMS_Parameters** where ParaCode is 'Company', ParaValue2 matches @Dept, and the current date falls between EffectiveDate and ExpiryDate.  
   2. Using the retrieved line, find the role ID in **TAMS_Role** where Line equals the line and Role starts with the line followed by 'ApplicantHOD'.  
   3. Insert a new row into **TAMS_User_QueryDept** with @UserID, the found role ID, @Dept, current timestamps, and @UpdatedBy.  
4. Commit the transaction.  
5. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_User_QueryDept, TAMS_Parameters, TAMS_Role  
* **Writes:** TAMS_User_QueryDept  

---