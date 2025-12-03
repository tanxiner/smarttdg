# Page: Login.aspx  
**File:** Login.aspx.cs  

### 1. User Purpose  
Users authenticate to access the system.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the login interface. |  
| btnLogin_Click | Validates user credentials, checks LAN authentication, and generates a token for session management. |  
| InternalLoginCheck | Performs core authentication logic, including password encryption and access validation. |  
| CheckAccess | Verifies user permissions and redirects based on role. |  
| GenerateToken | Creates a secure token for authenticated sessions. |  
| CheckLANAuthentication | Validates credentials against LAN-specific authentication systems. |  
| Encrypt | Encrypts sensitive data before storage or transmission. |  

### 3. Data Interactions  
* **Reads:** User, BlockedTar  
* **Writes:** None  

---

# Page: Logout.aspx  
**File:** Logout.aspx.cs  

### 1. User Purpose  
Users end their session and log out of the system.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Clears session data and redirects to the login page. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: MaintainCompany.aspx  
**File:** MaintainCompany.aspx.cs  

### 1. User Purpose  
Users search, view, and manage company records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the company management interface. |  
| SetupPage | Prepares the UI for company data entry or display. |  
| btn_search_Click | Filters and displays company records based on search criteria. |  
| btn_clear_Click | Resets search filters and clears input fields. |  

### 3. Data Interactions  
* **Reads:** Company, System  
* **Writes:** Company  

---

# Page: MaintainCompanyDetails.aspx  
**File:** MaintainCompanyDetails.aspx.cs  

### 1. User Purpose  
Users edit or update company details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads company details for editing. |  
| setupPage | Initializes the UI with company-specific data. |  
| btn_updateCompany_Click | Saves changes to the company record. |  
| btn_back_Click | Navigates back to the company list view. |  

### 3. Data Interactions  
* **Reads:** Company  
* **Writes:** Company  

---

# Page: MaintainUser.aspx  
**File:** MaintainUser.aspx.cs  

### 1. User Purpose  
Users search, view, and manage user records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the user management interface. |  
| SetupPage | Prepares the UI for user data entry or display. |  
| btn_search_Click | Filters and displays user records based on search criteria. |  
| btn_clear_Click | Resets search filters and clears input fields. |  

### 3. Data Interactions  
* **Reads:** User  
* **Writes:** User  

---

# Page: MaintainUserDetails.aspx  
**File:** MaintainUserDetails.aspx.cs  

### 1. User Purpose  
Users edit or update user details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user details for editing. |  
| setupPage | Initializes the UI with user-specific data. |  
| btn_updateUser_Click | Saves changes to the user record. |  
| btn_back_Click | Navigates back to the user list view. |  

### 3. Data Interactions  
* **Reads:** User  
* **Writes:** User