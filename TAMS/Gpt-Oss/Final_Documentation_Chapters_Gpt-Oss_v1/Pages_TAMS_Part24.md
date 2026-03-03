# Page: TARForm_App
**File:** TARForm_App.aspx.cs

---

### 1. User Purpose  
Users view and manage a Transmission Access Request (TAR) application. They can inspect request details, download attached documents, add buffer zones or TVF stations, review potential conflicts, and change the request’s status (reject, endorse, or forward to the next processing stage).

---

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, the page initializes the data‑access object (`DAL`), retrieves the TAR record identified by a query string or session variable, populates the UI with request details, and sets up any required client‑side scripts. |
| **Tab1_Click** | Switches the view to the first tab, typically showing core request information. |
| **Tab2_Click** | Switches to the second tab, usually displaying related data such as buffer zones or TVF stations. |
| **Tab3_Click** | Switches to the third tab, often used for conflict or review information. |
| **PopOnLoad** | Displays a modal or popup (e.g., a confirmation dialog) when the page finishes loading, based on certain conditions such as pending approvals. |
| **lnkDownload_Click** | Executes a SQL query to fetch the file name, type, and binary data from `TAMS_TAR_Attachment` for the current TAR, then streams the file to the browser for download. |
| **dgOR_ItemDataBound** | Formats each row of the “Other Requirements” data grid, setting visibility or styling based on the underlying data (e.g., marking missing items). |
| **gvPossAddPL_RowDataBound** | Configures each row of the “Possible Power Lines” grid, adding action links or status indicators. |
| **gvPossAddWL_RowDataBound** | Similar to the above but for “Possible Water Lines” or equivalent. |
| **gvPossAddOO_RowDataBound** | Handles row formatting for “Possible Other Objects” grid. |
| **dgPossPowerSector_ItemDataBound** | Formats rows in the power sector data grid, possibly highlighting sectors that overlap with the request. |
| **lbtnAddBufferZone_Click** | Adds a new buffer zone entry to the request, updating the underlying data store and refreshing the buffer zone grid. |
| **gvAddBufferZone_RowDataBound** | Sets up each buffer zone row, including delete or edit links and formatting. |
| **gvAddBufferZone_RowCommand** | Handles commands from the buffer zone grid (e.g., delete a buffer zone, open an edit dialog). |
| **lbtnAddTVFStation_Click** | Adds a new TVF station to the request, persisting the change and re‑binding the TVF station grid. |
| **gvAddTVF_RowDataBound** | Formats each TVF station row, adding action links and status indicators. |
| **gvAddTVF_RowCommand** | Processes commands from the TVF station grid (e.g., delete or edit a station). |
| **lbCReject_Click** | Marks the TAR as “Rejected – Conditional” in the database, logs the action, and updates the UI to reflect the new status. |
| **lbProcToApp_Click** | Moves the TAR to the next processing stage (e.g., “Under Review”), updating status fields and notifying relevant users. |
| **lbNReject_Click** | Marks the TAR as “Rejected – Not Approved”, records the decision, and refreshes the status display. |
| **lbEndorse_Click** | Records an endorsement of the TAR, updating status and any associated endorsement metadata. |
| **lbtnTARID_Click** | Opens a detailed view or modal for the specific TAR ID, allowing the user to see all related information in a focused window. |
| **gvConflictTAR_RowDataBound** | Highlights or annotates rows in the conflict grid where the TAR conflicts with other requests or regulatory constraints. |
| **rblTVFRunMode_SelectedIndexChanged** | Adjusts the UI or underlying data when the user selects a different TVF run mode (e.g., “Full”, “Partial”), possibly re‑filtering the TVF station list. |

---

### 3. Data Interactions  

* **Reads**  
  * `TAMS_TAR_Attachment` – to retrieve downloadable files.  
  * (Implied) `TAMS_TAR` – to load the main request record.  
  * (Implied) `TAMS_TAR_BufferZone`, `TAMS_TAR_TVFStation`, `TAMS_TAR_PossiblePowerSector`, etc. – to populate the various grids.

* **Writes**  
  * `TAMS_TAR` – status updates (reject, endorse, process to application).  
  * `TAMS_TAR_BufferZone` – adding or deleting buffer zones.  
  * `TAMS_TAR_TVFStation` – adding or deleting TVF stations.  
  * (Implied) audit or log tables for status changes and user actions.

* **Other Interactions**  
  * The `DAL` field of type `oFormApp` is used throughout to execute these database operations, encapsulating SQL commands and transaction handling.  

---