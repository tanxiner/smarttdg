# Page: TOAApplication
**File:** TOAApplication.aspx.cs

### 1. User Purpose
Users enter a user ID and password to request a TOA (Transfer of Authority) application; the page authenticates the credentials and initiates the application process.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Prepares the page on first load, initializing any necessary state or controls. |
| lbtnSubmit_Click | Gathers the entered user ID and password, encodes them if needed, calls `getLoginResponse` to validate the credentials, and then proceeds with the TOA application workflow. If an error occurs, it logs the exception via `LogError`. |
| ToDecode | Converts an encoded string back to its original form (likely Base‑64 or a custom scheme). |
| ToEncode | Encodes a plain string into a secure format for transmission or storage. |
| getLoginResponse | Uses the `DAL` (oTOAReg) data‑access object to verify the supplied user ID and password, returning a status string that indicates success or failure. |
| LogError | Records exception details into the static `ErrorLog` string for later review. |

### 3. Data Interactions
* **Reads:** User credentials (User ID, Password) are passed to the `oTOAReg` data‑access layer for validation.  
* **Writes:** Any error information is appended to the static `ErrorLog` string; the actual TOA application data is likely persisted through the `oTOAReg` layer during the workflow (not shown in the code snippet).