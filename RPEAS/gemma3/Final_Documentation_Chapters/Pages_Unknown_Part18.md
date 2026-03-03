# Page: RPEAS_Outstnd_Form
**File:** RPEAS_Outstnd_Form.aspx.vb

### 1. User Purpose
Users view and manage outstanding transactions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads inbox data, and sets the pager. |
| lbtStart_Click | Starts the process of displaying outstanding transactions. |
| lbtPrevious_Click | Navigates to the previous page of outstanding transactions. |
| lbtEnd_Click | Navigates to the next page of outstanding transactions. |
| lbtNext_Click | Navigates to the next page of outstanding transactions. |
| Load_Inbox | Loads the initial data for the inbox grid. |
| setPager | Updates the pager controls to reflect the current page. |
| gvInbox_RowDataBound | Handles events for each row in the inbox grid. |
| btnsub_ServerClick | Submits the selected transaction for processing. |

# Page: RPEAS_PA_SuperVisor
**File:** RPEAS_PA_SuperVisor.aspx.vb

### 1. User Purpose
Supervisors view and search for outstanding transactions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, binds the grid, and sets up event handlers. |
| BindGrid | Populates the grid with transaction data based on sorting and role code. |
| dgSearch_ItemDataBound | Handles events for each row in the search grid. |
| lksupervisor_Click | Changes the role code to filter the search results. |
| btnSearch_Click | Executes a search based on the current role code. |
| BtnClear_Click | Clears the search criteria. |