# Page: TARInbox  
**File:** TARInbox.aspx.cs  

### 1. User Purpose  
Users view the TAR (Technical Access Request) inbox, select requests for processing, and navigate to detailed request pages.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Loads the inbox data into two grid views (`gvDir1` and `gvDir2`), sets up any required page state, and ensures controls are ready for user interaction. |
| **lbSubmit_Click** | Processes the TAR items that the user has selected, updates their status in the database, and may trigger notifications or logging. |
| **lnkD1StrTARNo_Click** | Redirects the user to a detailed view of the selected TAR from Directory 1, passing the TAR number as a query parameter. |
| **lnkD2StrTARNo_Click** | Redirects the user to a detailed view of the selected TAR from Directory 2, passing the TAR number as a query parameter. |
| **lbAppList_Click** | Returns the user to the application list or a higher‑level overview page. |
| **gvDir1_RowDataBound** | Configures each row in the Directory 1 grid: sets link text, applies styling, and attaches any row‑specific data. |
| **gvDir2_RowDataBound** | Performs the same row‑level configuration for the Directory 2 grid. |

### 3. Data Interactions  

* **Reads:**  
  * TAR inbox entries (including request numbers, status, and related metadata).  
  * User and directory information needed to display the grids.  

* **Writes:**  
  * Updates to TAR status when requests are processed.  
  * Logging of user actions or audit trail entries.  


---  

# Page: TARSectorBooking  
**File:** TARSectorBooking.aspx.cs  

### 1. User Purpose  
Users book sectors for a TAR by selecting available sectors, specifying power requirements, and confirming the booking.

### 2. Key Events & Logic  

| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Loads sector availability data, populates the two sector grids (`gvDir1` and `gvDir2`), and initializes any default selections or page state. |
| **PopOnLoad** | Helper routine that sets up initial control values (e.g., default power requirement, pre‑selected sectors) when the page first loads. |
| **lbSubmit_Click** | Validates the user’s sector selections, checks sequence rules via `ChkSeq`, writes the booking to the database, updates the TAR record, and provides confirmation feedback. |
| **ChkSeq** | Ensures that the selected sectors follow the required sequence or ordering constraints before a booking can be saved. |
| **RBLPowerReq_SelectedIndexChanged** | Adjusts the UI or available sector options based on the user’s chosen power requirement (e.g., high vs. low power). |
| **cbDir1All_CheckedChanged** | Selects or deselects all sectors in Directory 1 when the “Select All” checkbox is toggled. |
| **cbDir2All_CheckedChanged** | Performs the same bulk selection logic for Directory 2. |
| **gvDir1_RowDataBound** | Configures each row in the Directory 1 grid: sets up selection controls, displays sector details, and applies any row‑specific logic. |
| **gvDir2_RowDataBound** | Performs the same configuration for the Directory 2 grid. |
| **lbAppList_Click** | Navigates back to the application list or a higher‑level page. |
| **lbBack_Click** | Returns the user to the previous page or cancels the current booking operation. |

### 3. Data Interactions  

* **Reads:**  
  * Sector availability and details for the selected TAR.  
  * TAR metadata (access date, type, etc.) stored in `StrAccessDate`, `StrAccessType`, `StrTARType`.  
  * User information for audit purposes.  

* **Writes:**  
  * Creates or updates sector booking records in the database.  
  * Updates the TAR status to reflect the new booking.  
  * Persists any changes to user selections or preferences.  

---