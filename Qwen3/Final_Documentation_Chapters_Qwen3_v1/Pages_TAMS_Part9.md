# Page: ExternalLogin  
**File:** ExternalLogin.aspx.cs  

### 1. User Purpose  
Users log in using an external authentication provider.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and checks if the user is already authenticated. |  
| btnLogin_Click | Triggers the external login process and redirects the user. |  
| CheckAccess | Validates if the user has access to the system based on external provider data. |  
| linkB_forgetPassword_Click | Sends a password reset link to the user's registered email address. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: GenQRCode  
**File:** GenQRCode.aspx.cs  

### 1. User Purpose  
Users generate a QR code for a specified URL or data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the QR code generation interface. |  
| btnGen_Click | Generates a QR code image based on user input and displays it. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: Login  
**File:** Login.aspx.cs  

### 1. User Purpose  
Users authenticate with a username and password or LAN credentials.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the login form and checks for existing session data. |  
| btnLogin_Click | Validates user credentials and redirects to the dashboard. |  
| InternalLoginCheck | Performs core authentication logic and checks user permissions. |  
| CheckAccess | Verifies if the user has access to the system based on role or permissions. |  
| GenerateToken | Creates a secure token for authenticated sessions. |  
| CheckLANAuthentication | Authenticates user via LAN network credentials and returns a token. |  
| Encrypt | Encrypts sensitive data before storing or transmitting. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: Logout  
**File:** Logout.aspx.cs  

### 1. User Purpose  
Users log out of their session.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Ends the user's session and redirects to the login page. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None