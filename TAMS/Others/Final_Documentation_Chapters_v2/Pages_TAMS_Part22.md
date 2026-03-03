# Page: ViewProfile  
**File:** ViewProfile.aspx.cs  

### 1. User Purpose  
Users view and manage their profile information, including system selections and access settings.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data into the interface. |  
| SetupPage | Configures UI elements and binds data to controls. |  
| ResetPage | Clears form fields and resets the interface state. |  
| btn_externalNext_Click | Saves external user data and navigates to the next step in the process. |  
| btn_internalNewSave_Click | Validates internal user input, saves changes, and updates the database. |  

### 3. Data Interactions  
* **Reads:** User, BlockedTar  
* **Writes:** User, BlockedTar  

---

# Page: ViewSignUpStatus  
**File:** ViewSignUpStatus.aspx.cs  

### 1. User Purpose  
Users track the status of their account registration, including verification and resend options.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user registration status and displays relevant information. |  
| SetupPage | Binds user data from a dataset to the interface. |  
| btn_resendRegistrationLink_Click | Triggers a resend of the registration confirmation email. |  

### 3. Data Interactions  
* **Reads:** User  
* **Writes:** None  

---

# Page: ViewSwitcher  
**File:** ViewSwitcher.ascx.cs  

### 1. User Purpose  
Users switch between different views or panels within the application interface.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the default view and prepares the switcher for user interaction. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None