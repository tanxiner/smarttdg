# Technical Documentation

## Table of Contents

### System Documentation
- [Basepage](#system-documentation-basepage)
- [RPEAS_Admin_Menu_Mapping](#system-documentation-rpeas-admin-menu-mapping)
- [RPEAS_Admin_Role_Maint - Copy.aspx](#system-documentation-rpeas-admin-role-maint---copyaspx)
- [RPEAS_Admin_Role_Maint](#system-documentation-rpeas-admin-role-maint)
- [RPEAS_Admin_User_Edit](#system-documentation-rpeas-admin-user-edit)
- [RPEAS_Admin_User_Maint](#system-documentation-rpeas-admin-user-maint)
- [RPEAS_Admin_User_Mapping](#system-documentation-rpeas-admin-user-mapping)
- [RPEAS_All_Forms](#system-documentation-rpeas-all-forms)
- [RPEAS_All_Forms_PA](#system-documentation-rpeas-all-forms-pa)
- [RPEAS_Approve_Form](#system-documentation-rpeas-approve-form)
- [RPEAS_Approve_Form_Org](#system-documentation-rpeas-approve-form-org)
- [RPEAS_Completed_Form](#system-documentation-rpeas-completed-form)
- [RPEAS_Create_Form](#system-documentation-rpeas-create-form)
- [RPEAS_Form_View.aspx](#system-documentation-rpeas-form-viewaspx)
- [RPEAS_Form_View_Org](#system-documentation-rpeas-form-view-org)
- [RPEAS_Login](#system-documentation-rpeas-login)
- [RPEAS_Main](#system-documentation-rpeas-main)
- [RPEAS_Outstnd_Form](#system-documentation-rpeas-outstnd-form)
- [RPEAS_PA_Supervisor_Edit](#system-documentation-rpeas-pa-supervisor-edit)
- [RPEAS_SysParameter_Edit](#system-documentation-rpeas-sysparameter-edit)
- [RPEAS_SysParameter_Main](#system-documentation-rpeas-sysparameter-main)

### Database Reference (SQL)
- [EAS_Admin_CheckRoles](#database-reference-sql-eas-admin-checkroles)
- [EAS_Admin_CheckUsers](#database-reference-sql-eas-admin-checkusers)
- [EAS_Admin_GET_Roles](#database-reference-sql-eas-admin-get-roles)
- [EAS_Admin_GET_Users](#database-reference-sql-eas-admin-get-users)
- [EAS_Admin_GetPALists](#database-reference-sql-eas-admin-getpalists)
- [EAS_Admin_GetSupervisorLists](#database-reference-sql-eas-admin-getsupervisorlists)
- [008_EAS_Admin_MenuRole_Insert.md](#database-reference-sql-008-eas-admin-menurole-insertmd)
- [EAS_Admin_MenuRoles_GetInfo](#database-reference-sql-eas-admin-menuroles-getinfo)
- [EAS_Admin_PA_Supervisor_Insert](#database-reference-sql-eas-admin-pa-supervisor-insert)
- [EAS_Admin_Role_Delete](#database-reference-sql-eas-admin-role-delete)
- [EAS_Admin_Role_Insert](#database-reference-sql-eas-admin-role-insert)
- [EAS_Admin_Role_Update](#database-reference-sql-eas-admin-role-update)
- [EAS_Admin_User_GetInfo](#database-reference-sql-eas-admin-user-getinfo)
- [EAS_Admin_UserRole_Insert](#database-reference-sql-eas-admin-userrole-insert)
- [EAS_Admin_User_Delete](#database-reference-sql-eas-admin-user-delete)
- [EAS_Admin_User_Insert](#database-reference-sql-eas-admin-user-insert)
- [EAS_Admin_User_Update](#database-reference-sql-eas-admin-user-update)
- [EAS_BinaryFileSave](#database-reference-sql-eas-binaryfilesave)
- [EAS_Form_Check_Action_Access_Lists](#database-reference-sql-eas-form-check-action-access-lists)
- [EAS_Form_Check_View_Access_Lists](#database-reference-sql-eas-form-check-view-access-lists)
- [EAS_Form_Create_New_Form](#database-reference-sql-eas-form-create-new-form)
- [EAS_Form_Get_All_Froms](#database-reference-sql-eas-form-get-all-froms)
- [EAS_Form_Get_All_Froms_PA](#database-reference-sql-eas-form-get-all-froms-pa)
- [EAS_Form_Get_ApproverLists](#database-reference-sql-eas-form-get-approverlists)
- [EAS_Form_Get_Attach_File_ByID](#database-reference-sql-eas-form-get-attach-file-byid)
- [EAS_Form_Get_Attach_Files](#database-reference-sql-eas-form-get-attach-files)
- [EAS_Form_Get_Company](#database-reference-sql-eas-form-get-company)
- [EAS_Form_Get_Completed_Lists](#database-reference-sql-eas-form-get-completed-lists)
- [EAS_Form_Get_Detail_Info](#database-reference-sql-eas-form-get-detail-info)
- [EAS_Form_Get_Detail_Info_ExportPDF](#database-reference-sql-eas-form-get-detail-info-exportpdf)
- [EAS_Form_Get_Outstanding_Lists](#database-reference-sql-eas-form-get-outstanding-lists)
- [EAS_Form_Get_Prefix](#database-reference-sql-eas-form-get-prefix)
- [EAS_Form_Get_ReRoute_User_Lists](#database-reference-sql-eas-form-get-reroute-user-lists)
- [EAS_Form_Get_ServerFileUploadDetails](#database-reference-sql-eas-form-get-serverfileuploaddetails)
- [EAS_Form_Get_UserLogid_Check](#database-reference-sql-eas-form-get-userlogid-check)
- [EAS_Form_Get_UserLogid_GUID](#database-reference-sql-eas-form-get-userlogid-guid)
- [EAS_Form_Get_UserLogid_Update](#database-reference-sql-eas-form-get-userlogid-update)
- [EAS_Form_Save_Approved_Action](#database-reference-sql-eas-form-save-approved-action)
- [EAS_Form_Save_Attach_Files](#database-reference-sql-eas-form-save-attach-files)
- [EAS_Form_Save_ReRoute_ProceedNxtLevel](#database-reference-sql-eas-form-save-reroute-proceednxtlevel)
- [EAS_Form_Save_Rejected_Action](#database-reference-sql-eas-form-save-rejected-action)
- [EAS_Form_Save_Withdrawn_Action](#database-reference-sql-eas-form-save-withdrawn-action)
- [EAS_Form_Update_Binary_File](#database-reference-sql-eas-form-update-binary-file)
- [EAS_GET_ErrorMessage](#database-reference-sql-eas-get-errormessage)
- [EAS_GetAttachList](#database-reference-sql-eas-getattachlist)
- [EAS_Get_Menu](#database-reference-sql-eas-get-menu)
- [EAS_Get_MenuChild](#database-reference-sql-eas-get-menuchild)
- [EAS_Get_System_Name](#database-reference-sql-eas-get-system-name)
- [EAS_Get_UserInfo](#database-reference-sql-eas-get-userinfo)
- [EAS_PARAM_GET_PARAM_REF_DET_ByParam](#database-reference-sql-eas-param-get-param-ref-det-byparam)
- [EAS_PARAM_GET_PARAM_TYPE](#database-reference-sql-eas-param-get-param-type)
- [EAS_PARAM_GET_REF](#database-reference-sql-eas-param-get-ref)
- [EAS_PARAM_GET_REF_DET](#database-reference-sql-eas-param-get-ref-det)
- [EAS_PARAM_REF_DET_Delete](#database-reference-sql-eas-param-ref-det-delete)
- [EAS_PARAM_REF_DET_Insert](#database-reference-sql-eas-param-ref-det-insert)
- [EAS_PARAM_REF_DET_Update](#database-reference-sql-eas-param-ref-det-update)
- [EAS_Send_Approval_Email](#database-reference-sql-eas-send-approval-email)
- [EAS_Send_Approval_Email_Reminder](#database-reference-sql-eas-send-approval-email-reminder)
- [EAS_Send_Final_Approved_Email](#database-reference-sql-eas-send-final-approved-email)
- [EAS_Send_ProcdNxtLvl_Email](#database-reference-sql-eas-send-procdnxtlvl-email)
- [EAS_Send_ReRoute_Email](#database-reference-sql-eas-send-reroute-email)
- [EAS_Send_Rejected_Email](#database-reference-sql-eas-send-rejected-email)
- [EAS_Send_Withdrawn_Email](#database-reference-sql-eas-send-withdrawn-email)
- [EAlertQ_EnQueue](#database-reference-sql-ealertq-enqueue)
- [SMTP_GET_Email_Lists](#database-reference-sql-smtp-get-email-lists)
- [SMTP_Update_Email_Lists](#database-reference-sql-smtp-update-email-lists)
- [test](#database-reference-sql-test)

<br>


<a id='system-documentation-basepage'></a>
# Page: Basepage
**File:** Basepage.aspx.vb

### 1. User Purpose
This page likely serves as a base page for other ASP.NET Web Forms pages within the RPEAS application. It provides common functionality and data access components.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | This method is the entry point for the page. It likely initializes data connections, loads initial data, and sets up event handlers. |
| PromptJsMsg | This method likely sends a JavaScript message to the browser, potentially for displaying alerts or updating the user interface dynamically. (inferred from: Basepage.aspx.vb) |
| OpenNewWindow | This method opens a new browser window or tab, potentially for displaying a detailed form or external resource. (inferred from: Basepage.aspx.vb) |
| MsgBox | This method displays a message box to the user, likely for error reporting or confirmation. (inferred from: Basepage.aspx.vb) |
| GetSqlConnection | This method retrieves a connection object to the database. (inferred from: Basepage.aspx.vb) |
| GetSqlCommand | This method creates a SQL command object, likely based on a string passed to it. (inferred from: Basepage.aspx.vb) |
| GetSqlDataAdapter | This method creates a SqlDataAdapter object, used for populating data tables from a SQL database. (inferred from: Basepage.aspx.vb) |
| QuoteRemove | This method removes single quotes from a string, likely for use in constructing SQL queries. (inferred from: Basepage.aspx.vb) 

--- 

# Page: EAS_Home
**File:** EAS_Home.aspx.vb

### 1. User Purpose
This page likely displays the home page for the EAS (Enterprise Application Services) system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | This method is the entry point for the page. It likely initializes data connections, loads initial data, and sets up event handlers. |

---


<a id='system-documentation-rpeas-admin-menu-mapping'></a>
# Page: RPEAS_Admin_Menu_Mapping
**File:** RPEAS_Admin_Menu_Mapping.aspx.vb

### 1. User Purpose
This page allows administrators to map menu items to specific data records, likely for configuring a system's menu structure.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and prepares the data grid for display. |
| FillInfo | Populates the data grid with menu mapping data. |
| BinddgSearch | Binds the data grid with the populated data. |
| dgSearch_ItemDataBound | Handles the event when a new item is bound to the data grid, likely for adding or editing a menu mapping. |
| btnSave_Click | Saves the current menu mapping data to the system. |
| SaveInfo | Saves the menu mapping data, potentially including error handling. |
| dgSearch_SortCommand | Sorts the data displayed in the data grid based on the selected column. |
| btnclose_Click | Closes the current window or dialog. |

---

# Page: RPEAS_ExportPDF_Summary
**File:** REAPS_ExportPDF_Summary.aspx.vb

### 1. User Purpose
This page allows users to generate a PDF summary of data, likely related to REAPS transactions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and prepares for PDF generation. |
| PopulateData | Populates the data used for the PDF generation. |
| export_MergePDF | Merges the data into a single PDF document. |
| mergePdfs |  Merges multiple PDF files into a single PDF. |
| AddPageNumber | Adds page numbers to the generated PDF. |
| CreatePDF2 | Creates the PDF document. |
| populateloghistory | Logs the PDF generation process. |
| populateAttachment |  Handles attachments related to the PDF generation. |

---


<a id='system-documentation-rpeas-admin-role-maint---copyaspx'></a>
# Page: RPEAS_Admin_Role_Maint - Copy.aspx
**File:** RPEAS_Admin_Role_Maint - Copy.aspx.vb

### 1. User Purpose
Users can maintain and update administrative roles within the system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and sets up event handlers. |
| btnSearch_Click | Executes a search based on user input, likely populating a grid control with matching roles. |
| BindGrid | Populates the grid control with the retrieved role data. |
| btnSave_Click | Saves the changes made to the selected role(s) to the database. |
| BtnClear_Click | Clears the form fields, resetting the user interface. |
| btnUpdate_Click | Updates an existing role based on user input. |
| Update | Updates the data in the grid control, likely triggered by a user action. |
| dgSearch_ItemDataBound | Handles events when a new item is bound to the data grid. |
| dgSearch_SortCommand | Sorts the data displayed in the data grid. |
| btnDelete_Click | Deletes the selected role(s) from the database. |
| DeleteSelected | Deletes the selected role(s) from the database. |
| btndel_ServerClick | Handles the server-side click event for the delete button. |
| lkMenu_Click | Navigates to a different menu item, likely a main menu. |
| lkUser_Click | Navigates to a different menu item, likely a user management page. |

---

---


<a id='system-documentation-rpeas-admin-role-maint'></a>
# Page: RPEAS_Admin_Role_Maint
**File:** RPEAS_Admin_Role_Maint.aspx.vb

### 1. User Purpose
Users can maintain and update administrative roles within the system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and sets up event handlers. |
| btnSearch_Click | Executes a search based on user input, likely populating a grid control with matching roles. |
| BindGrid | Populates the grid control with the retrieved role data. |
| btnSave_Click | Saves the changes made to the selected role(s) to the database. |
| BtnClear_Click | Clears the form fields, resetting the user input. |
| btnUpdate_Click | Updates an existing role with the data entered in the form. |
| Update |  Updates the data in the grid control, likely based on a database update. |
| dgSearch_ItemDataBound | Handles the event when a new item is bound to the grid control, potentially setting up event handlers for row clicks. |
| dgSearch_SortCommand | Sorts the data displayed in the grid control based on the selected column. |
| btnDelete_Click | Deletes the selected role(s) from the database. |
| btndel_ServerClick | Handles the server-side click event for the delete button. |
| lkMenu_Click | Navigates to a different menu item, likely a main menu. |
| lkUser_Click | Navigates to a different page, potentially a user management page. |

---

---


<a id='system-documentation-rpeas-admin-user-edit'></a>
# Page: RPEAS_Admin_User_Edit
**File:** RPEAS_Admin_User_Edit.aspx.vb

### 1. User Purpose
Users can edit existing administrator user details.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, populates the user edit form with existing data, and handles event triggers. |
| GetUserDetails | Retrieves the details of the user being edited, populating the form fields. |
| btnBack_Click | Returns the user to the previous page. |
| btnUpdate_Click | Saves the updated user details to the database. |

---


<a id='system-documentation-rpeas-admin-user-maint'></a>
# Page: RPEAS_Admin_User_Maint
**File:** RPEAS_Admin_User_Maint.aspx.vb

### 1. User Purpose
Users can maintain user accounts, including searching, saving, and deleting user records.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, populates the data grid, and sets up event handlers. |
| btnSearch_Click | Triggers a search operation based on user input, updating the data grid with matching records. |
| BindGrid | Populates the data grid with the current data. |
| dgSearch_ItemCommand | Handles user selections within the data grid, likely triggering further actions based on the selected row. |
| dgSearch_ItemDataBound | Handles events that occur when a data grid item is bound, potentially performing actions like setting up event handlers for individual rows. |
| btnSave_Click | Saves the selected user record to the database. |
| btnDelete_Click | Deletes the selected user record from the database. |
| dgSearch_SortCommand | Sorts the data in the data grid based on the selected column. |
| btndel_ServerClick |  Handles the server-side click event for deleting a selected user. |
| DeleteSelected(dg: DataGrid) |  Deletes the selected rows in the data grid. Returns the number of rows deleted. |
| BtnClear_Click | Clears the search criteria and resets the data grid. |

---


<a id='system-documentation-rpeas-admin-user-mapping'></a>
# Page: RPEAS_Admin_User_Mapping
**File:** RPEAS_Admin_User_Mapping.aspx.vb

### 1. User Purpose
Users can map users to specific roles within the system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and populates the search data grid. |
| FillInfo | Populates the data grid with user mapping data. |
| BinddgSearch | Binds the data grid with the provided DataTable. |
| dgSearch_ItemDataBound | Handles the data bound event for each item in the data grid. |
| btnSave_Click | Saves the user mapping data. |
| SaveInfo | Saves the user mapping data to the database. |
| dgSearch_SortCommand | Sorts the data grid based on the selected column. |
| btnclose_Click | Closes the current page. |

---


<a id='system-documentation-rpeas-all-forms'></a>
# Page: RPEAS_All_Forms
**File:** RPEAS_All_Forms.aspx.vb

### 1. User Purpose
This page allows users to search for and view a list of forms, likely related to a transit system (inferred from file name and potential domain context).

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, likely setting up the search functionality and the data grid. |
| Load_Forms | Populates the data grid (gvInbox) with form data based on search criteria. |
| btnSearch_Click | Triggers the `Load_Forms` method, initiating the form search. |
| lbtStart_Click | Likely initiates the first page of the form list. |
| lbtPrevious_Click | Navigates to the previous page of the form list. |
| lbtEnd_Click | Likely navigates to the last page of the form list. |
| lbtNext_Click | Navigates to the next page of the form list. |
| setPager | Updates the pagination controls (e.g., page numbers) based on the current page and total number of forms. |
| gvInbox_RowDataBound | Handles events for each row in the data grid (gvInbox).  Likely performs actions specific to each row, such as setting up event handlers or formatting data. |
| btnReset_Click | Resets the search criteria, clearing the data grid and potentially re-initializing the search. |

---

---


<a id='system-documentation-rpeas-all-forms-pa'></a>
# Page: RPEAS_All_Forms_PA
**File:** RPEAS_All_Forms_PA.aspx.vb

### 1. User Purpose
This page allows users to search for and view a list of inbox items.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads forms data, and sets up the date pickers. |
| Load_Forms | Loads the forms data, likely from a data source (DAL). |
| btnSearch_Click | Executes a search based on user input (likely date range) and updates the grid view with the results. |
| lbtStart_Click | Sets the start date to the current date using the date picker. |
| lbtPrevious_Click | Sets the start date to the previous day. |
| lbtEnd_Click | Sets the end date to the current date using the date picker. |
| lbtNext_Click | Sets the end date to the previous day. |
| setPager |  Handles pagination of the grid view. |
| gvInbox_RowDataBound |  Handles events for each row in the grid view (e.g., on row bound). |
| btnReset_Click | Resets the date pickers and the grid view to its default state. |

### 3. Data Interactions
* **Reads:** DAL (likely a data access layer object)
* **Writes:** None

---


<a id='system-documentation-rpeas-approve-form'></a>
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

---


<a id='system-documentation-rpeas-approve-form-org'></a>
# Page: RPEAS_Approve_Form_Org
**File:** RPEAS_Approve_Form_Org.aspx.vb

### 1. User Purpose
Users review and approve or reject requests, updating the status of the request and potentially routing it to another level.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, sets up event handlers, and prepares the form for user input.  Handles initial page load and sets up the UI. |
| hide_ReRoute_Withdraw() | Hides the re-route withdrawal controls, likely based on the request status. |
| Check_UserViewAccess(errormsg: String) | Validates the user's permissions to view and modify the form. If access is denied, an error message is displayed. |
| PopulateData() | Populates the form with data related to the request being reviewed. This likely involves retrieving data from a database. |
| Read_Only_Checkbox(chkbox: CheckBox) | Sets the read-only property of a checkbox control, likely based on the request status. |
| Read_Only_Radiobutton(radio: RadioButton) | Sets the read-only property of a radio button control, likely based on the request status. |
| Set_ReadOnly_Submittedby() | Sets the read-only property of the SubmittedBy control, likely based on the request status. |
| Set_ReadOnly_SubmittedThru() | Sets the read-only property of the SubmittedThru control, likely based on the request status. |
| Set_ReadOnly_Approver() | Sets the read-only property of the Approver control, likely based on the request status. |
| Set_ReadOnly_Withdrawnby() | Sets the read-only property of the WithdrawnBy control, likely based on the request status. |
| Set_ReadOnly_ReRouteLevel3() | Sets the read-only property of the ReRouteLevel3 control, likely based on the request status. |
| Set_ReadOnly_ReRouteLevel2() | Sets the read-only property of the ReRouteLevel2 control, likely based on the request status. |
| rd_NxtLevel2_CheckedChanged(sender: Object, e: EventArgs) | Handles the change event for a radio button that likely determines the next level of routing. |
| rd_reroute2_CheckedChanged(sender: Object, e: EventArgs) | Handles the change event for a radio button that likely determines the routing level. |
| Populate_Route2(ReRoute_lvl: String, ddl: DropDownList) | Populates the dropdown list with routing options based on the selected level. |
| btnapprove_Submitby_Click(sender: Object, e: EventArgs) | Handles the click event for the "Approve" button, likely submitting the form with the approved status. |
| btnConfirmnapprove_Submitby_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Confirm Approve" button, likely submitting the form with the approved status. |
| btnapprove_Submitthru_Click(sender: Object, e: EventArgs) | Handles the click event for the "Approve Through" button, likely submitting the form with the approved status. |
| btnConfirmapprove_Submitthru_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Confirm Approve Through" button, likely submitting the form with the approved status. |
| btnapprove_Approver_Click(sender: Object, e: EventArgs) | Handles the click event for the "Approve by Approver" button, likely submitting the form with the approved status. |
| btnConfirmapprove_Approver_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Confirm Approve by Approver" button, likely submitting the form with the approved status. |
| btnreject_Submitby_Click(sender: Object, e: EventArgs) | Handles the click event for the "Reject" button, likely submitting the form with the rejected status. |
| btnConfirmnreject_Submitby_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Confirm Reject" button, likely submitting the form with the rejected status. |
| btnreject_Submitthru_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Reject Through" button, likely submitting the form with the rejected status. |
| btnConfirmreject_Submitthru_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Confirm Reject Through" button, likely submitting the form with the rejected status. |
| btnreject_Approver_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Reject by Approver" button, likely submitting the form with the rejected status. |
| btnConfirmreject_Approver_Click(sender: Object, e: System.EventArgs) | Handles the click event for the "Confirm Reject by Approver" button, likely submitting the form with the rejected status. |
| btnWithdrawn_Click | Handles the click event for the "Withdrawn" button, likely submitting the form with the withdrawn status. |
| btnConfirmWithdrawn_Click | Handles the click event for the "Confirm Withdrawn" button, likely submitting the form with the withdrawn status. |
| btnreroute_submit_lvl2_Click | Handles the click event for the "Re-route" button, likely submitting the form with the re-routed status. |
| btnConfirmreroute_submit_lvl2_Click | Handles the click event for the "Confirm Re-route" button, likely submitting the form with the re-routed status. |
| rd_reroute3_CheckedChanged(sender: Object, e: EventArgs) | Handles the change event for a radio button that likely determines the routing level. |
| btnsubmit_reroutelvl3_Click | Handles the click event for the "Re-route" button, likely submitting the form with the re-routed status. |
| btnConfirmreroute_submit_lvl3_Click | Handles the click event for the "Confirm Re-route" button, likely submitting the form with the re-routed status. |

### 3. Data Flow
The page likely retrieves request data from a database.  User input is validated and then used to update the request status in the database. The routing logic determines the next level of processing based on the user's selections.

---


<a id='system-documentation-rpeas-completed-form'></a>
# Page: RPEAS_Completed_Form
**File:** RPEAS_Completed_Form.aspx.vb

### 1. User Purpose
Users fill out a form to record the completion of a transit process.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads form lists, and sets up the pagination controls. |
| Load_Form_Lists | Loads data for the form lists (likely from a database). |
| lbtStart_Click |  Navigates to the first page of the completed transit record. |
| lbtPrevious_Click | Navigates to the previous page in the completed transit record. |
| lbtEnd_Click | Navigates to the last page of the completed transit record. |
| lbtNext_Click | Navigates to the next page in the completed transit record. |
| setPager() | Updates the pagination controls based on the current page number. |
| gvInbox_RowDataBound | Handles events related to the grid view, likely for data binding or event handling within the grid. |

# Page: RPEAS_Confirm
**File:** RPEAS_Confirm.aspx.vb

### 1. User Purpose
Users confirm the completion of a transit process.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page. |

# Page: RPEAS_Confirm_Submit
**File:** RPEAS_Confirm_Submit.aspx.vb

### 1. User Purpose
Users submit the completed transit record for confirmation.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page. |
| Button2_Click | Handles the click event for the submit button, likely triggering the confirmation process. |

---


<a id='system-documentation-rpeas-create-form'></a>
# Page: RPEAS_Create_Form
**File:** RPEAS_Create_Form.aspx.vb

### 1. User Purpose
Users fill out a form to create a new document, including details like approvers, supporting documents, and associated data.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads initial data, and sets up event handlers. |
| Load_Page | Performs initial page setup, likely loading default values or setting up the UI. |
| Populate_Company | Populates the company selection dropdown with available company options. |
| Populate_ApproverLists | Populates the approver lists based on criteria, likely retrieving approver data from a database. |
| ddlprepby2_SelectedIndexChanged | Handles the selection of a preparer from a dropdown list, likely updating other fields based on the chosen preparer. |
| btnAdd_ServerClick | Adds a new document row to the grid control, triggering the creation of a new record. |
| AddPageNumber | Adds a new page to the document, likely incrementing a page number and potentially adding a new row to the grid. |
| dgappdoc_ItemCommand | Handles the "Delete" command on the appdoc grid, deleting the selected row and updating the grid. |
| DeleteSelectedAppDoc | Deletes the selected row from the appdoc grid, likely updating the database. |
| btnAddSuppDoc_ServerClick | Adds a new supporting document row to the grid control, triggering the creation of a new record. |
| dgsuppdoc_ItemCommand | Handles the "Delete" command on the suppdoc grid, deleting the selected row and updating the grid. |
| DeleteSelectedSuppDoc | Deletes the selected row from the suppdoc grid, likely updating the database. |
| btnFormSubmit_Click | Handles the form submission, likely validating the data, saving the document to the database, and sending email notifications. |
| GetServerDetails | Retrieves server details, potentially for logging or reporting purposes. |
| ValidateInput | Validates user input, checking for required fields, data types, and other constraints. |
| Save_Document | Saves the document to the database, likely using a data access object (DAO) to interact with the database. |
| BindGridFileUpload | Binds the file upload control to the grid, allowing users to upload supporting documents. |
| btnFormClear_Click | Clears the form fields, resetting the data to its initial state. |
| btnConfirmnFormSubmit_Click | Handles a confirmation of the form submission, potentially triggering a second validation or confirmation step. |
| btnCancel_Click | Cancels the form submission, clearing the form fields and potentially reverting any changes. |
| txtAmount_TextChanged | Handles changes to the amount field, likely updating related fields or performing calculations. |
| FormatDec | Formats the amount field to a specific decimal format. |
| btnaddSupportby_Click | Adds a new supporting document row to the grid control, triggering the creation of a new record. |
| BindGridsupportby | Binds the grid control to a DataTable, displaying the data in the grid. |
| dgsupportby_ItemCommand | Handles the "Delete" command on the supportby grid, deleting the selected row and updating the grid. |
| dgsupportby_ItemDataBound | Handles events during the data binding process for the supportby grid. |
| btnaddSubmThru_Click | Adds a new supporting document row to the grid control, triggering the creation of a new record. |
| BindGridSbumitThru | Binds the grid control to a DataTable, displaying the data in the grid. |
| dgsubmitThru_ItemCommand | Handles the "Delete" command on the submitThru grid, deleting the selected row and updating the grid. |
| dgsubmitThru_ItemDataBound | Handles events during the data binding process for the submitThru grid. |
| GetApproverList | Retrieves a list of approvers, likely from a database. |
| FormApproverList | Creates a DataTable containing approver data. |

---


<a id='system-documentation-rpeas-form-viewaspx'></a>
# Page: RPEAS_Form_View.aspx
**File:** RPEAS_Form_View.aspx.vb

### 1. User Purpose
Users view and approve data related to a transaction, likely within a financial or logistics system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, likely loading data and setting up event handlers. |
| Check_UserViewAccess | Determines if the current user has the necessary permissions to view this form. If not, an error message is displayed. |
| PopulateData | Populates the form with data, potentially from a database or other data source. This likely involves calling a data access layer (DAL) to retrieve the data. |
| FillGroup2, FillGroup3, FillGroup4, FillGroup5, FillGroup6 | These methods likely populate specific groups of data within the form, possibly based on different transaction types or stages. They take DataTable objects as input, likely representing data retrieved from the database. |
| btncancel_Approver_Click | Allows the approver to cancel the transaction, likely triggering a rollback or cancellation process. |
| lnkFileURL_Click, lnkFileURL_Supp_Click | These links likely open files associated with the transaction, such as invoices or supporting documents. |
| btnexport_Click | Allows the user to export the data from the form, potentially to a CSV or Excel file. |

---

---


<a id='system-documentation-rpeas-form-view-org'></a>
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

---


<a id='system-documentation-rpeas-login'></a>
# Page: RPEAS_Login
**File:** RPEAS_Login.aspx.vb

### 1. User Purpose
Users log in to the system using their username and password.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads menu, and sets up event handlers. |
| btnLogin_Click | Validates the username and password, calls the `authenticateUser` method to verify credentials, and then loads the menu based on the user's GUID. |
| authenticateUser(uid: String, password: String) |  This method likely takes the username and password, performs a database lookup (not shown), and returns a task. |
| RetrieveToken() | This method likely retrieves a token from a system or database. |
| callPostMethod(url: String, token: String, arg: HttpContent) | This method likely makes an asynchronous POST request to a specified URL, passing the token and content. |
| callGetMethod(url: String) | This method likely makes an asynchronous GET request to a specified URL. |
| Encrypt(val: String) | This method likely encrypts a given string value. |
| getLoginresponce(uid: String, password: String) | This method likely returns a string response based on the provided username and password. |
| CheckAccess() | This method likely checks user access rights. |
| LoadMenu(UserGUID: String) | This method likely loads the appropriate menu based on the user's GUID. |
| btnReset_Click | Resets the login form. |

---

---


<a id='system-documentation-rpeas-main'></a>
# Page: RPEAS_Main
**File:** RPEAS_Main.aspx.vb

### 1. User Purpose
Users access this page to view and potentially interact with data, likely within a system where user actions trigger data updates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | This method is the entry point for the page. It likely initializes the page, loads data, and sets up event handlers. |
| LinkButton1_Click | This method is triggered when the user clicks the "LinkButton1".  It likely handles a specific action, such as submitting a form or navigating to another page. |
| AddUrlParam | This method appends a URL parameter to a string.  This is likely used to construct dynamic URLs based on user input or system state. |
| Generate_Menu | This method generates a menu, likely based on user ID.  It suggests a system where menus are dynamically created for different users. |

# Page: RPEAS_NO_ACESS
**File:** RPEAS_NO_ACESS.aspx.vb

### 1. User Purpose
This page likely provides access to a restricted set of functionalities or data, potentially for administrative or support purposes.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | This method is the entry point for the page. It likely initializes the page, loads data, and sets up event handlers. |

---


<a id='system-documentation-rpeas-outstnd-form'></a>
# Page: RPEAS_Outstnd_Form
**File:** RPEAS_Outstnd_Form.aspx.vb

### 1. User Purpose
Users view and manage outstanding transactions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads inbox data, and sets the pager. |
| lbtStart_Click | Starts the process of displaying outstanding transactions. |
| lbtPrevious_Click | Navigates to the previous page of outstanding transactions. |
| lbtEnd_Click | Navigates to the next page of outstanding transactions. |
| lbtNext_Click | Navigates to the next page of outstanding transactions. |
| Load_Inbox | Loads the initial data for the inbox grid. |
| setPager | Updates the pager controls to reflect the current page. |
| gvInbox_RowDataBound | Handles events for each row in the inbox grid. |
| btnsub_ServerClick | Submits the selected transaction for processing. |

# Page: RPEAS_PA_SuperVisor
**File:** RPEAS_PA_SuperVisor.aspx.vb

### 1. User Purpose
Supervisors view and search for outstanding transactions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, binds the grid, and sets up event handlers. |
| BindGrid | Populates the grid with transaction data based on sorting and role code. |
| dgSearch_ItemDataBound | Handles events for each row in the search grid. |
| lksupervisor_Click | Changes the role code to filter the search results. |
| btnSearch_Click | Executes a search based on the current role code. |
| BtnClear_Click | Clears the search criteria. |

---


<a id='system-documentation-rpeas-pa-supervisor-edit'></a>
# Page: RPEAS_PA_Supervisor_Edit
**File:** RPEAS_PA_Supervisor_Edit.aspx.vb

### 1. User Purpose
Users edit supervisor information.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and loads data. |
| FillInfo | Populates the data grid with supervisor information. |
| BinddgSearch | Binds the data grid with search data. |
| dgSearch_ItemDataBound | Handles the event when a data grid item is bound. |
| btnclose_Click | Closes the edit form. |
| btnSave_Click | Saves the updated supervisor information. |
| SaveInfo | Saves the data to the database. |
| dgSearch_SortCommand | Sorts the data grid based on the selected column. |

---


<a id='system-documentation-rpeas-sysparameter-edit'></a>
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

---


<a id='system-documentation-rpeas-sysparameter-main'></a>
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

---


<a id='database-reference-sql-eas-admin-checkroles'></a>
# Procedure: EAS_Admin_CheckRoles

### Purpose
This procedure determines the number of records in the EAS_Role table that match a specified RoleCode.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | Varchar(50) | The RoleCode to search for. |
| @Count | int | The number of matching RoleCodes. |

### Logic Flow
1.  The procedure receives a RoleCode as input.
2.  It queries the EAS_Role table, searching for records where the Role column matches the provided RoleCode.
3.  The query counts all matching records.
4.  The count of matching records is assigned to the output parameter @Count.
5.  The value of @Count is then returned.

### Data Interactions
* **Reads:** EAS_Role
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-checkusers'></a>
# Procedure: EAS_Admin_CheckUsers

### Purpose
This procedure counts the number of users in the EAS_User table matching a specified UserID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | Varchar(10) | The UserID to search for. |
| @Count | int | The count of users matching the @User. |

### Logic Flow
1.  The procedure receives a UserID as input.
2.  The procedure queries the EAS_User table.
3.  The query filters the table to include only rows where the UserID matches the provided @User.
4.  The COUNT aggregate function calculates the total number of rows that satisfy the filtering criteria.
5.  The calculated count is assigned to the output parameter @Count.
6.  The value of @Count is then returned.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-get-roles'></a>
# Procedure: EAS_Admin_GET_Roles

### Purpose
This procedure retrieves role information from the EAS_Role table based on specified criteria, including role code, role description, and active status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RoleCode | VARCHAR(50) | The role code to search for. |
| @RoleDesc | VARCHAR(250) | The role description to search for. |
| @Active | SMALLINT | The active status to filter by. |
| @LoginID | VARCHAR(10) | The login ID to determine if the user is an IT_ADMIN. |

### Logic Flow
The procedure first checks if the provided @LoginID corresponds to an IT_ADMIN user. If it does, it executes a search for roles where the Role is 'IT_ADMIN'.  If the @LoginID does not correspond to an IT_ADMIN, the procedure proceeds to search for roles based on the provided input parameters.

The procedure then selects role details from the EAS_Role table. The selection is filtered based on the @RoleCode, @RoleDesc, and @Active parameters. The Role column is filtered using an `OR` condition, allowing a search by @RoleCode or if @RoleCode is null. The RoleDesc column is filtered using a `LIKE` operator with a wildcard character (`%`) to perform a partial match against the @RoleDesc parameter. The Active column is filtered based on the @Active parameter. The results are ordered by the CreatedOn column in descending order.
 

### Data Interactions
* **Reads:** EAS_Role
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-get-users'></a>
# Procedure: EAS_Admin_GET_Users

### Purpose
This procedure retrieves user records from the EAS_User table based on specified search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LanID | VARCHAR(50) | User identifier; if null, ignores this field in the search. |
| @NAME | VARCHAR(200) | User name; performs a partial match using the LIKE operator.  If null, ignores this field in the search. |
| @BArea | VARCHAR(150) | Business area; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Dept | VARCHAR(250) | Department; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Section | VARCHAR(250) | Section; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Designation | VARCHAR(500) | Job title; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Active | VARCHAR(10) | User status; if 'True', returns active users; if 'False', returns inactive users. If null, ignores this field in the search. |

### Logic Flow
The procedure searches the EAS_User table for user records. The search is performed based on multiple criteria, allowing for partial matches using the LIKE operator. The search is performed on the Name, Department, BusinessArea, Designation, and Section fields. The search is case-insensitive. The search prioritizes matching the UserID field if a @LanID is provided. If no @LanID is provided, the search ignores this field. The search also considers the @Active field, returning active users if the value is 'True' or 'False' and ignores this field if the value is null. The results are ordered by the CreatedOn field in descending order.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-getpalists'></a>
# Procedure: EAS_Admin_GetPALists

### Purpose
This procedure retrieves a list of users and their associated PA counts for the specified role within the RPEAS environment.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | Varchar(50) | The role identifier to filter users by. |
| @RoleDesc | Varchar(200) | Output parameter containing the description of the role. |

### Logic Flow
1.  The procedure begins by retrieving the description for the role specified in the @Role parameter from the EAS_Role table, filtering for the RPEAS system and the provided role. This description is then assigned to the @RoleDesc output parameter.
2.  The procedure then selects user information from the EAS_User table, filtering for users within the RPEAS system that are marked as active.
3.  The selection further filters the users based on a subquery that retrieves all user IDs associated with the specified role from the EAS_User_ROLE table, again filtering for the RPEAS system and active users.
4.  Finally, the selected user data is ordered alphabetically by the user's name.

### Data Interactions
* **Reads:** EAS_Role, EAS_User, EAS_User_ROLE
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-getsupervisorlists'></a>
# Procedure: EAS_Admin_GetSupervisorLists

### Purpose
This procedure retrieves a list of supervisor details, including their name, designation, and active status, based on a provided user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PAID | VARCHAR(50) | The UserID of the employee for whom to retrieve supervisor details. |

### Logic Flow
1.  The procedure begins by selecting supervisor details from the `EAS_User` table (aliased as `r`) and the `EAS_PA_Supervisor` table (aliased as `ur`) where the `supervisorid` in `EAS_PA_Supervisor` matches the `UserID` in `EAS_User` and the `userid` in `EAS_PA_Supervisor` matches the input parameter `@PAID`.  It selects the supervisor's ID as `LanID`, name, designation, business area, department, section, active status (represented as 'True' or 'False'), and a flag indicating if the supervisor is selected ('True' or 'False').
2.  The procedure then adds a second set of results by selecting all users from the `EAS_User` table (aliased as `r`) whose `UserID` is *not* present in the `EAS_PA_Supervisor` table where the `userid` matches the input parameter `@PAID`. This effectively identifies supervisors who are not directly associated with the specified user.
3.  The results from both queries are combined using a `UNION ALL` operation.
4.  Finally, the combined result set is ordered by the supervisor's ID (`LanID`).

### Data Interactions
* **Reads:** `EAS_User`, `EAS_PA_Supervisor`
* **Writes:** None

---


<a id='database-reference-sql-008-eas-admin-menurole-insertmd'></a>
### Procedure: EAS_Admin_MenuRole_Insert

### Purpose
This procedure inserts a new role within the EAS Menu Role table, handling both initial insertion and updates based on existing role configurations.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RoleCode | VARCHAR(50) | The unique identifier for the role. |
| @MenuID | VARCHAR(50) | The ID of the menu to which the role is assigned. |
| @SysID | VARCHAR(10) | The system identifier for the menu and role. |
| @Active | SMALLINT = 1 | Indicates whether the role is active. |
| @LoginID | VARCHAR(50) | The ID of the user making the change. |
| @Sel | VARCHAR(5) |  Determines whether to insert a new role or update an existing one. |
| @P_ErrorMsge | varchar(225) | Output parameter to store any error messages. |

### Logic Flow
1.  **Initialization:** Sets the output error message parameter to an empty string.
2.  **Transaction Start:** Begins a database transaction to ensure atomicity (all operations succeed or none do).
3.  **Conditional Insertion/Update:**
    *   **If @Sel = 'Y':**  This block attempts to insert a new role.
        *   **Check for Existing Role:** Checks if a role with the same `MenuID` and `Role` already exists.
            *   **If Role Exists:** Updates the existing role with the provided `Active` status, `Updatedby`, and `UpdatedOn`.
            *   **If Role Does Not Exist:** Inserts a new row into the `EAS_Menu_Role` table with the provided `SysID`, `MenuID`, `Role`, `Active` status, `CreatedBy`, `CreatedOn`, `UpdatedBy`, and `UpdatedOn`.
            *   **Parent Menu Check:** Checks if the parent menu exists and if the role is associated with the parent menu. If not, it inserts a new row into the `EAS_Menu_Role` table with the provided `SysID`, `MenuID`, `Role`, `Active` status, `CreatedBy`, `CreatedOn`, `UpdatedBy`, and `UpdatedOn`.
    *   **If @Sel = 'N':** This block attempts to delete the role.
        *   **Delete Existing Role:** Deletes the role from the `EAS_Menu_Role` table based on the `MenuID` and `Role`.
        *   **Parent Menu Check:** Checks if the parent menu exists and if the role is associated with the parent menu. If not, it deletes the role from the `EAS_Menu_Role` table based on the `MenuID` and `Role`.
4.  **Transaction Commit/Rollback:** If all operations succeed, the transaction is committed. If any error occurs, the transaction is rolled back, and the output error message parameter is populated with the error message.
5.  **Error Handling:** Catches any errors that occur during the transaction and sets the output error message parameter with the error message.
6.  **Output:** Sets the output error message parameter to the value stored in the error message parameter.

### Data Interactions
* **Reads:** `EAS_Menu_Role`, `EAS_Menu`
* **Writes:** `EAS_Menu_Role`

---


<a id='database-reference-sql-eas-admin-menuroles-getinfo'></a>
# Procedure: EAS_Admin_MenuRoles_GetInfo

### Purpose
This procedure retrieves information about menu roles associated with a specified role, filtering for active menu items.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The role to filter menu roles by. |

### Logic Flow
The procedure begins by selecting data from the `EAS_Menu` table, filtering for rows where the `Active` column is equal to 1.  It then joins this data with the `EAS_Menu_Role` table based on matching `MenuID` and the provided `@Role` parameter. The selection includes the `MenuID`, `DispText` from the `EAS_Menu` table, an indicator of the role's active status (`_Active`), and an indicator of whether the menu role has a defined `MenuID` (`IsSelected`). Finally, the results are ordered by `MenuID`.

### Data Interactions
* **Reads:** `EAS_Menu`, `EAS_Menu_Role`
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-pa-supervisor-insert'></a>
# Procedure: EAS_Admin_PA_Supervisor_Insert

### Purpose
This procedure allows an administrator to manage PA Supervisor lists by either updating an existing record or deleting a record based on specified criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PAID | VARCHAR(50) | The unique identifier for the PA. |
| @SupervisorLanID | VARCHAR(50) | The unique identifier for the Supervisor. |
| @Active | SMALLINT | A flag indicating whether the PA Supervisor record is active. |
| @LoginID | VARCHAR(50) | The identifier of the user making the change. |
| @Sel | VARCHAR(5) |  A selection indicator, likely determining the action to take. |
| @P_ErrorMsge | VARCHAR(225) | An output parameter to hold any error messages. |

### Logic Flow
1.  The procedure initializes the `@P_ErrorMsge` output parameter to an empty string.
2.  It enters a TRY block to handle potential errors and begins a transaction.
3.  If the `@Sel` parameter is equal to 'Y', the procedure checks if a record already exists in the `EAS_PA_Supervisor` table with the specified `@PAID` and `@SupervisorLanID`.
    *   If the record exists, the procedure updates the `EAS_PA_Supervisor` record, setting the `@Active` flag to the value of the `@Active` parameter, the `Updatedby` field to the `@LoginID`, and the `updatedON` field to the current date and time.
    *   If the record does not exist, the procedure inserts a new record into the `EAS_PA_Supervisor` table, using the `SYSID` value 'RPEAS', the `@PAID`, the `@SupervisorLanID`, the `@Active` value, the current date and time for `CreatedOn`, the `@LoginID` for `CreatedBy`, the current date and time for `UpdatedOn`, and the `@LoginID` for `UpdatedBy`.
4.  If the `@Sel` parameter is not 'Y', the procedure deletes records from the `EAS_PA_Supervisor` table where the `UserID` matches the `@PAID` and the `SupervisorID` matches the `@SupervisorLanID`.
5.  The transaction is committed.
6.  If an error occurs within the TRY block, the CATCH block is executed. The error message is retrieved and stored in the `@P_ErrorMsge` output parameter. The transaction is rolled back.
7.  The `@P_ErrorMsge` output parameter is set to the value of `@P_ErrorMsge`, handling the case where no error occurred.

### Data Interactions
*   **Reads:** `EAS_PA_Supervisor`
*   **Writes:** `EAS_PA_Supervisor`

---


<a id='database-reference-sql-eas-admin-role-delete'></a>
# Procedure: EAS_Admin_Role_Delete

### Purpose
This procedure removes associated data related to a specified administrative role from multiple tables within the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The name of the administrative role to be deleted. |
| @P_ErrorMsg | Varchar(250) |  A variable to store any error messages that occur during the procedure execution. |

### Logic Flow
1.  The procedure begins with a `TRY` block to handle potential errors during the data deletion process.
2.  A transaction is initiated within the `TRY` block to ensure atomicity – either all operations succeed, or none do.
3.  The procedure attempts to delete records from the `EAS_Menu_Role` table where the `Role` column matches the provided `@Role` value.
4.  Next, it attempts to delete records from the `EAS_User_Role` table, again matching the `@Role` value.
5.  Finally, it attempts to delete records from the `EAS_Role` table, using the same `@Role` value.
6.  If any error occurs during these deletion operations, the `CATCH` block is executed.
7.  Within the `CATCH` block, the error message is retrieved using `ERROR_MESSAGE()` and stored in the `@P_ErrorMsg` variable.
8.  A `ROLLBACK TRANSACTION` command is executed to undo any changes made during the transaction, ensuring data consistency.
9.  The `@P_ErrorMsg` variable is set to the value of `@P_ErrorMsg` if it is not null, otherwise it is set to an empty string.

### Data Interactions
* **Reads:** None
* **Writes:** `EAS_Menu_Role`, `EAS_User_Role`, `EAS_Role`

---


<a id='database-reference-sql-eas-admin-role-insert'></a>
# Procedure: EAS_Admin_Role_Insert

### Purpose
This procedure inserts a new record into the EAS_Role table, representing an administrative role within the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The name of the administrative role to be created. |
| @RoleDesc | VARCHAR(250) | A description of the administrative role. |
| @Active | VARCHAR(5) | Indicates whether the administrative role is currently active. |
| @CreatedBy | VARCHAR(50) | The user account that initiated the role creation. |
| @P_ErrorMsg | Varchar(250) |  An output parameter to hold any error messages encountered during the procedure execution. |

### Logic Flow
1.  The procedure begins within a `TRY` block to handle potential errors during the role creation process.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  An `INSERT` statement is executed to add a new row to the `EAS_Role` table. The values being inserted are: the provided role name, the string literal "RPEAS", the provided role description, the value of the @Active parameter, the current date and time, and the @CreatedBy parameter, also with the current date and time.
4.  If the `INSERT` statement completes successfully, the transaction is committed, making the changes permanent.
5.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
6.  The error message is retrieved using `ERROR_MESSAGE()` and stored in the output parameter @P_ErrorMsg.
7.  The transaction is rolled back, undoing any changes made during the procedure.
8.  The @P_ErrorMsg parameter is set to an empty string if it was previously null.

### Data Interactions
* **Reads:** None
* **Writes:** EAS_Role

---


<a id='database-reference-sql-eas-admin-role-update'></a>
# Procedure: EAS_Admin_Role_Update

### Purpose
This procedure updates information for a specific role within the EAS system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The new name for the role. |
| @OrginRole | VARCHAR(250) | The current name of the role to be updated. |
| @RoleDesc | VARCHAR(250) | The new description for the role. |
| @Active | VARCHAR(5) |  Indicates whether the role is active or inactive. |
| @CreatedBy | VARCHAR(50) | The user who initiated the update. |
| @P_ErrorMsg | Varchar(250) |  Variable to store any error messages that occur during the process. |

### Logic Flow
1.  The procedure begins with a `TRY` block to handle potential errors during the update process.
2.  A transaction is started within the `TRY` block to ensure atomicity – either all changes are committed, or none are.
3.  The `EAS_Role` table is updated. The `Role` column is set to the value provided in the `@Role` parameter, the `RoleDesc` column is set to the value provided in the `@RoleDesc` parameter, the `Active` column is set to the value provided in the `@Active` parameter, and the `UpdatedBy` column is set to the value provided in the `@CreatedBy` parameter. The `UpdatedOn` column is automatically populated with the current date and time using `GETDATE()`. The update is performed where the `Role` column matches the value provided in the `@OrginRole` parameter.
4.  If the update is successful, the transaction is committed, finalizing the changes.
5.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
6.  The `ROLLBACK TRANSACTION` command is executed, undoing any changes made during the transaction.
7.  An error message is retrieved from the system and stored in the `@P_ErrorMsg` parameter.
8.  The `@P_ErrorMsg` parameter is set to an empty string if it is null.

### Data Interactions
* **Reads:** [EAS_Role]
* **Writes:** [EAS_Role]

---


<a id='database-reference-sql-eas-admin-user-getinfo'></a>
# Procedure: EAS_Admin_User_GetInfo

### Purpose
This procedure retrieves information about staff roles, including user identifiers, role names, and active status, based on a specified role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Role | VARCHAR(50) | The specific role to filter for. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_User` table and the `EAS_User_Role` table.
2.  It first selects user identifiers (`UserID`), role names (`Name`), and the active status (`_Active`) from `EAS_User` where the `UserID` exists in `EAS_User_Role` and the `Role` matches the input `@Role`. The active status is determined by checking the `Active` column in `EAS_User`.
3.  It then performs a `UNION ALL` operation to combine the results with a second set of data.
4.  The second set of data selects `UserID` and `Name` from `EAS_User` where the `UserID` is *not* present in the `EAS_User_Role` table. This identifies users who do not have an assigned role.
5.  The final result set is ordered by the `UserID` column.

### Data Interactions
* **Reads:** `EAS_User`, `EAS_User_Role`
* **Writes:** None

---


<a id='database-reference-sql-eas-admin-userrole-insert'></a>
# Procedure: EAS_Admin_UserRole_Insert

### Purpose
This procedure allows an administrator to insert, update, or delete user role entries within the EAS system, managing access permissions based on user and role definitions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RoleCode | VARCHAR(50) | The unique identifier for the role being assigned. |
| @LanID | VARCHAR(50) | The unique identifier for the user to which the role is being assigned. |
| @Active | SMALLINT = 1 | A flag indicating whether the role is currently active. |
| @LoginID | VARCHAR(50) | The identifier of the user who is performing the operation. |
| @Sel | VARCHAR(5) |  A flag indicating whether to update an existing role or insert a new one. |
| @P_ErrorMsge | VARCHAR(225) | An output parameter to store any error messages that occur during the procedure execution. |

### Logic Flow
1.  The procedure initializes the `@P_ErrorMsge` output parameter to an empty string.
2.  It enters a TRY block to handle potential errors during the operation.
3.  Within the TRY block, a transaction is started to ensure atomicity.
4.  The procedure checks the value of the `@Sel` parameter.
    *   If `@Sel` is 'Y', it checks if a role with the specified `@RoleCode` and `@LanID` already exists in the `EAS_User_Role` table.
        *   If the role exists, it updates the existing record in `EAS_User_Role` with the new `@RoleCode`, `@Active` status, and the current timestamp for `UpdatedOn` and `UpdatedBy`.
        *   If the role does not exist, it inserts a new record into the `EAS_User_Role` table with the provided `@LanID`, `SYSID` ('RPEAS'), `@RoleCode`, `@Active` status, the current timestamp for `CreatedOn`, the `@LoginID` as `CreatedBy`, the current timestamp for `UpdatedOn`, and the `@LoginID` as `UpdatedBy`.
    *   If `@Sel` is not 'Y', it executes a deletion operation.
        *   It deletes records from the `EAS_User_Role` table where the `UserID` matches the provided `@LanID` and the `Role` matches the specified `@RoleCode`.
        *   If `@RoleCode` is 'PA', it also deletes records from the `EAS_PA_Supervisor` table where the `UserID` matches the provided `@LanID` and the `SYSID` is 'RPEAS'.
5.  If any error occurs within the TRY block, the transaction is rolled back, and the error message is captured and stored in the `@P_ErrorMsge` output parameter.
6.  Finally, the `@P_ErrorMsge` parameter is set to its current value.

### Data Interactions
*   **Reads:** `EAS_User_Role`, `EAS_PA_Supervisor`
*   **Writes:** `EAS_User_Role`, `EAS_PA_Supervisor`

---


<a id='database-reference-sql-eas-admin-user-delete'></a>
# Procedure: EAS_Admin_User_Delete

### Purpose
This procedure deletes a user record from the EAS_User table based on the provided UserID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | VARCHAR(15) | The UserID of the user to be deleted. |
| @P_ErrorMsg | VARCHAR(250) | Stores an error message if the deletion fails. |

### Logic Flow
1.  The procedure begins with a `TRY` block to handle potential errors during the deletion process.
2.  A transaction is initiated within the `TRY` block to ensure atomicity – either all changes are committed, or none are.
3.  A `DELETE` statement is executed from the `EAS_User` table, removing the row where the `UserID` column matches the value provided in the `@User` parameter.
4.  If the `DELETE` statement executes successfully, the transaction is committed, saving the changes to the database.
5.  If any error occurs during the `DELETE` statement, the `CATCH` block is executed.
6.  Within the `CATCH` block, the error message is retrieved using `ERROR_MESSAGE()` and stored in the `@P_ErrorMsg` parameter.
7.  The transaction is rolled back using `ROLLBACK TRANSACTION`, undoing any changes made during the procedure.
8.  Finally, the `@P_ErrorMsg` parameter is set to an empty string if it was previously null.

### Data Interactions
* **Reads:** None
* **Writes:** EAS_User (deleted)

---


<a id='database-reference-sql-eas-admin-user-insert'></a>
# Procedure: EAS_Admin_User_Insert

### Purpose
This procedure inserts a new user record into the EAS_User table, populating fields with provided data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | VARCHAR(10) | The unique identifier for the user. |
| @Name | VARCHAR(200) | The user’s full name. |
| @BArea | VARCHAR(250) | The business area to which the user belongs. |
| @Dept | VARCHAR(250) | The department the user belongs to. |
| @Section | VARCHAR(250) | The section within the department the user belongs to. |
| @Email | VARCHAR(500) | The user’s email address. |
| @Designation | VARCHAR(100) | The user’s job title or designation. |
| @Active | VARCHAR(5) | A flag indicating whether the user account is active. |
| @CreatedBy | VARCHAR(50) | The user who created the record. |
| @P_ErrorMsg | Varchar(250) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure begins within a `TRY` block to handle potential errors during the insertion process.
2.  A transaction is initiated using `BEGIN TRANSACTION`.
3.  An `INSERT` statement is executed to add a new row to the `EAS_User` table.
4.  The `UserID` column is populated with the lowercase version of the input `@User` parameter.
5.  The `sysid` column is populated with the constant "RPEAS".
6.  The `Name`, `Email`, `Designation`, `BusinessArea`, `Department`, `Section`, `Active`, `CreatedOn`, and `CreatedBy` columns are populated with the corresponding values from the input parameters.
7.  The `Getdate()` function is used to populate the `CreatedOn` column with the current date and time.
8.  If the `INSERT` statement executes successfully, the transaction is committed using `COMMIT TRANSACTION`.
9.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
10. The `ERROR_MESSAGE()` function is called to retrieve the error message.
11. The error message is stored in the output parameter `@P_ErrorMsg`.
12. The transaction is rolled back using `ROLLBACK TRANSACTION` to undo any changes made during the process.
13. The `@P_ErrorMsg` parameter is set to the value of `@P_ErrorMsg` if it is not null, otherwise it is set to an empty string.

### Data Interactions
* **Reads:** None
* **Writes:** EAS_User

---


<a id='database-reference-sql-eas-admin-user-update'></a>
# Procedure: EAS_Admin_User_Update

### Purpose
This procedure updates user information within the EAS system, specifically targeting records associated with the "RPEAS" system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @User | VARCHAR(10) | The unique identifier for the user record to be updated. |
| @Name | VARCHAR(200) | The new name for the user. |
| @BArea | VARCHAR(250) | The new business area for the user. |
| @Dept | VARCHAR(250) | The new department for the user. |
| @Section | VARCHAR(250) | The new section for the user. |
| @Email | VARCHAR(500) | The new email address for the user. |
| @Designation | VARCHAR(100) | The new job title for the user. |
| @Active | VARCHAR(5) | The active status for the user. |
| @CreatedBy | VARCHAR(50) | The identifier of the user making the update. |
| @P_ErrorMsg | Varchar(250) | Output parameter to hold any error messages. |

### Logic Flow
1.  The procedure begins within a `TRY` block to manage potential errors.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  An `UPDATE` statement modifies the `EAS_User` table. It sets the `Name`, `Email`, `Designation`, `BusinessArea`, `Department`, `Section`, `Active`, `UpdatedOn`, and `UpdatedBy` columns for the user record identified by the `@User` parameter. The `sysid` column is set to 'RPEAS'.
4.  The `WHERE` clause of the `UPDATE` statement ensures that the update only applies to the user record with the specified `@User` and `sysid` of 'RPEAS'.
5.  If an error occurs within the `TRY` block, the `CATCH` block is executed.
6.  The error message is retrieved using `ERROR_MESSAGE()` and stored in the output parameter `@P_ErrorMsg`.
7.  The transaction is rolled back to undo any changes made during the update process.
8.  The `@P_ErrorMsg` parameter is set to the value of `@P_ErrorMsg` if it is not null, otherwise it is set to an empty string.

### Data Interactions
*   **Reads:** `EAS_User`
*   **Writes:** `EAS_User`

---


<a id='database-reference-sql-eas-binaryfilesave'></a>
# Procedure: EAS_BinaryFileSave

### Purpose
This procedure saves a binary file associated with a specific form, updating the corresponding record in the EAS_Form_Attach_Document table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FileID | int | The unique identifier for the file. |
| @p_FileRefNo | varchar(225) | The reference number identifying the form. |
| @p_FileContent | varbinary(max) | The binary data of the file. |
| @p_FileType | varchar(500) | The type of the file. |
| @p_ErrorMsg | varchar(500) | An output parameter to store any error messages. |

### Logic Flow
The procedure updates a record within the EAS_Form_Attach_Document table. It sets the `FileContent` column to the provided binary file data. Simultaneously, it updates the `FileContentType` column with the specified file type. The update is performed based on a matching `ID` value (representing the file) and a `FormGuid` value (representing the form). The `ErrorMsg` output parameter is intended to capture any potential errors during the update process, although it is not explicitly used within the procedure's logic.

### Data Interactions
* **Reads:** EAS_Form_Attach_Document
* **Writes:** EAS_Form_Attach_Document

---


<a id='database-reference-sql-eas-form-check-action-access-lists'></a>
# Procedure: EAS_Form_Check_Action_Access_Lists

### Purpose
This procedure determines if a user is authorized to view a specific form, considering their role, supervisor, and form approval levels.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |
| @P_UserID | varchar(15) | The unique identifier for the user. |
| @P_ErrorMsg | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure initializes the output error message parameter to an empty string.
2.  It retrieves the `userid` from the `EAS_Form_Approve_Lvl` table, filtering for the provided `@P_Guid` and associating it with a user from the `EAS_USER` table where the `sysid` is 'RPEAS' and the `active` flag is set to 1. This `userid` is stored in the `@p_Supervisorid` variable.
3.  It counts the number of rows in the `EAS_Form_Approve_Lvl` table where the `formguid` matches the input `@P_Guid` and the `userid` matches the input `@P_UserID`. This count is stored in the `@pcnt` variable.
4.  It counts the number of users whose `userid` matches the input `@P_UserID` and who are present in the `EAS_PA_Supervisor` table, where the `supervisorid` matches the `@p_Supervisorid` and the `active` flag is set to 1. This count is stored in the `@pPACnt` variable.
5.  It checks if both `@pcnt` and `@pPACnt` are zero. If they are, it sets the `@P_ErrorMsg` to 'You Are Not Authorised To View This Page.' and immediately exits the procedure.

### Data Interactions
* **Reads:** `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-check-view-access-lists'></a>
# Procedure: EAS_Form_Check_View_Access_Lists

### Purpose
This procedure determines if a user is authorized to view a specific form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) |  A unique identifier for the form. |
| @P_UserID | varchar(15) | The identifier for the user. |
| @P_ErrorMsg | varchar(500) | An output parameter to hold an error message if authorization is denied. |

### Logic Flow
1.  The procedure initializes an output parameter, @P_ErrorMsg, to an empty string.
2.  The procedure executes a query against the EAS_User table.
3.  The query checks if a user with the specified @P_UserID exists in the EAS_User table.
4.  The query also verifies that the user's active status is set to 1.
5.  If no user record is found matching the criteria, the procedure sets the @P_ErrorMsg to a predefined error message indicating the user is not authorized.
6.  The procedure then immediately returns, terminating execution.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None

---


<a id='database-reference-sql-eas-form-create-new-form'></a>
# Procedure: EAS_Form_Create_New_Form

### Purpose
This procedure creates a new form record within the EAS system, including its master data and initial approval levels.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_doctype | varchar(50) | Specifies the type of form being created. |
| @p_company | varchar(200) | Indicates the company associated with the form. |
| @p_Title | varchar(500) |  Stores the title or name of the form. |
| @p_Vendor | varchar(200) |  Represents the vendor associated with the form. |
| @p_Amt | decimal(18,2) |  Holds the amount related to the form. |
| @p_LoginID | varchar(15) |  The login ID of the user creating the form. |
| @p_formguid | nvarchar(225) | Output parameter containing the unique GUID for the newly created form. |
| @p_docruno | varchar(4) | Output parameter containing the run number assigned to the form. |
| @p_errormsg | varchar(500) | Output parameter to store any error messages that occur during the process. |

### Logic Flow
1.  **GUID Generation:** A unique GUID (Globally Unique Identifier) is generated and stored in the @p_guid variable.
2.  **Run Number Retrieval/Creation:**
    *   The procedure checks if a record already exists in the `EAS_Form_RefNo_Cntl` table with the specified year and prefix.
    *   If no record exists, it inserts a new record into this table, assigning a run number starting from 1.
    *   If a record does exist, it retrieves the next available run number from the table.
3.  **Form Master Record Creation:**
    *   The run number is converted to a string and assigned to the @p_docruno output parameter.
    *   A new record is inserted into the `EAS_Form_Master` table, populating fields with the generated GUID, retrieved run number, form type, company, title, status, vendor, amount, and active flag. The creation and update timestamps are set to the current login ID.
4.  **Approval Level Records Creation:**
    *   The procedure then inserts records into the `EAS_Form_Approve_Lvl` table to define the approval levels for the form.
    *   It inserts records for levels 1, 2, 3, and 4, depending on the values of the @p_PreparBy1, @p_SubmitBy, @p_SubmitThru, and @p_Approver parameters.
    *   Each approval level record specifies the form GUID, approval level, user ID, re-route type, remarks, conflict check flag, action, active flag, action by, action on, and creation details.
5.  **Log History Entry:** Finally, a record is inserted into the `EAS_Form_Log_History` table, documenting the preparation of the form by the user's login ID and timestamp.
6.  **Error Handling:** If any error occurs during the process, the error message is captured and stored in the @p_errormsg output parameter.

### Data Interactions
*   **Reads:** `EAS_Form_RefNo_Cntl`, `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
*   **Writes:** `EAS_Form_RefNo_Cntl`, `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`

---


<a id='database-reference-sql-eas-form-get-all-froms'></a>
# Procedure: EAS_Form_Get_All_Froms

### Purpose
This stored procedure retrieves all form records from the EAS_Form_Master table, filtering based on form status, title, date range, and user permissions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormStatus | varchar(1) | Specifies the form status to filter by ('P' for Progress, 'C' for Completed). |
| @P_FormTitle | varchar(100) | Specifies the form title to filter by. |
| @P_DateFrom | varchar(10) | Specifies the start date for the date range filter. |
| @P_DateTo | varchar(10) | Specifies the end date for the date range filter. |
| @P_UserID | varchar(10) | Specifies the user ID to determine user permissions. |

### Logic Flow
The stored procedure first determines the user's role and permissions. It checks if the user is a super administrator or IT administrator.

1.  **Role Determination:** The procedure checks if the user has a role of 'SUPER_ADMIN' or 'IT_ADMIN' from the `EAS_User_Role` table, using the provided `@P_UserID`. If the user has one of these roles, they are granted full access to all forms.

2.  **Form Status Filtering:**
    *   **'P' (Progress Forms):** If the `@P_FormStatus` is 'P', the procedure retrieves form records where the `FormStatus` is not 'Closed', 'Rejected', or 'Withdrawn'. It then further filters based on the approval status of the form.
        *   If the user is a super administrator, it retrieves all records matching the criteria.
        *   If the user is not a super administrator, it retrieves records based on the approval status of the form, using the `EAS_Form_Pending_NODays` table to determine the number of days pending approval.

    *   **'C' (Completed Forms):** If the `@P_FormStatus` is 'C', the procedure retrieves form records where the `FormStatus` is 'Closed', 'Rejected', or 'Withdrawn'. It then retrieves records based on the approval status of the form, using the `EAS_Form_Pending_NODays` table to determine the number of days pending approval.
        *   If the user is a super administrator, it retrieves all records matching the criteria.
        *   If the user is not a super administrator, it retrieves records based on the approval status of the form, using the `EAS_Form_Pending_NODays` table to determine the number of days pending approval.

3.  **Date Filtering:** The procedure filters the form records based on the provided `@P_DateFrom` and `@P_DateTo` values, ensuring that the form creation date falls within the specified date range.

4.  **Title Filtering:** The procedure filters the form records based on the provided `@P_FormTitle` value, using a wildcard search to find forms with titles that contain the specified text.

5.  **Data Retrieval:** Finally, the procedure retrieves the form data, including the form GUID, document reference number, document type, company, title, submit date (calculated from the `updatedon` field), and the form status (calculated based on the approval status).

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_User_Role`, `EAS_User`, `EAS_Form_Pending_NODays`
*   **Writes:** None

---


<a id='database-reference-sql-eas-form-get-all-froms-pa'></a>
# Procedure: EAS_Form_Get_All_Froms_PA

### Purpose
This stored procedure retrieves form data based on the form status and title, filtering for forms that have been submitted by a user with a PA role and within a specified date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormStatus | varchar(1) | Specifies the form status ('P' for Progress, 'C' for Completed). |
| @P_FormTitle | varchar(100) | Specifies the form title to search for. |
| @P_DateFrom | varchar(10) | Specifies the start date for the date range. |
| @P_DateTo | varchar(10) | Specifies the end date for the date range. |
| @P_UserID | varchar(10) | The UserID of the user to filter by. |

### Logic Flow
1.  **User Role Check:** The procedure first checks if the provided @P_UserID has a PA role. It does this by querying the `EAS_User_Role` table to determine if the user has the 'PA' role and is active. If the user does not have a PA role, the procedure will not return any data.
2.  **Form Status Handling:**
    *   **Progress Forms ('P'):** If @P_FormStatus is 'P', the procedure retrieves form data from the `EAS_Form_Master` table. It filters for forms that are not in the 'Closed', 'Rejected', or 'Withdrawn' status. It also filters based on the @P_FormTitle using a LIKE operator, allowing for partial matches. The date range is applied to filter forms created within the specified @P_DateFrom and @P_DateTo.  The procedure also checks if the form's GUID is present in a list of form GUIDs associated with users who are supervisors and have a matching @P_UserID.
    *   **Completed Forms ('C'):** If @P_FormStatus is 'C', the procedure retrieves form data from the `EAS_Form_Master` table, filtering for forms in the 'Closed', 'Rejected', or 'Withdrawn' status. It filters based on the @P_FormTitle using a LIKE operator, allowing for partial matches. The date range is applied to filter forms created within the specified @P_DateFrom and @P_DateTo. The procedure also checks if the form's GUID is present in a list of form GUIDs associated with users who are supervisors and have a matching @P_UserID.
3.  **Data Retrieval:** The procedure retrieves the `FormGuid`, `DocRefNo`, `DocType`, `Company`, `Title`, `updatedon` (as SubmitDate), and `FormStatus` from the `EAS_Form_Master` table. It also retrieves the `Applevel` and `userid` from the `EAS_Form_Approve_Lvl` table.
4.  **Grouping and Ordering:** The results are grouped by `FormGuid`, `Applevel`, `userid`, `DocRefNo`, `DocType`, `Company`, `Title`, and `updatedon` to avoid duplicate records. The results are then ordered by `updatedon` in descending order.

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_User_Role`, `EAS_User`, `EAS_Form_Approve_Lvl`, `EAS_PA_Supervisor`
*   **Writes:** None

---


<a id='database-reference-sql-eas-form-get-approverlists'></a>
# Procedure: EAS_Form_Get_ApproverLists

### Purpose
This procedure retrieves a list of user names and identifiers from the EAS_User table, excluding a specified user, and filtering for users with the PA role and those associated with the RPEAS system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_ExclUser | varchar(15) | User identifier to exclude from the results. |

### Logic Flow
1.  The procedure begins by selecting the userid and name columns from the EAS_User table.
2.  It filters the selection to include only users where the active flag is set to 1.
3.  It further restricts the selection to users associated with the RPEAS system, ensuring that only users linked to the RPEAS system are included.
4.  The procedure excludes a specified user identifier, @P_ExclUser, from the results.
5.  Finally, the results are ordered alphabetically by user name.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-attach-file-byid'></a>
# Procedure: EAS_Form_Get_Attach_File_ByID

### Purpose
This procedure retrieves information about a specific attachment file associated with a form, based on the form’s unique identifier and the attachment’s unique identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormGuid | nvarchar(225) | The unique identifier for the form. |
| @P_FileID | int | The unique identifier for the attachment file. |

### Logic Flow
The procedure begins by selecting data from the `EAS_Form_Attach_Document` table. The selection is filtered based on two criteria: the `FormGuid` column must match the input parameter `@P_FormGuid`, and the `ID` column must match the input parameter `@P_FileID`. The selected data includes the attachment’s `SNO`, `FormGuid`, `FileName`, `FileType`, `FileURL`, `FileSize`, `CreatedOn`, `Createdby`, `FileContent`, and `FileContentType`.

### Data Interactions
* **Reads:** `EAS_Form_Attach_Document`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-attach-files'></a>
# Procedure: EAS_Form_Get_Attach_Files

### Purpose
This procedure retrieves attachment files associated with a specific form, categorized as either ApprovalDocuments or SupportDocuments.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_FormGuid | nvarchar(225) | The unique identifier for the form. |

### Logic Flow
The procedure filters attachment documents from the `EAS_Form_Attach_Document` table based on the provided form identifier. It specifically selects documents where the `FormGuid` matches the input `@P_FormGuid`.  The selection includes the document’s unique identifier (`SNO`), the form’s unique identifier (`FormGuid`), the file name (`FileName`), the file type (`FileType`), the URL to access the file (`FileURL`), the file size (`FileSize`), the date and time the file was created (`CreatedOn`), the user who created the file (`Createdby`), the file content itself (`FileContent`), and the file content type (`FileContentType`). The procedure returns all selected attachment documents.

### Data Interactions
* **Reads:** `EAS_Form_Attach_Document`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-company'></a>
# Procedure: EAS_Form_Get_Company

### Purpose
This procedure retrieves a company name from a parameter reference table, filtering by effective dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PARAM_VAL_C1 | VARCHAR | The company name to retrieve. |

### Logic Flow
The procedure selects a value from the EAS_PARAM_REF_DET table. The selection is based on the criteria that the parameter record type is ‘EAS_COMP_NAME’, the parameter type is ‘COMP_NAME’, and the effective date falls within a specified range (EFF_FROM_DATE to EFF_TO_DATE). The selected value is aliased as Company.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-completed-lists'></a>
# Procedure: EAS_Form_Get_Completed_Lists

### Purpose
This procedure retrieves a list of completed forms for a specified user, ordered by the most recently updated form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_UserID | varchar(15) | The identifier for the user requesting the form list. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_Form_Master` table.
2.  It filters the selection to include only active forms.
3.  It further filters the selection to include only forms whose `FormGuid` is present in the `EAS_Form_Approve_Lvl` table, associated with the provided `@P_UserID`.
4.  The selection is further refined to include only forms where the `FormStatus` is 'Closed', 'Rejected', or 'Withdrawn'.
5.  The results are ordered by the `updatedon` column in descending order, ensuring the most recently updated forms appear first.
6.  The procedure returns the `FormGuid`, `DocRefNo`, `DocType`, `Company`, `Title`, `SubmitDate`, `FormStatus`, `Show_View`, `Show_ReRoute`, `Show_Withdraw`, and `Show_ForApproval` columns for each matching form.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-detail-info'></a>
# Procedure: EAS_Form_Get_Detail_Info

### Purpose
This procedure retrieves comprehensive details related to a form, including its master data, attachments, approver information, log history, and any withdrawn information, based on a provided GUID and user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |
| @P_UserID | varchar(15) | The user ID for context-specific data retrieval. |

### Logic Flow
1.  **Retrieve Form Master Data:** The procedure begins by selecting key details from the `EAS_Form_Master` table using the provided `@P_Guid`. This includes fields like document number, type, company, title, creation date, status, and approved amount. It also calls stored procedures `EAS_Form_Get_Approver_Name` to retrieve approver names based on the form GUID and level.  The `EAS_Form_Get_Form_Level` stored procedure is used to retrieve form level information based on the user ID.
2.  **Retrieve Attachments:** The procedure then executes the `EAS_Form_Get_Attach_Files` stored procedure, which likely retrieves associated document files linked to the form.
3.  **Retrieve Approver List:** The procedure selects data from the `EAS_Form_Approve_Lvl` table, joining it with the `EAS_Form_Log_History` table to capture approver actions and history. It uses the `@P_Guid` to filter the data. The `EAS_User_Name` stored procedure is called to display user names based on the user ID. The logic determines the status (Complete/Not Complete) and the true/false status of conflict declarations. It also uses the `GroupLevel` to determine the approver description.
4.  **Retrieve Current User Action:** The procedure selects the most recent action from the `EAS_Form_Approve_Lvl` table, filtering by the `@P_Guid` and ensuring it's the most recent action.
5.  **Retrieve Log History:** The procedure retrieves log history entries from the `EAS_Form_Log_History` table, filtering by the `@P_Guid`. It concatenates the action and the user name involved in the action to create a combined log remark.
6.  **Retrieve Withdrawn Information:** The procedure retrieves information related to withdrawn entries from the `EAS_Form_Log_History` table, filtering by the action being 'Withdrawn' and the `@P_Guid`.

### Data Interactions
* **Reads:**
    * `EAS_Form_Master`
    * `EAS_Form_Log_History`
    * `EAS_Form_Approve_Lvl`
    * `EAS_Form_Get_Attach_Files`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-detail-info-exportpdf'></a>
# Procedure: EAS_Form_Get_Detail_Info_ExportPDF

### Purpose
This procedure retrieves detailed information about a form, including its master data, attached documents (approval and support), and approval history, preparing the data for potential PDF export.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |

### Logic Flow
1.  **Retrieve Form Master Data:** The procedure begins by selecting data from the `EAS_Form_Master` table using the provided `@P_Guid`. This selection includes fields like form identifier, document reference number, document type, company, title, form status, vendor name, approved amount, and an active flag.
2.  **Retrieve Approval Documents:** The procedure then retrieves approval-related documents from the `EAS_Form_Attach_Document` table where the `FileType` is ‘ApprovalDoc’ and the `FormGuid` matches the input `@P_Guid`. It selects fields such as document sort order, document identifier, filename, file type, file URL, file size, creation date, creator, file content, and file content type.
3.  **Retrieve Support Documents:**  The procedure retrieves support-related documents from the `EAS_Form_Attach_Document` table where the `FileType` is ‘SupportDoc’ and the `FormGuid` matches the input `@P_Guid`. It selects fields such as document sort order, document identifier, filename, file type, file URL, file size, creation date, creator, file content, and file content type.
4.  **Retrieve Approval History:** The procedure retrieves the approval history associated with the form. It joins the `EAS_Form_Approve_Lvl` table with the `EAS_Form_Log_History` table based on the `FormGuid` and `ActionBy` columns. This join captures approval-level information, including the user who performed the action, the action date, and any associated remarks. The output includes the user's name, department, design, action, action date, remarks, and the role associated with the approval level.
5.  **Combine Results:** The results from the three sections (form master, approval documents, and approval history) are combined into a single result set. The approval history is ordered by the action date and action by.

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_Form_Attach_Document`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
*   **Writes:** None

---


<a id='database-reference-sql-eas-form-get-outstanding-lists'></a>
# Procedure: EAS_Form_Get_Outstanding_Lists

### Purpose
This procedure retrieves a list of outstanding forms, along with their status and associated authorization information, for a specified user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_UserID | varchar(15) | The identifier of the user requesting the form information. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_Form_Master` table.
2.  It filters the selection based on the `active` flag being set to 1, ensuring only currently active forms are considered.
3.  It further filters the selection to include only forms whose `FormGuid` is present in the `EAS_Form_Approve_Lvl` table, where the `userid` matches the input parameter `@P_UserID` and the `active` flag is also set to 1.
4.  The selection is further restricted to forms where the `FormStatus` is not 'Closed', 'Rejected', or 'Withdrawn'.
5.  The results are ordered by the `updatedon` column in ascending order.
6.  For each form, the procedure retrieves the `FormGuid`, `DocRefNo`, `DocType`, `Company`, `Title`, and `updatedon` (aliased as `SubmitDate`).
7.  It then determines the `FormStatus`. This is achieved by querying the `EAS_Form_Approve_Lvl` table for the corresponding `FormGuid` and the input user.  If there are pending approvals, the status will indicate the number of days pending approval, otherwise it will indicate "Pending Approval by [User Name]".
8.  The procedure also retrieves authorization information for 'View', 'ReRoute', 'Withdraw', and 'ForApproval' access, using the `EAS_Form_Get_User_Authorized_Functios` function, based on the input user's ID.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-prefix'></a>
# Procedure: EAS_Form_Get_Prefix

### Purpose
This procedure retrieves the value associated with the document prefix parameter from the EAS_PARAM_REF_DET table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_DocPrefix | varchar(50) | Output parameter containing the retrieved document prefix value. |

### Logic Flow
The procedure initializes an output parameter, @P_DocPrefix, to an empty string. It then executes a query against the EAS_PARAM_REF_DET table. The query filters records where the PARAM_REC_TYPE is ‘EAS_DOC_PREFIX’, the PARAM_TYPE is ‘DOC_PREFIX’, and the PARAM_CODE is ‘PREFIX_NAME’.  The query further restricts the selection to records where the effective date falls between the EFF_FROM_DATE and EFF_TO_DATE. The value from the [PARAM_VAL_C1] column of the matching record is then assigned to the output parameter @P_DocPrefix.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-reroute-user-lists'></a>
# Procedure: EAS_Form_Get_ReRoute_User_Lists

### Purpose
This procedure retrieves a list of active user IDs and names from the RPEAS system that are not associated with a specific form approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier of the form. |
| @P_ReRoute_lvl | varchar(1) |  The level of re-routing. |

### Logic Flow
The procedure begins by selecting user identifiers and names from the EAS_USER table. The selection is constrained to users associated with the RPEAS system.  Furthermore, the selection is filtered to include only active users.  The selection is further restricted to exclude users where the user identifier is present in the EAS_Form_Approve_Lvl table, specifically those linked to the provided form GUID. The results are then ordered alphabetically by user name.

### Data Interactions
* **Reads:** EAS_USER, EAS_Form_Approve_Lvl
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-serverfileuploaddetails'></a>
# Procedure: EAS_Form_Get_ServerFileUploadDetails

### Purpose
This procedure retrieves the server name and associated file path URL from a configuration table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FilePath | varchar(225) | Output parameter holding the server name. |
| @p_FilrURLPath | varchar(225) | Output parameter holding the file URL path. |

### Logic Flow
The procedure retrieves data from the `EAS_PARAM_REF_DET` table. It filters the table based on the `PARAM_REC_TYPE` being ‘EAS_FILE_PATH’, the `PARAM_TYPE` being ‘FILE_PATH’, and the `PARAM_CODE` being ‘SERVER_NAME’. The filtering also includes a date range check between `EFF_FROM_DATE` and `EFF_TO_DATE`. The retrieved server name is assigned to the output parameter `@p_FilePath`, and the associated file URL path is assigned to the output parameter `@p_FilrURLPath`.

### Data Interactions
* **Reads:** `EAS_PARAM_REF_DET`
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-userlogid-check'></a>
# Procedure: EAS_Form_Get_UserLogid_Check

### Purpose
This procedure determines if a user's session GUID and system ID match existing records in the EAS_User_login table within a specified active period.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(50) | System identifier associated with the user session. |
| @p_GUID | varchar(225) | The unique identifier for the user session. |
| @p_Cnt | varchar(225) | Output parameter containing the count of matching records. |

### Logic Flow
1.  The procedure begins by executing a count query against the EAS_User_login table.
2.  The count query filters the table based on three criteria: the provided session GUID, the provided system ID, and the current date falling within the start and end dates of a logged-in session.
3.  The count of matching records is then assigned to the output parameter @p_Cnt.

### Data Interactions
* **Reads:** EAS_User_login
* **Writes:** None

---


<a id='database-reference-sql-eas-form-get-userlogid-guid'></a>
# Procedure: EAS_Form_Get_UserLogid_GUID

### Purpose
This procedure generates a unique identifier and creates a new record in the EAS_User_login table, associating it with a specified user and session.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(50) |  System Identifier |
| @p_UserID | varchar(10) | User Identifier |
| @p_GUID | varchar(225) | Output: Unique Session Identifier |

### Logic Flow
1.  A new unique identifier is generated using the NEWID() function and stored in the @pNewGuiD variable.
2.  The value stored in @pNewGuiD is assigned to the output parameter @p_GUID.
3.  A new record is inserted into the EAS_User_login table.
4.  The record includes the provided system identifier (@P_SysID), the user identifier (@p_UserID), the current date and time for the start and end times, the newly generated unique identifier (@pNewGuiD) as the SessionGUID, a value of 'Y' for the Active flag, the current date and time for the CreatedOn timestamp, and the user identifier (@p_UserID) as the CreatedBy.

### Data Interactions
* **Reads:** None
* **Writes:** [dbo].[EAS_User_login]

---


<a id='database-reference-sql-eas-form-get-userlogid-update'></a>
# Procedure: EAS_Form_Get_UserLogid_Update

### Purpose
This procedure updates the active status of a user record in the EAS_User_login table based on provided system and GUID identifiers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(50) | System identifier of the user record. |
| @p_GUID | varchar(225) | Globally unique identifier associated with the user session. |

### Logic Flow
The procedure initiates by updating a record within the EAS_User_login table. Specifically, it sets the ‘active’ field to ‘N’ (inactive), records the current date and time in the ‘updatedon’ field, and assigns the ‘SYSTEM’ user as the user responsible for the update in the ‘updatedby’ field. The update is performed on records where the ‘SessionGUID’ matches the provided @p_GUID, the ‘sysid’ matches the provided @P_SysID, and the ‘active’ field is currently set to ‘Y’.

### Data Interactions
* **Reads:** EAS_User_login
* **Writes:** EAS_User_login

---


<a id='database-reference-sql-eas-form-save-approved-action'></a>
# Procedure: EAS_Form_Save_Approved_Action

### Purpose
This procedure updates form master data and form approval level data, logs the approval action, and optionally sends approval and final approval emails based on the form's status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | Unique identifier for the form being updated. |
| @P_Userid | varchar(15) | Identifier for the user performing the action. |
| @P_GroupLvl | int | Level of the user submitting the form. |
| @P_ActionID | int | Identifier for the approval level record. |
| @P_Status | varchar(50) | The status of the form after approval. |
| @P_Remarks | varchar(1000) | Additional remarks related to the approval. |
| @P_ChkConflict | varchar(1) | Flag indicating whether a conflict check was performed. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  Initialize the `@P_ErrorMsge` output parameter to an empty string.
2.  Determine the appropriate descriptive text based on the `@P_GroupLvl` value for logging the action.
3.  Begin a transaction to ensure atomicity of operations.
4.  Update the `EAS_Form_Master` table, setting the `FormStatus` to the provided `@P_Status`, updating the `UpdatedBy` field with the `@P_Userid`, and recording the update timestamp using `GETDATE()`. This update is performed where the `FormGuid` matches the input `@P_Guid`.
5.  Update the `EAS_Form_Approve_Lvl` table, setting the `Action` to 'Approved', the `ChkDeclareConflit` flag to the provided `@P_ChkConflict`, the `Remarks` field to the `@P_Remarks` value, the `ActionBy` field to the `@P_Userid`, and the `ActionOn` timestamp to `GETDATE()`. This update is performed where the `FormGuid` matches the input `@P_Guid` and the `id` field matches the input `@P_ActionID`.
6.  Insert a record into the `EAS_Form_Log_History` table, logging the form's approval action, the descriptive text determined by `@P_GroupLvl`, the `@P_Userid`, and the timestamp `GETDATE()`.
7.  If the `FormStatus` is not 'Closed', execute the stored procedure `EAS_Send_Approval_Email` with the form's GUID, the user ID, and the `@P_ErrorMsge` output parameter.
8.  If the `FormStatus` is 'Closed', execute the stored procedure `EAS_Send_Final_Approved_Email` with the form's GUID, the user ID, and the `@P_ErrorMsge` output parameter.
9.  Commit the transaction.
10. If an error occurs, rollback the transaction and set the `@P_ErrorMsge` with the error message.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
* **Writes:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`

---


<a id='database-reference-sql-eas-form-save-attach-files'></a>
# Procedure: EAS_Form_Save_Attach_Files

### Purpose
This procedure saves file attachment information associated with a form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_GUID | nvarchar(225) | Unique identifier for the form. |
| @P_FILENM | varchar(200) | Name of the attached file. |
| @P_FileType | varchar(200) | Type of the attached file. |
| @P_FILESIZE | varchar(200) | Size of the attached file. |
| @P_FILEURL | varchar(255) | URL location of the attached file. |
| @p_LoginID | varchar(15) | Identifier for the user creating the attachment. |
| @p_errormsg | varchar(500) | Output parameter to hold error messages. |

### Logic Flow
The procedure initializes an output parameter named @p_errormsg to an empty string. It then inserts a new record into the `EAS_Form_Attach_Document` table. The new record contains the form's unique identifier (@P_GUID), the file name (@P_FILENM), the file type (@P_FileType), the file URL (@P_FILEURL), the file size (@P_FILESIZE), the user identifier (@p_LoginID), and the current date and time.

### Data Interactions
* **Reads:** None
* **Writes:** `EAS_Form_Attach_Document`

---


<a id='database-reference-sql-eas-form-save-reroute-proceednxtlevel'></a>
# Procedure: EAS_Form_Save_ReRoute_ProceedNxtLevel

### Purpose
This procedure updates a form record and initiates a re-routing or progression to the next approval level based on a specified re-route type, logging the actions and potentially sending related emails.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier for the form. |
| @P_Userid | varchar(15) | The identifier of the user performing the action. |
| @P_FormLevel | int | The current approval level of the form. |
| @P_ReRouteType | varchar(15) | Indicates the type of re-routing or progression ('R' for Re-Route, 'N' for Next Level). |
| @P_ReRouteTo | varchar(15) | The identifier of the user to which the form is re-routed. |
| @P_Remarks | varchar(1000) |  A description of the action taken. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  **Initialization:** Sets the output error message parameter to an empty string.
2.  **Try Block:** Encloses the core logic within a transaction to ensure atomicity.
3.  **Transaction Start:** Begins a new database transaction.
4.  **Form Master Update:** Updates the `EAS_Form_Master` table with the user ID and timestamp, associated with the form's GUID.
5.  **Re-Route Logic (if @P_ReRouteType = 'R'):**
    *   **Existing Record Update:** Updates the `EAS_Form_Approve_Lvl` table, setting the action to 'Re-Routed', the remarks, the re-route type, the re-route to user, and marking the record as inactive. The action is performed by the user, and the timestamp is recorded.
    *   **New Record Insertion:** Inserts a new record into the `EAS_Form_Approve_Lvl` table with the form GUID, approval level, re-route to user, active status set to 1, created by the user, and the creation timestamp.
    *   **Log History Insertion:** Inserts a record into the `EAS_Form_Log_History` table with the form GUID, remarks, action (determined by the re-route type), action by the user, and the timestamp.
    *   **Re-Route Email Execution:** Executes the stored procedure `EAS_Send_ReRoute_Email` to send a re-route email.
6.  **Proceed to Next Level Logic (if @P_ReRouteType = 'N'):**
    *   **Next Level User Retrieval:** Selects the next approval level user ID and approval level from the `EAS_Form_Approve_Lvl` table, filtering for active records with an approval level greater than the current level, no action taken, and ordered by approval level.
    *   **Existing Record Update:** Updates the `EAS_Form_Approve_Lvl` record, setting the action to 'Proceed to Next Level', the remarks, the re-route type, the re-route to the next level user, and marking the record as inactive. The action is performed by the user, and the timestamp is recorded.
    *   **Log History Insertion:** Inserts a record into the `EAS_Form_Log_History` table with the form GUID, remarks, action (determined by the re-route type), action by the user, and the timestamp.
    *   **Proceed to Next Level Email Execution:** Executes the stored procedure `EAS_Send_ProcdNxtLvl_Email` to send a proceed to next level email.
7.  **Transaction Commit:** Commits the database transaction.
8.  **Error Handling (Catch Block):** If any error occurs within the try block:
    *   Sets the output error message parameter with the error message.
    *   Rolls back the database transaction.
9.  **Error Message Assignment:** Assigns the value of the output error message parameter to the output parameter @P_ErrorMsge.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`
* **Writes:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_Form_Log_History`

---


<a id='database-reference-sql-eas-form-save-rejected-action'></a>
# Procedure: EAS_Form_Save_Rejected_Action

### Purpose
This procedure records a form rejection action, updates related form and approval level records, and triggers an email notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | Unique identifier for the form being rejected. |
| @P_Userid | varchar(15) | Identifier of the user initiating the rejection. |
| @P_GroupLvl | int | Level of the group associated with the form. |
| @P_ActionID | int | Identifier for the specific approval action. |
| @P_Status | varchar(50) | The status assigned to the form upon rejection. |
| @P_Remarks | varchar(1000) |  Notes or comments regarding the rejection. |
| @P_ChkConflict | varchar(1) | Flag indicating whether a conflict was detected. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure begins with a check to ensure the `@P_ErrorMsge` output parameter is initialized to an empty string.
2.  A `TRY...CATCH` block is used to handle potential errors during the process.
3.  Inside the `TRY` block, a transaction is started to ensure atomicity – either all changes are committed, or none are.
4.  The `EAS_Form_Master` table is updated with the specified rejection status, the user who performed the action, and the current date and time. The update is performed using the form's unique identifier (`@P_Guid`).
5.  The `EAS_Form_Approve_Lvl` table is updated with the rejection status, conflict check flag, remarks, the user who performed the action, and the current date and time. The update is performed using the form's unique identifier (`@P_Guid`) and the action identifier (`@P_ActionID`).
6.  A new record is inserted into the `EAS_Form_Log_History` table, capturing the form's unique identifier, the rejection remarks, the action type ('Rejected by'), the user who performed the action, and the current date and time.
7.  The stored procedure `EAS_Send_Rejected_Email` is executed, passing the form's unique identifier, the user identifier, the action identifier, and the output parameter for error messages.
8.  If the transaction completes successfully, the transaction is committed.
9.  If any error occurs within the `TRY` block, the `CATCH` block is executed.
10. The `CATCH` block captures the error message using `ERROR_MESSAGE()` and stores it in the `@P_ErrorMsge` output parameter.
11. The transaction is rolled back to undo any changes made during the process.
12. Finally, the `@P_ErrorMsge` output parameter is set to the value of `@P_ErrorMsge` if it's not already empty.

### Data Interactions
* **Reads:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History
* **Writes:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History

---


<a id='database-reference-sql-eas-form-save-withdrawn-action'></a>
# Procedure: EAS_Form_Save_Withdrawn_Action

### Purpose
This procedure saves a form as withdrawn, updates related form and approval level records, and triggers an email notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | Unique identifier for the form. |
| @P_Userid | varchar(15) | Identifier of the user initiating the action. |
| @P_GroupLvl | int | Level of the group associated with the form. |
| @P_Status | varchar(50) | The status applied to the form. |
| @P_Remarks | varchar(1000) |  Notes or comments regarding the withdrawal. |
| @P_ChkConflict | varchar(1) | Flag indicating whether a conflict check was performed. |
| @P_ErrorMsge | varchar(500) | Output parameter to store any error messages. |

### Logic Flow
1.  The procedure begins with a try-catch block to handle potential errors during the process.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  The `EAS_Form_Master` table is updated with the specified `FormStatus`, `UpdatedBy`, and `UpdatedOn` based on the provided `FormGuid`.
4.  The `EAS_Form_Approve_Lvl` table is updated with the ‘Withdrawn’ action, conflict check flag, remarks, `ActionBy`, and `ActionOn` based on the `FormGuid`, `UserID`, and active status.
5.  A record is inserted into the `EAS_Form_Log_History` table, capturing the `FormGuid`, remarks, action type ('Withdrawn by'), `ActionBy`, and `ActionOn`.
6.  The `EAS_Send_Withdrawn_Email` stored procedure is executed, passing the `FormGuid` and `UserID` to send a withdrawal notification email.
7.  If the try block completes without errors, the transaction is committed.
8.  If any error occurs within the try block, the transaction is rolled back, and the error message is captured and stored in the output parameter `@P_ErrorMsge`.

### Data Interactions
* **Reads:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History
* **Writes:** dbo.EAS_Form_Master, dbo.EAS_Form_Approve_Lvl, dbo.EAS_Form_Log_History

---


<a id='database-reference-sql-eas-form-update-binary-file'></a>
# Procedure: EAS_Form_Update_Binary_File

### Purpose
This procedure updates a document attachment record within the EAS_Form_Attach_Document table with the provided binary file content and associated metadata.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_formguid | nvarchar(225) |  Unique identifier for the form. |
| @p_FileName | nvarchar(255) | Name of the file being attached. |
| @p_FileContentType | nvarchar(50) |  The MIME type of the file. |
| @p_FileContent | varbinary(MAX) | The binary data of the file. |
| @p_errormsg | varchar(500) | Output parameter to hold any error messages. |

### Logic Flow
The procedure begins by initializing an output parameter, @p_errormsg, to an empty string. It then executes a transaction block. Inside this block, it updates a record in the EAS_Form_Attach_Document table. The update sets the FileContent column to the provided binary file data, the FileContentType column to the specified MIME type, and it filters the update to only affect the record where the FormGuid matches the input @p_formguid and the FileName matches the input @p_FileName.  If an error occurs during the update process, the error message is captured and stored in the @p_errormsg output parameter.  The transaction block is implicitly handled, ensuring atomicity.

### Data Interactions
* **Reads:** EAS_Form_Attach_Document
* **Writes:** EAS_Form_Attach_Document

---


<a id='database-reference-sql-eas-get-errormessage'></a>
# Procedure: EAS_GET_ErrorMessage

### Purpose
This procedure retrieves the corresponding error message from the EAS_ERROR_MSG table based on a provided error code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_ErrorCode | integer | The error code to search for. |
| @p_Errormsg | Varchar(500) | The error message, populated by the procedure. |

### Logic Flow
1.  The procedure initializes the `@p_Errormsg` variable to an empty string.
2.  It checks if there exists at least one row in the `EAS_ERROR_MSG` table where the `ERROR_CODE` matches the input `@p_ErrorCode`.
3.  If a matching row is found, the procedure constructs the error message by concatenating the `ERROR_CODE` (converted to a string) with a hyphen and the `ERROR_TEXT` from the matching row. This constructed message is then assigned to the `@p_Errormsg` parameter.
4.  If no matching row is found in the `EAS_ERROR_MSG` table, the procedure sets `@p_Errormsg` to the string '9999 - Error Message not defined in EAS_ERROR_MSG table.' and immediately exits the procedure.

### Data Interactions
* **Reads:** `EAS_ERROR_MSG`
* **Writes:** None

---


<a id='database-reference-sql-eas-getattachlist'></a>
# Procedure: EAS_GetAttachList

### Purpose
This procedure retrieves a list of attachments associated with forms, including file identifiers, names, paths, content types, and constructed file paths.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | N/A | No input parameters are used. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_Form_Attach_Document` table, aliased as `a`, and the `EAS_Form_Master` table, aliased as `b`.
2.  It filters the `EAS_Form_Attach_Document` table to include only records where the `FileContent` column is null.
3.  The procedure joins the `EAS_Form_Attach_Document` table with the `EAS_Form_Master` table using the `FormGuid` column, linking attachments to their corresponding forms.
4.  It constructs a `FilePath` column by concatenating a fixed string with the substring of the `FileURL` column, up to the first forward slash.
5.  It constructs a `FileURL` column by removing the "https://apps.sbstransit.com.sg/RPEAS_Document/" prefix from the `FileURL` column.
6.  The selected data is then ordered by the `FILE_ID` column.
7.  The final result set contains the `FileRefNo`, `FILE_ID`, `FILE_NAME`, `FILE_PATH`, `FILE_CONTENT`, `CONT_TYPE`, and the calculated `FilePath` columns.

### Data Interactions
* **Reads:** `EAS_Form_Attach_Document`, `EAS_Form_Master`
* **Writes:** None

---


<a id='database-reference-sql-eas-get-menu'></a>
# Procedure: EAS_Get_Menu

### Purpose
This procedure retrieves a hierarchical menu structure for a specified user and system, displaying the menu items and their associated details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_UserID | nvarchar(100) | The identifier for the user. |
| @p_sysid | nvarchar(30) | The identifier for the system. |

### Logic Flow
1.  The procedure initializes a variable, @urole, to an empty string.
2.  It selects the roles associated with the specified user and system from the `EAS_User_Role` and `EAS_User` tables. The selection is based on matching UserID and Sysid, and the active status of both tables. The selected roles are concatenated into the @urole variable, separated by commas.
3.  The `LEFT` function is used to remove the trailing comma from the @urole variable.
4.  If @urole is not null and not empty, the procedure constructs a dynamic SQL string, @rsql.
5.  The dynamic SQL string selects menu items from the `EAS_Menu` table where the Active status is 1 and the ParentMenuID is null.
6.  The dynamic SQL string further filters the menu items to include only those whose Role is present in the @urole variable. The results are ordered by MenuLevel.
7.  The dynamic SQL string is executed, retrieving the specified menu details.

### Data Interactions
* **Reads:** `EAS_User`, `EAS_User_Role`, `EAS_Menu`, `EAS_Menu_Role`
* **Writes:** None

---


<a id='database-reference-sql-eas-get-menuchild'></a>
# Procedure: EAS_Get_MenuChild

### Purpose
This procedure retrieves child menu items from a specified parent menu, considering user roles and a system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_UserID | nvarchar(100) | The ID of the user making the request. |
| @p_MenuID | nvarchar(100) | The ID of the parent menu. |
| @p_Sysid | nvarchar(30) | A system identifier. |

### Logic Flow
1.  The procedure initializes a variable, @urole, to store the user's roles.
2.  It retrieves the user's roles from the `EAS_User_Role` and `EAS_User` tables, filtering by the provided `@p_UserID` and `@p_Sysid`. The retrieved roles are concatenated into the `@urole` variable, separated by commas. The `LEFT` function is used to remove the trailing comma from the `@urole` variable.
3.  If a user role is found and not empty, the procedure constructs a dynamic SQL string, `@rsql`, to execute a `SELECT` statement.
4.  The `SELECT` statement retrieves menu details from the `EAS_Menu` table, filtering by the provided `@p_MenuID` and `@p_Sysid`, and also by the roles stored in the `@urole` variable. The `MenuID` is filtered using a subquery that selects distinct `MenuID` values from the `EAS_Menu_Role` table, ensuring that only menu items accessible to the user are returned. The results are ordered by `MenuLevel`.
5.  The dynamic SQL string, `@rsql`, is executed, which retrieves the menu details and returns them as a result set.

### Data Interactions
* **Reads:** `EAS_User`, `EAS_User_Role`, `EAS_Menu`, `EAS_Menu_Role`
* **Writes:** None

---


<a id='database-reference-sql-eas-get-system-name'></a>
# Procedure: EAS_Get_System_Name

### Purpose
This procedure retrieves the system name associated with a specified system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_SysID | varchar(30) | The unique identifier for the system. |
| @P_SysName | varchar(200) | The system name, populated by the procedure. |

### Logic Flow
1.  The procedure initializes the output parameter @P_SysName to an empty string.
2.  The procedure queries the EAS_PARAM_REF_DET table.
3.  The query filters the table based on the following criteria:
    *   The PARAM_REC_TYPE column must equal 'EAS_APPL'.
    *   The PARAM_TYPE column must equal 'APPL_NAME'.
    *   The PARAM_CODE column must match the input @P_SysID.
    *   The EFF_FROM_DATE and EFF_TO_DATE columns must contain the current date.
4.  If a matching record is found, the value from the PARAM_VAL_C1 column is assigned to the output parameter @P_SysName.
5.  If no matching record is found, the output parameter @P_SysName remains an empty string.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None

---


<a id='database-reference-sql-eas-get-userinfo'></a>
# Procedure: EAS_Get_UserInfo

### Purpose
This procedure retrieves user information from the EAS_User table based on a provided user identifier and system identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_uid | nvarchar(100) | The unique identifier for the user. |
| @p_sysid | varchar(30) | A system identifier associated with the user record. |

### Logic Flow
The procedure retrieves data from the EAS_User table. It selects specific columns including UserID, Name, Email, Designation, BusinessArea, Department, and Section. The selection is filtered based on two criteria: the UserID must match the value provided in the @p_uid parameter, and the sysid must match the value provided in the @p_sysid parameter.  The procedure also includes a filter to ensure that only active user records are returned.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None

---


<a id='database-reference-sql-eas-param-get-param-ref-det-byparam'></a>
# Procedure: EAS_PARAM_GET_PARAM_REF_DET_ByParam

### Purpose
This procedure retrieves detailed reference information from the EAS_PARAM_REF_DET table based on specified parameter criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Param_Rec_Type | VARCHAR(50) |  Specifies the record type for the parameter reference. |
| @ParaType | VARCHAR(50) |  Identifies the parameter type. |
| @ParaCode | VARCHAR(50) |  Represents the parameter code. |

### Logic Flow
The procedure begins by selecting data from the EAS_PARAM_REF_DET table. The selection is filtered based on three criteria: the value of the @Param_Rec_Type parameter, the value of the @ParaType parameter, and the value of the @ParaCode parameter.  The results are ordered first by @Param_Rec_Type in ascending order, and then by the creation date in descending order within each @Param_Rec_Type group.

### Data Interactions
* **Reads:** dbo.EAS_PARAM_REF_DET
* **Writes:** None

---


<a id='database-reference-sql-eas-param-get-param-type'></a>
# Procedure: EAS_PARAM_GET_PARAM_TYPE

### Purpose
This procedure retrieves a list of distinct PARAM_TYPE values based on a specified PARAM_REC_TYPE and the current date falls within the EFF_FROM_DATE and EFF_TO_DATE ranges.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Param_RecType | varchar(50) | The identifier for a record type. |

### Logic Flow
The procedure filters the EAS_PARAM_REF_DET table to identify records where the PARAM_REC_TYPE matches the input @P_Param_RecType.  It then restricts the selection to only those records where the current date falls between the EFF_FROM_DATE and EFF_TO_DATE columns. Finally, the procedure returns a distinct list of all values found in the PARAM_TYPE column for these filtered records.

### Data Interactions
* **Reads:** EAS_PARAM_REF_DET
* **Writes:** None

---


<a id='database-reference-sql-eas-param-get-ref'></a>
# Procedure: EAS_PARAM_GET_REF

### Purpose
This procedure retrieves parameter descriptions based on a provided parameter record type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_ParamRecType | varchar(50) | The parameter record type to filter by. |

### Logic Flow
The procedure searches the `EAS_PARAM_REF` table. It filters the results based on the value provided in the `@P_ParamRecType` parameter. If `@P_ParamRecType` is null, the procedure returns all records from the table. The results are ordered alphabetically by `PARAM_REC_TYPE`.

### Data Interactions
* **Reads:** `EAS_PARAM_REF`
* **Writes:** None

---


<a id='database-reference-sql-eas-param-get-ref-det'></a>
# Procedure: EAS_PARAM_GET_REF_DET

### Purpose
This procedure retrieves detailed information about parameters from the EAS_PARAM_REF_DET table, filtering based on provided parameter type and record type criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_ParamRecType | NVARCHAR(50) | Specifies the desired parameter record type. If NULL, it matches all record types. |
| @P_ParamType | NVARCHAR(50) | Specifies the desired parameter type. If NULL, it matches the parameter type defined in the table. |

### Logic Flow
The procedure first assigns a sequential number to each row in the EAS_PARAM_REF_DET table, ordered by parameter record type in ascending order, and then by parameter code in ascending order.  It then filters the table based on the input parameters. Specifically, it selects rows where the parameter record type matches the value provided in @P_ParamRecType, or where @P_ParamRecType is NULL.  Additionally, it selects rows where the parameter type matches the value provided in @P_ParamType, or where @P_ParamType is NULL. The resulting set of rows is then returned.

### Data Interactions
* **Reads:** dbo.EAS_PARAM_REF_DET
* **Writes:** None

---


<a id='database-reference-sql-eas-param-ref-det-delete'></a>
# Procedure: EAS_PARAM_REF_DET_Delete

### Purpose
This procedure removes records from the EAS_PARAM_REF_DET table based on specified criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaRecType | VARCHAR(50) | Identifies the record type. |
| @ParaType | VARCHAR(50) | Identifies the parameter type. |
| @ParaCode | VARCHAR(50) | Identifies the parameter code. |
| @ParaDesc | VARCHAR(250) | Identifies the parameter description. |
| @EffFromDate | DATETIME | Specifies the start date for the deletion. |
| @EffToDate | DATETIME | Specifies the end date for the deletion. |
| @P_ErrorMsg | NVARCHAR(MAX) | Stores any error messages generated during the procedure execution. |

### Logic Flow
1.  The procedure begins with a try-catch block to handle potential errors during execution.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  The procedure then executes a DELETE statement against the EAS_PARAM_REF_DET table.
4.  The DELETE statement removes records where the PARAM_TYPE matches the value provided in the @ParaType parameter, the PARAM_CODE matches the value in the @ParaCode parameter, the PARAM_REC_TYPE matches the value in the @ParaRecType parameter, the PARAM_DESC matches the value in the @ParaDesc parameter, the EFF_FROM_DATE matches the value in the @EffFromDate parameter, and the EFF_TO_DATE matches the value in the @EffToDate parameter.
5.  After the DELETE statement completes, the EAS_GET_ErrorMessage procedure is executed with an error code of '102', and the resulting error message is stored in the @P_ErrorMsg parameter.
6.  The transaction is committed if no errors occurred.
7.  If any error occurs within the try block, the transaction is rolled back, and the error message from the database system is stored in the @P_ErrorMsg parameter.

### Data Interactions
* **Reads:** None
* **Writes:** [EAS_PARAM_REF_DET]

---


<a id='database-reference-sql-eas-param-ref-det-insert'></a>
# Procedure: EAS_PARAM_REF_DET_Insert

### Purpose
This procedure inserts a new record into the EAS_PARAM_REF_DET table, representing a parameter reference detail.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaRecType | VARCHAR(50) |  Specifies the record type for the parameter reference detail. |
| @ParaType | VARCHAR(50) |  Indicates the type of parameter being referenced. |
| @ParaCode | VARCHAR(50) |  Represents the unique code for the parameter reference. |
| @ParaDesc | VARCHAR(250) |  Provides a description for the parameter reference detail. |
| @EffFromDate | DATETIME |  Defines the start date for the parameter reference detail's validity. |
| @EffToDate | DATETIME |  Specifies the end date for the parameter reference detail's validity. |
| @d1 | DATETIME |  Stores a date/time value. |
| @d2 | DATETIME |  Stores a date/time value. |
| @c1 | VARCHAR(50) |  Stores a character string value. |
| @c2 | VARCHAR(50) |  Stores a character string value. |
| @n1 | INT |  Stores an integer value. |
| @n2 | DECIMAL(18,2) |  Stores a decimal number value. |
| @t1 | VARCHAR(4) |  Stores a character string value representing a time code. |
| @t2 | VARCHAR(4) |  Stores a character string value representing a time code. |
| @CreatedBy | VARCHAR(50) |  Identifies the user who created the record. |
| @P_ErrorMsg | NVARCHAR(MAX) |  Output parameter to hold any error messages. |

### Logic Flow
1.  **Duplicate Check:** The procedure first checks if a record already exists in the EAS_PARAM_REF_DET table with the same `PARAM_REC_TYPE`, `PARAM_TYPE`, and `PARAM_CODE`, and where the `EFF_FROM_DATE` falls within the range defined by `@EffFromDate` and `@EffToDate` or vice versa.
2.  **Error Handling (Duplicate):** If a duplicate record is found, the `EAS_GET_ErrorMessage` procedure is executed with an error code of '151', and the resulting error message is stored in the `@P_ErrorMsg` output parameter. The error message is then returned.
3.  **Transaction Start:** If no duplicate record is found, the procedure begins a new transaction.
4.  **Data Insertion:** A new record is inserted into the `EAS_PARAM_REF_DET` table, populating all the specified fields with the provided input values, including the current date and time for `ModifiedOn` and `CreatedOn` fields, and the `@CreatedBy` user identifier.
5.  **Success Confirmation:** The `EAS_GET_ErrorMessage` procedure is executed with an error code of '101', and the resulting error message is stored in the `@P_ErrorMsg` output parameter.
6.  **Transaction Commit:** The transaction is committed, making the changes permanent.
7.  **Error Handling (General):** If any error occurs during the process (e.g., data validation error), the `CATCH` block is executed. The error message is retrieved using `ERROR_MESSAGE()` and stored in the `@P_ErrorMsg` output parameter.
8.  **Transaction Rollback:** The transaction is rolled back, undoing any changes made during the process.

### Data Interactions
* **Reads:**  `EAS_PARAM_REF_DET`
* **Writes:** `EAS_PARAM_REF_DET`

---


<a id='database-reference-sql-eas-param-ref-det-update'></a>
# Procedure: EAS_PARAM_REF_DET_Update

### Purpose
This procedure updates information within the EAS_PARAM_REF_DET table based on provided parameter values.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaRecType | VARCHAR(50) | Specifies the record type for the parameter reference detail. |
| @ParaType | VARCHAR(50) | Identifies the type of parameter being referenced. |
| @ParaCode | VARCHAR(50) | Represents the unique code for the parameter. |
| @ParaDesc | VARCHAR(250) | Stores the description associated with the parameter. |
| @EffFromDate | DATETIME | Defines the effective date range for the parameter reference detail. |
| @EffToDate | DATETIME | Specifies the end date for the effective date range. |
| @d1 | DATETIME | Stores a numerical value associated with the parameter reference detail. |
| @d2 | DATETIME | Stores another numerical value associated with the parameter reference detail. |
| @c1 | VARCHAR(50) | Stores a character value associated with the parameter reference detail. |
| @c2 | VARCHAR(50) | Stores another character value associated with the parameter reference detail. |
| @n1 | INT | Stores an integer value associated with the parameter reference detail. |
| @n2 | DECIMAL(18,2) | Stores a decimal value associated with the parameter reference detail. |
| @t1 | VARCHAR(4) | Stores a character code associated with the parameter reference detail. |
| @t2 | VARCHAR(4) | Stores another character code associated with the parameter reference detail. |
| @UpdatedBy | VARCHAR(50) | Indicates the user who made the update. |
| @P_ErrorMsg | NVARCHAR(MAX) | Output parameter to hold any error messages. |

### Logic Flow
The procedure begins with a try-catch block to handle potential errors during the update process. It then starts a new transaction. The procedure updates the EAS_PARAM_REF_DET table. The update sets the PARAM_DESC, EFF_FROM_DATE, EFF_TO_DATE, PARAM_VAL_D1, PARAM_VAL_D2, PARAM_VAL_C1, PARAM_VAL_C2, PARAM_VAL_N1, PARAM_VAL_N2, PARAM_VAL_T1, and PARAM_VAL_T2 columns. The ISNULL function is used to handle potential NULL values for the D1 and D2 columns. The ModifiedOn and ModifiedBy columns are automatically populated with the current date and the user who performed the update, respectively. The update is performed based on the provided @ParaRecType, @ParaType, and @ParaCode values. After the update is complete, the transaction is committed. If any error occurs during the process, the catch block is executed, rolls back the transaction, and sets the @P_ErrorMsg output parameter with the error message.

### Data Interactions
* **Reads:** [EAS_PARAM_REF_DET]
* **Writes:** [EAS_PARAM_REF_DET]

---


<a id='database-reference-sql-eas-send-approval-email'></a>
# Procedure: EAS_Send_Approval_Email

### Purpose
This stored procedure sends an email notification to relevant parties to initiate an approval process for a form, providing a direct link to the form for review and action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form being approved. |
| @p_FormUserID | varchar(15) | The ID of the user who initiated the form. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1. **Initialization:** The procedure initializes all email-related variables to empty strings or zero values. It also sets the URL to a default RPEAS login page.
2. **Subject Retrieval:** It retrieves the subject line for the email from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3. **Current User Record:** It selects the ID of the current user record from the `EAS_Form_Approve_Lvl` table, which is the first record in the approval chain.
4. **Determine Maximum Level:** It identifies the highest level in the approval chain from the `EAS_Form_Approve_Lvl` table using the `@p_FormGuid`.
5. **Get Email Sender Detail:** It retrieves the sender's name from the `EAS_USER` table using the `@p_FormUserID`.
6. **Get Supervisor ID:** It retrieves the supervisor ID from the `EAS_Form_Approve_Lvl` and `EAS_USER` tables, based on the approval hierarchy.
7. **Get To Lists:** It selects the email addresses for the approvers, starting with the current user record and potentially including the supervisor. It uses the `EAS_Form_Approve_Lvl` and `EAS_USER` tables to determine the email addresses.
8. **Get CC Lists:** It determines the CC email addresses. If the next action is at level 4, it also includes the PA (Personal Assistant) in the CC list. It uses the `EAS_Form_Approve_Lvl` and `EAS_USER` tables to identify the relevant users.
9. **Email Content Construction:** It constructs the email body, including a standard greeting, a request for approval, and a hyperlink to the form. The hyperlink includes the form GUID, the user ID, and an encryption of the user's name.
10. **Error Handling:** It checks if the subject, to list, or body are empty. If any of these are empty, it sets the `@p_ErrorMsg` and raises an error, preventing the email from being sent.
11. **Email Queueing:** If no errors are detected, it executes the `EAlertQ_EnQueue` stored procedure, which enqueues the email for delivery. This procedure sends the email using the constructed subject, to list, CC list, body, and sender details.
12. **Cleanup:** After the email queueing, it resets the email-related variables to their initial empty states.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None

---


<a id='database-reference-sql-eas-send-approval-email-reminder'></a>
# Procedure: EAS_Send_Approval_Email_Reminder

### Purpose
This stored procedure sends a reminder email to approvers in an EAS form, prompting them to review and approve the form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages. |

### Logic Flow
The stored procedure `EAS_Send_Approval_Email_Reminder` initiates a process to send a reminder email to individuals involved in the approval workflow of an EAS form.

1.  **Initialization:** The procedure begins by setting default values for variables such as the email subject, recipient lists, and email body. It also initializes the alert queue ID and URL.

2.  **Form Iteration:** The procedure then uses a cursor to iterate through all active EAS forms that have not been closed, rejected, or withdrawn. The cursor selects forms based on their status.

3.  **Pending Day Calculation:** For each form, the procedure calculates the number of days the form has been pending approval using the `EAS_Form_Pending_NODays` function.

4.  **Reminder Email Trigger:** If the pending days exceed 2, the procedure proceeds to generate the reminder email.

5.  **Email Content Generation:** The procedure constructs the email content, including the subject line ("The above subject matter refer. For your approval please."), a link to the form, and the sender's name. The link directs the recipient to the form for review and action.

6.  **Recipient List Population:** The procedure populates the recipient lists (To and CC) by retrieving the relevant information from the `EAS_Form_Approve_Lvl` table. It identifies the approvers based on their level in the approval hierarchy.  It also identifies the PA Supervisor.

7.  **URL Construction:** The procedure constructs the URL for the email, incorporating the form's GUID, the user ID of the approver, and an action code.

8.  **Email Queueing:** Finally, the procedure uses the `EAlertQ_EnQueue` procedure to queue the email for sending. This function sends the email with the generated content and recipient lists.

9.  **Error Handling:** If any error occurs during the process (e.g., missing data), the procedure sets the `@p_ErrorMsg` output parameter and raises an error.

---

---


<a id='database-reference-sql-eas-send-final-approved-email'></a>
# Procedure: EAS_Send_Final_Approved_Email

### Purpose
This procedure initiates the sending of a final approval email notification to relevant stakeholders after a form has been approved.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form that has been approved. |
| @p_FormUserID | varchar(15) | The user ID of the user who initiated the form. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1.  **Initialization:** The procedure begins by setting all email-related variables to empty strings and zero. It also sets the URL to be used in the email.
2.  **Retrieve Subject:** The subject line for the email is retrieved from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Get Sender Detail:** The sender detail (currently set to 'REAS') is retrieved from a configuration.
4.  **Get Approver Information:** The name and user ID of the final approver are retrieved from the `EAS_Form_Approve_Lvl` and `EAS_USER` tables based on the `@p_FormGuid`.
5.  **Retrieve To Lists:** The email recipient list is populated by combining email addresses from the `EAS_Form_Approve_Lvl` table (for those already passed through approval levels) and the `EAS_USER` table (for PA users).
6.  **Email Content Construction:** The email body is constructed, including the subject line and a message indicating the form has been approved by the final approver.  The URL is included in the email body, directing recipients to a specific page for viewing the form.
7.  **Error Handling:** The procedure checks if any of the critical email components (subject, recipient list, or email body) are empty. If any are empty, an error message is raised, and the procedure terminates.
8.  **Enqueue Alert Queue:** If no errors are detected, the procedure executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, body, and recipient list. This effectively queues the email for delivery.
9.  **Cleanup:** After the email queue is enqueued, the email-related variables are reset to their initial empty states.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None

---


<a id='database-reference-sql-eas-send-procdnxtlvl-email'></a>
# Procedure: EAS_Send_ProcdNxtLvl_Email

### Purpose
This stored procedure sends an email notification related to a form approval process, directing recipients to a specific URL for further action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form being processed. |
| @p_FormUserID | varchar(15) | The user ID associated with the form. |
| @p_FormLevel | int |  Indicates the level of the form in the approval hierarchy. |
| @p_NextLevel | int |  Specifies the next level in the approval process. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1.  **Initialization:** The procedure initializes variables for the email subject, recipient lists (to and CC), email body, alert queue ID, and URL. It also sets the URL to a specific application URL.
2.  **Subject Retrieval:** It retrieves the email subject from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Sender Name Retrieval:** It retrieves the name of the form's creator from the `EAS_USER` table using the `@p_FormUserID`.
4.  **Supervisor ID Retrieval:** It retrieves the user ID of the supervisor associated with the form from the `EAS_Form_Approve_Lvl` table and `EAS_USER` table.
5.  **Recipient List Retrieval (To and CC):** It retrieves the recipient lists (to and CC) from the `EAS_Form_Approve_Lvl` table, considering the `@p_NextLevel`.  It uses a `CASE` statement to handle empty recipient lists.
6.  **CC List Retrieval (Conditional):** If `@p_NextLevel` is 4, it retrieves the CC list from the `EAS_Form_Approve_Lvl` table and `EAS_USER` table, including users from the `EAS_PA_Supervisor` table.  Otherwise, it retrieves the CC list from the `EAS_Form_Approve_Lvl` table.
7.  **Email Body Construction:** It constructs the email body, including the subject, a message directing recipients to the URL, and the sender's name. It uses the `fn_Encrypt` function to encrypt the user ID and other values for inclusion in the URL.
8.  **Error Handling:** It checks if the subject, to list, or body are empty. If any are empty, it sets the `@p_ErrorMsg` and raises an error, terminating the procedure.
9.  **Email Queueing:** If no errors are detected, it executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, recipient lists (to and CC), a salutation, the constructed email body, the sender's name, and the alert queue ID.
10. **Cleanup:** After the email queueing, it resets the subject, to list, and CC list variables to empty strings, and resets the email body to empty string.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_USER_ROLE`, `EAS_PA_Supervisor`
* **Writes:** `EAlertQ_EnQueue` (inserts a new alert queue entry)

---


<a id='database-reference-sql-eas-send-reroute-email'></a>
# Procedure: EAS_Send_ReRoute_Email

### Purpose
This stored procedure initiates the sending of an email alert regarding a re-routed form, including relevant details and a direct link for action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form being re-routed. |
| @p_FormUserID | varchar(15) | The user ID associated with the form. |
| @p_FormLevel | int | The level of the form approval process. |
| @p_ErrorMsg | NVARCHAR(500) | Output parameter to store any error messages encountered during the process. |

### Logic Flow
1.  **Initialization:** The procedure initializes all email related variables to empty strings or zero values. This includes the subject, to lists, CC lists, body, and alert queue ID. It also sets the URL to a specific application URL.
2.  **Subject Retrieval:** The procedure retrieves the form title from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Sender Name Retrieval:** The procedure retrieves the name of the user associated with the form from the `EAS_USER` table using the `@p_FormUserID`.
4.  **To Lists Retrieval:** The procedure retrieves the "To" list by querying the `EAS_Form_Approve_Lvl` and `EAS_USER` tables. It constructs the list by concatenating email addresses, handling the case where the list is empty. It also retrieves the `userid` and `name` from the `EAS_USER` table.
5.  **CC Lists Retrieval:** Similar to the "To" list, the procedure retrieves the "CC" list by querying the `EAS_Form_Approve_Lvl` and `EAS_USER` tables, concatenating email addresses. It also ensures the user ID is not included in the CC list.
6.  **Email Content Construction:** The procedure constructs the email body, including a message indicating the re-routing by the sender and a hyperlink to the form for action. The hyperlink includes the form GUID, encrypted user ID, and an action flag.
7.  **Error Handling:** The procedure checks if the subject, to list, or body are empty. If any of these are empty, it sets the `@p_ErrorMsg` and raises an error, terminating the procedure.
8.  **Email Queue Execution:** If no errors are detected, the procedure executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, body, to lists, CC lists, BCC list, separator, alert queue ID, and sender name as parameters.
9.  **Variable Reset:** After the email queue execution, the procedure resets all email related variables to their initial empty states.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`
* **Writes:** `EAlertQ_EnQueue` (writes to the email queue)

---


<a id='database-reference-sql-eas-send-rejected-email'></a>
# Procedure: EAS_Send_Rejected_Email

### Purpose
This stored procedure sends a rejection email notification to relevant parties involved in an EAS form approval process, including supervisors and users at different approval levels, providing a link to view the rejected form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the EAS form being rejected. |
| @p_FormUserID | varchar(15) | The user ID of the user who initiated the rejection. |
| @p_RejectID | int | The ID of the rejection record. |
| @p_ErrorMsg | output |  An output parameter to store any error messages encountered during the email sending process. |

### Logic Flow
1.  **Initialization:** The procedure initializes several variables, including email subject, recipient list, CC list, email body, alert queue ID, URL, sender detail, and error message. The URL is set to a specific RPEAS login page.
2.  **Subject Retrieval:** The procedure retrieves the email subject from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
3.  **Sender Name Retrieval:** The procedure retrieves the email sender's name from the `EAS_USER` table using the `@p_FormUserID`.
4.  **Max Approval Level Determination:** The procedure determines the maximum approval level associated with the form using the `EAS_Form_Approve_Lvl` table and the `@p_RejectID`.
5.  **Recipient List Construction:**
    *   **If Max Approval Level Matches Form Level:** The procedure constructs the recipient list by selecting email addresses from `EAS_Form_Approve_Lvl` for all approval levels up to the maximum level, including supervisors via a join with `EAS_USER` and PA supervisors.
    *   **If Max Approval Level Differs:** The procedure constructs the recipient list by selecting email addresses from `EAS_Form_Approve_Lvl` for all approval levels up to the `@p_RejectID`.
6.  **Email Content Assembly:** The email body is constructed, including a standard rejection message and a hyperlink to the RPEAS login page, incorporating the form GUID, user ID, and an encryption function for the user ID.
7.  **Error Handling:** The procedure checks if the subject, recipient list, or email body are empty. If any are empty, it sets the `@p_ErrorMsg` and raises an error, preventing the email from being sent.
8.  **Email Queueing:** If no errors are detected, the procedure executes the `EAlertQ_EnQueue` stored procedure, passing the sender detail, subject, body, sender name, recipient list, CC list, BCC list, and the alert queue ID. This effectively queues the email for delivery.
9.  **Variable Reset:** After the email queueing, the procedure resets the initialized variables.

### Data Interactions
*   **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_USER_ROLE`, `EAS_PA_Supervisor`
*   **Writes:** `EAlertQ_EnQueue` (queueing the email)

---


<a id='database-reference-sql-eas-send-withdrawn-email'></a>
# Procedure: EAS_Send_Withdrawn_Email

### Purpose
This procedure initiates the process of sending an email notification to relevant parties when a form has been withdrawn, providing a link to view the form details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_FormGuid | varchar(225) | The unique identifier for the form that was withdrawn. |
| @p_FormUserID | varchar(15) | The user ID of the form initiator. |
| @p_ErrorMsg | output |  An output parameter to hold any error messages generated during the process. |

### Logic Flow
1.  **Initialization:** The procedure begins by setting default values for all output variables, including the subject, to lists, and the body of the email. It also initializes the alert queue ID and URL.
2.  **URL Setup:** The URL for the RPEAS login page is set to `http://mssqldevpsvr/RPEAS/RPEAS_Login.aspx`.
3.  **Subject Retrieval:** The subject line for the email is retrieved from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
4.  **Sender Detail Retrieval:** The sender detail is set to 'REAS'.
5.  **Subject Retrieval:** The subject line for the email is retrieved from the `EAS_Form_Master` table using the provided `@p_FormGuid`.
6.  **To List Population:** The procedure constructs the recipient email list. It first attempts to retrieve emails from the `EAS_Form_Approve_Lvl` table, considering all levels that have passed through the form. If the `p_RejectGroupLevel` is equal to the maximum level, it also includes emails from the PA supervisor list.
7.  **Email Content Construction:** The email body is constructed, stating that the form has been withdrawn. It includes a hyperlink to the RPEAS login page, using the form's GUID and the user ID of the form initiator, along with an action parameter.
8.  **Error Handling:** If the subject, to list, or body are empty after all steps, an error message is set, and the procedure exits.
9.  **Email Queue Execution:** If no errors are encountered, the `EAlertQ_EnQueue` stored procedure is executed, passing the sender detail, subject, body, recipient email list, and sender name. This triggers the actual sending of the email alert.
10. **Variable Reset:** After the email queue execution, the subject, to list, and the body are reset to empty.

### Data Interactions
* **Reads:** `EAS_Form_Master`, `EAS_Form_Approve_Lvl`, `EAS_USER`, `EAS_PA_Supervisor`, `EAS_USER_ROLE`
* **Writes:** None

---


<a id='database-reference-sql-ealertq-enqueue'></a>
# Procedure: EAlertQ_EnQueue

### Purpose
This stored procedure creates a new alert queue entry, populating the EAlertQ table and then sequentially adding recipient email addresses from the SendTo, CC, and BCC fields to the EAlertQTo, EAlertQCC, and EAlertQBCC tables, respectively, based on the presence of a separator character.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(1000) | The sender's email address. |
| @Subject | nvarchar(500) | The subject line of the alert. |
| @Sys | nvarchar(100) | System identifier, likely for tracking. |
| @Greetings | ntext | A greeting message to be included in the alert. |
| @AlertMsg | ntext | The main body of the alert message. |
| @UserId | nvarchar(50) | The user ID associated with the alert creation. |
| @SendTo | ntext | The primary list of recipient email addresses. |
| @CC | ntext | The list of CC'd email addresses. |
| @BCC | ntext | The list of BCC'd email addresses. |
| @Separator | nvarchar(1) | A character used to delimit recipient addresses within the SendTo field. |
| @AlertID | decimal(18, 0) | Output parameter: The ID of the newly created alert queue entry. |
| @From | nvarchar(250) | The originating system or application. |

### Logic Flow
The stored procedure begins by creating a new alert queue entry in the `EAlertQ` table, populating fields like `From`, `Sender`, `Subject`, `Sys`, `Greetings`, `AlertMsg`, `CreatedOn`, `CreatedBy`, and `LastUpdatedOn` with provided values and the current user ID. The `AlertID` (a unique identifier for the alert) is generated and assigned to the output parameter.

The procedure then processes recipient addresses from the `SendTo`, `CC`, and `BCC` fields. It utilizes a loop and string manipulation to extract individual email addresses, delimited by the `@Separator` character.

1.  **Initialization:** A temporary table `#tsendto`, `#tcc`, and `#tbcc` are created to hold the respective recipient lists.
2.  **Looping:** The procedure enters a loop that continues as long as the `@Separator` character is found within the `SendTo`, `CC`, or `BCC` fields.
3.  **Email Extraction:** Inside the loop, the procedure extracts individual email addresses from the delimited string using `substring` and `PATINDEX`.
4.  **Recipient Table Population:** For each extracted email address, the procedure inserts a new record into the `EAlertQTo`, `EAlertQCC`, or `EAlertQBCC` table, depending on the source field. The `AlertID` is used as the primary key for all recipient tables. The `CreatedOn`, `CreatedBy`, and `LastUpdatedOn` fields are populated with the current date and user ID.
5.  **String Manipulation:** The `UPDATETEXT` function is used to move the pointer within the delimited string, allowing the procedure to process the next email address.
6.  **Cleanup:** After processing all email addresses, the temporary tables `#tsendto`, `#tcc`, and `#tbcc` are dropped.
7.  **Commit:** Finally, the transaction is committed, making the changes permanent.

### Data Interactions
* **Reads:** `EAlertQ`, `EAlertQTo`, `EAlertQCC`, `EAlertQBCC`
* **Writes:** `EAlertQ`, `EAlertQTo`, `EAlertQCC`, `EAlertQBCC`

---


<a id='database-reference-sql-smtp-get-email-lists'></a>
# Procedure: SMTP_GET_Email_Lists

### Purpose
This procedure retrieves a list of email addresses for sending alerts via SMTP, based on criteria within the EALERTQ table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ALERTID | INT | Identifies the alert for which email addresses are retrieved. |

### Logic Flow
1.  The procedure begins by selecting data from the EALERTQ table, filtering for records where the status is ‘Q’.
2.  It then retrieves a list of recipient email addresses associated with each alert. This list is constructed by querying the EALERTQTO table, filtering for active records where the email address is not empty.
3.  The email addresses are concatenated into a single string, separated by commas.
4.  The procedure retrieves the subject and greeting messages from the EALERTQ table.
5.  Finally, the procedure returns a result set containing the greeting, subject, alert message, sender, alert identifier, and the concatenated list of recipient email addresses (both recipients and CC recipients).

### Data Interactions
* **Reads:** EALERTQ, EALERTQTO
* **Writes:** None

---


<a id='database-reference-sql-smtp-update-email-lists'></a>
# Procedure: SMTP_Update_Email_Lists

### Purpose
This procedure updates records in the EALERTQ table to reflect the status of an alert and records the update activity.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_AlertID | int | The unique identifier for the alert being processed. |
| @p_SysID | varchar(50) | The system identifier used to track the update activity. |
| @p_ErrorMsg | varchar(255) | An output parameter to hold any error messages encountered during the process. |

### Logic Flow
The procedure begins by initializing the @p_ErrorMsg output parameter to an empty string.  It then updates records within the EALERTQ table. The update sets the Status field to 'S', records the date and time of the last update using the current date and time function, and records the system identifier (@p_SysID) as the user who performed the update. The update is performed based on the provided @p_AlertID, identifying the specific alert record to be modified.

### Data Interactions
* **Reads:** EALERTQ
* **Writes:** EALERTQ

---


<a id='database-reference-sql-test'></a>
# Procedure: test

### Purpose
This procedure retrieves all data from a specified READONLY table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @test | Table | Input table to be read. |

### Logic Flow
The procedure receives a table named @test as input. It then executes a select statement that retrieves all rows and columns from the specified table. The result of this select statement is not further processed or modified within the procedure. The retrieved data is simply returned.

### Data Interactions
* **Reads:** [dbo].[test]
* **Writes:** None

---

