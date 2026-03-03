# Page: TOABookIn  
**File:** TOABookIn.aspx.cs  

### 1. User Purpose  
Users complete a multi‑step form to book a Transfer of Assets (TOA) request, selecting protection types, adding parties and witnesses, and finally submitting the booking for processing.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, initializes the page: populates protection type list, sets up default tab visibility, and prepares any required data structures. |
| **loadProtectionType** | Retrieves available protection types from the database via the DAL and binds them to the protection type grid or list. |
| **BindWitness** | Accepts a DataSet of witness records and binds it to the witness grid, formatting each row for display. |
| **Tab1_Click** | Switches the view to the first tab (e.g., protection type selection) and updates tab styling. |
| **Tab2_Click** | Switches to the second tab (e.g., parties list) and updates tab styling. |
| **Tab3_Click** | Switches to the third tab (e.g., witness list) and updates tab styling. |
| **lbNextV1_Click** | Moves the user from Tab 1 to Tab 2 after validating the protection type selection. |
| **lbNextV2_Click** | Moves the user from Tab 2 to Tab 3 after validating the parties list. |
| **lbPrevV2_Click** | Returns the user from Tab 2 back to Tab 1. |
| **lbPrevV3_Click** | Returns the user from Tab 3 back to Tab 2. |
| **lbSubmit_Click** | Validates all entered data, calls `saveProtectionType` and other save routines, then persists the complete TOA booking to the database. On success, redirects or shows a confirmation. |
| **gvParties_RowDataBound** | Formats each row in the parties grid (e.g., sets up delete buttons, highlights selected rows). |
| **gvParties_RowCommand** | Handles commands from the parties grid such as deleting a party or editing details. |
| **lbAddParties_Click** | Opens a dialog or adds a new row to the parties grid, allowing the user to enter a new party’s information. |
| **LogError** | Static helper that records exception messages to a log table or file for troubleshooting. |
| **saveProtectionType** | Persists the user’s selected protection type(s) to the database, linking them to the current TOA record. |
| **BtnAddProt_Click** | Adds a new protection type entry to the grid and updates the underlying data structure. |
| **bindPoints** | Loads point data for a given TOA ID and binds it to the points grid or list. |
| **GVProtectionType_RowCommand** | Handles grid commands for protection types (e.g., delete or edit a protection type entry). |
| **rBtnProtectionList_SelectedIndexChanged** | Responds to changes in the protection type radio button list, updating related UI elements or data bindings. |

### 3. Data Interactions  

* **Reads:**  
  * ProtectionType (via `loadProtectionType`)  
  * Witness (via `BindWitness`)  
  * Parties (via grid data binding)  
  * Points (via `bindPoints`)  
  * TOAReg (initial record retrieval for editing)

* **Writes:**  
  * TOAReg (final booking record on submit)  
  * ProtectionType (selected types via `saveProtectionType`)  
  * Parties (add/delete via grid commands)  
  * Witness (add/delete via grid commands)  
  * Points (if applicable during booking)

The page uses a data access object named `DAL` of type `oTOAReg` to perform all database interactions.