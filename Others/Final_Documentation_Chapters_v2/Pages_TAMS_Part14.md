# Page: TARBlockDate  
**File:** TARBlockDate.aspx.cs  

### 1. User Purpose  
Users manage block dates for rail lines, including searching, viewing, and adding new entries.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads block date data. |  
| ReloadRecs | Refreshes the block date list based on current filters. |  
| gvBlockDate_RowDataBound | Formats grid rows to display block date details. |  
| gvBlockDate_RowCommand | Handles user actions like editing or deleting block dates. |  
| lbSearch_Click | Filters block dates based on user input. |  
| lbNew_Click | Redirects users to the new block date entry form. |  
| ddlRail_SelectedIndexChanged | Updates the block date list based on selected rail line. |  

### 3. Data Interactions  
* **Reads:** BlockDate  
* **Writes:** BlockDate  

---

# Page: TARBlockDate_Add  
**File:** TARBlockDate_Add.aspx.cs  

### 1. User Purpose  
Users add new block date entries for rail lines.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the new block date form. |  
| lbtnAddBlockDate_Click | Saves new block date data to the system. |  
| lbtnAddCancel_Click | Cancels the new block date entry and returns to the main list. |  

### 3. Data Interactions  
* **Writes:** BlockDate  

---

# Page: TAREnquiry  
**File:** TAREnquiry.aspx.cs  

### 1. User Purpose  
Users search and manage track access requests (TARs), including filtering, viewing details, and withdrawing requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the TAR list and initializes filters. |  
| bindGrid | Populates the TAR grid based on search criteria. |  
| populateTarStatus | Updates TAR status indicators in the grid. |  
| ddlLine_SelectedIndexChanged | Filters TARs by selected rail line. |  
| GridView1_PageIndexChanging | Updates the TAR list when navigating pages. |  
| btnSubmit_Click | Applies search filters to the TAR list. |  
| btnReset_Click | Clears search filters and reloads the TAR list. |  
| btnPrint_Click | Generates a printable version of the TAR list. |  
| GridView1_RowCommand | Handles row-level actions like editing or withdrawing TARs. |  
| GridView1_RowDataBound | Formats TAR rows to display status and details. |  
| GridView1_RowDeleting | Confirms and deletes a TAR entry. |  
| btnWithdrawTARConfirm_Click | Confirms withdrawal of a TAR and updates its status. |  

### 3. Data Interactions  
* **Reads:** TAR, TarStatus  
* **Writes:** TAR, TarStatus