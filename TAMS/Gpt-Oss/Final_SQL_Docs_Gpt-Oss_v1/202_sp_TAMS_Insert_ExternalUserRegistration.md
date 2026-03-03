# Procedure: sp_TAMS_Insert_ExternalUserRegistration

### Purpose
Insert a new external user registration record into the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UENNo | NVARCHAR(20) | Unique Entity Number of the company |
| @Company | NVARCHAR(200) | Company name |
| @Name | NVARCHAR(200) | Full name of the user |
| @Email | NVARCHAR(500) | Email address |
| @Dept | NVARCHAR(200) | Department |
| @OfficeNo | NVARCHAR(20) | Office telephone number |
| @Mobile | NVARCHAR(20) | Mobile phone number |
| @SBSTCPName | NVARCHAR(200) | Name of the SBSTCP contact |
| @SBSTCPDept | NVARCHAR(200) | Department of the SBSTCP contact |
| @SBSTCPOfficeNo | NVARCHAR(20) | Office number of the SBSTCP contact |
| @ValidTo | NVARCHAR(20) | Expiry date of the registration (string in dd/mm/yyyy format) |
| @Purpose | NVARCHAR(MAX) | Purpose of the registration |
| @LoginID | NVARCHAR(200) | Login identifier for the user |
| @Password | NVARCHAR(100) | Plain‑text password to be encrypted |

### Logic Flow
1. The supplied @Password is encrypted by calling the dbo.EncryptString function.  
2. An INSERT statement is executed against the TAMS_Registration table.  
   * The INSERT uses the OUTPUT clause to return the newly generated ID, but the value is not captured or used within the procedure.  
   * Values are supplied in the order expected by the table: LoginID, Name, Email, OfficeNo, Mobile, an empty string for the 6th column, Dept, the current date/time for the creation timestamp, the @ValidTo string converted to a date using style 103 (dd/mm/yyyy), Purpose, a hard‑coded status flag of 1, the encrypted password, UENNo, Company, five NULLs for unused columns, SBSTCPName, SBSTCPDept, SBSTCPOfficeNo, the current date/time again, a hard‑coded flag of 1, the current date/time, and a final hard‑coded flag of 1.  
3. The commented transaction block is ignored; the insert occurs without an explicit transaction.

### Data Interactions
* **Reads:** none  
* **Writes:** TAMS_Registration