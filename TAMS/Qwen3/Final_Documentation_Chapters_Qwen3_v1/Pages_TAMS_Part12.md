# Page: OCCUpdate_Roster  
**File:** OCCUpdate_Roster.aspx.cs  

### 1. User Purpose  
Users update and manage shift assignments for track operations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads default data, and sets up event handlers. |  
| bindSearchCriteria | Loads filter options for line, track, and shift selection. |  
| loadTrackType | Populates track type dropdown with available track types. |  
| bindFirstShift | Binds first shift data to the corresponding GridView. |  
| bindSecondShift | Binds second shift data to the corresponding GridView. |  
| bindThirdShift | Binds third shift data to the corresponding GridView. |  
| ddlLine_SelectedIndexChanged | Refreshes shift data based on selected line. |  
| ddlTrack_SelectedIndexChanged | Refreshes shift data based on selected track. |  
| gvFirstShift_RowDataBound | Formats rows in the first shift GridView (e.g., highlights status). |  
| gvSecondShift_RowDataBound | Formats rows in the second shift GridView (e.g., highlights status). |  
| gvThirdShift_RowDataBound | Formats rows in the third shift GridView (e.g., highlights status). |  
| btnUpdateRoster_Click | Saves changes to shift assignments and updates the roster. |  
| btnRefresh_Click | Reloads shift data to reflect the latest changes. |  

### 3. Data Interactions  
* **Reads:** Shift, Employee, Track, Line, ShiftAssignment  
* **Writes:** ShiftAssignment, EmployeeShift, TrackAssignment  

---

# Page: OCC_HoursAuthorisation  
**File:** OCC_HoursAuthorisation.aspx.cs  

### 1. User Purpose  
Users submit or preview authorized hours for operational duties.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user-specific data and initializes the hours grid. |  
| BindGrid | Populates the hours grid with authorization records. |  
| LoadOCCAuthCtrl_DTL | Loads detailed authorization data for a specific user. |  
| LoadOCCAuthCtrl_NEL | Loads nested authorization data (e.g., duty roster details). |  
| GridView1_RowDataBound | Formats rows in the hours grid (e.g., highlights approval status). |  
| GridView1_RowCreated | Sets up row templates for dynamic content in the hours grid. |  
| btnSubmit_Click | Submits authorized hours for approval and saves the record. |  
| ddlLine_SelectedIndexChanged | Filters hours data based on selected line. |  
| btnPreview_Click | Generates a preview of authorized hours for review. |  

### 3. Data Interactions  
* **Reads:** HoursAuthorization, DutyRoster, User, AuthorizationDetail  
* **Writes:** HoursAuthorization, AuthorizationDetail, DutyRoster