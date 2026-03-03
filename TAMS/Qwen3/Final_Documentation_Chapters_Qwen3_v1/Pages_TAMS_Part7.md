# Page: DepotTARForm_App  
**File:** DepotTARForm_App.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) forms, including viewing details, adding buffer zones, and handling approval/rejection actions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads default data, and sets up UI state. |  
| Tab1_Click | Switches the interface to the "Request Details" tab for form input. |  
| Tab2_Click | Switches to the "Attachments" tab to display or download files. |  
| Tab3_Click | Switches to the "Conflict Check" tab to review overlapping TAR requests. |  
| PopOnLoad | Preloads data such as user permissions or existing TAR records. |  
| lnkDownload_Click | Retrieves and downloads an attachment file from the database using the TARAccessReqId. |  
| dgOR_ItemDataBound | Binds data to DataGrid controls for displaying TAR-related records. |  
| gvPossAddPL_RowDataBound | Populates GridView rows for power line additions during TAR processing. |  
| gvPossAddWL_RowDataBound | Populates GridView rows for water line additions during TAR processing. |  
| gvPossAddOO_RowDataBound | Populates GridView rows for overhead line additions during TAR processing. |  
| dgPossPowerSector_ItemDataBound | Binds data to DataGrid for power sector-specific TAR details. |  
| lbtnAddBufferZone_Click | Triggers the addition of a buffer zone entry for conflict mitigation. |  
| gvAddBufferZone_RowDataBound | Displays buffer zone entries in a GridView for review. |  
| gvAddBufferZone_RowCommand | Handles user actions (e.g., editing/deleting) on buffer zone entries. |  
| lbCReject_Click | Marks a TAR request as rejected and updates its status in the system. |  
| lbProcToApp_Click | Moves a TAR request to the "Processing" stage for further review. |  
| lbNReject_Click | Notes a rejection reason and finalizes the TAR request closure. |  
| lbEndorse_Click | Approves a TAR request and initiates the access granting process. |  
| lbtnTARID_Click | Filters or searches TAR records by specific identifier (e.g., TARAccessReqId). |  
| gvConflictTAR_RowDataBound | Displays conflicting TAR records in a GridView for resolution. |  

### 3. Data Interactions  
* **Reads:** TARAccessReqId, FileName, FileType, FileUpload (from TAMS_TAR_Attachment)  
* **Writes:** TARAccessReqId (for status updates, buffer zone entries, and conflict records)