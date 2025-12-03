# Page: TAREnquiry  
**File:** TAREnquiry.aspx.cs  

### 1. User Purpose  
Users view and manage Track Access Requests (TAR) by filtering, paginating, and performing actions like submission, deletion, or withdrawal.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds data, and sets up UI controls. |  
| bindGrid | Loads TAR data into the grid based on a filter indicator (e.g., active/inactive status). |  
| ddlLine_SelectedIndexChanged | Refreshes the TAR grid when the user selects a different line from the dropdown. |  
| btnSubmit_Click | Validates user input, saves the TAR request, and triggers confirmation logic. |  
| btnReset_Click | Clears all form fields and resets filters. |  
| btnPrint_Click | Generates a printable version of the TAR grid data. |  
| GridView1_RowCommand | Handles user actions like editing or deleting a TAR entry. |  
| GridView1_RowDataBound | Formats grid rows (e.g., highlights status, displays additional details). |  
| GridView1_RowDeleting | Confirms deletion of a TAR record before removing it. |  
| btnWithdrawTARConfirm_Click | Confirms withdrawal of a TAR request and updates its status. |  

### 3. Data Interactions  
* **Reads:** TAR, Line, User, BlockedTar  
* **Writes:** TAR, BlockedTar  

---

# Page: TAREnquiry_Detail  
**File:** TAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view and edit detailed Track Access Request (TAR) information, including possession limits and operational requirements.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads TAR details, possession limits, and operational requirements into the form. |  
| BindPossessionLimit | Populates possession limit data for the selected TAR. |  
| gvOperationReq_RowDataBound | Formats operational requirement rows (e.g., displays timestamps, status). |  
| gvPowerReq_RowDataBound | Formats power requirement rows with conditional styling. |  
| lvTarApproval_ItemDataBound | Customizes approval status display in list views. |  
| Button1_Click | Saves changes to possession limits or operational requirements. |  
| gvPossLimit_PageIndexChanging | Updates possession limit data when the user navigates pages. |  

### 3. Data Interactions  
* **Reads:** TAR, PossessionLimit, OperationReq, PowerReq  
* **Writes:** PossessionLimit, OperationReq