# Page: TVFAcknowledgement_Enquiry  
**File:** TVFAcknowledgement_Enquiry.aspx.cs  

### 1. User Purpose  
Users search and view acknowledgment records related to TVF (Traffic Violation Form) submissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default data for the user interface. |  
| BindGrid | Loads acknowledgment records into a grid for display. |  
| LoadOCCTVF_AckCtrl | Populates a control with user-specific acknowledgment details based on a provided user ID. |  
| btnSearch_Click | Filters and displays acknowledgment records based on user input criteria. |  

### 3. Data Interactions  
* **Reads:** TVFAcknowledgement, User, BlockedTar  
* **Writes:** None  

---

# Page: Test  
**File:** Test.aspx.cs  

### 1. User Purpose  
Users interact with a test page to verify basic functionality or display static content.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads initial data or sets up the test environment. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TrafficBulletin  
**File:** TrafficBulletin.aspx.cs  

### 1. User Purpose  
Users generate and export traffic bulletin reports, including possession and summary reports.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default report parameters. |  
| btnGeneratePossessionReport_Click | Triggers the generation of a possession report and exports it as a PDF. |  
| ddlLine_SelectedIndexChanged | Filters report data based on selected line or route. |  
| btnGenerateSummaryReport_Click | Generates a summary report based on user-selected criteria. |  
| btnGenerateReport_Click | Initiates the report generation process for custom parameters. |  

### 3. Data Interactions  
* **Reads:** Tar, Line, ReportTemplate  
* **Writes:** None  

---

# Page: UserDetailView  
**File:** UserDetailView.aspx.cs  

### 1. User Purpose  
Users view detailed information about a user and request email access to their account.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user details and displays them in the interface. |  
| btn_requestViewEmail_Click | Sends an email request to grant view access to the user's account. |  

### 3. Data Interactions  
* **Reads:** User, EmailRequest  
* **Writes:** EmailRequest  

---

# Page: UserDetailViewFrmEmail  
**File:** UserDetailViewFrmEmail.aspx.cs  

### 1. User Purpose  
Users fill out a form to request email access to a user's account, selecting system options for the request.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the email request form and initializes system selection options. |  
| buildDummySystemSelectiondata | Generates placeholder data for system selection dropdowns. |  

### 3. Data Interactions  
* **Reads:** System, EmailRequest  
* **Writes:** EmailRequest