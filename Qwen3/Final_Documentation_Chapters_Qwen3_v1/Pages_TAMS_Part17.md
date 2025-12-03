# Page: SignUpNewSystem  
**File:** SignUpNewSystem.aspx.cs  

### 1. User Purpose  
Users register a new system by providing details and selecting system types.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads system data for display. |  
| SetupPage | Configures the form layout and pre-fills fields based on user context. |  
| ResetPage | Clears form inputs and resets the UI state. |  
| buildSystemSelectiondata | Generates a dataset of system options for dropdowns or grids. |  
| UpdateGVRows | Populates grid rows with system details and formatting. |  
| gv_internalNewSystem_RowDataBound | Applies conditional styling or labels to grid rows. |  
| btn_externalNext_Click | Advances the user to the next step in the external system registration flow. |  
| btn_internalNewSave_Click | Validates inputs, saves the new system record, and confirms completion. |  

### 3. Data Interactions  
* **Reads:** System, User, BlockedTar  
* **Writes:** System, User  

---

# Page: SiteMaster  
**File:** Site.Master.cs  

### 1. User Purpose  
Provides navigation and user-specific actions for the main application layout.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| linkB_signUpNewSystem_Click | Redirects the user to the `SignUpNewSystem` page. |  
| Page_Load | Loads user-specific data (e.g., profile links) into the master page. |  

### 3. Data Interactions  
* **Reads:** User, System  
* **Writes:** None  

---

# Page: SummaryReport  
**File:** SummaryReport.aspx.cs  

### 1. User Purpose  
Users generate and filter summary reports based on system or line selections.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads default report parameters and initializes the UI. |  
| lbSearch_Click | Triggers report generation based on user input. |  
| ddlLine_SelectedIndexChanged | Updates available report options based on selected line. |  
| PopOnLoad | Pre-fills dropdowns or filters with default values. |  

### 3. Data Interactions  
* **Reads:** ReportData, Line, System  
* **Writes:** None