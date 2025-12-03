# Page: DepotTARForm_App  
**File:** DepotTARForm_App.aspx.cs  

### 1. User Purpose  
Users manage Track Access Request (TAR) forms, including viewing, editing, and downloading attachments.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page, loads TAR request data, and sets up UI controls. |  
| **Tab1_Click / Tab2_Click / Tab3_Click** | Navigates between tabs (e.g., request details, approvals, conflicts) and updates the UI state. |  
| **PopOnLoad** | Preloads data or configurations when the page first loads. |  
| **lnkDownload_Click** | Retrieves attachment details for a specific TAR request to enable file downloads. |  
| **dgOR_ItemDataBound / gvPossAddPL_RowDataBound** | Binds data to grids/lists for displaying TAR-related entities (e.g., power lines, work locations). |  
| **lbtnAddBufferZone_Click** | Adds buffer zones to TAR requests by updating the database. |  
| **gvAddBufferZone_RowCommand** | Handles actions like deleting or modifying buffer zones in the grid. |  
| **lbCReject_Click / lbProcToApp_Click / lbNReject_Click / lbEndorse_Click** | Updates TAR request status (e.g., rejects, endorses, or processes the request). |  
| **gvConflictTAR_RowDataBound** | Displays conflicting TAR records for review. |  

### 3. Data Interactions  
* **Reads:** TARAccessReq, TAMS_TAR_Attachment, BlockedTar, PowerLine, WorkLocation, BufferZone  
* **Writes:** TARAccessReq, BlockedTar, BufferZone