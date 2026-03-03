# Page: RPEAS_All_Forms_PA
**File:** RPEAS_All_Forms_PA.aspx.vb

### 1. User Purpose
This page allows users to search for and view a list of inbox items.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads forms data, and sets up the date pickers. |
| Load_Forms | Loads the forms data, likely from a data source (DAL). |
| btnSearch_Click | Executes a search based on user input (likely date range) and updates the grid view with the results. |
| lbtStart_Click | Sets the start date to the current date using the date picker. |
| lbtPrevious_Click | Sets the start date to the previous day. |
| lbtEnd_Click | Sets the end date to the current date using the date picker. |
| lbtNext_Click | Sets the end date to the previous day. |
| setPager |  Handles pagination of the grid view. |
| gvInbox_RowDataBound |  Handles events for each row in the grid view (e.g., on row bound). |
| btnReset_Click | Resets the date pickers and the grid view to its default state. |

### 3. Data Interactions
* **Reads:** DAL (likely a data access layer object)
* **Writes:** None