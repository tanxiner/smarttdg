# Page: RGSPrint  
**File:** RGSPrint.aspx.cs  

### 1. User Purpose  
Users view and interact with a list of RGS records through data-bound grid actions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and binds data to the GridView (gvRGS). |  
| gvRGS_RowDataBound | Customizes GridView rows (e.g., formatting, adding controls) during data binding. |  
| gvRGS_RowCommand | Handles user actions like editing or deleting specific RGS records. |  

### 3. Data Interactions  
* **Reads:** RGS, User, System  
* **Writes:** RGS, User  

---

# Page: RegistrationInbox  
**File:** RegistrationInbox.aspx.cs  

### 1. User Purpose  
Users manage and view pending registration requests from users.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user-specific registration data and initializes the page. |  
| SetupPage | Configures the page with user-specific settings and data. |  
| EncryptID | Encrypts IDs in datasets to ensure secure data handling. |  

### 3. Data Interactions  
* **Reads:** User, RegistrationRequest  
* **Writes:** RegistrationRequest  

---

# Page: RegistrationRequest  
**File:** RegistrationRequest.aspx.cs  

### 1. User Purpose  
Users manage user registration requests, assign access roles, and update approval statuses.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads registration details and initializes the request form. |  
| SetupPage | Prepares the page with specific registration module data. |  
| BuildPage | Populates the form with user registration details. |  
| ResetPage | Clears form fields and resets the page state. |  
| btn_back_Click | Navigates back to the previous registration step. |  
| btn_assignAccess_Click | Assigns system roles to the requesting user. |  
| btn_rejectRequest_Click | Marks the registration request as rejected. |  
| btn_approveCompany_Click | Approves a company's registration request. |  
| btn_rejectCompany_Click | Rejects a company's registration request. |  
| btn_resendLink_Click | Resends the verification link to the user. |  
| btn_deleteRequest_Click | Removes the registration request from the system. |  

### 3. Data Interactions  
* **Reads:** UserRegistration, Company, Role, System  
* **Writes:** UserRegistration, Company, Role  

---

# Page: ResetPassword  
**File:** ResetPassword.aspx.cs  

### 1. User Purpose  
Users reset their passwords using a verification link sent via email.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the password reset form with user-specific data. |  
| setupPage | Initializes the form with user registration details. |  
| btn_externalSave_Click | Saves the new password after verification. |  
| btn_externalCancel_Click | Cancels the password reset process and exits. |  

### 3. Data Interactions  
* **Reads:** UserRegID, User  
* **Writes:** User