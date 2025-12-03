# Page: NewUserSignUp
**File:** NewUserSignUp.aspx.cs

### 1. User Purpose
Users fill out this form to create a new internal or external user account.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Determines whether the page is being accessed for an internal or external user, resets all form fields, and calls SetupPage with the appropriate flag. |
| ResetPage | Clears every input control on the form, resetting dropdowns, text boxes, and any validation messages to their default state. |
| SetupPage(isExternal) | Configures the UI for the selected user type: shows or hides sections, sets titles, and populates the system selection dropdown by calling buildSystemSelectiondata. |
| buildSystemSelectiondata(isExternal) | Builds a DataTable containing the list of systems that the user can be assigned to, filtering the list if the user is external. |
| btn_internalNewSave_Click | Validates the internal user form, creates a new internal user record, writes it to the database, and displays a success message or redirects to a confirmation page. |
| btn_internalNewCancel_Click | Cancels the internal user creation process, clears the form, and returns the user to the previous page or dashboard. |
| btn_externalSave_Click | Validates the external user form, creates a new external user record, writes it to the database, and displays a success message or redirects to a confirmation page. |
| btn_externalCancel_Click | Cancels the external user creation process, clears the form, and returns the user to the previous page or dashboard. |

### 3. Data Interactions
* **Reads:** System list (Systems table), possibly user data for validation.  
* **Writes:** New user record (User table) for either internal or external users.

---

# Page: OCCSearch_Roster
**File:** OCCSearch_Roster.aspx.cs

### 1. User Purpose
Users search and view the roster of operators for different shifts based on selected line and track criteria.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, populates line and track dropdowns via bindSearchCriteria and binds the first, second, and third shift grids with current roster data. |
| bindSearchCriteria | Retrieves available lines and tracks from the database and fills the corresponding dropdown lists. |
| bindFirstShift | Queries the roster for the first shift based on selected criteria and binds the results to the first shift GridView. |
| bindSecondShift | Queries the roster for the second shift based on selected criteria and binds the results to the second shift GridView. |
| bindThirdShift | Queries the roster for the third shift based on selected criteria and binds the results to the third shift GridView. |
| btnSearchRoster_Click | Executes a new search using the selected line and track, then refreshes all three shift grids with updated data. |
| ddlLine_SelectedIndexChanged | Updates dependent dropdowns or refreshes shift grids when the user selects a different line. |
| ddlTrack_SelectedIndexChanged | Updates dependent dropdowns or refreshes shift grids when the user selects a different track. |
| btnRefresh_Click | Rebinds all three shift grids to display the most recent roster information. |
| gvFirstShift_RowDataBound | Formats each row of the first shift GridView, adding any necessary styling or action links. |
| gvSecondShift_RowDataBound | Formats each row of the second shift GridView, adding any necessary styling or action links. |
| gvThirdShift_RowDataBound | Formats each row of the third shift GridView, adding any necessary styling or action links. |

### 3. Data Interactions
* **Reads:** Line and track lists, roster data for first, second, and third shifts.  
* **Writes:** None – the page displays read‑only roster information.