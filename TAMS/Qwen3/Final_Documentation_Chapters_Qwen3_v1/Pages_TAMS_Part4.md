# Page: DepotTAREnquiry  
**File:** DepotTAREnquiry.aspx.cs  

### 1. User Purpose  
Users search and manage Track Access Request (TAR) records, including submitting new requests, resetting filters, and performing actions like printing or deleting records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds data on first load, and sets up default filters. |  
| bindGrid | Loads TAR records into the grid based on a filter indicator (e.g., active/inactive status). |  
| ddlLine_SelectedIndexChanged | Updates the grid to display TAR records for the selected line. |  
| btnSubmit_Click | Validates user input, saves new TAR data, and triggers confirmation logic. |  
| btnReset_Click | Clears all filters and resets the form to its initial state. |  
| btnPrint_Click | Generates a printable view of the TAR records in the grid. |  
| GridView1_RowCommand | Handles user actions like approving or withdrawing a TAR from the grid. |  
| GridView1_RowDeleting | Confirms and deletes a TAR record from the database. |  
| btnWithdrawTARConfirm_Click | Confirms the withdrawal of a TAR and updates its status in the system. |  

### 3. Data Interactions  
* **Reads:** Track Access Request (TAR) records, Line information, TAR status details  
* **Writes:** Updates TAR status, deletes TAR records, saves new TAR submissions  

---

# Page: DepotTAREnquiry_Detail  
**File:** DepotTAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view detailed information about a specific Track Access Request (TAR), including related operational and power requirements, and approve or modify TAR details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads detailed TAR information into the page controls. |  
| gvOperationReq_RowDataBound | Formats and displays operational requirements for the TAR. |  
| gvPowerReq_RowDataBound | Formats and displays power requirements for the TAR. |  
| lvTarApproval_ItemDataBound | Populates approval status and related details for TAR records. |  
| Button1_Click | Approves the TAR, updates its status, and triggers confirmation logic. |  

### 3. Data Interactions  
* **Reads:** Track Access Request (TAR) details, Operational requirements, Power requirements, Approval status  
* **Writes:** Updates TAR approval status