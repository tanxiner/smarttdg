### **NewUserSignUp.aspx**  
**User Purpose**  
Users register new internal or external users by filling out form fields and submitting data.  

**Key Events & Logic**  
- **Page_Load**: Initializes the page, possibly calling `SetupPage` to configure UI elements based on internal/external mode.  
- **ResetPage**: Clears form fields and resets UI state.  
- **SetupPage**: Configures the form (e.g., dropdowns) for internal or external user registration.  
- **buildSystemSelectiondata**: Populates dropdowns (e.g., track types) for user selection.  
- **btn_internalNewSave_Click / btn_externalSave_Click**: Validates form inputs, saves user data to the server, and redirects to a confirmation or next step.  
- **btn_Cancel_Click**: Resets the form or navigates back to the previous page.  

**Data Flow**  
- User inputs (e.g., name, role) are captured in form fields.  
- Dropdown selections (e.g., track type) are used to filter or categorize the user.  
- On submission, data is sent to the server for storage, and the user is redirected.  

---

### **OCCSearch_Roster.aspx**  
**User Purpose**  
Users search for roster entries by selecting a line and track, then view shifts across three time periods.  

**Key Events & Logic**  
- **Page_Load**: Loads initial data or binds search criteria based on user preferences.  
- **bindSearchCriteria**: Populates dropdowns (e.g., lines, tracks) for filtering.  
- **ddlLine_SelectedIndexChanged / ddlTrack_SelectedIndexChanged**: Updates displayed roster data based on user selections.  
- **gvFirstShift_RowDataBound / gvSecondShift_RowDataBound / gvThirdShift_RowDataBound**: Formats or highlights specific rows in gridviews (e.g., high/low attendance).  
- **btnRefresh_Click**: Reloads and rebinds roster data to reflect current filters.  

**Data Flow**  
- Users select a line and track, triggering a data retrieval request.  
- The server fetches and binds roster data to gridviews, displaying shifts for the selected time periods.  
- Row formatting highlights key metrics (e.g., attendance trends).  

---

### **OCCUpdate_Roster.aspx**  
**User Purpose**  
Users update roster entries by selecting a line and track, editing shift details, and saving changes.  

**Key Events & Logic**  
- **Page_Load**: Loads initial data or binds search criteria for filtering.  
- **loadTrackType**: Populates dropdowns (e.g., track types) for user selection.  
- **bindFirstShift / bindSecondShift / bindThirdShift**: Displays editable shift details for the selected line and track.  
- **ddlLine_SelectedIndexChanged / ddlTrack_SelectedIndexChanged**: Updates displayed shifts based on user selections.  
- **gvFirstShift_RowDataBound / gvSecondShift_RowDataBound / gvThirdShift_RowDataBound**: Enables inline editing or validates changes.  
- **btnUpdateRoster_Click**: Saves modified shift data to the server and confirms updates.  
- **btnRefresh_Click**: Reloads and rebinds roster data to reflect current filters.  

**Data Flow**  
- Users select a line and track, triggering a data retrieval request.  
- The server fetches and binds editable shift details to gridviews.  
- Edits are saved to the server, and the user is notified of successful updates.