# Page: RegistrationRequest
**File:** RegistrationRequest.aspx.cs

### 1. User Purpose
Users review pending user registration requests, assign system and owner roles, approve or reject requests, resend activation links, and delete requests.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads the request details for the current user and initializes the page layout. |
| SetupPage | Retrieves the registration request by ID, populates hidden fields, and prepares the UI for editing. |
| BuildPage | Builds the visual representation of the request, including user details and role checkboxes. |
| ResetPage | Clears all form fields and resets the UI to its default state. |
| buildDummySystemSelectiondata | Generates a list of system selections for role assignment, used when assigning access. |
| btn_back_Click | Navigates back to the previous page or request list. |
| cb_gvSysAdminRole_CheckedChanged | Toggles the admin role checkbox state and updates internal tracking of selected roles. |
| btn_assignAccess_Click | Persists the selected system roles for the user and updates the database accordingly. |
| btn_rejectRequest_Click | Marks the registration request as rejected and records the reason. |
| btn_approvalUpdate_Click | Saves any changes made to the request’s approval status or comments. |
| btn_approvalReject_Click | Submits a final rejection of the request, updating status and notifying relevant parties. |
| cb_gvSysOwnerRole_CheckedChanged | Handles changes to the owner role checkbox, updating role selection logic. |
| btn_approveCompany_Click | Approves the company associated with the request, updating company status. |
| btn_rejectCompany_Click | Rejects the company, setting its status to rejected. |
| btn_resendLink_Click | Generates a new activation link and sends it to the user’s email address. |
| btn_deleteRequest_Click | Deletes the registration request record from the system after confirmation. |

### 3. Data Interactions
* **Reads:** UserRegistration, SystemSelection, Company (for approval status)
* **Writes:** UserRegistration (status, role assignments), Company (approval status), Email logs (for resend link)

---

# Page: ResetPassword
**File:** ResetPassword.aspx.cs

### 1. User Purpose
Users reset their account password using a secure link, entering a new password and confirming it.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Validates the reset token, loads the user record, and prepares the password reset form. |
| setupPage | Populates hidden fields with the user’s registration ID and sets up any necessary UI elements. |
| btn_externalSave_Click | Validates the new password, updates the user’s password in the database, and confirms success to the user. |
| btn_externalCancel_Click | Cancels the reset operation and redirects the user back to the login page. |

### 3. Data Interactions
* **Reads:** UserRegID, password reset token
* **Writes:** UserRegID (password field updated)