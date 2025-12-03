# Page: RGSEnquiry  
**File:** RGSEnquiry.aspx.cs  

### 1. User Purpose  
Users view and filter RGS data by line and track, refresh results, and print reports.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads dropdowns, and sets up the grid view. |  
| loadDepotControl | Populates depot selection options for filtering. |  
| PopOnLoad | Sets default values for line and track filters. |  
| gvRGS_RowDataBound | Formats grid rows for display (e.g., highlights status). |  
| ddlLine_SelectedIndexChanged | Filters RGS data based on selected line. |  
| ddlTrack_SelectedIndexChanged | Filters RGS data based on selected track. |  
| lbRefresh_Click | Reloads RGS data with current filters. |  
| gvRGS_RowCommand | Handles user actions like editing or deleting RGS records. |  
| lbPrint_Click | Triggers printing of the RGS grid in a formatted layout. |  

### 3. Data Interactions  
* **Reads:** RGS, Line, Track  
* **Writes:** None  

---

# Page: RGSPrint  
**File:** RGSPrint.aspx.cs  

### 1. User Purpose  
Users print RGS data in a formatted layout.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads RGS data into the grid for printing. |  
| gvRGS_RowDataBound | Applies formatting to grid rows for print (e.g., bold headers). |  
| gvRGS_RowCommand | Handles print-related actions (e.g., exporting to PDF). |  

### 3. Data Interactions  
* **Reads:** RGS  
* **Writes:** None  

---

# Page: RegistrationInbox  
**File:** RegistrationInbox.aspx.cs  

### 1. User Purpose  
Users manage registration inbox items, view encrypted data, and set up user pages.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user-specific inbox data and initializes the grid. |  
| SetupPage | Configures page settings based on the logged-in user. |  
| EncryptID | Applies encryption to data identifiers for security. |  

### 3. Data Interactions  
* **Reads:** User, Message  
* **Writes:** None