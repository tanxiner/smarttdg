# Page: OCCAuth_NEL  
**File:** OCCAuth_NEL.ascx.cs  

### 1. User Purpose  
Users review a list of OCC authorization requests for a specific line and track type and can submit a new request or update an existing one.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| `Page_Load` | On first load, the control initializes by calling `populateOCCAuth` to fill the grid with pending requests. |
| `populateOCCAuth` | Retrieves the current user’s pending OCC authorization records from the database and binds them to the GridView. |
| `GridView1_RowDataBound` | For each row, formats data (e.g., date formatting, status icons) and attaches client‑side handlers for row actions. |
| `btnSubmit_Click` | Validates the selected request, updates its status to “Submitted,” records the submission timestamp, and refreshes the grid. |

### 3. Data Interactions  

* **Reads:** OCCAuthRequests, Users  
* **Writes:** OCCAuthRequests (status update, submission timestamp)  

---  

# Page: OCCAuth_NEL_bak  
**File:** OCCAuth_NEL_bak.ascx.cs  

### 1. User Purpose  
Provides a backup interface for reviewing and submitting OCC authorization requests, mirroring the primary control’s functionality.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| `Page_Load` | Calls `populateOCCAuth` to load pending requests when the page first renders. |
| `populateOCCAuth` | Fetches pending OCC authorization entries for the user and binds them to the GridView. |
| `GridView1_RowDataBound` | Formats each row’s display and prepares any required client‑side interactions. |
| `btnSubmit_Click` | Validates the selected request, marks it as “Submitted,” logs the action, and refreshes the grid. |

### 3. Data Interactions  

* **Reads:** OCCAuthRequests, Users  
* **Writes:** OCCAuthRequests (status update, submission timestamp)  

---  

# Page: OCCTVF_Ack  
**File:** OCCTVF_Ack.ascx.cs  

### 1. User Purpose  
Allows users to acknowledge or reject Track Verification Form (TVF) entries, add remarks, and view tariff details related to the selected TVF.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| `Page_Load` | On initial load, invokes `populateOCCTVF_Ack` to display the list of TVFs awaiting action. |
| `populateOCCTVF_Ack` | Retrieves TVF records for the user’s line and track type, binding them to the GridView. |
| `GridView1_RowDataBound` | Formats each TVF row (e.g., status icons, date formatting) and sets up row‑specific controls. |
| `btnSubmit_Click` | Marks the selected TVF as “Acknowledged,” records the acknowledgment timestamp, and updates the grid. |
| `btnReject_Click` | Marks the selected TVF as “Rejected,” records the rejection timestamp, and updates the grid. |
| `ShowRemark` | Displays a modal or panel where the user can view or edit remarks associated with the TVF. |
| `btnSave_Click` | Persists any entered remarks to the database and refreshes the remark display. |
| `ShowTarTVF` | Loads and displays tariff or TVF details for the selected record, typically in a popup or side panel. |

### 3. Data Interactions  

* **Reads:** TVFRecords, Remarks, TariffDetails, Users  
* **Writes:** TVFRecords (status updates, timestamps), Remarks (insert/update)  

---