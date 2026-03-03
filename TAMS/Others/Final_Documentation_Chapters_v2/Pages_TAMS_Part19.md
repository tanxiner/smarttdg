# Page: TOAAddParties  
**File:** TOAAddParties.aspx.cs  

### 1. User Purpose  
Users add and manage parties associated with a TOA application.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads party data based on the TOA ID. |  
| bindPoints | Populates dropdowns or lists with relevant party points or options. |  
| lbNextV1_Click | Advances the user to the next step in the party addition workflow. |  
| Tab1_Click / Tab2_Click | Switches between tabs for different party management views. |  
| lbAddParties_Click | Triggers the addition of a new party record to the application. |  
| gvParties_RowDataBound | Formats GridView rows to display party details dynamically. |  
| gvParties_RowCommand | Handles user actions like editing or deleting a party entry. |  
| LogError | Records errors during party management operations. |  

### 3. Data Interactions  
* **Reads:** TOA, Party, User  
* **Writes:** Party, TOA  

---

# Page: TOAApplication  
**File:** TOAApplication.aspx.cs  

### 1. User Purpose  
Users submit a TOA application and manage login credentials for the system.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the application form and initializes login validation. |  
| lbtnSubmit_Click | Processes the submitted TOA application data. |  
| getLoginResponse | Validates user credentials against the system database. |  
| LogError | Records errors during application submission or login attempts. |  

### 3. Data Interactions  
* **Reads:** User, TOA  
* **Writes:** TOA, User