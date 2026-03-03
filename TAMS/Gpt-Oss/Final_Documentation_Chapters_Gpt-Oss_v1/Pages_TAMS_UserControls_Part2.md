# Page: OCCAuthPreview_NEL  
**File:** OCCAuthPreview_NEL.ascx.cs  

### 1. User Purpose  
Users view a preview of OCC authorization records for a specific line and operation date.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, triggers the preview population routine. |
| populateOCCAuthPreview | Retrieves authorization data for the configured line and operation date, binds it to the grid view, and prepares any necessary formatting. |
| GridView1_RowDataBound | Formats each row of the grid view, applying conditional styling or inserting additional controls based on the data values. |
| GridView1_RowCreated | Sets up row-level attributes or placeholders before the row is rendered, ensuring consistent layout. |

### 3. Data Interactions  
* **Reads:** OCC authorization records filtered by line and operation date.  
* **Writes:** None.  

---

# Page: OCCAuthPreview_Roster  
**File:** OCCAuthPreview_Roster.ascx.cs  

### 1. User Purpose  
Users examine duty roster information for a selected line, track type, and operation date, broken down by shift.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initiates the roster binding process for all three shifts on initial load. |
| bindFirstShift | Loads first‑shift roster data for the specified line, track type, and date, then binds it to the first grid view. |
| bindSecondShift | Loads second‑shift roster data and binds it to the second grid view. |
| bindThirdShift | Loads third‑shift roster data and binds it to the third grid view. |
| searchDutyRoster | Executes a search based on user‑supplied criteria (line, track type, date) and refreshes all shift grids. |
| gvFirstShift_RowDataBound | Applies row‑level formatting or data transformations for the first‑shift grid. |
| gvSecondShift_RowDataBound | Applies row‑level formatting or data transformations for the second‑shift grid. |
| gvThirdShift_RowDataBound | Applies row‑level formatting or data transformations for the third‑shift grid. |

### 3. Data Interactions  
* **Reads:** Duty roster entries for the selected line, track type, and operation date, separated by shift.  
* **Writes:** None.  

---

# Page: OCCAuthTC_DTL  
**File:** OCCAuthTC_DTL.ascx.cs  

### 1. User Purpose  
Users review detailed OCC authorization information for a specific user and submit any necessary updates or approvals.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Calls the data population routine to display current authorization details. |
| populateOCCAuth | Retrieves detailed authorization data for the configured user, line, track type, and access date, then binds it to the grid view. |
| GridView1_RowDataBound | Formats each row of the detail grid, potentially adding action links or status indicators. |
| btnSubmit_Click | Processes the user's submission, updating authorization records or recording approval actions, and then refreshes the displayed data. |

### 3. Data Interactions  
* **Reads:** Detailed OCC authorization records for the specified user and context.  
* **Writes:** Updates to authorization status or approval logs based on the submit action.  

---