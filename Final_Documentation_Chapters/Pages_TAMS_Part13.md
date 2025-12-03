# Page: OCC_HoursAuthorisation_Preview
**File:** OCC_HoursAuthorisation_Preview.aspx.cs

### 1. User Purpose
Users view a preview of hours authorised for a specific line and can search or return to the main authorisation screen.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, initialises controls and binds the preview grid. |
| BindGrid | Retrieves the current set of authorised hours and displays them in a grid. |
| LoadDutyRoster_Ctrl | Loads duty roster information for a given user ID and populates the relevant control. |
| LoadOCCAuthPreviewCtrl_DTL | Loads detailed line‑type (DTL) preview data into the preview control. |
| LoadOCCAuthPreviewCtrl_NEL | Loads non‑exempt line (NEL) preview data into the preview control. |
| ddlLine_SelectedIndexChanged | When the user selects a different line from the dropdown, refreshes the preview data for that line. |
| btnSearchOCC_Preview_Click | Executes a search based on the current filter criteria and updates the preview grid. |
| btnBackToOCCAuth_Click | Navigates the user back to the main OCC authorisation page. |

### 3. Data Interactions
* **Reads:** DutyRoster, OCCAuthPreview (DTL and NEL), HoursAuthorisation
* **Writes:** None

---

# Page: OPD
**File:** OPD.aspx.cs

### 1. User Purpose
Users view and refresh operational performance data for a selected line.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, calls PopOnLoad to populate controls and display initial data. |
| PopOnLoad | Retrieves OPD data for the default or selected line and binds it to the page. |
| ddlLine_SelectedIndexChanged | When the user changes the line selection, reloads the OPD data for that line. |
| lbRefresh_Click | Re‑fetches the current OPD data and updates the display. |

### 3. Data Interactions
* **Reads:** OPD (Operational Performance Data) for the selected line
* **Writes:** None