# Page: OCCTVF_Ack_Preview  
**File:** OCCTVF_Ack_Preview.ascx.cs  

### 1. User Purpose  
Users review a list of CCTV footage acknowledgements, can approve or reject each item, add remarks, and view related tariff information.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, calls `populateOCCTVF_Ack` to fill the grid with pending acknowledgements. |
| **populateOCCTVF_Ack** | Retrieves acknowledgement records for the current user and binds them to the grid. |
| **GridView1_RowDataBound** | Formats each row (e.g., highlights status, sets up action buttons). |
| **btnSubmit_Click** | Marks the selected acknowledgement as approved, updates the status in the database, and refreshes the grid. |
| **btnReject_Click** | Marks the selected acknowledgement as rejected, updates the status in the database, and refreshes the grid. |
| **ShowRemark** | Displays a remark input area for the selected acknowledgement, allowing the user to enter comments. |
| **btnSave_Click** | Persists the entered remark to the database and updates the acknowledgement record. |
| **ShowTarTVF** | Toggles visibility of tariff details related to the selected acknowledgement. |

### 3. Data Interactions  

* **Reads:**  
  * Acknowledgement records (e.g., `OCCTVF_Ack` table)  
  * User information (e.g., `UserID`, `RosterCode`)  
  * Tariff details (e.g., `TarTVF` data)  

* **Writes:**  
  * Updates acknowledgement status (approved/rejected)  
  * Saves user remarks to the acknowledgement record  

---  

# Page: menu  
**File:** menu.ascx.cs  

### 1. User Purpose  
Displays a navigation menu tailored to the logged‑in user’s role and the environment (internal or internet).

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Determines the current user and environment, then calls either `Generate_Menu` or `Generate_Menu2` to build the menu. |
| **Generate_Menu** | Builds a menu structure based on the supplied `userid` and `isInternet` flag, pulling role‑specific items from the database. |
| **Generate_Menu2** | Builds a simplified or alternative menu for internal users, using only the `userid`. |

### 3. Data Interactions  

* **Reads:**  
  * User role and permission data from the user/role tables.  

* **Writes:**  
  * None – the control only renders menu items.  

---