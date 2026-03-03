# Page: TARBlockDate
**File:** TARBlockDate.aspx.cs

### 1. User Purpose
Users view, search, and manage train block dates for specific rail lines.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, initializes controls and calls `ReloadRecs` to populate the grid with block dates. |
| ReloadRecs | Retrieves block dates from the database (via `DAL`) applying any selected rail filter, then binds the result to the grid view. |
| gvBlockDate_RowDataBound | Formats each grid row, setting up command buttons (e.g., Edit, Delete) and applying any row‑specific styling. |
| gvBlockDate_RowCommand | Handles grid commands: if the user clicks Edit, redirects to the add/edit page with the selected record ID; if Delete, removes the record via `DAL` and refreshes the grid. |
| lbSearch_Click | Applies the current search criteria (e.g., rail selection) and reloads the grid. |
| lbNew_Click | Navigates the user to the `TARBlockDate_Add` page to create a new block date. |
| ddlRail_SelectedIndexChanged | Updates the rail filter and reloads the grid to show block dates for the newly selected rail line. |

### 3. Data Interactions
* **Reads:** BlockDate (filtered by rail), Rail (for dropdown population)  
* **Writes:** BlockDate (deletion via RowCommand)

---

# Page: TARBlockDate_Add
**File:** TARBlockDate_Add.aspx.cs

### 1. User Purpose
Users add a new train block date or cancel the operation.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up the form controls (e.g., populates rail dropdown) and prepares the page for data entry. |
| lbtnAddBlockDate_Click | Validates the entered block date information, then calls `DAL` to insert a new record into the BlockDate table; upon success, redirects back to the main block date list. |
| lbtnAddCancel_Click | Discards any entered data and redirects the user back to the block date list without making changes. |

### 3. Data Interactions
* **Reads:** Rail (to populate selection options)  
* **Writes:** BlockDate (new record insertion)