# Page: RPEAS_All_Forms
**File:** RPEAS_All_Forms.aspx.vb

### 1. User Purpose
This page allows users to search for and view a list of forms, likely related to a transit system (inferred from file name and potential domain context).

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, likely setting up the search functionality and the data grid. |
| Load_Forms | Populates the data grid (gvInbox) with form data based on search criteria. |
| btnSearch_Click | Triggers the `Load_Forms` method, initiating the form search. |
| lbtStart_Click | Likely initiates the first page of the form list. |
| lbtPrevious_Click | Navigates to the previous page of the form list. |
| lbtEnd_Click | Likely navigates to the last page of the form list. |
| lbtNext_Click | Navigates to the next page of the form list. |
| setPager | Updates the pagination controls (e.g., page numbers) based on the current page and total number of forms. |
| gvInbox_RowDataBound | Handles events for each row in the data grid (gvInbox).  Likely performs actions specific to each row, such as setting up event handlers or formatting data. |
| btnReset_Click | Resets the search criteria, clearing the data grid and potentially re-initializing the search. |

---