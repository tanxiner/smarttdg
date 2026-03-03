# Page: TOABookIn  
**File:** TOABookIn.aspx.cs  

### 1. User Purpose  
Users navigate through tabs to book in a TOA (Track Access) request, add parties, and submit the form.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page, loads default data, and sets up UI state. |  
| **loadProtectionType** | Loads protection type options into a dropdown list for user selection. |  
| **BindWitness** | Binds witness-related data to a grid or list control for display. |  
| **Tab1_Click / Tab2_Click / Tab3_Click** | Switches the user between different sections (tabs) of the booking form. |  
| **lbNextV1_Click / lbNextV2_Click / lbPrevV2_Click / lbPrevV3_Click** | Navigates through form steps or views (e.g., next/previous pages in a multi-step process). |  
| **lbSubmit_Click** | Validates form data, saves the TOA request, and processes submission. |  
| **gvParties_RowCommand** | Handles user actions (e.g., edit/delete) on rows in the parties grid. |  
| **lbAddParties_Click** | Opens a dialog or form to add new parties associated with the TOA request. |  
| **saveProtectionType** | Saves the selected or edited protection type configuration. |  
| **GVProtectionType_RowCommand** | Manages row-level actions (e.g., delete or edit) for protection type entries. |  
| **rBtnProtectionList_SelectedIndexChanged** | Updates the UI or data based on the selected protection type in a radio button list. |  

### 3. Data Interactions  
* **Reads:** ProtectionType, Witness, Party, TOA  
* **Writes:** TOA, Party, ProtectionType