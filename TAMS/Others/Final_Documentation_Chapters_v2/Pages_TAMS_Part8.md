# Page: NewUserSignUp  
**File:** NewUserSignUp.aspx.cs  

### 1. User Purpose  
Users register new accounts with internal or external access levels.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and sets up UI elements. |  
| ResetPage | Clears form fields and resets user input. |  
| SetupPage | Configures the form based on whether the user is internal or external. |  
| buildSystemSelectiondata | Populates dropdowns with system-specific options. |  
| btn_internalNewSave_Click | Validates inputs, saves user data to the database, and sends a confirmation email. |  
| btn_externalSave_Click | Validates inputs, saves user data to the database, and sends a confirmation email. |  
| btn_internalNewCancel_Click | Resets the form and navigates back to the user list. |  
| btn_externalCancel_Click | Resets the form and navigates back to the user list. |  

### 3. Data Interactions  
* **Reads:** User, BlockedTar  
* **Writes:** User  

---

# Page: OCCSearch_Roster  
**File:** OCCSearch_Roster.aspx.cs  

### 1. User Purpose  
Users search and view roster data for specific lines and tracks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads initial search criteria and binds data to UI elements. |  
| bindSearchCriteria | Populates dropdowns with line and track options. |  
| bindFirstShift | Loads first shift roster data into the grid. |  
| bindSecondShift | Loads second shift roster data into the grid. |  
| bindThirdShift | Loads third shift roster data into the grid. |  
| btnSearchRoster_Click | Filters and displays roster data based on selected criteria. |  
| ddlLine_SelectedIndexChanged | Updates track options based on the selected line. |  
| ddlTrack_SelectedIndexChanged | Updates shift data based on the selected track. |  
| gvFirstShift_RowDataBound | Formats grid rows for first shift data. |  
| gvSecondShift_RowDataBound | Formats grid rows for second shift data. |  
| gvThirdShift_RowDataBound | Formats grid rows for third shift data. |  

### 3. Data Interactions  
* **Reads:** Roster, Line, Track  
* **Writes:** None  

---

# Page: OCCUpdate_Roster  
**File:** OCCUpdate_Roster.aspx.cs  

### 1. User Purpose  
Users update roster data for specific lines and tracks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads initial search criteria and binds data to UI elements. |  
| bindSearchCriteria | Populates dropdowns with line and track options. |  
| loadTrackType | Loads track type options for the UI. |  
| bindFirstShift | Loads first shift roster data into the grid. |  
| bindSecondShift | Loads second shift roster data into the grid. |  
| bindThirdShift | Loads third shift roster data into the grid. |  
| ddlLine_SelectedIndexChanged | Updates track options based on the selected line. |  
| ddlTrack_SelectedIndexChanged | Updates shift data based on the selected track. |  
| gvFirstShift_RowDataBound | Formats grid rows for first shift data. |  
| gvSecondShift_RowDataBound | Formats grid rows for second shift data. |  
| gvThirdShift_RowDataBound | Formats grid rows for third shift data. |  
| btnUpdateRoster_Click | Applies changes to roster data and saves updates. |  
| btnRefresh_Click | Reloads data and resets the UI to its initial state. |  

### 3. Data Interactions  
* **Reads:** Roster, Line, Track  
* **Writes:** Roster