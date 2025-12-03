# Page: ViewProfile  
**File:** ViewProfile.aspx.cs  

### 1. User Purpose  
Users view and manage their profile information, including system access settings.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data into the interface. |  
| SetupPage | Configures UI elements based on user role (internal/external). |  
| ResetPage | Clears form fields and resets the interface state. |  
| buildSystemSelectiondata | Generates dropdown options for system selection based on user type. |  
| UpdateGVRows | Populates grid views with user-specific data rows. |  
| btn_externalNext_Click | Advances external users through multi-step profile setup. |  
| btn_internalNewSave_Click | Saves internal user profile changes to the database. |  

### 3. Data Interactions  
* **Reads:** User, System, AccessLevel  
* **Writes:** User, AccessLevel  

---

# Page: ViewSignUpStatus  
**File:** ViewSignUpStatus.aspx.cs  

### 1. User Purpose  
Users track the status of their registration request and manage resend options.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Displays user registration status and associated data. |  
| SetupPage | Binds user data from a dataset to UI controls. |  
| ResetPage | Clears UI state and resets display settings. |  
| btn_externalBack_Click | Navigates external users back to a previous registration step. |  
| btn_internalBack_Click | Returns internal users to a prior registration stage. |  
| btn_resendRegistrationLink_Click | Triggers a resend of the registration confirmation email. |  

### 3. Data Interactions  
* **Reads:** User, RegistrationStatus  
* **Writes:** RegistrationStatus  

---

# Page: ViewSwitcher  
**File:** ViewSwitcher.ascx.cs  

### 1. User Purpose  
Users switch between different views (e.g., internal vs. external interfaces).  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the current view based on user permissions or URL parameters. |  

### 3. Data Interactions  
* **Reads:** ViewConfiguration  
* **Writes:** None