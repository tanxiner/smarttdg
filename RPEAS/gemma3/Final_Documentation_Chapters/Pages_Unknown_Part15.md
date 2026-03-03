# Page: RPEAS_Form_View_Org
**File:** RPEAS_Form_View_Org.aspx.vb

### 1. User Purpose
Users view organizational data.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and populates data. |
| hide_ReRoute_Withdraw |  (No specific logic described in the input) |
| Check_UserViewAccess(errormsg: String) | Checks user permissions and displays an error message if access is denied. |
| PopulateData() | Populates the page with data, likely from a data source. |
| Read_Only_Checkbox(chkbox: CheckBox) | Sets the read-only property of a checkbox control. |
| Read_Only_Radiobutton(radio: RadioButton) | Sets the read-only property of a radio button control. |
| btncancel_Approver_Click(sender: Object, e: EventArgs) | Handles the click event of a "Cancel" button, likely navigating the user back to a previous page. |

---