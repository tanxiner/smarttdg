# Page: ExternalLogin  
**File:** ExternalLogin.aspx.cs  

### 1. User Purpose  
Users enter their credentials to authenticate and gain access to the application.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Checks whether a user is already authenticated; if so, redirects to the main dashboard. |
| btnLogin_Click | Validates the entered username and password, then calls `CheckAccess` to verify credentials and establish a session. |
| CheckAccess | Queries the user store for the supplied credentials, sets session variables on success, and redirects to the appropriate landing page; on failure, displays an error message. |
| linkB_forgetPassword_Click | Redirects the user to the password‑reset workflow. |

### 3. Data Interactions  
* **Reads:** User credentials from the user store.  
* **Writes:** Session state (user ID, role, etc.).

---

# Page: GenQRCode  
**File:** GenQRCode.aspx.cs  

### 1. User Purpose  
Users generate a QR code that encodes a specified value (e.g., a URL or identifier).

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Prepares the page for QR code generation (e.g., clears previous output). |
| btnGen_Click | Takes the user‑supplied input, creates a QR code image using a library, and displays it on the page. |

### 3. Data Interactions  
* **Reads:** User input from a form field.  
* **Writes:** None (the QR code image is generated in memory and rendered to the response).

---

# Page: Login  
**File:** Login.aspx.cs  

### 1. User Purpose  
Users provide their username and password to log into the system.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Checks if a session already exists; if so, redirects to the main page. |
| btnLogin_Click | Initiates `InternalLoginCheck` to validate credentials and establish a session. |
| InternalLoginCheck | Calls `CheckLANAuthentication` to verify credentials against the LAN service; on success, generates a token via `GenerateToken`, stores it in the session, and redirects to the dashboard. |
| CheckAccess | Validates that the current session contains a valid user; otherwise, forces a redirect to the login page. |
| GenerateToken | Creates a secure token (e.g., JWT) that represents the authenticated user. |
| CheckLANAuthentication | Sends the supplied user ID, password, and bearer token to the LAN authentication endpoint; returns the authentication result. |
| Encrypt | Applies a cryptographic transformation to a string value (used for secure storage or transmission). |

### 3. Data Interactions  
* **Reads:** User credentials from the login form; authentication result from the LAN service.  
* **Writes:** Session state (user ID, token, role); possibly logs authentication attempts.

---

# Page: Logout  
**File:** Logout.aspx.cs  

### 1. User Purpose  
Users terminate their session and return to the login screen.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Clears all session data, invalidates authentication cookies, and redirects the user to the login page. |

### 3. Data Interactions  
* **Reads:** None.  
* **Writes:** Session state (cleared), authentication cookies (removed).