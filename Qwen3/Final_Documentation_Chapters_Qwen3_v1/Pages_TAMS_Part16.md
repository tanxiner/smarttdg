# Page: RegistrationRequest  
**File:** RegistrationRequest.aspx.cs  

### 1. User Purpose  
Users manage registration requests by approving, rejecting, or modifying access for new users.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data based on the request context. |  
| SetupPage | Prepares the interface with specific registration details and permissions. |  
| BuildPage | Constructs the UI elements for editing or viewing a registration request. |  
| ResetPage | Clears form fields and resets the user interface to a default state. |  
| btn_back_Click | Navigates the user back to a previous step in the registration workflow. |  
| btn_assignAccess_Click | Grants or modifies access rights for the requested user. |  
| btn_rejectRequest_Click | Marks the registration request as rejected and updates its status. |  
| btn_approveCompany_Click | Approves a company's registration request and finalizes the process. |  
| btn_rejectCompany_Click | Rejects a company's registration request and updates its status. |  
| btn_resendLink_Click | Sends a new confirmation link to the user's registered email address. |  
| btn_deleteRequest_Click | Removes the registration request from the system. |  

### 3. Data Interactions  
* **Reads:** UserRegistration, Company, SystemRole  
* **Writes:** UserRegistration, Company, SystemRole  

---

# Page: ResetPassword  
**File:** ResetPassword.aspx.cs  

### 1. User Purpose  
Users reset their password by entering a new one and confirming it.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the password reset form and initializes user-specific data. |  
| setupPage | Populates the form with user details based on the provided UserRegID. |  
| btn_externalSave_Click | Validates the new password, updates the user's credentials, and confirms the change. |  
| btn_externalCancel_Click | Cancels the password reset process and redirects the user to a previous page. |  

### 3. Data Interactions  
* **Reads:** UserRegistration  
* **Writes:** UserRegistration