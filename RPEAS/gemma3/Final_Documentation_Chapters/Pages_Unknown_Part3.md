# Page: RPEAS_Admin_Role_Maint - Copy.aspx
**File:** RPEAS_Admin_Role_Maint - Copy.aspx.vb

### 1. User Purpose
Users can maintain and update administrative roles within the system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and sets up event handlers. |
| btnSearch_Click | Executes a search based on user input, likely populating a grid control with matching roles. |
| BindGrid | Populates the grid control with the retrieved role data. |
| btnSave_Click | Saves the changes made to the selected role(s) to the database. |
| BtnClear_Click | Clears the form fields, resetting the user interface. |
| btnUpdate_Click | Updates an existing role based on user input. |
| Update | Updates the data in the grid control, likely triggered by a user action. |
| dgSearch_ItemDataBound | Handles events when a new item is bound to the data grid. |
| dgSearch_SortCommand | Sorts the data displayed in the data grid. |
| btnDelete_Click | Deletes the selected role(s) from the database. |
| DeleteSelected | Deletes the selected role(s) from the database. |
| btndel_ServerClick | Handles the server-side click event for the delete button. |
| lkMenu_Click | Navigates to a different menu item, likely a main menu. |
| lkUser_Click | Navigates to a different menu item, likely a user management page. |

---