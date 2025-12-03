# Page: DepotTARForm_App  
**File:** DepotTARForm_App.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) forms, including adding buffer zones, viewing attachments, and processing request statuses.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and loads default data for TAR forms. |  
| Tab1_Click | Switches the user interface to the "Request Details" tab. |  
| Tab2_Click | Switches the user interface to the "Buffer Zones" tab. |  
| Tab3_Click | Switches the user interface to the "Conflicts" tab. |  
| PopOnLoad | Loads pre-populated data for TAR forms based on user context. |  
| lnkDownload_Click | Retrieves and displays TAR attachments stored in the database. |  
| dgOR_ItemDataBound | Binds data to DataGrid controls for displaying TAR-related records. |  
| gvPossAddPL_RowDataBound | Populates GridView rows with power line data for buffer zone additions. |  
| gvPossAddWL_RowDataBound | Populates GridView rows with water line data for buffer zone additions. |  
| gvPossAddOO_RowDataBound | Populates GridView rows with overhead data for buffer zone additions. |  
| dgPossPowerSector_ItemDataBound | Binds power sector data to DataGrid for visualization. |  
| lbtnAddBufferZone_Click | Triggers the addition of a new buffer zone entry. |  
| gvAddBufferZone_RowDataBound | Displays buffer zone details in GridView rows. |  
| gvAddBufferZone_RowCommand | Handles user actions (e.g., editing/deleting) on buffer zone entries. |  
| lbCReject_Click | Processes a "Reject" action for a TAR request. |  
| lbProcToApp_Click | Processes a "Process to Application" action for a TAR request. |  
| lbNReject_Click | Processes a "Not Reject" action for a TAR request. |  
| lbEndorse_Click | Endorses a TAR request for approval. |  
| lbtnTARID_Click | Loads TAR details based on a specific request ID. |  
| gvConflictTAR_RowDataBound | Displays conflicting TAR records in GridView rows. |  

### 3. Data Interactions  
**Reads:**  
- `TAMS_TAR_Attachment`: Retrieves attachment files for TAR requests.  

**Writes:**  
- (No explicit write operations documented in the provided code.)