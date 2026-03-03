# Page: RPEAS_PA_Supervisor_Edit
**File:** RPEAS_PA_Supervisor_Edit.aspx.vb

### 1. User Purpose
Users edit supervisor information.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and loads data. |
| FillInfo | Populates the data grid with supervisor information. |
| BinddgSearch | Binds the data grid with search data. |
| dgSearch_ItemDataBound | Handles the event when a data grid item is bound. |
| btnclose_Click | Closes the edit form. |
| btnSave_Click | Saves the updated supervisor information. |
| SaveInfo | Saves the data to the database. |
| dgSearch_SortCommand | Sorts the data grid based on the selected column. |