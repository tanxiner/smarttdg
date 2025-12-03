# Page: OCC_HoursAuthorisation_Preview  
**File:** OCC_HoursAuthorisation_Preview.aspx.cs  

### 1. User Purpose  
Users preview authorized OCC hours and manage duty roster data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and loads default data. |  
| BindGrid | Loads and displays authorized OCC hours data in a grid. |  
| LoadDutyRoster_Ctrl | Populates duty roster details for the current user. |  
| LoadOCCAuthPreviewCtrl_DTL | Loads detailed authorization data for the preview. |  
| LoadOCCAuthPreviewCtrl_NEL | Loads non-essential line data for the preview. |  
| ddlLine_SelectedIndexChanged | Filters data based on selected line and updates the grid. |  
| btnSearchOCC_Preview_Click | Triggers a search for specific OCC hours and refreshes the grid. |  
| btnBackToOCCAuth_Click | Navigates the user back to the main authorization interface. |  

### 3. Data Interactions  
* **Reads:** DutyRoster, OCCAuthorization, User  
* **Writes:** OCCAuthorization (updates or saves changes)  

---

# Page: OPD  
**File:** OPD.aspx.cs  

### 1. User Purpose  
Users manage operational data and refresh line information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and loads default line data. |  
| PopOnLoad | Populates initial operational data and line details. |  
| ddlLine_SelectedIndexChanged | Filters operational data based on selected line. |  
| lbRefresh_Click | Reloads and updates line information from the database. |  

### 3. Data Interactions  
* **Reads:** Line, OperationalData  
* **Writes:** OperationalData (updates or saves changes)