# Page: TARApplication  
**File:** TARApplication.aspx.cs  

### 1. User Purpose  
Users submit a Technical Access Request (TAR) by selecting a line, choosing between possession or protection, reviewing available dates, and clicking **Submit** to record the request.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On the first load, sets default selections, initializes hidden fields, and calls **BindGrid** to populate the data grids. |
| **BindGrid** | Queries the database for TAR sector information and associated dates, stores the results in `tarSectors` and `dates`, and binds them to the grid views. |
| **btnSubmit_Click** | Validates that the user has selected a line, an access type, and at least one date; compiles the selected dates into a list; writes a new TAR application record to the database; and displays a confirmation message. |
| **displayDates** | Formats a list of `DateTime` values into a user‑friendly string and assigns it to the appropriate grid column based on the provided `TarType`, `AccessType`, and `Line`. |
| **showHideControls** | Toggles visibility of UI elements (date grids, legend, action buttons) depending on whether possession or protection is selected. |
| **GridView1_RowDataBound** | Handles row binding for the main grid, populating cells with sector data and applying any required formatting or styling. |
| **gv1_B1_RowDataBound … gv7_B2_RowDataBound** | Each method processes a specific grid view row, filling cells with sector details, applying color coding or icons, and adding interactive controls such as checkboxes or action links. |
| **displayLegend** | Builds a visual legend that explains the meaning of grid cell colors or symbols used to indicate status or availability. |
| **ddlLine_SelectedIndexChanged** | When the user selects a different line, updates internal boundary fields (`m_Bound1`, `m_Bound2`), refreshes the grids to show data for the chosen line, and resets any previously selected dates. |
| **rbPossession_CheckedChanged** | Switches the page to possession mode, sets `m_AccessType` accordingly, and calls **showHideControls** to adjust visible elements. |
| **rbProtection_CheckedChanged** | Switches the page to protection mode, sets `m_AccessType` accordingly, and calls **showHideControls** to adjust visible elements. |

### 3. Data Interactions  
* **Reads** – Retrieves data from the following tables/entities:  
  * `TarSector` – sector definitions for the selected line.  
  * `TarDate` – available dates for each sector.  
  * `TarAccess` – current access status for sectors.  
  * `TarLine` – line information used to populate the line dropdown.  

* **Writes** – Persists data to the following tables/entities:  
  * `TarApplication` – records the user’s submitted request, including selected line, access type, and dates.  
  * `TarAccessLog` (optional) – logs the user’s selections and any status changes for audit purposes.