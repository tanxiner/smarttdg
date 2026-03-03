# Page: TOAAddParties  
**File:** TOAAddParties.aspx.cs  

### 1. User Purpose  
Users add and manage parties (e.g., individuals or organizations) associated with a TOA request.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads existing party data if the request ID is provided. |  
| bindPoints | Loads dropdowns or lists of related entities (e.g., points of contact) based on the TOA request ID. |  
| lbNextV1_Click | Advances the user to the next step in the party addition workflow. |  
| Tab1_Click / Tab2_Click | Switches between tabs for different party types (e.g., primary vs. secondary parties). |  
| lbPrevV2_Click | Returns the user to a previous step in the workflow. |  
| lbAddParties_Click | Triggers the addition of a new party to the TOA request. |  
| gvParties_RowDataBound | Populates GridView rows with party details during rendering. |  
| gvParties_RowCommand | Handles user actions (e.g., edit, delete) on GridView rows. |  
| LogError | Records errors during page operations to a log. |  

### 3. Data Interactions  
* **Reads:** TOA, Party, User  
* **Writes:** Party, TOA  

---

# Page: TOAApplication  
**File:** TOAApplication.aspx.cs  

### 1. User Purpose  
Users submit a TOA (Track Access Request) application form and manage login credentials.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the application form and initializes session variables. |  
| lbtnSubmit_Click | Validates form data, encodes sensitive fields, and submits the TOA request. |  
| ToDecode / ToEncode | Encrypts/decrypts sensitive data (e.g., passwords) for secure storage. |  
| getLoginResponse | Validates user credentials against the database. |  
| LogError | Records errors during form submission or authentication. |  

### 3. Data Interactions  
* **Reads:** User, TOA  
* **Writes:** TOA, Application