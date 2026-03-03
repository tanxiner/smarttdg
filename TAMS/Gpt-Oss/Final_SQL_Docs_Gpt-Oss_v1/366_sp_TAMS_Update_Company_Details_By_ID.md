# Procedure: sp_TAMS_Update_Company_Details_By_ID

### Purpose
Updates the details of a company record identified by its ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompID | INT | Identifier of the company to update |
| @Company | NVARCHAR(100) | New company name |
| @BizOwner | NVARCHAR(200) | New business owner name |
| @CompanyOfficeNo | NVARCHAR(20) | New office phone number |
| @CompanyMobileNo | NVARCHAR(20) | New mobile phone number |
| @CompanyEmail | NVARCHAR(200) | New email address |
| @IsActive | BIT | (Unused in current logic) |
| @UpdatedBy | INT | User ID performing the update |

### Logic Flow
1. Begin a TRY block and start a transaction.  
2. Check if a record exists in **TAMS_Company** where **ID** equals **@CompID**.  
3. If the record exists, execute an UPDATE on that row, setting the columns **Company**, **BizOwner**, **CompanyOfficeNo**, **CompanyMobileNo**, **CompanyEmail**, **UpdatedBy**, and **UpdatedOn** to the supplied values, with **UpdatedOn** set to the current date/time.  
4. Commit the transaction.  
5. If any error occurs, roll back the transaction.

### Data Interactions
* **Reads:** TAMS_Company  
* **Writes:** TAMS_Company  

---