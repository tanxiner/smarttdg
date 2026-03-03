# Page: TARApplication  
**File:** TARApplication.aspx.cs  

### 1. User Purpose  
Users submit track access requests, select lines and access types, and view associated dates and sector information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page by binding grid views and setting up UI elements based on user session data. |  
| **BindGrid** | Loads and displays track sector data into grid views for user review. |  
| **btnSubmit_Click** | Validates user input, saves track access request details to the database, and sends confirmation notifications. |  
| **displayDates** | Formats and displays date ranges for specific track sectors based on access type and line selection. |  
| **showHideControls** | Toggles visibility of UI elements (e.g., date pickers) depending on the selected access type. |  
| **GridView1_RowDataBound** | Highlights rows in the main grid based on access type (e.g., possession vs. protection). |  
| **ddlLine_SelectedIndexChanged** | Updates displayed data and date ranges when the user selects a different track line. |  
| **rbPossession_CheckedChanged / rbProtection_CheckedChanged** | Adjusts UI visibility and data bindings based on whether the user selects possession or protection access. |  

### 3. Data Interactions  
* **Reads:** TarSector, BlockedTar, User  
* **Writes:** TarSector, BlockedTar