# Page: RPEAS_Admin_User_Maint
**File:** RPEAS_Admin_User_Maint.aspx.vb

### 1. User Purpose
Users can maintain user accounts, including searching, saving, and deleting user records.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, populates the data grid, and sets up event handlers. |
| btnSearch_Click | Triggers a search operation based on user input, updating the data grid with matching records. |
| BindGrid | Populates the data grid with the current data. |
| dgSearch_ItemCommand | Handles user selections within the data grid, likely triggering further actions based on the selected row. |
| dgSearch_ItemDataBound | Handles events that occur when a data grid item is bound, potentially performing actions like setting up event handlers for individual rows. |
| btnSave_Click | Saves the selected user record to the database. |
| btnDelete_Click | Deletes the selected user record from the database. |
| dgSearch_SortCommand | Sorts the data in the data grid based on the selected column. |
| btndel_ServerClick |  Handles the server-side click event for deleting a selected user. |
| DeleteSelected(dg: DataGrid) |  Deletes the selected rows in the data grid. Returns the number of rows deleted. |
| BtnClear_Click | Clears the search criteria and resets the data grid. |