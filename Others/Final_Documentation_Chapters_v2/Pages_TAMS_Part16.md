# Page: TARForm
**File:** TARForm.aspx.cs

### 1. User Purpose
Users submit access requests with attachments and manage permissions for track access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes form state and loads user data |
| Tab1_Click | Navigates to the first tab section of the form |
| Tab2_Click | Navigates to the second tab section of the form |
| Tab3_Click | Navigates to the third tab section of the form |
| PopOnLoad | Preloads form data and sets initial configurations |
| chkOR_CheckedChanged | Updates access request status based on checkbox selection |
| dgOR_ItemDataBound | Binds data to DataGrid controls for OR records |
| btnUploadOR_Click | Handles file upload for OR attachments |
| lnkDelete_Click | Deletes selected OR records |
| lnkDownload_Click | Retrieves and downloads file attachments from the database |
| lbtnPossAPLAdd_Click | Adds a new access permission entry |
| lbtnPossWLAdd_Click | Adds a new access permission entry |
| lbtnPossOPAdd_Click | Adds a new access permission entry |
| gvPossAddPL_RowDataBound | Binds data to GridView for permission lists |
| gvPossAddPL_RowCommand | Handles row commands for permission list interactions |
| gvPossAddWL_RowDataBound | Binds data to GridView for permission lists |
| gvPossAddWL_RowCommand | Handles row commands for permission list interactions |
| gvPossAddOO_RowDataBound | Binds data to GridView for permission lists |
| gvPossAddOO_RowCommand | Handles row commands for permission list interactions |
| ddlDeptComp_SelectedIndexChanged | Updates department component selections |
| lbCancelV1_Click | Cancels the current form step |
| lbNextV1_Click | Advances to the next form step |
| lbCancelV2_Click | Cancels the current form step |
| lbNextV2_Click | Advances to the next form step |
| lbCancelV3_Click | Cancels the current form step |
| lbNextV3_Click | Advances to the next form step |
| lbSubmitV2_Click | Submits the form data for processing |
| dgPossPowerSector_ItemDataBound | Binds data to DataGrid for power sector records |
| ddlBreakersOut_SelectedIndexChanged | Updates breaker output selections |
| valAccDets | Validates access details before form submission |

### 3. Data Interactions
* **Reads:** TAR, TARAccessReq, TARAttachmentTemp, UserRoles, BlockedTar
* **Writes:** TAR, TARAccessReq, TARAttachmentTemp, UserRoles, BlockedTar