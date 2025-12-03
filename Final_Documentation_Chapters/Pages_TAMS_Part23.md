# Page: TARForm
**File:** TARForm.aspx.cs

### 1. User Purpose
Users fill out and submit a Technical Access Request (TAR) form, upload supporting documents, review and manage attachments, and navigate through a multi‑step wizard to provide all required details before final submission.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Initializes the page on first load: populates controls with existing TAR data, sets up wizard step visibility, and calls `PopOnLoad` to load related data such as attachments and possible items. |
| **Tab1_Click** | Switches the view to the first tab of the wizard, ensuring that any unsaved changes are preserved and the UI reflects the current step. |
| **Tab2_Click** | Switches to the second tab, updating navigation controls and preparing any dynamic lists needed for that step. |
| **Tab3_Click** | Switches to the third tab, finalizing the review section and enabling the submit button. |
| **PopOnLoad** | Loads initial data sets (e.g., department list, power sector options, existing attachments) into the page’s controls and stores them in session or view state for later use. |
| **chkOR_CheckedChanged** | Toggles the visibility of the “Other Reason” text field based on whether the user selects the “Other” option in the reason dropdown. |
| **dgOR_ItemDataBound** | Binds each row of the “Other Reasons” data grid, setting up controls such as delete links and formatting. |
| **btnUploadOR_Click** | Handles file upload for the TAR: validates the file type and size, stores the file in a temporary table, and refreshes the attachment grid. |
| **lnkDelete_Click** | Deletes a selected attachment from the temporary table and updates the attachment grid to reflect the removal. |
| **lnkDownload_Click** | Retrieves the selected attachment from `TAMS_TAR_Attachment_Temp` using the TAR and access request IDs, streams the file to the user for download. |
| **lbtnPossAPLAdd_Click** | Adds a new “Possible Access Point List” entry to the in‑memory collection and refreshes the corresponding grid view. |
| **lbtnPossWLAdd_Click** | Adds a new “Possible Work Load” entry to the in‑memory collection and updates the grid view. |
| **lbtnPossOPAdd_Click** | Adds a new “Possible Operation Point” entry to the in‑memory collection and updates the grid view. |
| **gvPossAddPL_RowDataBound** | Formats each row of the Possible Access Point List grid, attaching delete links and setting row styles. |
| **gvPossAddPL_RowCommand** | Processes commands from the Possible Access Point List grid (e.g., delete an entry) and updates the underlying collection. |
| **gvPossAddWL_RowDataBound** | Formats each row of the Possible Work Load grid, attaching delete links and setting row styles. |
| **gvPossAddWL_RowCommand** | Handles commands from the Possible Work Load grid, such as removing an entry. |
| **gvPossAddOO_RowDataBound** | Formats each row of the Possible Operation Point grid, attaching delete links and setting row styles. |
| **gvPossAddOO_RowCommand** | Processes commands from the Possible Operation Point grid, such as deleting an entry. |
| **ddlDeptComp_SelectedIndexChanged** | Updates dependent controls (e.g., department‑specific options) when the user selects a different department or company. |
| **lbCancelV1_Click** | Cancels the current wizard step, reverting any unsaved changes and returning to the previous step or the main page. |
| **lbNextV1_Click** | Validates the first step’s inputs, saves temporary data, and advances to the second step. |
| **lbCancelV2_Click** | Cancels changes made in the second step and returns to the first step. |
| **lbNextV2_Click** | Validates the second step’s inputs, saves temporary data, and advances to the third step. |
| **lbCancelV3_Click** | Cancels changes made in the third step and returns to the second step. |
| **lbNextV3_Click** | Validates the third step’s inputs and prepares the form for final submission. |
| **lbSubmitV2_Click** | Performs final validation across all steps, writes the TAR record and all related data (attachments, possible items) to the database, and redirects the user to a confirmation page. |
| **dgPossPowerSector_ItemDataBound** | Binds each row of the power sector data grid, setting up controls such as checkboxes or delete links. |
| **ddlBreakersOut_SelectedIndexChanged** | Updates breaker‑related controls when the user selects a different breaker type or quantity. |
| **valAccDets** | Validates that all required access details (date, type, TAR type, user roles) are present and correctly formatted before allowing the form to be submitted. |

### 3. Data Interactions
* **Reads:**  
  - TAR details and metadata from the main TAR table.  
  - Existing attachments from `TAMS_TAR_Attachment_Temp`.  
  - Department, company, and power sector lookup data.  
  - Possible access point, work load, and operation point lists from temporary collections.  

* **Writes:**  
  - New or updated TAR record to the main TAR table.  
  - Uploaded attachments to `TAMS_TAR_Attachment_Temp`.  
  - Deletion of attachments from `TAMS_TAR_Attachment_Temp`.  
  - Possible item entries (access points, work loads, operation points) to temporary collections or related tables upon final submission.  

---