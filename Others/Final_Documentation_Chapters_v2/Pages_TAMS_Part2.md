# Page: DepotTARApplication  
**File:** DepotTARApplication.aspx.cs  

### 1. User Purpose  
Users submit track access requests and manage associated data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page, binds location dropdown and grid data. |  
| BindLocation | Loads location options for user selection. |  
| BindGrid | Populates grid with track access records based on filters. |  
| btnSubmit_Click | Validates user input, saves TAR application data, and updates related records. |  
| displayDates | Formats and displays date ranges based on selected track type and access type. |  
| showHideControls | Toggles visibility of form fields based on user permissions or selections. |  
| GridView1_RowDataBound | Formats grid rows to highlight critical data or status indicators. |  
| ddlLine_SelectedIndexChanged | Refreshes grid or filters data based on selected line. |  
| rbPossession_CheckedChanged | Updates grid or form fields based on possession vs. protection access type. |  

### 3. Data Interactions  
* **Reads:** Tar, BlockedTar, DepotTarSector, DepotTar  
* **Writes:** DepotTar, DepotTarSector  

---

# Page: DepotTAREnquiry  
**File:** DepotTAREnquiry.aspx.cs  

### 1. User Purpose  
Users view, filter, and manage track access requests (TARs) and their statuses.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page, binds grid with TAR records based on user permissions. |  
| bindGrid | Loads and filters TAR data into the grid, supporting pagination and sorting. |  
| populateTarStatus | Updates status indicators (e.g., active, withdrawn) in the grid. |  
| btnSubmit_Click | Applies filters to narrow down TAR records displayed in the grid. |  
| btnReset_Click | Clears all filters and reloads the full TAR dataset. |  
| btnPrint_Click | Generates a printable version of the grid for offline review. |  
| GridView1_RowCommand | Handles user actions like withdrawing a TAR or editing records. |  
| GridView1_RowDataBound | Formats rows to visually distinguish between TAR types and statuses. |  
| GridView1_RowDeleting | Confirms and executes deletion of a TAR record. |  

### 3. Data Interactions  
* **Reads:** Tar, BlockedTar, DepotTar  
* **Writes:** DepotTar (for deletions or status updates)