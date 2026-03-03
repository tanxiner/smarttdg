# Page: DepotTAREnquiry_Detail  
**File:** DepotTAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view and manage TAREnquiry details, including operations, power requirements, and approval statuses.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and binds TAREnquiry data to grids and lists. |  
| gvOperationReq_RowDataBound | Customizes GridView rows for operation requests (e.g., adds action buttons). |  
| gvPowerReq_RowDataBound | Customizes GridView rows for power requirements (e.g., highlights critical fields). |  
| gvPossPowerSector_RowDataBound | Customizes GridView rows for power sectors (e.g., displays sector-specific details). |  
| lvTarApproval_ItemDataBound | Customizes ListView items for approval records (e.g., formats dates or statuses). |  
| Button1_Click | Processes user actions like approving or rejecting a TAREnquiry and updates the approval status. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry, OperationReq, PowerReq, PossPowerSector, TarApproval  
* **Writes:** TarApproval (updates approval status or adds new records)  

---

# Page: DepotTAREnquiry_Print  
**File:** DepotTAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users generate a printable version of a TAREnquiry record for review or documentation.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads TAREnquiry data into the page for display in a formatted print layout. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry