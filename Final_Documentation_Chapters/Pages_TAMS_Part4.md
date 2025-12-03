# Page: DepotTAREnquiry  
**File:** DepotTAREnquiry.aspx.cs  

### 1. User Purpose  
Users view and manage TAR (Tariff) inquiries for a depot. They can filter by depot line, submit new requests, reset filters, print the current list, and withdraw existing TARs.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, populates the depot line dropdown and displays the initial grid of TARs. |
| **bindGrid** | Retrieves TAR records from the database based on the selected line and status indicator, then binds them to the GridView. |
| **populateTarStatus** | Sets status indicators or filter options that correspond to the chosen depot line. |
| **ddlLine_SelectedIndexChanged** | When the user selects a different depot line, the grid is refreshed to show TARs for that line. |
| **GridView1_PageIndexChanging** | Handles pagination of the TAR list, updating the displayed page of records. |
| **btnSubmit_Click** | Validates user input for a new TAR request, saves the request to the database, and refreshes the grid. |
| **btnReset_Click** | Clears all filter selections and reloads the grid with the default set of TARs. |
| **btnPrint_Click** | Generates a printable view of the currently displayed TAR list. |
| **GridView1_RowCommand** | Processes row‑level commands such as viewing details or initiating a withdrawal. |
| **GridView1_RowDataBound** | Customizes the appearance of each row (e.g., color‑coding status) as it is bound. |
| **GridView1_RowDeleting** | Deletes a TAR record after user confirmation and updates the grid. |
| **btnWithdrawTARConfirm_Click** | Confirms the withdrawal of a TAR, updates its status in the database, and refreshes the grid. |

### 3. Data Interactions  
* **Reads:** TAR records, depot line information, status codes.  
* **Writes:** New TAR entries, updates to TAR status (withdrawal), deletions of TAR records.  

---  

# Page: DepotTAREnquiry_Detail  
**File:** DepotTAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Displays comprehensive details for a selected TAR, including operation requests, power requests, potential power sectors, and approval status. Users can review these details and perform approval actions.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Loads the TAR details based on query parameters and binds all related data grids and lists. |
| **gvOperationReq_RowDataBound** | Formats each operation request row (e.g., displays status icons or action links). |
| **gvPowerReq_RowDataBound** | Formats each power request row, ensuring relevant data is presented clearly. |
| **gvPossPowerSector_RowDataBound** | Formats rows for possible power sectors, highlighting selections or constraints. |
| **lvTarApproval_ItemDataBound** | Binds approval items, showing current approval status and providing approve/reject controls. |
| **Button1_Click** | Executes the approval or rejection of selected items, updates the database, and refreshes the approval list. |

### 3. Data Interactions  
* **Reads:** TAR detail records, operation requests, power requests, possible power sectors, approval logs.  
* **Writes:** Approval decisions, updates to TAR status, and any related audit entries.