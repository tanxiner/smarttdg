# Page: DepotTARForm  
**File:** DepotTARForm.aspx.cs  

### 1. User Purpose  
Users request track access by filling out a multi-step form with detailed information, attachments, and permissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the form, loads default data, and sets up tab navigation states. |  
| **Tab1_Click / Tab2_Click / Tab3_Click** | Navigates between form steps, validates required fields, and saves progress. |  
| **PopOnLoad** | Populates dropdowns and grids with preloaded data (e.g., departments, breakers). |  
| **chkOR_CheckedChanged** | Toggles visibility of attachment fields based on checkbox selection. |  
| **dgOR_ItemDataBound / btnUploadOR_Click** | Manages temporary attachment uploads and displays them in a grid. |  
| **lnkDelete_Click / lnkDownload_Click** | Deletes or downloads temporary attachments from the database. |  
| **lbtnPossAPLAdd / lbtnPossWLAdd / lbtnPossOPAdd** | Adds new entries to permission grids (e.g., access lists, worklists). |  
| **gvPossAddPL_RowCommand / gvPossAddWL_RowCommand** | Handles row-level actions (e.g., delete, edit) in permission grids. |  
| **ddlDeptComp_SelectedIndexChanged / ddlBreakersOut_SelectedIndexChanged** | Updates dependent fields or filters based on dropdown selections. |  
| **lbCancelV1 / lbNextV1 / lbSubmitV2** | Validates form data, navigates between steps, or submits the request. |  
| **valAccDets** | Validates user access details (e.g., roles, permissions) before proceeding. |  
| **rdProtectionType_onSelectedIndexChanged** | Updates protection-related fields based on selected protection type. |  

### 3. Data Interactions  
* **Reads:** TARAccessRequest, TARAccessReqId, TAMS_TAR_Attachment_Temp, UserRoles, LocationCode  
* **Writes:** TARAccessRequest, TARAccessReqId, TAMS_TAR_Attachment_Temp, UserPermissions