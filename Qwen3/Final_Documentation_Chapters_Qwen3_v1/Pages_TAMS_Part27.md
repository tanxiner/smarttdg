# Page: TOAApplication  
**File:** TOAApplication.aspx.cs  

### 1. User Purpose  
Users submit application forms and authenticate to access tracking services.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and checks user authentication status. |  
| lbtnSubmit_Click | Validates form inputs, encodes data using ToEncode, saves application details, and redirects to a confirmation page. |  
| getLoginResponse | Verifies user credentials against the database and returns a login status message. |  
| LogError | Records error messages to a static log file for troubleshooting. |  

### 3. Data Interactions  
* **Reads:** User, ApplicationRegistry  
* **Writes:** ApplicationRegistry