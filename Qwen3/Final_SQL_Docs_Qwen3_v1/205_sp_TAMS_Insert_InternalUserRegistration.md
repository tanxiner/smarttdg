# Procedure: sp_TAMS_Insert_InternalUserRegistration

### Purpose
This stored procedure performs internal user registration by inserting a new record into the TAMS_Registration table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SapNo | NVARCHAR(20) | Unique SAP number for the registered user. |
| @Name | NVARCHAR(200) | Full name of the registered user. |
| @UserName | NVARCHAR(200) | Username chosen by the registered user. |
| @Email | NVARCHAR(500) | Email address of the registered user. |
| @Mobile | NVARCHAR(20) | Mobile number of the registered user. |
| @OfficeNo | NVARCHAR(20) | Office number of the registered user. |
| @Dept | NVARCHAR(100) | Department of the registered user. |
| @ValidTo | NVARCHAR(100) | Date until which the registration is valid. |
| @Purpose | NVARCHAR(MAX) | Purpose of the internal user registration. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then attempts to insert a new record into the TAMS_Registration table using the provided parameters, including the username as the primary key.
3. If the insertion is successful, the procedure commits the transaction.
4. If an error occurs during the insertion process, the procedure rolls back the transaction.

### Data Interactions
* **Reads:** None explicitly listed in this procedure.
* **Writes:** TAMS_Registration table