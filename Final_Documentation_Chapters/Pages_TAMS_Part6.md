# Page: DepotTARForm
**File:** DepotTARForm.aspx.cs

### 1. User Purpose
Users fill out and submit a Depot TAR (Tariff) request, upload supporting documents, manage potential access points, and review the status of their submission through a multi‑step wizard interface.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Initializes the wizard: loads user role and location data, populates dropdowns, sets the default tab, and calls `PopOnLoad` to display any introductory popup. |
| **Tab1_Click** | Switches the view to the first tab, showing basic request details and enabling related controls. |
| **Tab2_Click** | Switches to the second tab, where users can add or edit access request information. |
| **Tab3_Click** | Switches to the third tab, which displays uploaded attachments and allows further file operations. |
| **PopOnLoad** | Displays a modal or message box with guidance or alerts when the page first loads. |
| **chkOR_CheckedChanged** | Toggles visibility or required status of fields related to “Other Request” selections. |
| **dgOR_ItemDataBound** | Configures each row of the access request data grid, adding delete links and setting row styles. |
| **btnUploadOR_Click** | Handles file upload for an access request: validates the file, stores it in the temporary attachment table, and refreshes the grid. |
| **lnkDelete_Click** | Deletes the selected attachment from the temporary table and updates the grid display. |
| **lnkDownload_Click** | Retrieves the chosen file from the temporary table and streams it to the browser for download. |
| **lbtnPossAPLAdd_Click** | Adds a new possible access point to the current request and refreshes the corresponding grid. |
| **lbtnPossWLAdd_Click** | Adds a new possible work location to the current request and refreshes the corresponding grid. |
| **lbtnPossOPAdd_Click** | Adds a new possible operation point to the current request and refreshes the corresponding grid. |
| **gvPossAddPL_RowDataBound** | Sets up each row in the possible access point grid, including command buttons and data formatting. |
| **gvPossAddPL_RowCommand** | Processes row commands such as delete or edit for access points. |
| **gvPossAddWL_RowDataBound** | Configures each row in the possible work location grid. |
| **gvPossAddWL_RowCommand** | Handles commands for work location rows. |
| **gvPossAddOO_RowDataBound** | Configures each row in the possible operation point grid. |
| **gvPossAddOO_RowCommand** | Handles commands for operation point rows. |
| **ddlDeptComp_SelectedIndexChanged** | Updates dependent controls (e.g., sub‑departments or related data) when the department component selection changes. |
| **lbCancelV1_Click** | Cancels the current step and returns to the previous step or resets the wizard. |
| **lbNextV1_Click** | Validates step 1 data and moves the wizard forward to step 2. |
| **lbCancelV2_Click** | Cancels step 2 and returns to step 1. |
| **lbNextV2_Click** | Validates step 2 data and advances to step 3. |
| **lbCancelV3_Click** | Cancels step 3 and returns to step 2. |
| **lbNextV3_Click** | Validates step 3 data and moves to the final review or submission step. |
| **lbSubmitV2_Click** | Performs final validation, writes all collected data to the permanent TAR tables, clears temporary attachments, and displays a confirmation message. |
| **dgPossPowerSector_ItemDataBound** | Populates each row of the power sector grid with sector information and formatting. |
| **ddlBreakersOut_SelectedIndexChanged** | Adjusts available breaker options or related fields when the breaker selection changes. |
| **valAccDets** | Validates all access detail fields; returns `true` if the data passes validation, otherwise shows error messages. |
| **rdProtectionType_onSelectedIndexChanged** | Updates UI elements or required fields based on the selected protection type. |
| **ddlTimeslot_SelectedIndexChanged** | Refreshes time‑slot dependent data or constraints when the timeslot selection changes. |

### 3. Data Interactions
* **Reads:**  
  - `TAMS_TAR_Attachment_Temp` (to list and download attachments)  
  - Department, component, and power‑sector lookup tables for dropdowns  
  - Breaker and timeslot tables for selection lists  
  - Existing TAR and access‑request records when editing a submission  

* **Writes:**  
  - `TAMS_TAR_Attachment_Temp` (uploading new files, deleting temporary files)  
  - Permanent TAR tables (upon final submission)  
  - Access‑request and related detail tables (access points, work locations, operation points)  
  - Temporary staging tables for wizard steps before final commit  

---