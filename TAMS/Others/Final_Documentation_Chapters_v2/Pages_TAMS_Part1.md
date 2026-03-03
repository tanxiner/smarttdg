# Page: AddCompany  
**File:** AddCompany.aspx.cs  

### 1. User Purpose  
Users add new company information to the system.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads existing company data if needed. |  
| setupPage | Prepares the form by setting default values or loading related data. |  
| btn_externalSave_Click | Validates user input, saves the new company to the database, and redirects the user. |  
| btn_externalCancel_Click | Navigates the user back to the previous page without saving changes. |  

### 3. Data Interactions  
* **Reads:** Company, UserRegID  
* **Writes:** Company  

---

# Page: AnonymousSite  
**File:** AnonymousSite.Master.cs  

### 1. User Purpose  
Provides a layout for anonymous user access to the application.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Sets up the master page structure and initializes anonymous user session data. |  

### 3. Data Interactions  
* **Reads:** User session data (if any)  
* **Writes:** None  

---

# Page: Default  
**File:** Default.aspx.cs  

### 1. User Purpose  
Displays the homepage or default landing page for authenticated users.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the homepage content and initializes user-specific data. |  

### 3. Data Interactions  
* **Reads:** User session data  
* **Writes:** None  

---

# Page: DepotTARAppList  
**File:** DepotTARAppList.aspx.cs  

### 1. User Purpose  
Allows users to view and manage a list of depot TAR applications.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads and binds the list of TAR applications to the UI. |  
| BindLocation | Populates location-based filters or dropdowns. |  
| lbSubmit_Click | Handles form submission to filter or update TAR applications. |  
| gvDir1_RowDataBound | Formats rows in the GridView to display application details. |  
| lnkD1StrTARNo_Click | Navigates to a detailed view of a specific TAR application. |  
| lbBack_Click | Returns the user to the previous navigation level. |  
| ddlLine_SelectedIndexChanged | Filters TAR applications based on selected line options. |  

### 3. Data Interactions  
* **Reads:** TARApplication, Location, Line  
* **Writes:** TARApplication (via updates or submissions)