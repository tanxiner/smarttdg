# Page: TARApplication
**File:** TARApplication.aspx.cs

### 1. User Purpose
Users submit track access requests and manage associated data through form inputs and grid controls.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes page state, loads default data, and sets up UI elements |
| btnSubmit_Click | Validates user inputs, saves track access request data, and updates related records |
| displayDates | Populates date fields based on selected track type and access permissions |
| showHideControls | Toggles visibility of form fields based on user role or selection criteria |
| GridView1_RowDataBound | Formats grid row display for main track information |
| gvX_BY_RowDataBound | Applies conditional formatting to blocked track segments in specific grids |
| displayLegend | Renders visual indicators for different track access status types |
| ddlLine_SelectedIndexChanged | Updates available access options based on selected track line |
| rbPossession_CheckedChanged | Adjusts form fields and data bindings based on possession vs protection selection |

### 3. Data Interactions
* **Reads:** TarSector, BlockedTar, User
* **Writes:** BlockedTar, TarSector