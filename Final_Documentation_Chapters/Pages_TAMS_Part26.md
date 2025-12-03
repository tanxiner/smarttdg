# Page: TARViewDetails
**File:** TARViewDetails.aspx.cs

### 1. User Purpose
Users view the detailed information of a specific TAR (Technical Application Request) and its related components.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads the TAR data via the DAL object, and triggers PopOnLoad to populate controls. |
| PopOnLoad | Retrieves related data sets (orders, power sectors, etc.) and binds them to the page’s data grids and grid views. |
| dgOR_ItemDataBound | Formats each row of the Order Request data grid, applying any necessary styling or value transformations. |
| gvPossAddPL_RowDataBound | Formats each row of the Potential Power Line grid view, ensuring correct display of line details. |
| gvPossAddWL_RowDataBound | Formats each row of the Potential Water Line grid view, ensuring correct display of line details. |
| gvPossAddOO_RowDataBound | Formats each row of the Potential Other Object grid view, ensuring correct display of object details. |
| dgPossPowerSector_ItemDataBound | Formats each row of the Power Sector data grid, applying any necessary styling or value transformations. |
| lbBack_Click | Navigates the user back to the previous page or list view. |

### 3. Data Interactions
* **Reads:** TAR, OrderRequest, PowerSector, PowerLine, WaterLine, OtherObject  
* **Writes:** None

---

# Page: TOA
**File:** TOA.Master.cs

### 1. User Purpose
Provides the common layout and navigation elements for all pages within the TOA section of the application.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up master page elements such as user information, navigation links, and any session‑based settings. |

### 3. Data Interactions
* **Reads:** User session data (implicit)  
* **Writes:** None

---

# Page: TOAAddParties
**File:** TOAAddParties.aspx.cs

### 1. User Purpose
Allows users to add and manage parties associated with a specific TOA (Transfer of Asset) record, navigating through multiple tabs and confirming selections.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads the current TOA context, binds initial data to controls, and prepares the UI for user interaction. |
| bindPoints(toaid) | Retrieves and displays point information related to the specified TOA ID, populating relevant controls. |
| lbNextV1_Click | Advances the user to the next step or tab in the party addition workflow. |
| Tab1_Click | Switches the view to the first tab, updating UI state accordingly. |
| Tab2_Click | Switches the view to the second tab, updating UI state accordingly. |
| lbPrevV2_Click | Returns the user to the previous step or tab in the workflow. |
| lbAddParties_Click | Processes the selected parties, adding them to the TOA record via the DAL, and provides feedback to the user. |
| gvParties_RowDataBound | Formats each row of the parties grid view, applying any necessary styling or value transformations. |
| gvParties_RowCommand | Handles commands from the parties grid view (e.g., delete or edit actions) and updates the underlying data. |
| LogError(ex) | Records error information to a log for troubleshooting purposes. |

### 3. Data Interactions
* **Reads:** TOAReg, Party, Point, TOAParty (association table)  
* **Writes:** TOAParty (adds new party associations), possibly updates Party status or details

---