# Page: RPEAS_Admin_User_Edit
**File:** RPEAS_Admin_User_Edit.aspx.vb

### 1. User Purpose
Users can edit existing administrator user details.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, populates the user edit form with existing data, and handles event triggers. |
| GetUserDetails | Retrieves the details of the user being edited, populating the form fields. |
| btnBack_Click | Returns the user to the previous page. |
| btnUpdate_Click | Saves the updated user details to the database. |