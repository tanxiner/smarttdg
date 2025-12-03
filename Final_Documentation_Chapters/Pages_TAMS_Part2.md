# Page: Default
**File:** Default.aspx.cs

### 1. User Purpose
Users arrive at the default landing page to view the main entry point of the application.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page state on each request, ensuring any necessary session or user context is set up before the page is rendered. |

### 3. Data Interactions
* **Reads:** None explicitly shown.  
* **Writes:** None explicitly shown.

---

# Page: DepotTARAppList
**File:** DepotTARAppList.aspx.cs

### 1. User Purpose
Users use this page to view and filter a list of TAR (Transportation Application Request) records associated with a specific depot, and to navigate to detailed views of individual records.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads initial data for the page, such as populating location and line dropdowns, and binding the main grid with TAR records. |
| BindLocation | Retrieves available depot locations from the data layer and populates the location selection control. |
| lbSubmit_Click | Applies the selected filters (location, line, etc.) and refreshes the grid to display matching TAR records. |
| displayLegend | Generates a visual legend explaining status codes or symbols used in the grid. |
| gvDir1_RowDataBound | Formats each row of the main grid, setting up controls and data bindings for individual TAR entries. |
| lnkD1StrTARNo_Click | Handles clicks on a TAR number link, redirecting the user to a detailed view of that specific TAR record. |
| lbBack_Click | Returns the user to the previous page or resets the current view. |
| gvDir1Child_RowDataBound | Formats nested child rows within the main grid, often used for related details or sub‑records. |
| ddlLine_SelectedIndexChanged | Updates the grid or other controls when the user selects a different line from the dropdown. |

### 3. Data Interactions
* **Reads:** Depot locations, TAR application records, line information.  
* **Writes:** None explicitly shown; the page primarily displays data and navigates to detail views.