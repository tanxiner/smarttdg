# Page: TARForm
**File:** TARForm.aspx.cs

### 1. User Purpose
Users complete a multi-tab form to request track access, manage attachments, and define access permissions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes page state, loads base data, and sets up UI elements |
| Tab1_Click | Navigates to the first tab section of the form |
| Tab2_Click | Navigates to the second tab section of the form |
| Tab3_Click | Navigates to the third tab section of the form |
| PopOnLoad | Preloads data and sets initial form state |
| chkOR_CheckedChanged | Updates UI based on checkbox selection for OR documents |
| dgOR_ItemDataBound | Binds OR document data to DataGrid controls |
| btnUploadOR_Click | Handles file upload for OR documents |
| lnkDelete_Click | Deletes selected OR document entries |
| lnkDownload_Click | Retrieves and displays attachment metadata from the database |
| lbtnPossAPLAdd_Click | Adds access permission entries to the application list |
| lbtnPossWLAdd_Click | Adds access permission entries to the worklist |
| lbtnPossOPAdd_Click | Adds access permission entries to the operations list |
| gvPossAddPL_RowDataBound | Binds data to GridView controls for permission lists |
| gvPossAddPL_RowCommand | Handles row-level actions in permission list GridView |
| ddlDeptComp_SelectedIndexChanged | Updates form based on selected department/component |
| lbCancelV1_Click | Cancels form submission at validation step 1 |
| lbNextV1_Click | Proceeds to validation step 2 |
| lbCancelV2_Click | Cancels form submission at validation step 2 |
| lbNextV2_Click | Proceeds to validation step 3 |
| lbCancelV3_Click | Cancels form submission at final validation step |
| lbNextV3_Click | Proceeds to final submission confirmation |
| lbSubmitV2_Click | Submits form data for processing |
| dgPossPowerSector_ItemDataBound | Binds power sector data to DataGrid controls |
| ddlBreakersOut_SelectedIndexChanged | Updates form based on selected breaker configuration |
| valAccDets | Validates access details before allowing form submission |

### 3. Data Interactions
* **Reads:** TAMS_TAR_Attachment_Temp (attachment metadata), User (access permissions), BlockedTar (blocked track records)
* **Writes:** TAMS_TAR_Attachment_Temp (attachment storage), TARAccessReq (access request records), TARAccess (permission definitions)