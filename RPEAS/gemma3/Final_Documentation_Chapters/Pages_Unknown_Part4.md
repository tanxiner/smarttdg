# Page: RPEAS_Admin_Role_Maint
**File:** RPEAS_Admin_Role_Maint.aspx.vb

### 1. User Purpose
Users can maintain and update administrative roles within the system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and sets up event handlers. |
| btnSearch_Click | Executes a search based on user input, likely populating a grid control with matching roles. |
| BindGrid | Populates the grid control with the retrieved role data. |
| btnSave_Click | Saves the changes made to the selected role(s) to the database. |
| BtnClear_Click | Clears the form fields, resetting the user input. |
| btnUpdate_Click | Updates an existing role with the data entered in the form. |
| Update |  Updates the data in the grid control, likely based on a database update. |
| dgSearch_ItemDataBound | Handles the event when a new item is bound to the grid control, potentially setting up event handlers for row clicks. |
| dgSearch_SortCommand | Sorts the data displayed in the grid control based on the selected column. |
| btnDelete_Click | Deletes the selected role(s) from the database. |
| btndel_ServerClick | Handles the server-side click event for the delete button. |
| lkMenu_Click | Navigates to a different menu item, likely a main menu. |
| lkUser_Click | Navigates to a different page, potentially a user management page. |

---