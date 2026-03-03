# Page: OCCAuthCC_DTL
**File:** OCCAuthCC_DTL.ascx.cs

### 1. User Purpose
Users view and submit details for a “CC” type OCC authorization request.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control on first load, calling `populateOCCAuth` to fill the grid with existing CC authorization data. |
| populateOCCAuth | Retrieves the current user’s CC authorization records (filtered by `UserID`, `Line`, `TrackType`, and `AccessDate`) and binds them to the GridView. |
| GridView1_RowDataBound | Formats each row of the GridView, applying any necessary styling or data transformations for display. |
| btnSubmit_Click | Gathers user input from the GridView, validates the entries, and persists any changes or new records to the database. After a successful save, it may refresh the grid to reflect updated data. |

### 3. Data Interactions
* **Reads:** OCCAuth (CC type) records for the current user and context.  
* **Writes:** Updated or new OCCAuth (CC type) records.

---

# Page: OCCAuthPFR_DTL
**File:** OCCAuthPFR_DTL.ascx.cs

### 1. User Purpose
Users view and submit details for a “PFR” type OCC authorization request.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up the control on initial load, invoking `populateOCCAuth` to load existing PFR authorization data into the GridView. |
| populateOCCAuth | Fetches the current user’s PFR authorization entries (using `UserID`, `Line`, `TrackType`, and `AccessDate`) and binds them to the GridView. |
| GridView1_RowDataBound | Applies formatting or data manipulation to each row before it is rendered. |
| btnSubmit_Click | Validates user modifications or additions in the GridView, then writes the changes back to the database. The grid is refreshed afterward to show the latest data. |

### 3. Data Interactions
* **Reads:** OCCAuth (PFR type) records for the current user and context.  
* **Writes:** Updated or new OCCAuth (PFR type) records.

---

# Page: OCCAuthPreview
**File:** OCCAuthPreview.ascx.cs

### 1. User Purpose
Users preview grouped OCC authorization data before final submission, allowing them to review aggregated information.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Triggers the preview population routine on first load, calling `populateOCCAuthPreview` to gather data for display. |
| populateOCCAuthPreview | Retrieves the relevant OCC authorization data (based on `Line`, `TrackType`, and `OperationDate`), organizes it into groups, and binds the grouped data to the GridView. |
| ShowingGroupingDataInGridView | Handles the visual grouping of rows within the GridView, inserting group headers or separators as needed to reflect the data hierarchy. |
| GridView1_RowDataBound | Formats each data row, applying any necessary transformations or styling. |
| GridView1_RowCreated | Prepares the row structure, potentially inserting group header rows or adjusting layout before data binding. |

### 3. Data Interactions
* **Reads:** OCCAuth records filtered by `Line`, `TrackType`, and `OperationDate`.  
* **Writes:** None – this control is read‑only and used solely for preview purposes.