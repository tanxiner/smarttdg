# Page: RPEAS_Create_Form
**File:** RPEAS_Create_Form.aspx.vb

### 1. User Purpose
Users fill out a form to create a new document, including details like approvers, supporting documents, and associated data.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads initial data, and sets up event handlers. |
| Load_Page | Performs initial page setup, likely loading default values or setting up the UI. |
| Populate_Company | Populates the company selection dropdown with available company options. |
| Populate_ApproverLists | Populates the approver lists based on criteria, likely retrieving approver data from a database. |
| ddlprepby2_SelectedIndexChanged | Handles the selection of a preparer from a dropdown list, likely updating other fields based on the chosen preparer. |
| btnAdd_ServerClick | Adds a new document row to the grid control, triggering the creation of a new record. |
| AddPageNumber | Adds a new page to the document, likely incrementing a page number and potentially adding a new row to the grid. |
| dgappdoc_ItemCommand | Handles the "Delete" command on the appdoc grid, deleting the selected row and updating the grid. |
| DeleteSelectedAppDoc | Deletes the selected row from the appdoc grid, likely updating the database. |
| btnAddSuppDoc_ServerClick | Adds a new supporting document row to the grid control, triggering the creation of a new record. |
| dgsuppdoc_ItemCommand | Handles the "Delete" command on the suppdoc grid, deleting the selected row and updating the grid. |
| DeleteSelectedSuppDoc | Deletes the selected row from the suppdoc grid, likely updating the database. |
| btnFormSubmit_Click | Handles the form submission, likely validating the data, saving the document to the database, and sending email notifications. |
| GetServerDetails | Retrieves server details, potentially for logging or reporting purposes. |
| ValidateInput | Validates user input, checking for required fields, data types, and other constraints. |
| Save_Document | Saves the document to the database, likely using a data access object (DAO) to interact with the database. |
| BindGridFileUpload | Binds the file upload control to the grid, allowing users to upload supporting documents. |
| btnFormClear_Click | Clears the form fields, resetting the data to its initial state. |
| btnConfirmnFormSubmit_Click | Handles a confirmation of the form submission, potentially triggering a second validation or confirmation step. |
| btnCancel_Click | Cancels the form submission, clearing the form fields and potentially reverting any changes. |
| txtAmount_TextChanged | Handles changes to the amount field, likely updating related fields or performing calculations. |
| FormatDec | Formats the amount field to a specific decimal format. |
| btnaddSupportby_Click | Adds a new supporting document row to the grid control, triggering the creation of a new record. |
| BindGridsupportby | Binds the grid control to a DataTable, displaying the data in the grid. |
| dgsupportby_ItemCommand | Handles the "Delete" command on the supportby grid, deleting the selected row and updating the grid. |
| dgsupportby_ItemDataBound | Handles events during the data binding process for the supportby grid. |
| btnaddSubmThru_Click | Adds a new supporting document row to the grid control, triggering the creation of a new record. |
| BindGridSbumitThru | Binds the grid control to a DataTable, displaying the data in the grid. |
| dgsubmitThru_ItemCommand | Handles the "Delete" command on the submitThru grid, deleting the selected row and updating the grid. |
| dgsubmitThru_ItemDataBound | Handles events during the data binding process for the submitThru grid. |
| GetApproverList | Retrieves a list of approvers, likely from a database. |
| FormApproverList | Creates a DataTable containing approver data. |