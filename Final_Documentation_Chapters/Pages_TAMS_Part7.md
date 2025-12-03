# Page: DepotTARForm_App
**File:** DepotTARForm_App.aspx.cs

### 1. User Purpose
Users review and manage a Depot Transfer Application (TAR), including viewing details, approving or rejecting the request, adding buffer zones, and downloading related attachments.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads the TAR data via the DAL, sets up UI elements, and ensures the correct tab is displayed on first load. |
| Tab1_Click | Switches the view to the first tab, typically showing core TAR details. |
| Tab2_Click | Switches the view to the second tab, usually displaying related power sector or buffer zone information. |
| Tab3_Click | Switches the view to the third tab, often used for conflict or approval history. |
| PopOnLoad | Executes additional UI setup after the page has loaded, such as enabling/disabling controls based on user role or TAR status. |
| lnkDownload_Click | Retrieves the attachment record for the current TAR from the database and streams the file to the user for download. |
| dgOR_ItemDataBound | Formats each row of the “Other Requirements” data grid, possibly adding status icons or action links. |
| gvPossAddPL_RowDataBound | Formats rows in the “Potential Power Lines” grid, adding contextual information or action buttons. |
| gvPossAddWL_RowDataBound | Formats rows in the “Potential Water Lines” grid, similar to the power line grid. |
| gvPossAddOO_RowDataBound | Formats rows in the “Potential Other Objects” grid, preparing data for display. |
| dgPossPowerSector_ItemDataBound | Formats rows in the power sector data grid, ensuring correct display of sector details. |
| lbtnAddBufferZone_Click | Opens a dialog or form to add a new buffer zone to the TAR, then refreshes the buffer zone grid. |
| gvAddBufferZone_RowDataBound | Formats each buffer zone row, adding delete or edit links as appropriate. |
| gvAddBufferZone_RowCommand | Handles commands from the buffer zone grid, such as deleting a buffer zone or marking it as approved. |
| lbCReject_Click | Records a “Conditional Reject” action, updates the TAR status, and logs the decision. |
| lbProcToApp_Click | Moves the TAR from the processing stage to the approval stage, updating status and notifying relevant users. |
| lbNReject_Click | Records a “Non‑Conditional Reject” action, updates the TAR status, and logs the decision. |
| lbEndorse_Click | Marks the TAR as endorsed, updating status and recording the endorsement. |
| lbtnTARID_Click | Opens a detailed view or popup for the TAR ID, allowing the user to see full request information. |
| gvConflictTAR_RowDataBound | Formats rows in the conflict TAR grid, highlighting conflicts and providing quick actions. |

### 3. Data Interactions
* **Reads:**  
  - TAR details (core request data) via DAL.  
  - Attachments from `TAMS_TAR_Attachment` table (used in `lnkDownload_Click`).  
  - Buffer zone, power sector, and other related entities displayed in various grids.  
  - Conflict TAR records for the conflict grid.  

* **Writes:**  
  - Updates TAR status when approving, rejecting, or endorsing (handled in the corresponding button click methods).  
  - Adds or removes buffer zones through `lbtnAddBufferZone_Click` and `gvAddBufferZone_RowCommand`.  
  - Logs approval/rejection decisions and endorsements.  

The page relies on the `DAL` field of type `oDepotFormApp` for most data operations, ensuring a single point of data access throughout the lifecycle of the TAR review process.