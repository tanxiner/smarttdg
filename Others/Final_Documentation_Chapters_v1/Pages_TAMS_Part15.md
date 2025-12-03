# Page: TAREnquiry_Detail  
**File:** TAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view, edit, and manage track access requests and associated approvals.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data for display. |  
| BindPossessionLimit | Loads possession limit details into a grid for review. |  
| gvOperationReq_RowDataBound | Formats rows in the operation request grid (e.g., highlights critical data). |  
| gvPowerReq_RowDataBound | Formats rows in the power request grid (e.g., displays conditional text). |  
| gvPossPowerSector_RowDataBound | Formats rows in the power sector grid (e.g., applies styling based on sector type). |  
| lvTarApproval_ItemDataBound | Populates approval list items with dynamic content (e.g., status indicators). |  
| Button1_Click | Saves changes to the track access request and triggers approval workflow. |  
| gvPossLimit_PageIndexChanging | Updates the possession limit grid when the user navigates between pages. |  

### 3. Data Interactions  
* **Reads:** TarEnquiry, PossessionLimit, OperationRequest, PowerRequest, PossPowerSector, TarApproval  
* **Writes:** TarEnquiry, TarApproval  

---

# Page: TAREnquiry_Print  
**File:** TAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users generate a printable version of a track access request for offline review.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads track access request details into the page for printing. |  

### 3. Data Interactions  
* **Reads:** TarEnquiry, PossessionLimit, OperationRequest, PowerRequest, PossPowerSector, TarApproval