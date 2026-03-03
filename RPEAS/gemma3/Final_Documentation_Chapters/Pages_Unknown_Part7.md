# Page: RPEAS_Admin_User_Mapping
**File:** RPEAS_Admin_User_Mapping.aspx.vb

### 1. User Purpose
Users can map users to specific roles within the system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and populates the search data grid. |
| FillInfo | Populates the data grid with user mapping data. |
| BinddgSearch | Binds the data grid with the provided DataTable. |
| dgSearch_ItemDataBound | Handles the data bound event for each item in the data grid. |
| btnSave_Click | Saves the user mapping data. |
| SaveInfo | Saves the user mapping data to the database. |
| dgSearch_SortCommand | Sorts the data grid based on the selected column. |
| btnclose_Click | Closes the current page. |