# Page: MaintainCompany  
**File:** MaintainCompany.aspx.cs  

### 1. User Purpose  
Users manage company information, including searching, clearing, and viewing company data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads company data dynamically. |  
| SetupPage | Configures UI elements and prepares the interface for user interaction. |  
| btn_search_Click | Filters and displays company records based on user input criteria. |  
| btn_clear_Click | Resets all input fields and clears displayed data. |  

### 3. Data Interactions  
* **Reads:** Company, SystemSelection  
* **Writes:** Company  

---

# Page: MaintainCompanyDetails  
**File:** MaintainCompanyDetails.aspx.cs  

### 1. User Purpose  
Users update specific company details based on a preselected company ID.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads company details into the form for editing. |  
| setupPage | Fetches and populates company data using the provided companyID. |  
| btn_updateCompany_Click | Saves modified company information to the database. |  
| btn_back_Click | Navigates back to the company listing view. |  

### 3. Data Interactions  
* **Reads:** Company  
* **Writes:** Company  

---

# Page: MaintainUser  
**File:** MaintainUser.aspx.cs  

### 1. User Purpose  
Users manage user information, including searching, clearing, and viewing user data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data dynamically. |  
| SetupPage | Configures UI elements and prepares the interface for user interaction. |  
| btn_search_Click | Filters and displays user records based on user input criteria. |  
| btn_clear_Click | Resets all input fields and clears displayed data. |  

### 3. Data Interactions  
* **Reads:** User, SystemSelection  
* **Writes:** User  

---

# Page: MaintainUserDetails  
**File:** MaintainUserDetails.aspx.cs  

### 1. User Purpose  
Users update specific user details based on a preselected user ID.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user details into the form for editing. |  
| setupPage | Fetches and populates user data using the provided userID. |  
| btn_updateUser_Click | Saves modified user information to the database. |  
| btn_back_Click | Navigates back to the user listing view. |  

### 3. Data Interactions  
* **Reads:** User  
* **Writes:** User