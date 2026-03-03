# Page: RPEAS_SysParameter_Main
**File:** RPEAS_SysParameter_Main.aspx.vb

### 1. User Purpose
Users can view and modify system parameter values.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, binds controls, and sets up event handlers. |
| gv_BindControl | Populates the grid view with system parameter data. |
| ddl_BindControl | Populates the dropdown list with available parameter types. |
| BtnClear_Click | Clears the form fields. |
| dgSearch_EditCommand | Enables editing of a system parameter row in the grid view. |
| dgSearch_DeleteCommand | Deletes the selected system parameter row from the grid view. |
| ddlParaRecType_SelectedIndexChanged | Updates the display based on the selected parameter record type. |
| Fill_ParamType | Populates the parameter type dropdown list. |
| btnSave_Click | Saves the modified system parameter values to the database. |
| btnSearch_Click | Executes a search for system parameters. |
| btndel_ServerClick | Handles the delete command for a selected row. |