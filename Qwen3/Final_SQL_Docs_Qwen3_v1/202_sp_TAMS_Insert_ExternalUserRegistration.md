# Procedure: sp_TAMS_Insert_ExternalUserRegistration

### Purpose
This stored procedure performs the business task of inserting a new external user registration into the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UENNo | NVARCHAR(20) | Unique identifier for the external user. |
| @Company | NVARCHAR(200) | The company associated with the external user. |
| @Name | NVARCHAR(200) | The name of the external user. |
| @Email | NVARCHAR(500) | The email address of the external user. |
| @Dept | NVARCHAR(200) | The department of the external user. |
| @OfficeNo | NVARCHAR(20) | The office number of the external user. |
| @Mobile | NVARCHAR(20) | The mobile phone number of the external user. |
| @SBSTCPName | NVARCHAR(200) | The name of the SBSTC department. |
| @SBSTCPDept | NVARCHAR(200) | The department of the SBSTC. |
| @SBSTCPOfficeNo | NVARCHAR(20) | The office number of the SBSTC. |
| @ValidTo | NVARCHAR(20) | The date until which the registration is valid. |
| @Purpose | NVARCHAR(MAX) | The purpose of the external user's registration. |
| @LoginID | NVARCHAR(200) | The login ID for the external user. |
| @Password | NVARCHAR(100) | The password for the external user. |

### Logic Flow
1. The procedure starts by encrypting the provided password using the `dbo.EncryptString` function.
2. It then inserts a new record into the `TAMS_Registration` table, specifying all required fields and parameters.
3. If an error occurs during this insertion process, the transaction is rolled back to maintain database consistency.

### Data Interactions
* **Reads:** None explicitly listed in the procedure code.
* **Writes:** 
  * TAMS_Registration table