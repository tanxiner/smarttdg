# Page: SignUpNewSystem
**File:** SignUpNewSystem.aspx.cs

### 1. User Purpose
Users register a new system—either internal or external—by selecting options and submitting the form.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page; if first load, calls `SetupPage` to populate controls. |
| SetupPage | Builds and binds data tables for system selection, configuring internal and external options. |
| ResetPage | Clears all input fields and resets control states to defaults. |
| buildSystemSelectiondata(isExternal) | Generates a `DataTable` containing system options filtered by the `isExternal` flag. |
| UpdateGVRows(dr, isExternal) | Updates a GridView row with data from the provided `DataRow`, applying formatting based on whether the system is external. |
| gv_internalNewSystem_RowDataBound | Handles row‑level formatting and control visibility during GridView data binding. |
| btn_externalNext_Click | Advances the user to the next step of the external system registration workflow. |
| btn_internalNewSave_Click | Validates entered data, creates a new internal system record, and persists it to the database. |

### 3. Data Interactions
* **Reads:** System catalog (internal and external), User session data.  
* **Writes:** New system record (internal system table).

---

# Page: SiteMaster
**File:** Site.Master.cs

### 1. User Purpose
Provides navigation and session management for all pages, allowing users to view their profile, log out, or start a new system sign‑up.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up common master page elements and ensures user session is active. |
| linkB_viewProfile_Click | Redirects the user to their profile page. |
| linkB_logout_Click | Terminates the user session and redirects to the login page. |
| linkB_signUpNewSystem_Click | Navigates the user to the SignUpNewSystem page. |

### 3. Data Interactions
* **Reads:** Current user session information.  
* **Writes:** Session termination on logout.

---

# Page: Site_Mobile
**File:** Site.Mobile.Master.cs

### 1. User Purpose
Renders a mobile‑optimized layout for the application, ensuring consistent navigation and styling on handheld devices.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Configures mobile‑specific resources and layout settings. |

### 3. Data Interactions
* **Reads:** None explicitly; primarily layout configuration.  
* **Writes:** None.

---

# Page: SummaryReport
**File:** SummaryReport.aspx.cs

### 1. User Purpose
Displays aggregated reporting data, allowing users to filter by line and perform searches to refine the displayed results.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Calls `PopOnLoad` to populate initial report data and sets up controls. |
| PopOnLoad | Retrieves baseline report data via the `DAL` (oRGS) object and binds it to the UI. |
| lbSearch_Click | Executes a search based on user input, refreshing the report display with matching records. |
| ddlLine_SelectedIndexChanged | Updates the report to show data for the selected line, re‑binding the grid or chart accordingly. |

### 3. Data Interactions
* **Reads:** Report data from the `oRGS` data access layer.  
* **Writes:** None (report is read‑only).