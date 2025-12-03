# Page: OCCAuthCC_DTL  
**File:** OCCAuthCC_DTL.ascx.cs  

### 1. User Purpose  
Users view and manage access records for specific tracks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads access records into the grid. |  
| populateOCCAuth | Loads track access data into the user interface. |  
| GridView1_RowDataBound | Formats grid rows (e.g., highlights specific entries). |  
| btnSubmit_Click | Saves changes to the selected access record. |  

### 3. Data Interactions  
* **Reads:** Access records, TrackType  
* **Writes:** Updated access records  

---

# Page: OCCAuthPFR_DTL  
**File:** OCCAuthPFR_DTL.ascx.cs  

### 1. User Purpose  
Users review and submit access requests for specific track types.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads track type access data. |  
| populateOCCAuth | Loads track type access data into the user interface. |  
| GridView1_RowDataBound | Formats grid rows (e.g., highlights specific entries). |  
| btnSubmit_Click | Submits the access request for approval. |  

### 3. Data Interactions  
* **Reads:** Track type access records  
* **Writes:** Submitted access requests  

---

# Page: OCCAuthPreview  
**File:** OCCAuthPreview.ascx.cs  

### 1. User Purpose  
Users preview grouped access records for review.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads grouped access data. |  
| populateOCCAuthPreview | Loads and groups access records for display. |  
| ShowingGroupingDataInGridView | Organizes grid rows into grouped sections. |  
| GridView1_RowDataBound | Formats grid rows (e.g., applies styling to grouped headers). |  
| GridView1_RowCreated | Sets up grouping headers for the grid. |  

### 3. Data Interactions  
* **Reads:** Access records, TrackType  
* **Writes:** None (data is only viewed)