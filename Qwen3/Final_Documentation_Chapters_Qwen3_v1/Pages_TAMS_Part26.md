# Page: TARViewDetails  
**File:** TARViewDetails.aspx.cs  

### 1. User Purpose  
Users view detailed information about a Track Access Request (TAR) and related party data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads TAR data into controls. |  
| PopOnLoad | Sets up data bindings for grids and lists on the page. |  
| dgOR_ItemDataBound | Formats or highlights specific data rows in the OR grid. |  
| gvPossAddPL_RowDataBound | Customizes display of Power Line data in the grid. |  
| gvPossAddWL_RowDataBound | Formats data for Work Locations in the grid. |  
| gvPossAddOO_RowDataBound | Adjusts display for Ownership data in the grid. |  
| dgPossPowerSector_ItemDataBound | Applies styling or logic to Power Sector data rows. |  
| lbBack_Click | Navigates users back to the previous TAR listing or overview. |  

### 3. Data Interactions  
* **Reads:** TAR, BlockedTar, Parties, PowerLine, WorkLocation, Ownership, PowerSector  
* **Writes:** None (data is read-only for this page)  

---

# Page: TOAAddParties  
**File:** TOAAddParties.aspx.cs  

### 1. User Purpose  
Users manage parties (e.g., individuals or organizations) associated with a Track Ownership Agreement (TOA).  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads TOA data and binds party information to grids. |  
| bindPoints | Populates dropdowns or lists with relevant points based on TOA ID. |  
| lbNextV1_Click | Advances to the next step in the party addition workflow. |  
| Tab1_Click / Tab2_Click | Switches between tabs for different party types or views. |  
| lbPrevV2_Click | Returns to the previous step in the workflow. |  
| lbAddParties_Click | Triggers logic to add a new party to the TOA. |  
| gvParties_RowDataBound | Customizes display of party data in the grid. |  
| gvParties_RowCommand | Handles user actions like editing or deleting a party entry. |  

### 3. Data Interactions  
* **Reads:** TOA, Parties, Points  
* **Writes:** Parties (adds or updates party records)  

---

# Page: TOA.Master  
**File:** TOA.Master.cs  

### 1. User Purpose  
Provides a shared layout and navigation structure for TOA-related pages.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes master page controls like navigation menus or headers. |  

### 3. Data Interactions  
* **Reads:** None (master page does not directly interact with data)  
* **Writes:** None