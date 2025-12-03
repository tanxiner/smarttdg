# Page: AddCompany.aspx
**File:** AddCompany.aspx.cs

### 1. User Purpose
Users fill out this form to request track access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and loads user-specific data. |
| setupPage | Prepares the UI for the current user by setting up form fields. |
| btn_externalSave_Click | Saves the company information to the database and redirects the user. |
| btn_externalCancel_Click | Cancels the current action and returns the user to the previous page. |

### 3. Data Interactions
* **Reads:** User
* **Writes:** Company

---

# Page: AnonymousSite.Master
**File:** AnonymousSite.Master.cs

### 1. User Purpose
Sets up the layout for anonymous user access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the master page layout and loads common elements. |

### 3. Data Interactions
* **Reads:** None
* **Writes:** None

---

# Page: BasePage.aspx
**File:** BasePage.aspx.cs

### 1. User Purpose
Provides common functionality for all pages, including database access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the base page and sets up database connection parameters. |
| GetSqlConnection | Establishes a connection to the database. |
| GetSqlCommand | Creates a SQL command for database operations. |
| GetSqlDataAdapter | Prepares data adapters for retrieving or updating data. |

### 3. Data Interactions
* **Reads:** User, Company, Track
* **Writes:** User, Company, Track

---

# Page: DTCAuth.aspx
**File:** DTCAuth.aspx.cs

### 1. User Purpose
Manages user authentication and session token generation.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the authentication page and checks session validity. |
| SessionExpire | Handles session expiration by redirecting the user. |
| GenerateToken | Creates a secure session token for authenticated users. |

### 3. Data Interactions
* **Reads:** User, Session
* **Writes:** Session, Token