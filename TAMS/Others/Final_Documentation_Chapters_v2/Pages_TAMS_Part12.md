# Page: SignUpNewSystem  
**File:** SignUpNewSystem.aspx.cs  

### 1. User Purpose  
Users register new systems, either internally or externally, and submit the information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads system data for display. |  
| SetupPage | Configures the UI for internal system registration. |  
| ResetPage | Clears form fields and resets the interface state. |  
| buildSystemSelectiondata | Generates a data table of system options based on user type (internal/external). |  
| UpdateGVRows | Binds system data to GridView rows for display. |  
| gv_internalNewSystem_RowDataBound | Formats GridView rows to highlight critical system details. |  
| btn_externalNext_Click | Advances the external system registration workflow to the next step. |  
| btn_internalNewSave_Click | Validates internal system details, saves the record, and confirms completion. |  

### 3. Data Interactions  
* **Reads:** System, User, BlockedTar  
* **Writes:** System, User  

---

# Page: SiteMaster  
**File:** Site.Master.cs  

### 1. User Purpose  
Users access the new system registration page from the main menu.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| linkB_signUpNewSystem_Click | Redirects the user to the `SignUpNewSystem` page. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: Site_Mobile  
**File:** Site.Mobile.Master.cs  

### 1. User Purpose  
Users access the new system registration page from the mobile menu.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads mobile-specific layout and navigation elements. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: SummaryReport  
**File:** SummaryReport.aspx.cs  

### 1. User Purpose  
Users search and filter summary reports by line.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| lbSearch_Click | Triggers a search for report data based on user input. |  
| ddlLine_SelectedIndexChanged | Filters report results dynamically based on selected line. |  
| PopOnLoad | Loads default report data when the page first loads. |  

### 3. Data Interactions  
* **Reads:** Report, Line  
* **Writes:** None  

---

# Page: TARAppList  
**File:** TARAppList.aspx.cs  

### 1. User Purpose  
Users submit or modify TAR applications and view related data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| lbSubmit_Click | Validates TAR application details and submits the record. |  
| displayLegend | Renders a legend for interpreting TAR application statuses. |  
| gvDir2_RowDataBound | Formats GridView rows for directory 2 TAR applications. |  
| gvDir1_RowDataBound | Formats GridView rows for directory 1 TAR applications. |  
| lnkD2StrTARNo_Click | Opens details for a specific directory 2 TAR application. |  
| lnkD1StrTARNo_Click | Opens details for a specific directory 1 TAR application. |  
| lbBack_Click | Navigates back to the previous TAR application list view. |  
| gvDir2Child_RowDataBound | Formats child GridView rows for directory 2 TAR applications. |  
| gvDir1Child_RowDataBound | Formats child GridView rows for directory 1 TAR applications. |  

### 3. Data Interactions  
* **Reads:** TARApp, Dir2, Dir1, Dir2Child, Dir1Child  
* **Writes:** TARApp