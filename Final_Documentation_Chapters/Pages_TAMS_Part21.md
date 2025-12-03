# Page: TAREnquiry  
**File:** TAREnquiry.aspx.cs  

### 1. User Purpose  
Users view a list of Transmission Application Requests (TARs), filter them by transmission line, submit new requests, reset the filter, print the list, and manage individual requests (view details, delete, or withdraw).

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, initializes the page, populates the line dropdown, and binds the grid with all TARs. |
| **bindGrid** | Retrieves TAR records based on the selected line or all lines when indicator is 0, then binds the data to the GridView. |
| **populateTarStatus** | For each TAR row, determines its current status (e.g., Pending, Approved, Withdrawn) and updates the status label or icon. |
| **ddlLine_SelectedIndexChanged** | When the user selects a different transmission line, re‑binds the grid to show only TARs for that line. |
| **GridView1_PageIndexChanging** | Handles pagination; updates the grid to display the requested page of TARs. |
| **btnSubmit_Click** | Validates the request form, creates a new TAR record, and refreshes the grid to show the new entry. |
| **btnReset_Click** | Clears any filter selections and reloads the grid with all TARs. |
| **btnPrint_Click** | Generates a printable view of the current grid contents. |
| **GridView1_RowCommand** | Responds to command buttons in each row (e.g., View, Edit, Delete, Withdraw). Executes the corresponding action and refreshes the grid. |
| **GridView1_RowDataBound** | Formats each row’s data (e.g., date formatting, status styling) before it is rendered. |
| **GridView1_RowDeleting** | Deletes the selected TAR record from the database and updates the grid. |
| **btnWithdrawTARConfirm_Click** | Confirms the withdrawal of a TAR, updates its status to “Withdrawn,” and refreshes the grid. |

### 3. Data Interactions  

* **Reads:**  
  * Transmission Application Requests (TAR) table  
  * Transmission Line information (for dropdown)  
  * TAR status definitions  

* **Writes:**  
  * Insert new TAR records  
  * Update TAR status (e.g., to Withdrawn)  
  * Delete TAR records  

---  

# Page: TAREnquiry_Detail  
**File:** TAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view detailed information about a specific TAR, including possession limits, operation requests, power requests, and approval status, and can approve or reject the request.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Loads the TAR details based on the request ID, populates all detail sections, and sets up the approval controls. |
| **BindPossessionLimit** | Retrieves and displays the possession limits associated with the TAR. |
| **gvOperationReq_RowDataBound** | Formats each operation request row (e.g., status icons, action links). |
| **gvPowerReq_RowDataBound** | Formats each power request row, showing requested power and approval status. |
| **gvPossPowerSector_RowDataBound** | Formats rows that list power sectors involved in the possession request. |
| **lvTarApproval_ItemDataBound** | Sets up approval controls for each approval item, such as approve/reject buttons and comments. |
| **Button1_Click** | Handles the main approval action (e.g., submit approval decisions), updates the TAR approval status, and refreshes the detail view. |
| **gvPossLimit_PageIndexChanging** | Supports pagination for the possession limits grid, updating the displayed page. |

### 3. Data Interactions  

* **Reads:**  
  * TAR detail record (by ID)  
  * Possession limits linked to the TAR  
  * Operation request entries  
  * Power request entries  
  * Power sector associations  
  * Approval history and current status  

* **Writes:**  
  * Update approval status and comments for the TAR  
  * Persist any changes to possession limits or related records (if applicable)  

---