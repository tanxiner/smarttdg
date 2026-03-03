# Page: TARForm_App
**File:** TARForm_App.aspx.cs

### 1. User Purpose
Users manage Track Access Request (TAR) forms with multiple tabs, attachment downloads, and buffer zone/TVF station configurations.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes page state, loads default data, and sets up UI controls |
| Tab1_Click | Switches view to the main TAR form section |
| Tab2_Click | Switches view to additional TAR details and permissions |
| Tab3_Click | Switches view to conflict checks and approvals |
| PopOnLoad | Preloads data for buffer zones and TVF stations |
| lnkDownload_Click | Retrieves and displays TAR attachments from the database |
| dgOR_ItemDataBound | Formats data grid rows for OR records |
| gvPossAddPL_RowDataBound | Customizes GridView rows for power line additions |
| gvPossAddWL_RowDataBound | Customizes GridView rows for water line additions |
| gvPossAddOO_RowDataBound | Customizes GridView rows for overhead line additions |
| dgPossPowerSector_ItemDataBound | Formats data grid rows for power sector information |
| lbtnAddBufferZone_Click | Triggers buffer zone addition workflow |
| gvAddBufferZone_RowDataBound | Customizes GridView rows for buffer zone entries |
| gvAddBufferZone_RowCommand | Handles buffer zone addition/removal actions |
| lbtnAddTVFStation_Click | Triggers TVF station addition workflow |
| gvAddTVF_RowDataBound | Customizes GridView rows for TVF station entries |
| gvAddTVF_RowCommand | Handles TVF station addition/removal actions |
| lbCReject_Click | Processes complete rejection of TAR request |
| lbProcToApp_Click | Moves TAR to application review stage |
| lbNReject_Click | Processes partial rejection of TAR request |
| lbEndorse_Click | Approves TAR request for final processing |
| lbtnTARID_Click | Searches for TAR by ID |
| gvConflictTAR_RowDataBound | Customizes GridView rows for conflict checks |
| rblTVFRunMode_SelectedIndexChanged | Updates UI based on TVF run mode selection |

### 3. Data Interactions
* **Reads:** TAMS_TAR_Attachment (for file downloads), TARAccessReq (for request details)
* **Writes:** TARAccessReq (for request updates), BufferZone (for zone additions), TVFStation (for station additions)