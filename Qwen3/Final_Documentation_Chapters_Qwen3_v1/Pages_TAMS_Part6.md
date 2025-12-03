# Page: DepotTARForm  
**File:** DepotTARForm.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) forms, including uploading documents, configuring access settings, and submitting requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the form, loads default data, and sets up UI state based on user permissions. |  
| **Tab1_Click / Tab2_Click / Tab3_Click** | Navigates between form sections (tabs) and initializes tab-specific fields. |  
| **PopOnLoad** | Pre-fills form fields with existing TAR data or default values. |  
| **chkOR_CheckedChanged** | Toggles visibility of related fields based on checkbox selection. |  
| **btnUploadOR_Click** | Handles file uploads for attachments, saves metadata to the database. |  
| **lnkDelete_Click / lnkDownload_Click** | Deletes or retrieves attachments from the TAMS_TAR_Attachment_Temp table. |  
| **lbtnPossAPLAdd_Click / lbtnPossWLAdd_Click / lbtnPossOPAdd_Click** | Adds entries to access lists (e.g., approved users, watchlist, operators). |  
| **gvPossAddPL_RowCommand / gvPossAddWL_RowCommand / gvPossAddOO_RowCommand** | Manages row-level actions (e.g., edit/delete) for access lists. |  
| **lbNextV1_Click / lbNextV2_Click / lbNextV3_Click** | Advances users through form validation stages. |  
| **lbSubmitV2_Click** | Validates all form data, saves TAR details to the database, and finalizes the request. |  
| **valAccDets** | Validates access configuration details (e.g., roles, permissions) before submission. |  

### 3. Data Interactions  
* **Reads:** TARAccessReq, TARId, TARAccessReqId, UserRoles, AttachmentMetadata (TAMS_TAR_Attachment_Temp)  
* **Writes:** TARAccessReq, TARId, TARAccessReqId, UserRoles, AttachmentMetadata (TAMS_TAR_Attachment_Temp)