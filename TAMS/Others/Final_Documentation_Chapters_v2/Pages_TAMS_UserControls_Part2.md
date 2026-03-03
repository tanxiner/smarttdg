# Page: OCCAuthTC_DTL.ascx  
**File:** OCCAuthTC_DTL.ascx.cs  

### 1. User Purpose  
Users submit detailed access requests for track operations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the user interface and loads existing data. |  
| populateOCCAuth | Populates the grid view with access request details. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the grid view. |  
| btnSubmit_Click | Validates user input, saves the access request, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: OCCAuth_NEL.ascx  
**File:** OCCAuth_NEL.ascx.cs  

### 1. User Purpose  
Users submit non-essential access requests for track operations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the user interface and loads existing data. |  
| populateOCCAuth | Populates the grid view with access request details. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the grid view. |  
| btnSubmit_Click | Validates user input, saves the access request, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: OCCAuth_NEL_bak.ascx  
**File:** OCCAuth_NEL_bak.ascx.cs  

### 1. User Purpose  
Users submit non-essential access requests for track operations (backup version).  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the user interface and loads existing data. |  
| populateOCCAuth | Populates the grid view with access request details. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the grid view. |  
| btnSubmit_Click | Validates user input, saves the access request, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: OCCTVF_Ack.ascx  
**File:** OCCTVF_Ack.ascx.cs  

### 1. User Purpose  
Users acknowledge or reject track access requests and manage related remarks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the user interface and loads existing data. |  
| populateOCCTVF_Ack | Populates the grid view with acknowledgment details. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the grid view. |  
| btnSubmit_Click | Submits acknowledgment for approval. |  
| btnReject_Click | Rejects the access request and records the reason. |  
| ShowRemark | Displays additional remarks for a specific request. |  
| btnSave_Click | Saves changes to remarks or approvals. |  
| ShowTarTVF | Displays tariff or TVF-related information for a request. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None