# Page: TARBlockDate  
**File:** TARBlockDate.aspx.cs  

### 1. User Purpose  
Users manage block date records, including viewing, searching, and modifying block dates associated with rail lines.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads block date data when the page is first accessed. |  
| ReloadRecs | Refreshes the grid view with updated block date records based on current filters. |  
| gvBlockDate_RowDataBound | Formats grid rows to highlight specific block date details or apply conditional styling. |  
| gvBlockDate_RowCommand | Handles user actions like editing or deleting a block date record from the grid. |  
| lbSearch_Click | Triggers a search for block dates based on user input criteria. |  
| lbNew_Click | Opens a new block date entry form for user input. |  
| ddlRail_SelectedIndexChanged | Filters block date records dynamically based on the selected rail line. |  

### 3. Data Interactions  
* **Reads:** BlockDate, Rail  
* **Writes:** BlockDate  

---

# Page: TARBlockDate_Add  
**File:** TARBlockDate_Add.aspx.cs  

### 1. User Purpose  
Users create new block date records by entering details such as dates, rail lines, and associated track information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the form with default values and initializes controls for new record entry. |  
| lbtnAddBlockDate_Click | Validates user input, saves the new block date to the database, and redirects to the main block date list. |  
| lbtnAddCancel_Click | Closes the form and returns the user to the main block date management page. |  

### 3. Data Interactions  
* **Writes:** BlockDate