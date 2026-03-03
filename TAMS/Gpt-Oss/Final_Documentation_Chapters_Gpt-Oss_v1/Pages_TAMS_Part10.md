# Page: MaintainCompany  
**File:** MaintainCompany.aspx.cs  

### 1. User Purpose  
Users search for and view a list of companies.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, calls `SetupPage` to populate any dropdowns or controls needed for searching. |
| SetupPage | Retrieves lookup data (e.g., system selections) and binds it to the search controls. |
| buildDummySystemSelectiondata | Generates a temporary data table used to populate a system‑selection dropdown when no real data is available. |
| btn_search_Click | Gathers search criteria from the form, queries the company database, encrypts returned IDs via `EncryptID`, and displays the results in a grid. |
| btn_clear_Click | Resets all search fields to their default state and clears any displayed results. |
| EncryptID | Takes a `DataSet` of company records, encrypts each company ID for security, and returns the modified set for display. |

### 3. Data Interactions  
* **Reads:** Company table, SystemSelection lookup data.  
* **Writes:** None.  

---  

# Page: MaintainCompanyDetails  
**File:** MaintainCompanyDetails.aspx.cs  

### 1. User Purpose  
Users view and edit the details of a selected company.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Extracts the company ID from the query string, then calls `setupPage` to load the company’s current data into the form. |
| setupPage | Queries the company record by ID, populates form fields (name, address, etc.), and prepares any related lookup data. |
| btn_updateCompany_Click | Validates the edited fields, updates the company record in the database, and displays a success or error message. |
| btn_back_Click | Redirects the user back to the company search page. |

### 3. Data Interactions  
* **Reads:** Company record by ID.  
* **Writes:** Updated company record.  

---  

# Page: MaintainUser  
**File:** MaintainUser.aspx.cs  

### 1. User Purpose  
Users search for and view a list of system users.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On initial load, invokes `SetupPage` to fill any search dropdowns (e.g., roles, departments). |
| SetupPage | Retrieves lookup data for user search controls and binds it. |
| btn_search_Click | Collects search criteria, queries the user database, encrypts returned user IDs via `EncryptID`, and displays the results. |
| btn_clear_Click | Clears all search inputs and any displayed results. |
| EncryptID | Encrypts each user ID in the returned `DataSet` before it is bound to the results grid. |

### 3. Data Interactions  
* **Reads:** User table, role/department lookup data.  
* **Writes:** None.  

---  

# Page: MaintainUserDetails  
**File:** MaintainUserDetails.aspx.cs  

### 1. User Purpose  
Users view and edit the details of a selected system user.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Retrieves the user ID from the query string and calls `setupPage` to load the user’s current data into the form. |
| setupPage | Queries the user record by ID, populates form fields (name, email, role, etc.), and prepares any related lookup data. |
| btn_updateUser_Click | Validates the edited fields, updates the user record in the database, and shows a confirmation or error message. |
| btn_back_Click | Navigates back to the user search page. |

### 3. Data Interactions  
* **Reads:** User record by ID.  
* **Writes:** Updated user record.  

---