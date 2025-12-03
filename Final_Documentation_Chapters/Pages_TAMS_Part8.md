# Page: DepotTARInbox
**File:** DepotTARInbox.aspx.cs

### 1. User Purpose
Users view a list of pending Terminal Access Requests (TARs) in the depot inbox, filter them by location, inspect individual requests, and submit selected requests for processing.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, initializes the page by calling `BindLocation` to populate the location dropdown and sets up any necessary view state. |
| **BindLocation** | Retrieves the list of depot locations from the data layer and binds them to the location selector control. |
| **lbSubmit_Click** | Gathers the selected TARs from the grid, updates their status to “Submitted”, and persists the changes via the data access layer. |
| **lnkD1StrTARNo_Click** | Handles clicks on the first TAR number link; opens a detailed view of that TAR in a modal or new page. |
| **lnkD2StrTARNo_Click** | Handles clicks on the second TAR number link; similar to the first link but may display alternate details or a different view. |
| **lbAppList_Click** | Navigates the user to a page that lists all applications associated with the selected TARs. |
| **gvDir1_RowDataBound** | During grid row binding, formats each row (e.g., sets link text, applies conditional styling) and attaches event handlers for row-specific actions. |
| **ddlLine_SelectedIndexChanged** | When the user selects a different depot line, refreshes the grid to show TARs relevant to that line. |

### 3. Data Interactions
* **Reads:** TAR, Location, DepotLine
* **Writes:** TAR (status update), AuditLog (submission record)

---

# Page: DepotTARSectorBooking
**File:** DepotTARSectorBooking.aspx.cs

### 1. User Purpose
Users allocate depot sectors for selected TARs, specify power requirements, review sector diagrams, and submit the booking for approval.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On initial load, calls `PopOnLoad` to populate controls (e.g., sector list, power options) and sets default selections. |
| **PopOnLoad** | Retrieves sector availability and power requirement options from the data layer and binds them to the corresponding controls. |
| **lbSubmit_Click** | Validates the selected sectors and power settings, creates a new sector booking record, and saves it via the data access layer. |
| **RBLPowerReq_SelectedIndexChanged** | Updates the UI to reflect the chosen power requirement, possibly enabling or disabling related controls. |
| **cbDir1All_CheckedChanged** | When the “Select All” checkbox is toggled, selects or deselects all sector rows in the grid. |
| **gvDir1_RowDataBound** | Formats each sector row (e.g., displays availability status, attaches selection checkboxes) and prepares data for submission. |
| **lbAppList_Click** | Navigates to a page listing all applications tied to the current booking context. |
| **lbBack_Click** | Returns the user to the previous page or clears the current booking form. |
| **lbDiagram_Click** | Opens a visual diagram of the depot layout, highlighting selected sectors. |
| **chkSel_CheckedChanged** | Handles individual sector selection changes, updating internal state or UI indicators accordingly. |

### 3. Data Interactions
* **Reads:** Sector, TAR, PowerRequirement, BookingTemplate
* **Writes:** SectorBooking, BookingAudit, TAR (booking status update)