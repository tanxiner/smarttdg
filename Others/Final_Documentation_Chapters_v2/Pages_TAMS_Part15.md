# Page: TAREnquiry_Detail  
**File:** TAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users manage and view details of a Track Access Request (TAR) enquiry, including possession limits and approvals.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds possession limit data, and loads TAR enquiry details. |  
| BindPossessionLimit | Loads possession limit records for display in the grid. |  
| gvOperationReq_RowDataBound | Formats rows in the Operation Request grid (e.g., highlights critical data). |  
| gvPowerReq_RowDataBound | Formats rows in the Power Request grid. |  
| gvPossPowerSector_RowDataBound | Formats rows in the Power Sector grid. |  
| lvTarApproval_ItemDataBound | Customizes approval list items (e.g., adds status indicators). |  
| Button1_Click | Saves changes to the TAR enquiry, updates possession limits, and triggers approval workflows. |  
| gvPossLimit_PageIndexChanging | Handles pagination for the possession limit grid. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry, PossessionLimit, OperationRequest, PowerRequest, PossessionPowerSector, TarApproval  
* **Writes:** PossessionLimit, TAREnquiry  

---

# Page: TAREnquiry_Print  
**File:** TAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users view a printable version of a Track Access Request (TAR) enquiry details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads TAR enquiry data for display in a formatted, printable layout. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry, PossessionLimit, OperationRequest, PowerRequest, PossessionPowerSector, TarApproval