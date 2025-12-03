# Page: OCCAuthCC_DTL.ascx
**File:** OCCAuthCC_DTL.ascx.cs

### 1. User Purpose
Users view and manage access records for specific tracks and dates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads access records for the current user. |
| populateOCCAuth | Loads and binds access records to the GridView for display. |
| GridView1_RowDataBound | Formats rows in the GridView based on access type and date. |
| btnSubmit_Click | Validates user input, saves new access records, and updates the display. |

### 3. Data Interactions
* **Reads:** Access records (AccessDate, TrackType, Line)
* **Writes:** Access records (AccessDate, TrackType, Line)


# Page: OCCAuthPFR_DTL.ascx
**File:** OCCAuthPFR_DTL.ascx.cs

### 1. User Purpose
Users view and manage permission records for specific tracks and dates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads permission records for the current user. |
| populateOCCAuth | Loads and binds permission records to the GridView for display. |
| GridView1_RowDataBound | Formats rows in the GridView based on permission type and date. |
| btnSubmit_Click | Validates user input, saves new permission records, and updates the display. |

### 3. Data Interactions
* **Reads:** Permission records (AccessDate, TrackType, Line)
* **Writes:** Permission records (AccessDate, TrackType, Line)


# Page: OCCAuthPreview.ascx
**File:** OCCAuthPreview.ascx.cs

### 1. User Purpose
Users preview grouped access records for specific tracks and dates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads grouped access records for display. |
| populateOCCAuthPreview | Loads and binds grouped access records to the GridView. |
| ShowingGroupingDataInGridView | Groups and formats data in the GridView by track type. |
| GridView1_RowDataBound | Applies visual styling to grouped rows in the GridView. |

### 3. Data Interactions
* **Reads:** Access records (OperationDate, TrackType, Line)
* **Writes:** No direct writes


# Page: OCCAuthPreview_NEL.ascx
**File:** OCCAuthPreview_NEL.ascx.cs

### 1. User Purpose
Users preview non-editable access records for specific tracks and dates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads non-editable access records for display. |
| populateOCCAuthPreview | Loads and binds access records to the GridView. |
| GridView1_RowDataBound | Applies read-only formatting to all GridView rows. |

### 3. Data Interactions
* **Reads:** Access records (OperationDate, TrackType, Line)
* **Writes:** No direct writes


# Page: OCCAuthPreview_Roster.ascx
**File:** OCCAuthPreview_Roster.ascx.cs

### 1. User Purpose
Users view and search duty roster records for specific tracks and shifts.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads duty roster data for display. |
| bindFirstShift | Loads and binds first shift roster data to the GridView. |
| bindSecondShift | Loads and binds second shift roster data to the GridView. |
| bindThirdShift | Loads and binds third shift roster data to the GridView. |
| searchDutyRoster | Filters and updates roster data based on search criteria. |
| gvFirstShift_RowDataBound | Formats rows in the first shift GridView. |
| gvSecondShift_RowDataBound | Formats rows in the second shift GridView. |
| gvThirdShift_RowDataBound | Formats rows in the third shift GridView. |

### 3. Data Interactions
* **Reads:** Duty roster records (OperationDate, TrackType, Line)
* **Writes:** No direct writes