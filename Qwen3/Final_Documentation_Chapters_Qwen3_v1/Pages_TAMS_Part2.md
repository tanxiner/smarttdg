# Page: Default.aspx  
**File:** Default.aspx.cs  

### 1. User Purpose  
Users access this page to navigate the application's main interface.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default user settings. |  

### 3. Data Interactions  
* **Reads:** UserPreferences  
* **Writes:** None  

---

# Page: DepotTARAppList.aspx  
**File:** DepotTARAppList.aspx.cs  

### 1. User Purpose  
Users manage and view depot TAR applications, including filtering and navigating through records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the application list and binds data to UI controls. |  
| BindLocation | Populates location-based filters for the application list. |  
| lbSubmit_Click | Submits user input to filter or update the application list. |  
| displayLegend | Shows visual indicators for application statuses or categories. |  
| gvDir1_RowDataBound | Customizes grid rows to highlight specific application details. |  
| lnkD1StrTARNo_Click | Navigates to a detailed view for a specific TAR number. |  
| lbBack_Click | Returns to the previous navigation level (e.g., from a detail view). |  
| gvDir1Child_RowDataBound | Renders child grid rows for nested application data. |  
| ddlLine_SelectedIndexChanged | Filters the application list based on selected line or category. |  

### 3. Data Interactions  
* **Reads:** DepotApp, Location, TAR, Line  
* **Writes:** TAR (updates status or notes)