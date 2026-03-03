# Procedure: sp_TAMS_Update_External_User_Details_By_ID

### Purpose
Updates the details of an external user identified by UserID in the TAMS_User table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | Identifier of the user to update |
| @Name | NVARCHAR(100) | New full name |
| @Dept | NVARCHAR(100) | New department |
| @OfficeTel | NVARCHAR(100) | New office telephone number |
| @Mobile | NVARCHAR(100) | New mobile number |
| @Email | NVARCHAR(200) | New email address |
| @SBSTContactPersonName | NVARCHAR(100) | New contact person name |
| @SBSTContactPersonDept | NVARCHAR(200) | New contact person department |
| @SBSTContactPersonOffTel | NVARCHAR(20) | New contact person office number |
| @ValidTo | NVARCHAR(20) | New validity end date |
| @IsActive | BIT | New active status flag |
| @UpdatedBy | INT | Identifier of the user performing the update |

### Logic Flow
1. Begin a TRY block and start a transaction.  
2. Check if a record exists in TAMS_User where UserID equals @UserID.  
3. If the record exists, execute an UPDATE on that row, setting each column to the corresponding input parameter and updating UpdatedOn to the current date/time.  
4. Commit the transaction.  
5. If any error occurs, roll back the transaction in the CATCH block.

### Data Interactions
* **Reads:** TAMS_User  
* **Writes:** TAMS_User  

---