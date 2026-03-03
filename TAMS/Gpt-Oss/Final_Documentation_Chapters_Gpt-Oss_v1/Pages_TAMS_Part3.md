# Page: DepotTARApplication
**File:** DepotTARApplication.aspx.cs

### 1. User Purpose
Users submit a TAR (Transfer Authorization Request) for a depot location, selecting the desired line, access type, and dates, then review a grid of available sectors before confirming the application.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On the first request, the page populates the location dropdown via `BindLocation()` and fills the sector grid via `BindGrid()`. Subsequent postbacks preserve user selections. |
| **BindLocation** | Retrieves a list of depot locations from the data layer and binds them to the location selector control. |
| **BindGrid** | Queries the data layer for sector information relevant to the selected location, line, and access type, then binds the result to the main grid view. |
| **btnSubmit_Click** | Gathers the selected location, line, access type, and dates, validates the input, and calls the data layer to persist the TAR request. It then displays a confirmation message or error feedback. |
| **displayDates** | Formats and displays a list of dates for a specific TAR type, access type, line, and location, updating the UI with the appropriate date controls. |
| **showHideControls** | Shows or hides UI elements (e.g., date pickers, sector grid) based on the current toggle state, ensuring the interface reflects the chosen access type or possession option. |
| **GridView1_RowDataBound** | Applies row‑level formatting to the main grid, such as setting CSS classes or adding tooltips based on sector status. |
| **gv1_B1_RowDataBound** to **gv7_B1_RowDataBound** | Each of these methods handles row formatting for the seven sub‑grids that display sector details for different categories or statuses. |
| **displayLegend** | Generates a legend explaining the meaning of icons or color codes used in the sector grids. |
| **ddlLine_SelectedIndexChanged** | When the user selects a different line, the method refreshes the sector grid to show only sectors applicable to that line. |
| **rbPossession_CheckedChanged** | Toggles the possession option; updates internal state and may trigger a UI refresh to show relevant sectors or dates. |
| **rbProtection_CheckedChanged** | Toggles the protection option; updates internal state and may trigger a UI refresh to show relevant sectors or dates. |

### 3. Data Interactions
* **Reads:**  
  * Depot locations (for the location dropdown)  
  * Sector information for the selected location, line, and access type (for the grid views)  
  * Date ranges or availability lists (for the date display controls)

* **Writes:**  
  * New TAR request record (including selected location, line, access type, dates, and sector selections) stored via the `oDepotTarForn` data access object.