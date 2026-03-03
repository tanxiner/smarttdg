# Page: RPEAS_Login
**File:** RPEAS_Login.aspx.vb

### 1. User Purpose
Users log in to the system using their username and password.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads menu, and sets up event handlers. |
| btnLogin_Click | Validates the username and password, calls the `authenticateUser` method to verify credentials, and then loads the menu based on the user's GUID. |
| authenticateUser(uid: String, password: String) |  This method likely takes the username and password, performs a database lookup (not shown), and returns a task. |
| RetrieveToken() | This method likely retrieves a token from a system or database. |
| callPostMethod(url: String, token: String, arg: HttpContent) | This method likely makes an asynchronous POST request to a specified URL, passing the token and content. |
| callGetMethod(url: String) | This method likely makes an asynchronous GET request to a specified URL. |
| Encrypt(val: String) | This method likely encrypts a given string value. |
| getLoginresponce(uid: String, password: String) | This method likely returns a string response based on the provided username and password. |
| CheckAccess() | This method likely checks user access rights. |
| LoadMenu(UserGUID: String) | This method likely loads the appropriate menu based on the user's GUID. |
| btnReset_Click | Resets the login form. |

---