# Page: TARAppList
**File:** TARAppList.aspx.cs

### 1. User Purpose
Users view a list of TAR (Technical Application Request) submissions, filter them, and navigate to detailed views of individual requests.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, initializes the data access object, retrieves the full list of TAR applications, binds the data to the main grid views (`gvDir1` and `gvDir2`), and displays a status legend. |
| **lbSubmit_Click** | When the user clicks the “Submit” button, the page re‑queries the TAR list using any entered filter criteria, updates the grid views, and refreshes the legend. |
| **displayLegend** | Builds a visual legend that explains the meaning of status icons or colors used in the grid rows. |
| **gvDir2_RowDataBound** | For each row in the second‑level directory grid, sets display values (e.g., status text, color coding) and attaches click handlers for the TAR number link. |
| **gvDir1_RowDataBound** | Similar to `gvDir2_RowDataBound`, but for the first‑level directory grid; prepares row data and link actions. |
| **lnkD2StrTARNo_Click** | Handles clicks on a TAR number link in the second‑level grid; redirects the user to a detailed view page for that specific TAR request. |
| **lnkD1StrTARNo_Click** | Handles clicks on a TAR number link in the first‑level grid; redirects to the detailed view page for that TAR request. |
| **lbBack_Click** | Returns the user to the previous page or clears any applied filters, resetting the grid views to their default state. |
| **gvDir2Child_RowDataBound** | Populates child rows (sub‑entries) under a second‑level directory row, formatting data and setting up any necessary controls. |
| **gvDir1Child_RowDataBound** | Populates child rows under a first‑level directory row, applying formatting and control logic. |

### 3. Data Interactions
* **Reads:** TAR application records, directory hierarchy information, status codes, and any related metadata needed for display.
* **Writes:** None – the page only retrieves and displays data; navigation actions do not modify data.