# Page: AddCompany
**File:** AddCompany.aspx.cs

### 1. User Purpose
Users add or edit company information through a form on this page.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | On first load, calls `setupPage` to populate form fields based on the current user registration ID. |
| setupPage | Retrieves the current user’s registration ID, loads any existing company data for that user, and fills the form controls. |
| btn_externalSave_Click | Validates the entered company details, then inserts or updates the company record in the database and redirects the user to a confirmation or listing page. |
| btn_externalCancel_Click | Cancels the operation and redirects the user back to the previous page or company list without saving changes. |

### 3. Data Interactions
* **Reads:** Company, UserRegID  
* **Writes:** Company  

---

# Page: AnonymousSite
**File:** AnonymousSite.Master.cs

### 1. User Purpose
Provides the common layout and navigation for pages accessed by anonymous users.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up any master‑page level elements (e.g., navigation links, page title) that are visible to all anonymous visitors. |

### 3. Data Interactions
* **Reads:** None  
* **Writes:** None  

---

# Page: Basepage
**File:** BasePage.aspx.cs

### 1. User Purpose
Serves as a foundational class for other pages, offering reusable database connection and command utilities.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes any common page‑level settings or resources needed by derived pages. |
| GetSqlConnection | Creates and returns a new SQL connection using the configured connection string. |
| GetSqlCommand | Builds a `SqlCommand` object for a given SQL string, ready for execution. |
| GetSqlDataAdapter | Wraps a `SqlCommand` in a `SqlDataAdapter` for filling datasets or performing updates. |
| QuoteRemove | Removes quotation marks from a string, typically used to sanitize input before database operations. |

### 3. Data Interactions
* **Reads:** Any table accessed through commands created by `GetSqlCommand`.  
* **Writes:** Any table modified through commands created by `GetSqlCommand`.  

---

# Page: DTCAuth
**File:** DTCAuth.aspx.cs

### 1. User Purpose
Handles authentication for DTC users, managing session state and token generation.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Checks whether the user is already authenticated; if not, initiates the authentication flow. |
| SessionExpire | Handles the event when a user’s session expires, typically redirecting to a login or timeout page. |
| GenerateToken | Creates a unique token string (e.g., a GUID or hashed value) used for session validation or API access. |

### 3. Data Interactions
* **Reads:** Session data, user credentials (if validated against a store).  
* **Writes:** Session token, possibly logging authentication events.  

---