# Page: NewUserSignUp
**File:** NewUserSignUp.aspx.cs

### 1. User Purpose
Users create new user accounts with internal or external access options.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and sets up UI elements based on user type. |
| ResetPage | Clears form fields to start a new entry. |
| SetupPage | Configures the page layout or options depending on internal/external flag. |
| buildSystemSelectiondata | Populates dropdowns or selection lists for system options. |
| btn_internalNewSave_Click | Validates user input, saves the new user to the database, and redirects to a confirmation page. |
| btn_internalNewCancel_Click | Cancels the operation, resets the form, and returns to the previous page. |
| btn_externalSave_Click | Validates user input, saves the external user to the database, and redirects to a confirmation page. |
| btn_externalCancel_Click | Cancels the operation, resets the form, and returns to the previous page. |

### 3. Data Interactions
* **Reads:** User, BlockedTar
* **Writes:** User, BlockedTar

---

# Page: OCCSearch_Roster
**File:** OCCSearch_Roster.aspx.cs

### 1. User Purpose
Users search and view employee rosters filtered by line or track.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads initial data and sets up the search criteria. |
| bindSearchCriteria | Populates dropdowns or filters for searching. |
| bindFirstShift | Loads data for the first shift into a grid. |
| bindSecondShift | Loads data for the second shift into a grid. |
| bindThirdShift | Loads data for the third shift into a grid. |
| btnSearchRoster_Click | Executes the search based on selected criteria and updates the grids. |
| ddlLine_SelectedIndexChanged | Filters the search based on the selected line and updates the data. |
| ddlTrack_SelectedIndexChanged | Filters the search based on the selected track and updates the data. |
| btnRefresh_Click | Reloads the data without changing the search criteria. |
| gvFirstShift_RowDataBound | Formats the grid rows for the first shift. |
| gvSecondShift_RowDataBound | Formats the grid rows for the second shift. |
| gvThirdShift_RowDataBound | Formats the grid rows for the third shift. |

### 3. Data Interactions
* **Reads:** Shift, User, Line, Track
* **Writes:** None