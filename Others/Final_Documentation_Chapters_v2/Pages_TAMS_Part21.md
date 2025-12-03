# Page: TOAGenURL  
**File:** TOAGenURL.aspx.cs  

### 1. User Purpose  
Users generate encoded URLs for tracking access requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and prepares the URL generation interface. |  
| lblGen_Click | Triggers URL generation by encoding input string and displaying the result. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TVFAcknowledgement  
**File:** TVFAcknowledgement.aspx.cs  

### 1. User Purpose  
Users view acknowledgment records for traffic violations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads acknowledgment data and initializes the grid view. |  
| LoadOCCTVF_AckCtrl | Fetches and displays acknowledgment details for a specific user. |  

### 3. Data Interactions  
* **Reads:** Acknowledgment records (e.g., TVFAcknowledgement table)  
* **Writes:** None  

---

# Page: TVFAcknowledgement_Enquiry  
**File:** TVFAcknowledgement_Enquiry.aspx.cs  

### 1. User Purpose  
Users search for acknowledgment records using filters.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the enquiry interface and initializes search parameters. |  
| btnSearch_Click | Filters and displays acknowledgment records based on user input. |  

### 3. Data Interactions  
* **Reads:** Acknowledgment records (e.g., TVFAcknowledgement table)  
* **Writes:** None  

---

# Page: Test  
**File:** Test.aspx.cs  

### 1. User Purpose  
Users test page functionality for development purposes.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads a static test interface with no functional logic. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TrafficBulletin  
**File:** TrafficBulletin.aspx.cs  

### 1. User Purpose  
Users generate possession and summary reports for traffic data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| btnGeneratePossessionReport_Click | Triggers generation of a possession report in PDF format. |  
| btnGenerateSummaryReport_Click | Triggers generation of a summary report in PDF format. |  
| ddlLine_SelectedIndexChanged | Filters report data based on selected line or category. |  

### 3. Data Interactions  
* **Reads:** Traffic records (e.g., Tar table)  
* **Writes:** None  

---

# Page: UserDetailView  
**File:** UserDetailView.aspx.cs  

### 1. User Purpose  
Users view detailed information about a specific user.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| btn_requestViewEmail_Click | Sends an email request to view user details to the specified recipient. |  

### 3. Data Interactions  
* **Reads:** User records (e.g., User table)  
* **Writes:** None  

---

# Page: UserDetailViewFrmEmail  
**File:** UserDetailViewFrmEmail.aspx.cs  

### 1. User Purpose  
Users configure email settings for viewing user details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| buildDummySystemSelectiondata | Generates placeholder data for system selection dropdowns. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None