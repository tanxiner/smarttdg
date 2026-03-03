# Page: RPEAS_SysParameter_Edit
**File:** RPEAS_SysParameter_Edit.aspx.vb

### 1. User Purpose
Users edit system parameter details.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, populating data based on the selected system parameter. |
| FillInfo | Populates the form fields with data retrieved from the system parameter. |
| btnUpdate_Click | Saves the updated system parameter details. |
| btnSave_Click | Saves the system parameter details. |
| btnClear_Click | Clears the form fields. |
| btnback_Click | Returns to the previous page. |

### 3. Data Interactions
* **Reads:** BlockedTar (Not explicitly mentioned, but likely used for related data)
* **Writes:** RPEAS_SysParameter (The system parameter is saved)