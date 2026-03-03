# Procedure: sp_TAMS_TOA_Submit_Register
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of submitting a new TOA (Tender Order Acceptance) and updating its status to "Registered".

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(20) | The ID of the user who submitted the TOA |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the TOA status to "Registered" and records the current date and time as the registered time.
4. Inserts a new audit record into the TAMS_TOA_Audit table with the updated information.
5. Updates the parties' witness status in the TAMS_TOA_Parties table.
6. Updates the book-in time for the TOA in the TAMS_TOA_Parties table.
7. If any errors occur during these operations, sets an error message and returns it to the caller.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties

---

# Procedure: sp_TAMS_TOA_Surrender
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of surrendering a TOA and updating its status to "Surrendered".

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TOA being surrendered |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the TOA status to "Surrendered" and records the current date and time as the surrender time.
4. Inserts a new audit record into the TAMS_TOA_Audit table with the updated information.
5. If any errors occur during these operations, sets an error message and returns it to the caller.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA, TAMS_TOA_Audit

---

# Procedure: sp_TAMS_TOA_Update_Details
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of updating the details of a TOA.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @MobileNo | NVARCHAR(50) | The new mobile number for the TOA |
| @TetraRadioNo | NVARCHAR(50) | The new Tetra radio number for the TOA |
| @UserID | NVARCHAR(20) | The ID of the user who updated the TOA |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the mobile number and Tetra radio number for the TOA with the provided values.
4. Records the current date and time as the updated on date.
5. If any errors occur during these operations, sets an error message and returns it to the caller.

### Data Interactions
* Reads: TAMS_TOA
* Writes: TAMS_TOA

---

# Procedure: sp_TAMS_TOA_Update_TOA_URL
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of updating the TOA URL.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PLine | NVARCHAR(50) | The new line for the TOA URL |
| @PLoc | NVARCHAR(50) | The new location for the TOA URL |
| @PType | NVARCHAR(50) | The new type for the TOA URL |
| @EncPLine | NVARCHAR(100) | The encrypted line for the TOA URL |
| @EncPLoc | NVARCHAR(100) | The encrypted location for the TOA URL |
| @EncPType | NVARCHAR(100) | The encrypted type for the TOA URL |
| @GenURL | NVARCHAR(500) | The generated URL for the TOA |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Inserts a new record into the TAMS_TOA_URL table with the provided values.
4. If any errors occur during these operations, sets an error message and returns it to the caller.

### Data Interactions
* Writes: TAMS_TOA_URL

---

# Procedure: sp_TAMS_Update_Company_Details_By_ID
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of updating company details for a specific company ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompID | INT | The ID of the company to update |
| @Company | NVARCHAR(100) | The new company name |
| @BizOwner | NVARCHAR(200) | The new business owner |
| @CompanyOfficeNo | NVARCHAR(20) | The new company office number |
| @CompanyMobileNo | NVARCHAR(20) | The new company mobile number |
| @CompanyEmail | NVARCHAR(200) | The new company email |
| @IsActive | BIT | The new active status |
| @UpdatedBy | INT | The ID of the user who updated the company |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the company details with the provided values.
4. Records the current date and time as the updated on date.
5. If any errors occur during these operations, rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_Company
* Writes: TAMS_Company

---

# Procedure: sp_TAMS_Update_External_UserPasswordByUserID
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of updating the external user password for a specific user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to update |
| @Password | NVARCHAR(200) | The new password |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the external user password with the provided value.
4. Records the current date and time as the password changed date.
5. If any errors occur during these operations, rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User
* Writes: TAMS_User

---

# Procedure: sp_TAMS_Update_External_User_Details_By_ID
**Type:** Stored Procedure

Purpose: This stored procedure performs the business task of updating external user details for a specific user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to update |
| @Name | NVARCHAR(100) | The new name |
| @Dept | NVARCHAR(100) | The new department |
| @OfficeTel | NVARCHAR(100) | The new office phone number |
| @Mobile | NVARCHAR(100) | The new mobile number |
| @Email | NVARCHAR(200) | The new email |
| @SBSTContactPersonName | NVARCHAR(100) | The new SBST contact person name |
| @SBSTContactPersonDept | NVARCHAR(200) | The new SBST contact person department |
| @SBSTContactPersonOffTel | NVARCHAR(20) | The new SBST contact person office phone number |
| @ValidTo | NVARCHAR(20) | The new valid to date |
| @IsActive | BIT | The new active status |
| @UpdatedBy | INT | The ID of the user who updated the user |

### Logic Flow
1. Checks if a transaction is already in progress.
2. If not, sets an internal flag to indicate that a new transaction has started and begins a new transaction.
3. Updates the external user details with the provided values.
4. Records the current date and time as the updated on date.
5. If any errors occur during these operations, rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User
* Writes: TAMS_User