# Page: TARInbox  
**File:** TARInbox.aspx.cs  

### 1. User Purpose  
Users manage and interact with tracking requests in their inbox.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads inbox data into grids and initializes user interface elements. |  
| lbSubmit_Click | Submits a new tracking request, validates inputs, and updates the inbox. |  
| lnkD1StrTARNo_Click | Filters or navigates to a specific tracking request in the first directory grid. |  
| lnkD2StrTARNo_Click | Filters or navigates to a specific tracking request in the second directory grid. |  
| lbAppList_Click | Opens or modifies a selected tracking request from the list. |  
| gvDir1_RowDataBound | Formats rows in the first directory grid (e.g., highlights status, adds action buttons). |  
| gvDir2_RowDataBound | Formats rows in the second directory grid (e.g., displays additional metadata). |  

### 3. Data Interactions  
* **Reads:** TAR, User, BlockedTar  
* **Writes:** TAR, User  

---

# Page: TARSectorBooking  
**File:** TARSectorBooking.aspx.cs  

### 1. User Purpose  
Users book sectors for track access, specifying power requirements and access details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads sector booking form and initializes data for available sectors. |  
| PopOnLoad | Sets up default values or pre-fills fields based on user context. |  
| lbSubmit_Click | Processes the sector booking request, validates inputs, and saves the booking. |  
| ChkSeq | Validates sequence numbers for sector selection to prevent duplicates. |  
| RBLPowerReq_SelectedIndexChanged | Updates power requirement details based on user selection. |  
| cbDir1All_CheckedChanged | Toggles selection of all items in the first directory grid. |  
| cbDir2All_CheckedChanged | Toggles selection of all items in the second directory grid. |  
| gvDir1_RowDataBound | Formats rows in the first directory grid (e.g., highlights availability, adds action buttons). |  
| gvDir2_RowDataBound | Formats rows in the second directory grid (e.g., displays additional metadata). |  
| lbAppList_Click | Opens or modifies a selected sector booking from the list. |  
| lbBack_Click | Navigates back to the previous page or cancels the booking process. |  

### 3. Data Interactions  
* **Reads:** Sector, Booking, User  
* **Writes:** Booking, Sector