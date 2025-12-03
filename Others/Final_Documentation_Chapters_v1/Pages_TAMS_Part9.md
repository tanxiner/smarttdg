# Page: OCC_HoursAuthorisation  
**File:** OCC_HoursAuthorisation.aspx.cs  

### 1. User Purpose  
Users submit and preview authorization requests for OCC hours.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads data into the GridView. |  
| BindGrid | Loads user data and authorization details into the GridView. |  
| LoadOCCAuthCtrl_DTL | Populates detailed authorization controls with user-specific data. |  
| LoadOCCAuthCtrl_NEL | Loads non-essential line data for authorization context. |  
| GridView1_RowDataBound | Formats GridView rows for visual clarity (e.g., highlights status). |  
| GridView1_RowCreated | Sets up row templates for dynamic content rendering. |  
| btnSubmit_Click | Validates inputs, saves authorization data, and triggers confirmation. |  
| ddlLine_SelectedIndexChanged | Filters displayed data based on selected line. |  
| btnPreview_Click | Generates a preview of the authorization request for review. |  

### 3. Data Interactions  
* **Reads:** User, OCCAuthorization, DutyRoster, Line  
* **Writes:** OCCAuthorization  

---

# Page: OCC_HoursAuthorisation_Preview  
**File:** OCC_HoursAuthorisation_Preview.aspx.cs  

### 1. User Purpose  
Users view a preview of submitted OCC hours authorization requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads preview data into the GridView and initializes controls. |  
| BindGrid | Loads filtered authorization data for preview display. |  
| LoadDutyRoster_Ctrl | Displays duty roster details for context. |  
| LoadOCCAuthPreviewCtrl_DTL | Loads detailed authorization data for preview. |  
| LoadOCCAuthPreviewCtrl_NEL | Loads non-essential line data for preview context. |  
| ddlLine_SelectedIndexChanged | Filters preview data based on selected line. |  
| btnSearchOCC_Preview_Click | Searches for specific authorization records to preview. |  
| btnBackToOCCAuth_Click | Navigates back to the main authorization submission page. |  

### 3. Data Interactions  
* **Reads:** User, DutyRoster, OCCAuthorization, Line  
* **Writes:** None  

---

# Page: OPD  
**File:** OPD.aspx.cs  

### 1. User Purpose  
Users manage operational data (OPD) by viewing, filtering, and refreshing records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default data. |  
| PopOnLoad | Populates initial data or filters based on user context. |  
| ddlLine_SelectedIndexChanged | Filters displayed OPD records based on selected line. |  
| lbRefresh_Click | Reloads and updates the displayed OPD data. |  

### 3. Data Interactions  
* **Reads:** User, OPD  
* **Writes:** OPD