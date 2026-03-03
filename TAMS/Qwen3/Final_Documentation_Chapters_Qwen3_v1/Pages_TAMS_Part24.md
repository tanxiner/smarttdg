# Page: TARForm_App  
**File:** TARForm_App.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) applications, including viewing attachments, adding buffer zones/TVF stations, and approving/rejecting requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page state and loads default data (e.g., TAR details, attachments). |  
| Tab1_Click | Switches to the main TAR request view. |  
| Tab2_Click | Switches to the buffer zone management section. |  
| Tab3_Click | Switches to the TVF station management section. |  
| PopOnLoad | Loads initial data (e.g., user permissions, TAR status) when the page loads. |  
| lnkDownload_Click | Retrieves and displays TAR attachments from the database. |  
| dgOR_ItemDataBound | Binds data to DataGrid controls for displaying TAR-related records. |  
| gvPossAddPL_RowDataBound | Formats GridView rows for adding power line entries. |  
| gvPossAddWL_RowDataBound | Formats GridView rows for adding work location entries. |  
| gvPossAddOO_RowDataBound | Formats GridView rows for adding operational override entries. |  
| dgPossPowerSector_ItemDataBound | Binds power sector data to DataGrid for display. |  
| lbtnAddBufferZone_Click | Triggers adding a new buffer zone entry. |  
| gvAddBufferZone_RowDataBound | Formats GridView rows for buffer zone management. |  
| gvAddBufferZone_RowCommand | Handles user actions (e.g., delete) on buffer zone entries. |  
| lbtnAddTVFStation_Click | Triggers adding a new TVF station entry. |  
| gvAddTVF_RowDataBound | Formats GridView rows for TVF station management. |  
| gvAddTVF_RowCommand | Handles user actions (e.g., delete) on TVF station entries. |  
| lbCReject_Click | Rejects a TAR request and updates the status. |  
| lbProcToApp_Click | Processes a TAR request for approval. |  
| lbNReject_Click | Rejects a TAR request with additional notes. |  
| lbEndorse_Click | Endorses a TAR request for final approval. |  
| lbtnTARID_Click | Searches or filters TAR records by ID. |  
| gvConflictTAR_RowDataBound | Formats GridView rows to show conflicting TAR entries. |  
| rblTVFRunMode_SelectedIndexChanged | Updates TVF run mode settings based on user selection. |  

### 3. Data Interactions  
* **Reads:** TARAccessReq, TARAccess, BlockedTar, User, TAMS_TAR_Attachment  
* **Writes:** TARAccessReq, TARAccess, BlockedTar, User