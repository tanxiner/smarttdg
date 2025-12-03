# Page: OCCAuthPreview_NEL
**File:** OCCAuthPreview_NEL.ascx.cs

### 1. User Purpose
Users view authorization details for a specific line and operation date.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads authorization data into the GridView |
| populateOCCAuthPreview | Binds authorization records to the GridView for display |
| GridView1_RowDataBound | Formats GridView rows to highlight specific data or apply styling |
| GridView1_RowCreated | Sets up initial row structure for the GridView |

### 3. Data Interactions
* **Reads:** [Authorization Records]
* **Writes:** []

---

# Page: OCCAuthPreview_Roster
**File:** OCCAuthPreview_Roster.ascx.cs

### 1. User Purpose
Users view duty roster assignments for specific lines and operation dates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and binds duty roster data to the GridView sections |
| bindFirstShift | Loads first shift assignments into the corresponding GridView |
| bindSecondShift | Loads second shift assignments into the corresponding GridView |
| bindThirdShift | Loads third shift assignments into the corresponding GridView |
| searchDutyRoster | Filters and updates the GridView sections based on user input criteria |
| gvFirstShift_RowDataBound | Formats first shift GridView rows to highlight specific data |
| gvSecondShift_RowDataBound | Formats second shift GridView rows to highlight specific data |
| gvThirdShift_RowDataBound | Formats third shift GridView rows to highlight specific data |

### 3. Data Interactions
* **Reads:** [Duty Roster Assignments]
* **Writes:** []

---

# Page: OCCAuthTC_DTL
**File:** OCCAuthTC_DTL.ascx.cs

### 1. User Purpose
Users submit track access requests and view detailed authorization records.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads authorization records into the GridView |
| populateOCCAuth | Binds detailed authorization data to the GridView for display |
| GridView1_RowDataBound | Formats GridView rows to highlight specific data or apply styling |
| btnSubmit_Click | Validates user input, saves the access request, and updates the authorization records |

### 3. Data Interactions
* **Reads:** [Authorization Records]
* **Writes:** [Authorization Records]