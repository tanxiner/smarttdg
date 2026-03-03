# Page: TARBlockDate  
**File:** TARBlockDate.aspx.cs  

### 1. User Purpose  
Users manage block date records, including searching, adding new entries, and filtering by rail line.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads existing block date records. |  
| ReloadRecs | Refreshes the displayed block date records based on current filters. |  
| gvBlockDate_RowDataBound | Formats grid rows to highlight specific data (e.g., status or dates). |  
| gvBlockDate_RowCommand | Handles user actions like editing or deleting a block date entry. |  
| lbSearch_Click | Filters block date records based on user input criteria. |  
| lbNew_Click | Navigates to a new block date entry form. |  
| ddlRail_SelectedIndexChanged | Updates the displayed records based on the selected rail line. |  

### 3. Data Interactions  
* **Reads:** BlockDate, RailLine  
* **Writes:** BlockDate  

---

#.SetString  
**File:** TARBlockDate_Add.aspx.cs  

### 1. User Purpose  
Users add new block date records by filling out a form.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the form and pre-fills fields if editing an existing record. |  
| lbtnAddBlockDate_Click | Saves the new block date record to the database. |  
| lbtnAddCancel_Click | Cancels the operation and returns to the main block date management page. |  

### 3. Data Interactions  
* **Writes:** BlockDate  

---

# Page: TAREnquiry  
**File:** TAREnquiry.aspx.cs  

### 1. User Purpose  
Users search and manage track access requests (TARs) by filtering, viewing details, and performing actions like withdrawal or printing.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the TAR grid and initializes search filters. |  
| bindGrid | Populates the TAR grid based on search criteria or user permissions. |  
| populateTarStatus | Updates the status display for selected TAR entries. |  
| ddlLine_SelectedIndexChanged | Filters TAR records based on the selected rail line. |  
| btnSubmit_Click | Applies search filters to narrow down TAR results. |  
| btnReset_Click | Clears all filters and displays all TAR records. |  
| btnPrint_Click | Generates a printable version of the TAR grid. |  
| GridView1_RowCommand | Handles actions like withdrawing a TAR or editing details. |  
| GridView1_RowDeleting | Confirms and deletes a TAR record. |  
| btnWithdrawTARConfirm_Click | Finalizes the withdrawal of a TAR and updates its status. |  

### 3. Data Interactions  
* **Reads:** TAR, RailLine, Status  
* **Writes:** TAR, Status