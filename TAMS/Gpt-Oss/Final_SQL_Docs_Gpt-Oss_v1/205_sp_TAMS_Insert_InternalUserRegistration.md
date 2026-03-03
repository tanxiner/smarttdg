# Procedure: sp_TAMS_Insert_InternalUserRegistration

### Purpose
Inserts a new internal user registration record into TAMS_Registration.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SapNo | NVARCHAR(20) | SAP identifier for the user |
| @Name | NVARCHAR(200) | Full name of the user |
| @UserName | NVARCHAR(200) | Login name for the user |
| @Email | NVARCHAR(500) | Email address of the user |
| @Mobile | NVARCHAR(20) | Mobile phone number |
| @OfficeNo | NVARCHAR(20) | Office telephone number |
| @Dept | NVARCHAR(100) | Department of the user |
| @ValidTo | NVARCHAR(100) | (Unused in current logic) |
| @Purpose | NVARCHAR(MAX) | Reason for registration |

### Logic Flow
1. Begin a TRY block to handle potential errors.  
2. Start a database transaction.  
3. Insert a new row into TAMS_Registration using the supplied parameters and a set of constant values:  
   - @UserName, @Name, @Email, @OfficeNo, @Mobile, @SapNo, @Dept are inserted directly.  
   - The current date is used for the registration date.  
   - A far‑future date '2999-12-31' is set as the expiration date.  
   - @Purpose is stored.  
   - Several columns are set to 0 or NULL as placeholders.  
   - Additional timestamps and flags are set to the current date or 1.  
4. Capture the generated ID of the inserted row via the OUTPUT clause.  
5. Commit the transaction to persist the changes.  
6. If any error occurs, the CATCH block rolls back the transaction to maintain data integrity.

### Data Interactions
* **Reads:** None  
* **Writes:** TAMS_Registration

---