# Procedure: sp_TAMS_Update_User_Details_By_ID

### Purpose
Updates the contact and status details of a user identified by UserID in the TAMS_User table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | Identifier of the user to update |
| @Name | NVARCHAR(100) | New full name |
| @Email | NVARCHAR(200) | New email address |
| @Mobile | NVARCHAR(20) | New mobile number |
| @OfficeTel | NVARCHAR(20) | New office telephone number |
| @Dept | NVARCHAR(100) | New department name |
| @ValidTo | NVARCHAR(20) | New validity end date |
| @IsActive | BIT | New active status flag |
| @UpdatedBy | INT | Identifier of the user performing the update |

### Logic Flow
1. Begin a TRY block and start a transaction.  
2. Check if a record exists in TAMS_User where UserID equals @UserID.  
3. If the record exists, execute an UPDATE on that row, setting each column to the corresponding input parameter and updating UpdatedOn to the current date/time.  
4. Commit the transaction.  
5. If any error occurs during the TRY block, catch it, roll back the transaction, and exit.

### Data Interactions
* **Reads:** TAMS_User  
* **Writes:** TAMS_User

---