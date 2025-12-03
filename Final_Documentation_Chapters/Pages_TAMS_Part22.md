# Page: TAREnquiry_Print  
**File:** TAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users open this page to view a printable snapshot of a TAR enquiry record.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | When the page loads, it pulls the relevant TAR enquiry data (typically identified by a query‑string or session value), formats that data for display, and renders the controls so the user can print the information. |

### 3. Data Interactions  
* **Reads:** TAREnquiry (and any related lookup data such as User or TarDetails)  
* **Writes:** None  

---