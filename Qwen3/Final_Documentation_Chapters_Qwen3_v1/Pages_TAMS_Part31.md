# Page: ViewProfile  
**File:** ViewProfile.aspx.cs  

### 1. User Purpose  
Users view and manage their profile information, including system selections and access settings.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data into the interface. |  
| SetupPage | Configures the UI based on user role (internal/external) and preloads system options. |  
| ResetPage | Clears form fields and resets the interface to its initial state. |  
| btn_externalNext_Click | Advances the external user through the profile setup workflow. |  
| btn_internalNewSave_Click | Saves internal user profile changes to the database. |  

### 3. Data Interactions  
* **Reads:** User, SystemSelection, AccessSettings  
* **Writes:** User, AccessSettings  

---

# Page: ViewSignUpStatus  
**File:** ViewSignUpStatus.aspx.cs  

### 1. User Purpose  
Users check the status of their registration request and manage resend options for verification links.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Displays user registration status based on provided dataset. |  
| SetupPage | Populates UI elements with user-specific registration details. |  
| btn_resendRegistrationLink_Click | Triggers a resend of the verification link to the user’s email. |  

### 3. Data Interactions  
* **Reads:** User, RegistrationStatus  
* **Writes:** RegistrationStatus  

---

# Page: ViewSwitcher  
**File:** ViewSwitcher.ascx.cs  

### 1. User Purpose  
Users switch between different views (e.g., internal vs. external) within the application.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Dynamically loads and displays the appropriate view based on user permissions. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None