# Page: TOABookIn  
**File:** TOABookIn.aspx.cs  

### 1. User Purpose  
Users input and submit details for a transaction involving protection type registration and party management.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default data (e.g., protection types, witness information). |  
| loadProtectionType | Fetches and displays available protection type options for user selection. |  
| BindWitness | Binds witness-related data to UI controls for display or editing. |  
| Tab1_Click | Navigates to the first tab section for initial transaction details. |  
| Tab2_Click | Navigates to the second tab section for additional transaction parameters. |  
| Tab3_Click | Navigates to the third tab section for final confirmation or submission. |  
| lbSubmit_Click | Validates user inputs, saves transaction data, and processes submission. |  
| gvParties_RowCommand | Handles user actions (e.g., editing, deleting) on party records in the GridView. |  
| lbAddParties_Click | Opens a dialog or form to add new parties associated with the transaction. |  
| saveProtectionType | Saves or updates the selected protection type configuration. |  
| GVProtectionType_RowCommand | Manages user interactions with protection type entries in the GridView. |  

### 3. Data Interactions  
* **Reads:** ProtectionType, Witness, Parties  
* **Writes:** TOAReg, Parties  

---

# Page: TOABookOut  
**File:** TOABookOut.aspx.cs  

### 1. User Purpose  
Users complete and submit details for an outbound transaction, including surrendering documents or finalizing the process.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default data (e.g., transaction details, parties). |  
| lbNextV1_Click | Advances the user through sequential steps in the outbound process. |  
| Tab1_Click | Navigates to the first tab section for initial outbound details. |  
| Tab2_Click | Navigates to the second tab section for additional outbound parameters. |  
| lbPrevV2_Click | Returns the user to a previous step in the outbound process. |  
| lbAddParties_Click | Opens a dialog or form to add new parties associated with the outbound transaction. |  
| gvParties_RowCommand | Handles user actions (e.g., editing, deleting) on party records in the GridView. |  
| lbSurrender_Click | Processes the surrender of documents or finalizes the outbound transaction. |  

### 3. Data Interactions  
* **Reads:** TOAReg, Parties  
* **Writes:** TOAReg, SurrenderRecord  

---

# Page: TOAError  
**File:** TOAError.aspx.cs  

### 1. User Purpose  
Users view error messages or status information related to failed transactions or system issues.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Displays error messages or system status information to the user. |  

### 3. Data Interactions  
* **Reads:** ErrorLog, SystemStatus  
* **Writes:** None