# Page: TARApplication  
**File:** TARApplication.aspx.cs  

### 1. User Purpose  
Users submit track access requests, view associated data, and manage access type configurations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page, binds data to grids, and sets up UI state. |  
| **BindGrid** | Loads and displays track sector data in multiple grid views. |  
| **btnSubmit_Click** | Validates user input, saves access request details, and updates related records. |  
| **displayDates** | Formats and displays date ranges based on selected track sectors and access type. |  
| **showHideControls** | Toggles visibility of UI elements depending on user selections (e.g., access type). |  
| **RowDataBound** (GridView events) | Customizes row appearance to highlight critical data or status indicators. |  
| **displayLegend** | Renders a visual legend to explain grid view color coding or icon meanings. |  
| **ddlLine_SelectedIndexChanged** | Refreshes grid data based on the selected track line. |  
| **rbPossession_CheckedChanged / rbProtection_CheckedChanged** | Updates UI and data bindings when the user selects "Possession" or "Protection" access type. |  

### 3. Data Interactions  
**Reads:**  
- Track sector details (TarSector)  
- Blocked track records (BlockedTar)  
- User-selected line configurations  
- Date range metadata  

**Writes:**  
- Updated access request records (BlockedTar)  
- Temporary state variables for UI controls (e.g., m_Track, m_AccessType)  
- Formatted date ranges (dates list)