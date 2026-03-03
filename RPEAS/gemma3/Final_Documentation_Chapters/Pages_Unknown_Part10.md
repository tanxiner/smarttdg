# Page: RPEAS_Approve_Form
**File:** RPEAS_Approve_Form.aspx.vb

### 1. User Purpose
Users review and approve or reject requests, potentially including actions like withdrawing funds or confirming approvals.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and sets up event handlers. |
| hide_ReRoute_Withdraw | Hides the ReRoute_Withdraw control, likely based on the current workflow. |
| Check_UserViewAccess(errormsg: String) | Validates the user's permissions to view and interact with the form. If access is denied, an error message is displayed. |
| PopulateData() | Loads data related to the request being reviewed, likely from a database. |
| FillGroup2(dtApprover: DataTable, dtCurrentUserAction: DataTable) | Populates a group of controls with data related to the approver and the current user's actions. |
| FillGroup3(dtApprover: DataTable, dtCurrentUserAction: DataTable) | Populates another group of controls with data, likely mirroring Group2. |
| FillGroup4(dtApprover: DataTable, dtCurrentUserAction: DataTable) | Populates a third group of controls with data. |
| FillGroup6(dtApprover: DataTable, dtCurrentUserAction: DataTable) | Populates a fourth group of controls with data. |
| FillGroup5(dtApprover: DataTable, dtCurrentUserAction: DataTable) | Populates a fifth group of controls with data. |
| Read_Only_Checkbox(chkbox: CheckBox) | Sets the value of a checkbox to read-only, likely to prevent the user from modifying it. |
| Read_Only_Radiobutton(radio: RadioButton) | Sets the value of a radio button to read-only. |
| Populate_Route2(ReRoute_lvl: String, ddl: DropDownList) | Populates a dropdown list with route options, likely based on the request type. |
| btnWithdrawn_Click(sender: Object, e: EventArgs) | Handles the click event for a button that allows the user to withdraw funds (if applicable). |
| btnConfirmWithdrawn_Click(sender: Object, e: System.EventArgs) | Handles the click event for a button that confirms the withdrawal action. |
| btnapprove_Submitby_Click(sender: Object, e: EventArgs) | Handles the click event for a button that submits the approval action. |
| btnConfirmApprove_Approve_Click(sender: Object, e: System.EventArgs) | Handles the click event for a button that confirms the approval action. |
| btnApprove_reject_Click(sender: Object, e: System.EventArgs) | Handles the click event for a button that submits the rejection action. |
| btnclose_Click(sender: Object, e: EventArgs) | Handles the click event for a button that closes the form. |
| btnEndorseCancel_Click(sender: Object, e: EventArgs) | Handles the click event for a button that cancels the endorsement (if applicable). |
| btnSubmitThruCancel_Click(sender: Object, e: EventArgs) | Handles the click event for a button that submits the cancellation action. |