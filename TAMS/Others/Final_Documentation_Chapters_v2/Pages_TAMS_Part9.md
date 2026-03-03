# Page: OCC_HoursAuthorisation  
**File:** OCC_HoursAuthorisation.aspx.cs  

### 1. User Purpose  
Users submit and preview hours authorizations for approval.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default data. |  
| BindGrid | Loads and displays authorization records in a grid. |  
| LoadOCCAuthCtrl_DTL | Populates detailed authorization information. |  
| LoadOCCAuthCtrl_NEL | Loads non-essential line data for the authorization. |  
| GridView1_RowDataBound | Formats grid rows based on data context. |  
| GridView1_RowCreated | Sets up grid row structure for dynamic content. |  
| btnSubmit_Click | Validates inputs, saves authorization data, and triggers confirmation. |  
| ddlLine_SelectedIndexChanged | Filters authorization records based on line selection. |  
| btnPreview_Click | Generates a preview of the authorization for review. |  

### 3. Data Interactions  
* **Reads:** User, OCCAuthorization, DutyRoster  
* **Writes:** OCCAuthorization  

---

# Page: OCC_HoursAuthorisation_Preview  
**File:** OCC_HoursAuthorisation_Preview.aspx.cs  

### 1. User Purpose  
Users preview and search for hours authorization details before final submission.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the preview interface and initializes search parameters. |  
| BindGrid | Displays filtered authorization records in a grid. |  
| LoadDutyRoster_Ctrl | Loads duty roster data for context. |  
| LoadOCCAuthPreviewCtrl_DTL | Populates detailed authorization information for preview. |  
| LoadOCCAuthPreviewCtrl_NEL | Loads non-essential line data for the preview. |  
| ddlLine_SelectedIndexChanged | Filters preview data based on line selection. |  
| btnSearchOCC_Preview_Click | Executes a search for specific authorization records. |  
| btnBackToOCCAuth_Click | Navigates back to the main authorization form. |  

### 3. Data Interactions  
* **Reads:** User, DutyRoster, OCCAuthorization  
* **Writes:** None  

---

# Page: OPD  
**File:** OPD.aspx.cs  

### 1. User Purpose  
Users manage and refresh operational data records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default operational data. |  
| PopOnLoad | Preloads critical data or configurations on page load. |  
| ddlLine_SelectedIndexChanged | Filters operational records based on line selection. |  
| lbRefresh_Click | Reloads and updates operational data dynamically. |  

### 3. Data Interactions  
* **Reads:** User, OPDRecord  
* **Writes:** OPDRecord