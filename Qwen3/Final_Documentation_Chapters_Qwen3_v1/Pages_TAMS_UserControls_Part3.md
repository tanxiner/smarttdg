# Page: OCCAuth_NEL  
**File:** OCCAuth_NEL.ascx.cs  

### 1. User Purpose  
Users submit access requests for track operations by providing details like user ID, line, track type, access date, and roster code.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads user data into the interface. |  
| populateOCCAuth | Loads a list of access requests into a grid for review. |  
| GridView1_RowDataBound | Applies formatting or additional logic to individual grid rows. |  
| btnSubmit_Click | Validates user input, saves the access request to the database, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** User, AccessRequest  
* **Writes:** AccessRequest  

---

# Page: OCCAuth_NEL_bak  
**File:** OCCAuth_NEL_bak.ascx.cs  

### 1. User Purpose  
Users submit access requests for track operations using a legacy interface with similar functionality to the active version.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads user data into the interface. |  
| populateOCCAuth | Loads a list of access requests into a grid for review. |  
| GridView1_RowDataBound | Applies formatting or additional logic to individual grid rows. |  
| btnSubmit_Click | Validates user input, saves the access request to the database, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** User, AccessRequest  
* **Writes:** AccessRequest  

---

# Page: OCCTVF_Ack  
**File:** OCCTVF_Ack.ascx.cs  

### 1. User Purpose  
Users review, approve, reject, or modify access requests by interacting with a grid of pending requests and associated remarks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads pending access requests into the interface. |  
| populateOCCTVF_Ack | Loads a list of access requests into a grid for review. |  
| GridView1_RowDataBound | Applies formatting or additional logic to individual grid rows. |  
| btnSubmit_Click | Approves an access request and updates the status in the database. |  
| btnReject_Click | Rejects an access request and updates the status in the database. |  
| ShowRemark | Displays additional remarks or notes related to a specific request. |  
| btnSave_Click | Saves changes to remarks or other metadata associated with an access request. |  
| ShowTarTVF | Displays related track or TVF (Train Vehicle File) data for a specific request. |  

### 3. Data Interactions  
* **Reads:** AccessRequest, Remark, Track, TVF  
* **Writes:** AccessRequest, Remark