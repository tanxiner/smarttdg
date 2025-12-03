# Page: TVFAcknowledgement_Enquiry  
**File:** TVFAcknowledgement_Enquiry.aspx.cs  

### 1. User Purpose  
Users search for and view traffic violation acknowledgement records for a specific user or vehicle.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page; if it is the first load, it may set up default controls and call `BindGrid` to display existing records. |
| BindGrid | Retrieves a list of acknowledgement entries from the database and binds them to a grid control for display. |
| LoadOCCTVF_AckCtrl | Loads detailed acknowledgement information for a given user ID (`uID`) and populates the acknowledgement control on the page. |
| btnSearch_Click | Captures search criteria entered by the user, queries the database for matching acknowledgement records, and refreshes the grid with the results. |

### 3. Data Interactions  
* **Reads:** TrafficViolationAcknowledgement (or similar entity)  
* **Writes:** None  

---

# Page: Test  
**File:** Test.aspx.cs  

### 1. User Purpose  
This page is likely used for internal testing or diagnostics and does not expose functional user actions.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Executes any test‑specific initialization logic when the page is first requested. |

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TrafficBulletin  
**File:** TrafficBulletin.aspx.cs  

### 1. User Purpose  
Users generate traffic possession and summary reports, view them in PDF format, and filter data by line selection.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up initial state, populates dropdowns (e.g., line selection), and prepares any necessary data structures. |
| ddlLine_SelectedIndexChanged | Responds to a change in the line dropdown; updates displayed data or report parameters accordingly. |
| btnGenerateReport_Click | Initiates the creation of a detailed possession report based on current filters and displays it in PDF. |
| btnGenerateSummaryReport_Click | Generates a summarized report of traffic data and presents it as a PDF. |
| btnGeneratePossessionReport_Click | Triggers the generation of a possession report, likely a subset of the detailed report, and outputs it as PDF. |
| GenerateReportInPDF | Accepts a list of `Tar` objects, constructs a PDF table for each, and compiles them into a single PDF document. |
| getPDFPageLoadDataTAR | Builds a PDF table row for a single `Tar` record, formatting its fields for display. |
| exportPDF | Sends the constructed PDF to the client browser for download or inline viewing. |

### 3. Data Interactions  
* **Reads:** `Tar` (traffic record) entities, possibly related possession and summary data via the `oTrafficBulletin` data access layer.  
* **Writes:** None (report generation is read‑only).  

---

# Page: UserDetailView  
**File:** UserDetailView.aspx.cs  

### 1. User Purpose  
Users view detailed information about a specific user account and can request an email containing that information.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads the selected user’s profile data from the database and populates the page controls for display. |
| btn_requestViewEmail_Click | Sends an email to the user (or to a requester) containing the user’s details, possibly using a pre‑formatted template. |

### 3. Data Interactions  
* **Reads:** UserProfile (or similar entity)  
* **Writes:** Email sent (no database write).  

---

# Page: UserDetailViewFrmEmail  
**File:** UserDetailViewFrmEmail.aspx.cs  

### 1. User Purpose  
Provides a form for composing and sending an email that includes user details, with a selection of dummy system data for testing.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Prepares the email form, possibly populating dropdowns or selection lists with dummy system data for the user to choose from. |
| buildDummySystemSelectiondata | Generates a `DataTable` containing placeholder system selection options used to populate a dropdown or list on the form. |

### 3. Data Interactions  
* **Reads:** None (dummy data is generated in memory).  
* **Writes:** Email sent (no database write).  

---