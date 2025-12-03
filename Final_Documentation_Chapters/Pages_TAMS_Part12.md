# Page: OCCUpdate_Roster
**File:** OCCUpdate_Roster.aspx.cs

### 1. User Purpose
Users update the OCC shift roster by selecting a production line and track, reviewing the three shift grids, and submitting changes.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, populates search criteria controls, loads available track types, and binds the three shift grids with current roster data. |
| bindSearchCriteria | Fills dropdowns for line and track selection based on current database values. |
| loadTrackType | Retrieves track options for the selected line and updates the track dropdown. |
| bindFirstShift / bindSecondShift / bindThirdShift | Queries the roster for each shift period and binds the results to the corresponding GridView. |
| ddlLine_SelectedIndexChanged | When a new line is chosen, reloads track options and refreshes all three shift grids to reflect the new line’s roster. |
| ddlTrack_SelectedIndexChanged | When a new track is chosen, refreshes the shift grids to show roster entries for that track. |
| gvFirstShift_RowDataBound / gvSecondShift_RowDataBound / gvThirdShift_RowDataBound | For each row, populates controls (e.g., checkboxes, textboxes) with existing roster data and sets up client‑side behavior. |
| btnUpdateRoster_Click | Gathers updated values from all three grids, validates them, and writes the changes back to the roster tables. |
| btnRefresh_Click | Re‑executes the binding logic to reload the latest roster data without submitting changes. |

### 3. Data Interactions
* **Reads:** Roster, Shift, Track, Line, Employee (for display purposes).  
* **Writes:** Roster (updates shift assignments and related fields).

---

# Page: OCC_HoursAuthorisation
**File:** OCC_HoursAuthorisation.aspx.cs

### 1. User Purpose
Users review OCC hour records for a selected line, preview authorization details, and submit approvals or rejections.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads initial line options and calls BindGrid to display the current hour records for the default line. |
| BindGrid | Queries the hour records for the selected line and binds them to GridView1. |
| LoadOCCAuthCtrl_DTL | Loads detailed authorization controls for a specific user ID, populating controls that allow approval or rejection. |
| LoadOCCAuthCtrl_NEL | Loads authorization controls for a user ID and a specific duty roster code, used when multiple rosters are involved. |
| GridView1_RowDataBound | For each row, sets up display values and attaches the appropriate authorization controls (e.g., approve/reject buttons). |
| GridView1_RowCreated | Initializes row-level controls and ensures they are correctly wired to event handlers. |
| ddlLine_SelectedIndexChanged | When the user selects a different line, rebinds the grid to show hour records for that line. |
| btnPreview_Click | Generates a preview of the authorization status for the selected line, possibly opening a modal or new view. |
| btnSubmit_Click | Collects the approval decisions from the grid, validates them, and writes the authorization status back to the database. |

### 3. Data Interactions
* **Reads:** Hours, Authorization records, Line, DutyRoster (for NEL), Employee (for display).  
* **Writes:** Authorization records (updates approval status, timestamps, approver IDs).