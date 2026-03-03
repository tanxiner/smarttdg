# Page: DepotTAREnquiry_Detail  
**File:** DepotTAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view and manage detailed information for a TAREnquiry request.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page by binding data to GridView controls and setting up the user interface. |  
| gvOperationReq_RowDataBound | Formats or customizes rows in the OperationReq GridView to display relevant data. |  
| gvPowerReq_RowDataBound | Formats or customizes rows in the PowerReq GridView to display relevant data. |  
| gvPossPowerSector_RowDataBound | Formats or customizes rows in the PossPowerSector GridView to display relevant data. |  
| lvTarApproval_ItemDataBound | Customizes ListView items for TarApproval data display. |  
| Button1_Click | Saves changes to the TAREnquiry request, updates related records, and confirms the action. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry, OperationReq, PowerReq, PossPowerSector, TarApproval  
* **Writes:** TAREnquiry, TarApproval  

---

# Page: DepotTAREnquiry_Print  
**File:** DepotTAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users view a printable version of a TAREnquiry request.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads and displays TAREnquiry data in a formatted layout suitable for printing. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry